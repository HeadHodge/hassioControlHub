#############################################
##            GLOBAL VARIABLES
#############################################
import sys, time, json, websockets
import asyncio

class wsServer:
    """
    """
    
    def __init__(self, options={"ip":"127.0.0.1", "port":8181}):
        print('Starting wsServer', options)
        
        start_server = websockets.serve(self.onConnect, options['ip'], options['port'])
        print('Server Created')
        eventloop = asyncio.get_event_loop()
        eventloop.run_until_complete(start_server)
        print('Connecting')
        eventloop.run_forever()
    
    async def sleep(self):
            print('sleep')
            await asyncio.sleep(1)
        
    async def onConnect(self, websocket, path):
        print('Connected')

        try:
            await websocket.send('{"format": "greeting", "greeting": "Hello?", "from": ""}')
            async for text in websocket:
                print('received text: ', json.loads(text))
                await websocket.send('{"format": "reply", "reply": "Got It"}')
        except Exception as e:
            print(e)
        finally:
            print('Disconnected')
 