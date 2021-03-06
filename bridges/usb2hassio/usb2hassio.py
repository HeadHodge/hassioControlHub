#############################################
##            MODULE VARIABLES
#############################################
print('Load keyCode2hassio')
    
from gi.repository import GLib
from multiprocessing import Process
import os, sys, time, json, traceback, queue

if len(sys.argv) < 3: 
    print('Terminate usb2hassio, missing required zone name and/or event list arguments')
    print('Example: python3 usb2hassio.py masterBedroom 3,4,5,6')
    sys.exit()

path = os.path.join(os.path.dirname(__file__), '../../imports/usb')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/websockets')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/key2hassioMap')
sys.path.append(path)
import wsClient, usbServer, key2hassioMap

# keyCode formatted Input
_inputOptions = {
    "zone": sys.argv[1],
    "channels": sys.argv[2].split(','),
    "queue": None,
    "onEvent": None
   }

# hassio service events Output
_outputOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "queue": None,
    "onEvent": None
   }
   
def onInputEvent(eventType='key', eventData=''):
    print(f'onInputEvent type: {eventType}, type: {eventData}')
    #keyCodeMap.translate(json.loads(eventData))
    #return '{"format": "reply", "reply": "Got It"}'
 
async def onOutputEvent(eventType='post', eventData=''):
    print(f'onOutputEvent type: {eventType}, type: {eventData}')
    content = json.loads(eventData)

    if(content['type'] != "auth_required"): return None
    print('auth_required')
    return '{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}'       

def reply(content):
    print(f'reply: {content}')
    
#############################################
##                MAIN
#############################################

#eventData='{"type": "command", "command": "Louder", "id": "webClient", "zone": "livingRoom", "device": "webBrowser"}'
#print(f'key2hassio translation: {key2hassioMap.translateKey(json.loads(eventData), reply)}')

try:
    # Start wsServer Module
    try:
        _inputOptions['onEvent'] = onInputEvent
        usbServer = Process(target=usbServer.start, args=(_inputOptions,))
        usbServer.start()
    except:
        print('Abort run usbServer: ', sys.exc_info()[0])
        traceback.print_exc()
    """
    # Start wsClient Module
    try:
        _outputOptions['onEvent'] = onOutputEvent
        wsClient = Process(target=wsClient.start, args=(_outputOptions,))
        wsClient.start()
    except:
        print('Abort run wsClient: ', sys.exc_info()[0])
        traceback.print_exc()
    """
except:
    print('Abort keyCode2hassio.py', sys.exc_info()[0])
    traceback.print_exc()
