#############################################
##            MODULE VARIABLES
#############################################
print('Load key2bt')

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
from multiprocessing import Process
import os, sys, time, json, asyncio, traceback, queue, threading

path = os.path.join(os.path.dirname(__file__), '../../imports/network')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/bluetooth')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/dbus')
sys.path.append(path)

import wsClient, btServer, dbus

DBusGMainLoop(set_as_default=True)
_ioQueue = queue.Queue()
_sessionId = 0
_bluetoothState = 0
_bluetoothAddress = '0:0:0:0:0:0'
_system_bus = dbus.SystemBus()

# keyCode Input
_inputOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "guestEvent" : None,
    "hostEvent" : None
}

#############################################
def onSignal(sender1=None, sender2=None, sender3=None):
#############################################
    dBusProperty = dbus.Interface(_system_bus.get_object('org.bluez', '/org/bluez/hci0/dev_80_FD_7A_4A_DB_39'), 'org.freedesktop.DBus.Properties')
    _bluetoothState = dBusProperty.Get('org.bluez.Device1', 'Connected')
    print(f'****onSignal called from: {sender1}, isConnected: {_bluetoothState}****')
         
#############################################
def ipInput():
#############################################
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

#############################################
def btOutput():
#############################################
    print('Start btOutput')
    
    try:
        # Start btServer
        btServer.start(_ioQueue, _bluetoothState)

        # Start btOutput event loop
        print('start btOutput eventLoop')
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort btOutput: ', sys.exc_info()[0])
        traceback.print_exc()
        
#############################################
def inputGuestEvent(hostPost):
#############################################
    #print(f'***inputGuestEvent for hostPost: {hostPost}')
    global _ioQueue, _sessionId
    
    post = json.loads(hostPost)
    if(post['type'] == "auth_required"): return '{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}'    

    if(post['type'] == "auth_ok"):
        _sessionId += 1
        
        payload = {
            "id": _sessionId, 
            "type": "subscribe_events",	
            "event_type": "state_changed"
        }
    
        return json.dumps(payload)
    
    return 'NOPOST'

#############################################
def inputHostEvent(post):
#############################################
    #print(f'***inputHostEvent post: {post}')
    global _ioQueue, _sessionId
        
    
#############################################
##                MAIN
#############################################   
try:
    # Start wsClient Module
    try:
        #_inputOptions['hostEvent'] = inputHostEvent
        _inputOptions['guestEvent'] = inputGuestEvent
        wsClient = threading.Thread(target=wsClient.start, args=(_inputOptions,))
        wsClient.start()
    except:
        print('Abort run wsClient: ', sys.exc_info()[0])
        traceback.print_exc()
    """
    state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
    print('send string: ', state)
    _ioQueue.put([ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ])
    
    state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]            
    print('send string: ', state)
    _ioQueue.put([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ])
      
    # Start btOutput Module
    try:
        p = Process(target=btOutput)
        p.start()
    except:
        print('Abort start btOutput: ', sys.exc_info()[0])
        traceback.print_exc()
    """        
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



    """        
    # Start event loop
    print('Start ip2btBridge eventLoop')
    eventloop = GLib.MainLoop()
    eventloop.run()
    """        
    
except:
    print('Abort key2bt', sys.exc_info()[0])
    traceback.print_exc()
