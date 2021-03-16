#############################################
##            MODULE VARIABLES
#############################################
print('Load hassio2bt')

from multiprocessing import Process
from dbus.mainloop.glib import DBusGMainLoop
import os, sys, time, json, asyncio, traceback, queue, threading

path = os.path.join(os.path.dirname(__file__), '../../imports/network')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/bluetooth')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/dbus')
sys.path.append(path)

import wsClient, btServer, btDevice, btProfile

_ioQueue = queue.Queue()
_sessionId = 0

_inOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "userEvent" : None,
    "agentEvent" : None
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
def inAgentEvent(userPost):
#############################################
    #print(f'***inUserPost for post: {userPost}')
    global _ioQueue, _sessionId
    
    content = json.loads(userPost)
    if(content['type'] == "auth_required"): return '{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}'    

    if(content['type'] == "auth_ok"):
        _sessionId += 1
        
        payload = {
            "id": _sessionId, 
            "type": "subscribe_events",	
            "event_type": "scripts_keyCode"
        }
    
        return json.dumps(payload)
    
    return 'NOPOST'
        
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
 
##########################
def outAgentPost():
##########################
    try:
        print(' \n***WAIT for Agent post')
        time.sleep(5)

        return bytes([ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ])
        #return bytes([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ])
            
    except:
        print('Abort getAgentPost', sys.exc_info()[0])
        traceback.print_exc()
        return None
  
#############################################
def onConnectSignal(interface, changed, path):
#############################################
    print(f'****CONNECTION ALERT****, interface: {interface}, connected: {changed["Connected"]}')
   
#############################################
def start(options={"controlPort": 17, "interruptPort": 19}):
#############################################
    print('Start hassio2bt')
    
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
            _inOptions['agentEvent'] = inAgentEvent
            threading.Thread(target=wsClient.start, args=(_inOptions,)).start()
        except:
            print('Abort wsClient: ', sys.exc_info()[0])
            traceback.print_exc()
    except:
        print('Abort hassio2bt: ', sys.exc_info()[0])
        traceback.print_exc()
  
#############################################
##                MAIN
#############################################   

# Run this module on main thread to unit test with following code
if __name__ == '__main__':

    start()
