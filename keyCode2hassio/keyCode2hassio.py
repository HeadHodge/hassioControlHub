#############################################
##            MODULE VARIABLES
#############################################
print('Load keyCode2hassio')
from gi.repository import GLib
from multiprocessing import Process
import os, sys, time, json, traceback, queue

path = os.path.join(os.path.dirname(__file__), '../imports/websockets')
sys.path.append(path)
import wsClient, wsServer

# keyCode formatted Input
_inputOptions = {
    "endpoint": "ws://192.168.0.164:8080",
    "address": "192.168.0.164",
    "port": "8080",
    "path": "/",
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
   
async def onInputEvent(eventType='post', eventData=''):
    print(f'onInputEvent type: {eventType}, type: {eventData}')
    content = json.loads(eventData)
    return '{"format": "reply", "reply": "Got It"}'
 
async def onOutputEvent(eventType='post', eventData=''):
    print(f'onOutputEvent type: {eventType}, type: {eventData}')
    content = json.loads(eventData)

    if(content['type'] != "auth_required"): return None
    print('auth_required')
    return '{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}'       
   
#############################################
##                MAIN
#############################################
try:
    # Start wsServer Module
    try:
        _inputOptions['onEvent'] = onInputEvent
        wsServer = Process(target=wsServer.start, args=(_inputOptions,))
        wsServer.start()
    except:
        print('Abort run wsServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start wsClient Module
    try:
        _outputOptions['onEvent'] = onOutputEvent
        wsClient = Process(target=wsClient.start, args=(_outputOptions,))
        wsClient.start()
    except:
        print('Abort run wsClient: ', sys.exc_info()[0])
        traceback.print_exc()
except:
    print('Abort keyCode2hassio.py', sys.exc_info()[0])
    traceback.print_exc()
