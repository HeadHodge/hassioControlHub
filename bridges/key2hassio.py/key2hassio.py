#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassio')
    
from gi.repository import GLib
from multiprocessing import Process
import os, sys, time, json, traceback, queue, threading, asyncio

path = os.path.join(os.path.dirname(__file__), '../../imports/network')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps/key2hassioMap')
sys.path.append(path)
import httpServer, wsClient, wsioServer, key2hassioMap

_ioQueue = queue.Queue()
_sessionId = 0

# keyCode Input
_inOptions = {
    "port": "8080",
    "queue": _ioQueue,
    "firstPost": "User",
    "userEvent" : None,
    "agentEvent" : None
   }

# hassio service events Output
_outOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "firstPost": "User",
    "userEvent" : None,
    "agentEvent" : None
}
 
#############################################
def inPosts(post):
#############################################
    print(f' \n***inUSER: {post}')
    global _ioQueue, _sessionId
    
    #if(post.get('command', None) == 'Echo'): print('ignore Echo'); return
    
    hassioSequence = key2hassioMap.translate(post)
    if(hassioSequence == None): print(f'Abort inUserEvent, invalid keyCode: "{post["code"]}"'); return
    
    for task in hassioSequence:
        key = list(task.keys())[0]
        data = task[key]
        command = key.split('/')
        if(command[0] == 'sleep'): time.sleep(int(data)); continue
        
        _sessionId += 1
        
        post = {
            "id": _sessionId, 
            "type": "call_service",	
            "domain": command[0],
            "service": command[1],
            "service_data": data
        }
        
        #print(f' \n***QUEUE: {post}')
        _ioQueue.put(post)
        
#############################################
def outPosts(post):
#############################################
    print(f' \n***outUSER: {post}')

    content = json.loads(post)
    if(content['type'] == "auth_required"):
        post = {
            "type": "auth",
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"
        }
        
        print(f' \n***outTRANSFER: {post}')
        print(f' \n***outUser WAIT')
        return post
    
    print(' \n***outAGENT WAIT')    
    while True:
        if(_ioQueue.empty()): continue
        post = _ioQueue.get()
        
        print(f' \n***outTRANSFER: {post}')
        print(f' \n***outUser WAIT')
        return post
    
    return None
    
"""        
#############################################
def outAgentEvent():
#############################################
    print('***wsAGENT WAIT')    
    
    while True:
        if(_ioQueue.empty()): continue

        post = _ioQueue.get()
        return post
    
    return None
"""

#############################################
##                MAIN
#############################################
try:
    # Start httpServer Module
    try:
        httpServer = threading.Thread(target=httpServer.start)
        httpServer.start()
    except:
        print('Abort httpServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start wsServer Module
    try:
        _inOptions['userEvent'] = inPosts
        wsServer = threading.Thread(target=wsioServer.start, args=(_inOptions,))
        wsServer.start()
    except:
        print('Abort wsServer: ', sys.exc_info()[0])
        traceback.print_exc()
        
    # Start wsClient Module
    try:
        _outOptions['userEvent'] = outPosts
        #_outOptions['agentEvent'] = outAgentEvent
        wsClient = threading.Thread(target=wsClient.start, args=(_outOptions,))
        wsClient.start()
    except:
        print('Abort run wsClient: ', sys.exc_info()[0])
        traceback.print_exc()

except:
    print('Abort key2hassio', sys.exc_info()[0])
    traceback.print_exc()
