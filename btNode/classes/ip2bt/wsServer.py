#############################################
##            GLOBAL VARIABLES
#############################################
import sys, time, json, websockets
import asyncio

class wsServer:
    """
    """
    
    def __init__(self, pname):
        print('Starting wsServer')
        pname('pissy')
        #self._ip = ip
        #self._port = port
        start_server = websockets.serve(self.onConnect, "127.0.0.1", 8181)
        print('Server Created')
        #eventloop = asyncio.new_event_loop()
        eventloop = asyncio.get_event_loop()
        #self.asyncio.set_event_loop(eventloop)
        eventloop.run_until_complete(start_server)
        #eventloop.run_forever()

    async def onConnect(self, websocket, path):
        #global myName         
        print('Connected', myName)

        try:
            await websocket.send('{"format": "greeting", "greeting": "Hello?", "from": ""}')
            async for text in websocket:
                #print('received text: ', json.loads(text))
                await websocket.send('{"format": "reply", "reply": "Got It"}')
        except Exception as e:
            print(e)
        finally:
            print('Disconnected')
 