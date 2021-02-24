#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
import os, sys, time, json, threading
import dbus, dbus.service, socket

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

class btOutput:
    print("Loading btOutput")
    
    """
    create a bluetooth device to emulate a HID keyboard
    """
    MY_DEV_NAME = 'smartKeypads'
    # Service port - must match port configured in SDP record
    P_CTRL = 17
    # Service port - must match port configured in SDP record#Interrrupt port
    P_INTR = 19
    # BlueZ dbus
    PROFILE_DBUS_PATH = '/bluez/yaptb/btkb_profile'
    ADAPTER_IFACE = 'org.bluez.Adapter1'
    DEVICE_INTERFACE = 'org.bluez.Device1'
    DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
    DBUS_OM_IFACE = 'org.freedesktop.DBus.ObjectManager'
    DEVICE_PATH = '/org/bluez/hci0'

    # file path of the sdp record to laod
    install_dir  = os.path.dirname(os.path.realpath(__file__))
    SDP_RECORD_PATH = os.path.join(install_dir, 'btProfile.xml')
    # UUID for HID service (1124)
    # https://www.bluetooth.com/specifications/assigned-numbers/service-discovery
    UUID = '00001124-0000-1000-8000-00805f9b34fb'
        
    def __init__(self):

        print('Starting btServer')
        self.scontrol = None
        self.ccontrol = None  # Socket object for control
        self.sinterrupt = None
        self.cinterrupt = None  # Socket object for interrupt
        self.bus = dbus.SystemBus()
        self.adapter_methods = dbus.Interface(self.bus.get_object('org.bluez', self.DEVICE_PATH), self.ADAPTER_IFACE)
        self.adapter_property = dbus.Interface(self.bus.get_object('org.bluez', self.DEVICE_PATH), self.DBUS_PROP_IFACE)

        self.DEVICE_ADDRESS = self.adapter_property.Get(self.ADAPTER_IFACE, 'Address')
        self.connect()
        
    ################################################
    # Wait for client connection
    ################################################
    def connect(self):
        print('Enter connect')

        """
        Listen for connections coming from HID client
        """

        self.scontrol = socket.socket(socket.AF_BLUETOOTH,
                                      socket.SOCK_SEQPACKET,
                                      socket.BTPROTO_L2CAP)
        self.scontrol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sinterrupt = socket.socket(socket.AF_BLUETOOTH,
                                        socket.SOCK_SEQPACKET,
                                        socket.BTPROTO_L2CAP)
        self.sinterrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.scontrol.bind((self.DEVICE_ADDRESS, self.P_CTRL))
        self.sinterrupt.bind((self.DEVICE_ADDRESS, self.P_INTR))

        # Start listening on the server sockets
        self.scontrol.listen(1)  # Limit of 1 connection
        self.sinterrupt.listen(1)

        print('Wait for connections')
        self.ccontrol, cinfo = self.scontrol.accept()
        print('{} connected on the control socket'.format(cinfo[0]))

        self.cinterrupt, cinfo = self.sinterrupt.accept()
        print('{} connected on the interrupt channel'.format(cinfo[0]))

    ################################################
    # send a string to the bluetooth host machine
    ################################################
    def send(self, text):
        """
        Send HID message
        :param msg: (bytes) HID packet to send
        """
        try:
            print('Send Message: ', message)
            self.cinterrupt.send(bytes(message), 'UTF-8')
        except:
            print('send_string failed, Error: ', sys.exc_info()[0])
            cinterrupt.close()
            sinterrupt.close()
