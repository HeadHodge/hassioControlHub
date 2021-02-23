#############################################
##            GLOBAL VARIABLES
#############################################
import asyncio
import sys, time, json, websockets

class wsServer:
    """
    """
    
    def __init__(self, ip="127.0.0.1", port=8181):
        print('Starting wsServer')
        self._ip = ip
        self._port = port
        #start_server = websockets.serve(onConnect, "127.0.0.1", 8181)
        #print('Server Created')

    async def onConnect(websocket, path):
        print('Connected')

        try:
            await websocket.send('{"format": "greeting", "greeting": "Hello?", "from": ""}')
            async for text in websocket:
                print('received text: ', json.loads(text))
                await websocket.send('{"format": "reply", "reply": "Got It"}')
        finally:
            print('Disconnected')

    async def start():
        print('Start server')

    start_server = websockets.serve(onConnect, "127.0.0.1", 8181)
    print('Server Created')

    asyncio.get_event_loop().run_until_complete(start_server)
    print('Wait for Connection')
    asyncio.get_event_loop().run_forever()
