#############################################
##            GLOBAL VARIABLES
#############################################

import asyncio
import sys, time, json, websockets

async def onConnect(websocket):
    try:
        print('Connected')
        
        async for text in websocket:
            print('received text: ', json.loads(text))
            await websocket.send('{"format": "reply", "reply": "Hi There"}')
    finally:
        print('Disconnected')

async def connect(endPoint):
    async with websockets.connect(endPoint) as websocket:
        await onConnect(websocket)

asyncio.get_event_loop().run_until_complete(connect("ws://127.0.0.1:8181"))


"""
import websocket
import sys, time, json, threading, _thread as thread
              
###################
def checkConnection(connection):
###################
    print("Enter checkConnection")

    time.sleep(300)
    connection.send('{' + f'"type": "command", "command": "Ping", "zone": "{zone}", "device": "usb remote"' + '}')
    checkConnection(connection)
    
###################
# onMessage
###################
def onMessage(connection, text):
    print("Enter onMessage, received: ", text)
    payload = json.loads(text)
    if(payload['format'] == 'greeting'): connection.send('{"format": "reply", "reply": "Hi There"}')

###################
# onError
###################
def onError(connection, error):
    print(f"Enter onError: ", error)
    sys.exit(1)

###################
# onClose
###################
def onClose(connection):
    print("Enter onClose")
         
###################
# onOpen
###################
def onOpen(connection):
    print("Enter onOpen USB Input")
	
#############################################
##                MAIN
##Open server to listen for control input
#############################################
print('Started mqttClient.py')
websocket.enableTrace(True)

_webSocket = websocket.WebSocketApp("ws://127.0.0.1:8181/",
    on_message = onMessage,
    on_error = onError,
    on_close = onClose,
    on_open = onOpen) 

_webSocket.run_forever()
"""