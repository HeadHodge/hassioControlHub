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
    "userEvent": None,
    "agentEvent": None
   }
 
def inUserEvent(post):
    print(f' \n*************************************************************************')
    print(f'***INPUT: {post}')
    global _ioQueue, _sessionId
    
    if(post.get('command', None) == 'Echo'): print('ignore Echo'); return
    
    key = usb2keyMap.translateKey(post)
    if(key == None): return
    #print(f' \n***TRANSLATE: {key}')
    
    hassioSequence = key2hassioMap.translateKey(key)
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
        
        print(f' \n***QUEUE: {task}')
        _ioQueue.put(payload)
 
 
def outUserEvent(post):
    print(f'outUserEvent: {post}')

    content = json.loads(post)
    if(content['type'] == "auth_required"):
        _ioQueue.put('{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}')
    
def outAgentEvent():
    print(f'outAgentEvent')
    
    while True:
        if(_ioQueue.empty()): continue

        post = _ioQueue.get()
        #print(f'\n***DEQUEUE: {post}')
        return post
    
    return None
    
#############################################
##                MAIN
#############################################
try:
    # Start wsServer Module
    try:
        _inOptions['userEvent'] = inUserEvent
        usbServer = threading.Thread(target=usbServer.start, args=(_inOptions,))
        usbServer.start()
    except:
        print('Abort run usbServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start wsClient Module
    try:
        _outOptions['userEvent'] = outUserEvent
        _outOptions['agentEvent'] = outAgentEvent
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
