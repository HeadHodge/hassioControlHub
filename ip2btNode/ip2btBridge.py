#############################################
##            GLOBAL VARIABLES
#############################################
print('Load ip2btBridge')
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
from multiprocessing import Process
import os, sys, time, asyncio, traceback, queue

sys.path.append('/inputHub/ip2btNode/modules')
import wsServer
import btServer
import dbus

DBusGMainLoop(set_as_default=True)
_bluetoothData = queue.Queue()
_bluetoothState = 0
_bluetoothAddress = '0:0:0:0:0:0'
_system_bus = dbus.SystemBus()

def onSignal(sender1=None, sender2=None, sender3=None):
    dBusProperty = dbus.Interface(_system_bus.get_object('org.bluez', '/org/bluez/hci0/dev_80_FD_7A_4A_DB_39'), 'org.freedesktop.DBus.Properties')
    _bluetoothState = dBusProperty.Get('org.bluez.Device1', 'Connected')
    print(f'****onSignal called from: {sender1}, isConnected: {_bluetoothState}****')
         
def ipInput():
    print('Start ipInput')

    try:
        # Start wsServer
        wsServer.start()
       
        # Start event loop
        print('start ipInput eventLoop')
        eventloop = asyncio.get_event_loop()
        eventloop.run_forever()
    except:
        print('Abort ipInput', sys.exc_info()[0])
        traceback.print_exc()

def btOutput():
    print('Start btOutput')
    
    try:
        # Start btServer
        btServer.start(_bluetoothData, _bluetoothState)

        # Start btOutput event loop
        print('start btOutput eventLoop')
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort btOutput: ', sys.exc_info()[0])
        traceback.print_exc()
   
try:
    state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
    print('send string: ', state)
    _bluetoothData.put([ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ])
    
    state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]            
    print('send string: ', state)
    _bluetoothData.put([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ])

    # Start ipInput Module
    try:
        p = Process(target=ipInput)
        p.start()
    except:
        print('Abort start ipInput: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start btOutput Module
    try:
        p = Process(target=btOutput)
        p.start()
    except:
        print('Abort start btOutput: ', sys.exc_info()[0])
        traceback.print_exc()
        
    # Connect to dbus
    try:
        dBusProperty = dbus.Interface(_system_bus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
        _bluetoothAddress = dBusProperty.Get('org.bluez.Adapter1', 'Address')
        print(f'bluetooth address: {_bluetoothAddress}')
        
        _system_bus.add_signal_receiver(onSignal, signal_name='PropertiesChanged', path='/org/bluez/hci0/dev_80_FD_7A_4A_DB_39')
        print(f'enabled bluetooth PropertiesChanged signal')
        
    except:
        print('Abort start btOutput: ', sys.exc_info()[0])
        traceback.print_exc()



    # Start event loop
    print('Start ip2btBridge eventLoop')
    eventloop = GLib.MainLoop()
    eventloop.run()
    
except:
    print('Abort ip2btBridge.py', sys.exc_info()[0])
    traceback.print_exc()
