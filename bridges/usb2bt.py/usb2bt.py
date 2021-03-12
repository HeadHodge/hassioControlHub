#############################################
##            MODULE VARIABLES
#############################################
print('Load usb2bt')

from multiprocessing import Process
from dbus.mainloop.glib import DBusGMainLoop
import os, sys, time, json, asyncio, traceback, queue, threading
if len(sys.argv) < 3: 
    print('Terminate usb2hassio, missing required zone name and/or event list arguments')
    print('Example: python3 usb2hassio.py masterBedroom 3,4,5,6')
    sys.exit()

path = os.path.join(os.path.dirname(__file__), '../../imports/usb')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/bluetooth')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/dbus')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps/usb2keyMap')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps/usb2btMap')
sys.path.append(path)

import usbServer, btServer, btDevice, btProfile, usb2keyMap, usb2btMap

_ioQueue = queue.Queue()

_inOptions = {
    "zone": sys.argv[1],
    "channels": sys.argv[2].split(','),
    "queue": _ioQueue,
    "userEvent": None,
    "agentEvent": None
}

_outAgentOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "userEvent" : None,
    "agentEvent" : None
}

_outControlOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "userEvent" : None,
    "agentEvent" : None
}
        
#############################################
def inUserEvent(post):
#############################################
    print(f'***USB: {post}')
    global _ioQueue, _sessionId
    
    key = usb2btMap.translate(post)
    if(key == None): return
    print(f'***KEY: {key}')
    _ioQueue.put(key)   
    
    return

##########################
def outAgentPost():
##########################
    print('***WAIT for BT post')

    while True:
        if(_ioQueue.empty()): continue
        key = _ioQueue.get()
        print(f'***DEQUEUE: {key}')
        print(f'************************************************************************* \n')
        print(f' \n*************************************************************************')
        print('***WAIT for USB USER post')

        return bytes(key)
        
    """
    try:
        print(' \n***WAIT for Agent post')
        time.sleep(5)

        return bytes([ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ])
        #return bytes([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ])
            
    except:
        print('Abort getAgentPost', sys.exc_info()[0])
        traceback.print_exc()
        return None
    """
    
##########################
def outControlPost():
##########################
    try:
        print(' \n***WAIT for Control post')

        #infinite wait to block control channel thread
        while True:
            pass

    except:
        print('Abort getControlPost', sys.exc_info()[0])
        traceback.print_exc()
        return None
   
#############################################
def onConnectSignal(interface, changed, path):
#############################################
    print(f'****CONNECTION ALERT****, interface: {interface}, connected: {changed["Connected"]}')
   
#############################################
def start(options={"controlPort": 17, "interruptPort": 19}):
#############################################
    print('Start usb2bt')
    
    try:
        # Enable ConnectSignal
        try:
            threading.Thread(target=btDevice.enableConnectSignal, args=(onConnectSignal,)).start()
            threading.Thread(target=btProfile.start).start()
            time.sleep(1)
        except:
            print('Abort enableConnectSignal: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start output module
        try:
            
            _outControlOptions['agentEvent'] = outControlPost
            threading.Thread(target=btServer.start, args=(options["controlPort"], _outControlOptions)).start()

            _outAgentOptions['agentEvent'] = outAgentPost
            threading.Thread(target=btServer.start, args=(options["interruptPort"], _outAgentOptions)).start()

            time.sleep(1)
        except:
            print('Abort btServer: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start input module
        try:
            _inOptions['userEvent'] = inUserEvent
            threading.Thread(target=usbServer.start, args=(_inOptions,)).start()
            time.sleep(1)
            print(f' \n*************************************************************************')
            print('***WAIT for USB USER post')
        except:
            print('Abort wsClient: ', sys.exc_info()[0])
            traceback.print_exc()
    except:
        print('Abort usb2bt: ', sys.exc_info()[0])
        traceback.print_exc()
  
#############################################
##                MAIN
#############################################   

# Run this module on main thread to unit test with following code
if __name__ == '__main__':

    start()
