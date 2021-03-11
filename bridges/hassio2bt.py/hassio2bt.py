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

import wsClient, btServer

_ioQueue = queue.Queue()
_sessionId = 0

_inOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "guestEvent" : None,
    "hostEvent" : None
}

_outAgentOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "guestEvent" : None,
    "hostEvent" : None
}

_outControlOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "guestEvent" : None,
    "hostEvent" : None
}
        
#############################################
def inGuestEvent(hostPost):
#############################################
    #print(f'***inGuestEvent for hostPost: {hostPost}')
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
        

##########################
def getControlPost():
##########################
    try:
        print(' \n***WAIT for Control post')

        while True:
            pass
            #print('sleep')
            #time.sleep(30)
    except:
        print('Abort getControlPost', sys.exc_info()[0])
        traceback.print_exc()
        return None
 
##########################
def getAgentPost():
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
def start(options={"controlPort": 17, "interruptPort": 19}):
#############################################
    print('Start hassio2bt')
    
    try:
        # Start input module
        try:
            _inOptions['guestEvent'] = inGuestEvent
            threading.Thread(target=wsClient.start, args=(_inOptions,)).start()
        except:
            print('Abort wsClient: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start output module
        try:
            _outControlOptions['agentEvent'] = getControlPost
            threading.Thread(target=btServer.start, args=(options["controlPort"], _outControlOptions)).start()

            _outAgentOptions['agentEvent'] = getAgentPost
            threading.Thread(target=btServer.start, args=(options["interruptPort"], _outAgentOptions)).start()
        except:
            print('Abort btServer: ', sys.exc_info()[0])
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
    """        
    # Start event loop
    print('Start ip2btBridge eventLoop')
    eventloop = GLib.MainLoop()
    eventloop.run()
    """        

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
