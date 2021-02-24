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


class btServer:
    """
    create a bluetooth device to emulate a HID keyboard
    """
    MY_DEV_NAME = 'X_HID_Keyboard'
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

    # file path of the sdp record to laod
    install_dir  = os.path.dirname(os.path.realpath(__file__))
    SDP_RECORD_PATH = os.path.join(install_dir,
                                   'sdp_record.xml')
    # UUID for HID service (1124)
    # https://www.bluetooth.com/specifications/assigned-numbers/service-discovery
    UUID = '00001124-0000-1000-8000-00805f9b34fb'

    def __init__(self, hci=0):
        print("3. Configuring Device name " + self.MY_DEV_NAME)
        # set the device class to a keybord and set the name
        #os.system("hciconfig hci0 up")
        #os.system("hciconfig hci0 class 0x000540")

        self.scontrol = None
        self.ccontrol = None  # Socket object for control
        self.sinterrupt = None
        self.cinterrupt = None  # Socket object for interrupt
        self.dev_path = '/org/bluez/hci{}'.format(hci)
        print('Setting up BT device')
        
        """
        self.bus = dbus.SystemBus()
        self.adapter_methods = dbus.Interface(self.bus.get_object('org.bluez', self.dev_path), self.ADAPTER_IFACE)
        self.adapter_property = dbus.Interface(self.bus.get_object('org.bluez', self.dev_path), self.DBUS_PROP_IFACE)
        self.bus.add_signal_receiver(self.interfaces_added,
                                     dbus_interface=self.DBUS_OM_IFACE,
                                     signal_name='InterfacesAdded')

        self.bus.add_signal_receiver(self._properties_changed,
                                     dbus_interface=self.DBUS_PROP_IFACE,
                                     signal_name='PropertiesChanged',
                                     arg0=self.DEVICE_INTERFACE,
                                     path_keyword='path')
        """

        print('Configuring for name {}'.format(self.MY_DEV_NAME))

        #self.config_hid_profile()

        # set the Bluetooth device configuration
        #self.alias = BTKbDevice.MY_DEV_NAME
        #self.discoverabletimeout = 0
        #self.discoverable = True
    """

    def interfaces_added(self):
        pass

    def _properties_changed(self, interface, changed, invalidated, path):
        if self.on_disconnect is not None:
            if 'Connected' in changed:
                if not changed['Connected']:
                    self.on_disconnect()

    def on_disconnect(self):
        print('The client has been disconnect')
        self.listen()
                                       'Address')

    @property
    def powered(self):
        #power state of the Adapter.
        return self.adapter_property.Get(self.ADAPTER_IFACE, 'Powered')

    @powered.setter
    def powered(self, new_state):
        self.adapter_property.Set(self.ADAPTER_IFACE, 'Powered', new_state)

    @property
    def alias(self):
        return self.adapter_property.Get(self.ADAPTER_IFACE,
                                         'Alias')

    @alias.setter
    def alias(self, new_alias):
        self.adapter_property.Set(self.ADAPTER_IFACE,
                                  'Alias',
                                  new_alias)

    @property
    def discoverabletimeout(self):
        #Discoverable timeout of the Adapter.
        return self.adapter_props.Get(self.ADAPTER_IFACE,
                                      'DiscoverableTimeout')

    @discoverabletimeout.setter
    def discoverabletimeout(self, new_timeout):
        self.adapter_property.Set(self.ADAPTER_IFACE,
                                  'DiscoverableTimeout',
                                  dbus.UInt32(new_timeout))

    @property
    def discoverable(self):
        #Discoverable state of the Adapter.
        return self.adapter_props.Get(
            self.ADAPTER_INTERFACE, 'Discoverable')

    @discoverable.setter
    def discoverable(self, new_state):
        self.adapter_property.Set(self.ADAPTER_IFACE,
                                  'Discoverable',
                                  new_state)

    def config_hid_profile(self):
        #Setup and register HID Profile

        print('Configuring Bluez Profile')
        service_record = self.read_sdp_service_record()

        opts = {
            'Role': 'server',
            'RequireAuthentication': False,
            'RequireAuthorization': False,
            'AutoConnect': True,
            'ServiceRecord': service_record,
        }

        manager = dbus.Interface(self.bus.get_object('org.bluez',
                                                     '/org/bluez'),
                                 'org.bluez.ProfileManager1')

        #HumanInterfaceDeviceProfile(self.bus, BTKbDevice.PROFILE_DBUS_PATH)

        manager.RegisterProfile(self.PROFILE_DBUS_PATH,
                                self.UUID,
                                opts)

        print('Profile registered ')

    @staticmethod
    def read_sdp_service_record():
        #Read and return SDP record from a file
        #:return: (string) SDP record
        print('Reading service record')
        try:
            fh = open(self.SDP_RECORD_PATH, 'r')
        except OSError:
            sys.exit('Could not open the sdp record. Exiting...')

        return fh.read()   
    """
    
    @property
    def address(self):
        """Return the adapter MAC address."""
        return 'DC:A6:32:65:8A:AB'
        return self.adapter_property.Get(self.ADAPTER_IFACE, 'Address')
  
    def listen(self):
        """
        Listen for connections coming from HID client
        """

        print('Waiting for connections')
        self.scontrol = socket.socket(socket.AF_BLUETOOTH,
                                      socket.SOCK_SEQPACKET,
                                      socket.BTPROTO_L2CAP)
        self.scontrol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sinterrupt = socket.socket(socket.AF_BLUETOOTH,
                                        socket.SOCK_SEQPACKET,
                                        socket.BTPROTO_L2CAP)
        self.sinterrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.scontrol.bind((self.address, self.P_CTRL))
        self.sinterrupt.bind((self.address, self.P_INTR))

        # Start listening on the server sockets
        self.scontrol.listen(1)  # Limit of 1 connection
        self.sinterrupt.listen(1)

        self.ccontrol, cinfo = self.scontrol.accept()
        print('{} connected on the control socket'.format(cinfo[0]))

        self.cinterrupt, cinfo = self.sinterrupt.accept()
        print('{} connected on the interrupt channel'.format(cinfo[0]))

    def send(self, msg):
        """
        Send HID message
        :param msg: (bytes) HID packet to send
        """
        print('Send Message: ', msg)
        #self.cinterrupt.send(bytes(bytearray(msg)))

    # send a string to the bluetooth host machine
    def send_string(self, message):
        try:
            print('Send Message: ', message)
            self.cinterrupt.send(bytes(message))
        except OSError as err:
            print('Send Error: ', error(err))
            error(err)
        
if __name__ == '__main__':
    # The sockets require root permission
    if not os.geteuid() == 0:
        sys.exit('Only root can run this script')

    #thread.start_new_thread(checkConnection)

    #DBusGMainLoop(set_as_default=True)
    # create and setup our device
    device = btServer()

    # start listening for socket connections
    device.listen()
    
    time.sleep(10)
    state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
    device.send_string(state)
    
    time.sleep(.35)
    state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]
    device.send_string(state)

    mainloop = GLib.MainLoop()
    mainloop.run()
