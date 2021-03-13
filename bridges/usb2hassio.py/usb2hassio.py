#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassio')
    
from gi.repository import GLib
from multiprocessing import Process
import os, sys, time, json, traceback, queue, threading, asyncio
if len(sys.argv) < 3: 
    print('Terminate usb2hassio, missing required zone name and/or event list arguments')
    print('Example: python3 usb2hassio.py masterBedroom 3,4,5,6')
    sys.exit()

path = os.path.join(os.path.dirname(__file__), '../../imports/usb')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/network')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps/key2hassioMap')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps/usb2keyMap')
sys.path.append(path)
import wsClient, usbServer, usb2keyMap, key2hassioMap

_ioQueue = queue.Queue()
_sessionId = 0

# keyCode formatted Input
_inOptions = {
    "zone": sys.argv[1],
    "channels": sys.argv[2].split(','),
    "queue": _ioQueue,
    "firstPost": "User",
    "userEvent": None,
    "agentEvent": None
   }

# hassio service events Output
_outOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "firstPost": "User",
    "userEvent": None,
    "agentEvent": None
   }
 
def inPosts(post):
    print(f' \n***inUSER: {post}')
    global _ioQueue, _sessionId
    
    if(post.get('command', None) == 'Echo'): print('ignore Echo'); return
    
    key = usb2keyMap.translate(post)
    print(f' \n***TRANSLATE: {key}')
    if(key == None): return
    
    hassioSequence = key2hassioMap.translate(key)
    if(hassioSequence == None): return
    
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
        
        #print(f' \n***QUEUE: {task}')
        _ioQueue.put(payload)
 
 
def outPosts(post):
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
def outAgentEvent():
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
    # Start wsServer Module
    try:
        _inOptions['userEvent'] = inPosts
        usbServer = threading.Thread(target=usbServer.start, args=(_inOptions,))
        usbServer.start()
    except:
        print('Abort run usbServer: ', sys.exc_info()[0])
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



#eventData='{"type": "command", "command": "Louder", "id": "webClient", "zone": "livingRoom", "device": "webBrowser"}'
#print(f'key2hassio translation: {key2hassioMap.translateKey(json.loads(eventData), reply)}')
