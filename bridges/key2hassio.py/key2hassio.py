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

# keyCode formatted Input
_inputOptions = {
    #"zone": sys.argv[1],
    #"channels": sys.argv[2].split(','),
    "port": "8080",
    "queue": _ioQueue,
    "onEvent": None
   }

# hassio service events Output
_outputOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": _ioQueue,
    "onEvent": None
   }
 
#############################################
def onInputEvent(eventType='key', eventData=''):
#############################################
    print(f'***INPUT: {eventData}')
    
    if(eventData.get('command', None) == 'Echo'): print('ignore Echo'); return
    return
    
    key = usb2keyMap.translateKey(eventData)
    if(key == None): return
    print(f'***TRANSLATE: {key}')
    
    hassioSequence = key2hassioMap.translateKey(key)
    if(hassioSequence == None): return
    
    for task in hassioSequence:
        print(f'***OUTPUT: {task}')
        _ioQueue.put(task)
        
    #print(' \n***Queue: ', hassioSequence)
    
#############################################
def onOutputEvent(eventType='post', eventData=''):
#############################################
    print(f' \n*************************************************************************')
    print(f'***REPLY: {eventData}')
    global _ioQueue, _sessionId
    
    content = json.loads(eventData)
    if(content['type'] == "auth_required"): print('auth_required'); return '{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}'       

    print(f'Wait for Output ')
    
    while True:
        if(_ioQueue.empty()): continue #await asyncio.sleep(.1);
        
        #send payload to hassio server
        task = _ioQueue.get()
        #print(f'deQueue task: {task}')
        
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
        
        #print(' \n***Output: ', payload)
        return json.dumps(payload)
            
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
        _inputOptions['onEvent'] = onInputEvent
        wsServer = threading.Thread(target=wsioServer.start, args=(_inputOptions,))
        wsServer.start()
    except:
        print('Abort wsServer: ', sys.exc_info()[0])
        traceback.print_exc()
        
    # Start wsClient Module
    try:
        _outputOptions['onEvent'] = onOutputEvent
        wsClient = threading.Thread(target=wsClient.start, args=(_outputOptions,))
        wsClient.start()
    except:
        print('Abort run wsClient: ', sys.exc_info()[0])
        traceback.print_exc()

except:
    print('Abort key2hassio', sys.exc_info()[0])
    traceback.print_exc()



#eventData='{"type": "command", "command": "Louder", "id": "webClient", "zone": "livingRoom", "device": "webBrowser"}'
#print(f'key2hassio translation: {key2hassioMap.translateKey(json.loads(eventData), reply)}')
