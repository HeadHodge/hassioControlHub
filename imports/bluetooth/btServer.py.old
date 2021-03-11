#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
"""
create a bluetooth device to emulate a HID keyboard
"""
#############################################
##            MODULE VARIABLES
#############################################
print("Load btServer")

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
import traceback
import os, sys, time, json, socket
import asyncio, queue, dbus
DBusGMainLoop(set_as_default=True)

_dataOut = None
_isConnected = 0
_deviceAddress = 'DC:A6:32:65:8A:AB'
_systemBus = dbus.SystemBus()

P_CTRL = 17 # Service port - must match port configured in SDP record
P_INTR = 19 # Service port - must match port configured in SDP record#Interrrupt port

#############################################
def onSignal(sender1=None, sender2=None, sender3=None):
#############################################
    dBusProperty = dbus.Interface(_system_bus.get_object('org.bluez', '/org/bluez/hci0/dev_80_FD_7A_4A_DB_39'), 'org.freedesktop.DBus.Properties')
    _bluetoothState = dBusProperty.Get('org.bluez.Device1', 'Connected')
    print(f'****onSignal called from: {sender1}, isConnected: {_bluetoothState}****')

#############################################
def onDbusSignal(sender1=None, sender2=None, sender3=None):
#############################################
    print(f'****onDbusSignal called from: {sender1}****')
    
    myproperty = dbus.Interface(_system_bus.get_object('org.bluez', '/org/bluez/hci0/dev_80_FD_7A_4A_DB_39'), 'org.freedesktop.DBus.Properties')
    print('bluetooth connection state: ', myproperty.Get('org.bluez.Device1', 'Connected'))
  
#############################################
def connect():
#############################################
    """
    Listen for connections coming from HID client
    """

    # Socket server & client objects for hid control
    scontrol = None
    ccontrol = None
        
    # Socket server & client object for hid interrupt
    sinterrupt = None
    cinterrupt = None
    
    while True:
        print(f' \nwait for bluetooth connections on {_deviceAddress} ports {P_CTRL} and {P_INTR}')

        if(scontrol): scontrol.close
        scontrol = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        scontrol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        scontrol.bind((_deviceAddress, P_CTRL))
        scontrol.listen(1) # Limit of 1 connection
        ccontrol, cinfo = scontrol.accept() # Block until connected
        print(f'{cinfo[0]} connected to control channel')
        
        if(sinterrupt): sinterrupt.close
        sinterrupt = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        sinterrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sinterrupt.bind((_deviceAddress, P_INTR))
        sinterrupt.listen(1) # Limit of 1 connection
        cinterrupt, cinfo = sinterrupt.accept() # Block until connected
        print(f'{cinfo[0]} connected to interrupt channel')
        
        time.sleep(5)
        
        while True:
            if(_dataOut.empty() == True): continue
            dataOut = _dataOut.get()
            print('sendData: ', dataOut)
             
            try:
               cinterrupt.send(bytes(dataOut))
            except:
                print(f'send dataOut error: {sys.exc_info()[0]}')
                traceback.print_exc()
                break
        
#############################################
def start(options):
#############################################
    print("Start btServer")
    global _options

    try:
        _options = options

        dBusProperty = dbus.Interface(_systemBus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
        _deviceAddress = dBusProperty.Get('org.bluez.Adapter1', 'Address')
        print(f'deviceAddress: {_deviceAddress}')
        
        _systemBus.add_signal_receiver(onSignal, signal_name='PropertiesChanged', path='/org/bluez/hci0/dev_80_FD_7A_4A_DB_39')
        print(f'enabled PropertiesChanged signal')

        connect()
        
        # Start btOutput event loop
        print('start btServer eventLoop')
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort btServer: ', sys.exc_info()[0])
        traceback.print_exc()
    
#############################################
##                MAIN
#############################################   
DBusGMainLoop(set_as_default=True)

# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    start()
    
"""
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
    # The sockets require root permission
    if not os.geteuid() == 0:
        sys.exit('Only root can run this script')

    try:
        device = btServer()
    
        time.sleep(10)
        state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
        device.send_string(state)
    
        time.sleep(.35)
        state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]
        device.send_string(state)

        mainloop = GLib.MainLoop()
        mainloop.run()
    except:
        print('\n! Received keyboard interrupt, quitting threads.\n')
"""