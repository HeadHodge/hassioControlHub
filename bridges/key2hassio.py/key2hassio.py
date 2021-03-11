#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassio')
    
from gi.repository import GLib
from multiprocessing import Process
import os, sys, time, json, traceback, queue, threading, asyncio

"""
if len(sys.argv) < 3: 
    print('Terminate usb2hassio, missing required zone name and/or event list arguments')
    print('Example: python3 usb2hassio.py masterBedroom 3,4,5,6')
    sys.exit()
"""

path = os.path.join(os.path.dirname(__file__), '../../imports/network')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps/key2hassioMap')
sys.path.append(path)
import httpServer, wsClient, wsioServer, key2hassioMap

_ioQueue = queue.Queue()
_sessionId = 0

# keyCode Input
_inputOptions = {
    #"zone": sys.argv[1],
    #"channels": sys.argv[2].split(','),
    "port": "8080",
    "queue": _ioQueue,
    "userEvent" : None,
    "agentEvent" : None
   }

# hassio service events Output
_outputOptions = {
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
    print(f' \n***INPUT: {post}')
    global _ioQueue, _sessionId
    
    if(post.get('command', None) == 'Echo'): print('ignore Echo'); return
    
    hassioSequence = key2hassioMap.translateKey(post)
    if(hassioSequence == None): print(f'Abort inHostEvent, invalid keyCode: "{post["code"]}"'); return
    
    for task in hassioSequence:
        key = list(task.keys())[0]
        data = task[key]
        command = key.split('/')
        if(command[0] == 'sleep'): time.sleep(int(data)); continue
        
        _sessionId += 1
        
        payload = {
            "id": _sessionId, 
            "type": "call_service",	
            "domain": command[0],
            "service": command[1],
            "service_data": data
        }
        
        print(f' \n***QUEUE: {task}')
        _ioQueue.put(payload)
        
#############################################
def outAgentEvent(userPost):
#############################################
    #print(f'***inputGuestEvent for userPost: {userPost}')
    global _ioQueue, _sessionId
    
    post = json.loads(userPost)
    if(post['type'] == "auth_required"): return '{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}'    
    
    return None

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
        _inputOptions['userEvent'] = inUserEvent
        wsServer = threading.Thread(target=wsioServer.start, args=(_inputOptions,))
        wsServer.start()
    except:
        print('Abort wsServer: ', sys.exc_info()[0])
        traceback.print_exc()
        
    # Start wsClient Module
    try:
        _outputOptions['agentEvent'] = outAgentEvent
        wsClient = threading.Thread(target=wsClient.start, args=(_outputOptions,))
        wsClient.start()
    except:
        print('Abort run wsClient: ', sys.exc_info()[0])
        traceback.print_exc()

except:
    print('Abort key2hassio', sys.exc_info()[0])
    traceback.print_exc()
