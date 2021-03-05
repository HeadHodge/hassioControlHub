#############################################
##            MODULE VARIABLES
#############################################
print('Load wsServer')
import sys, time, json, websockets
import asyncio, traceback

_options = None

#######################################
async def onInput(connection, post):
#######################################
    print('received post: ', json.loads(post))
    await connection.send('{"format": "reply", "reply": "Got It"}')
       
#######################################
async def onConnect(connection, path):
#######################################
    print('wsServer Connected')

    await connection.send('{"format": "greeting", "greeting": "Hello?", "from": ""}')
        
    async for post in connection:
        await onInput(connection, post)
 
#######################################
def start(options):
#######################################
    print('Start wsServer')
    global _options
    
    try:
        _options = options
        
        start_server = websockets.serve(onConnect, options["address"], options["port"])
        #start_server = websockets.serve(onConnect, '127.0.0.1', 8080)
        asyncio.get_event_loop().run_until_complete(start_server)

        print(f'wait for connections on address: {options["address"]}, port: {options["port"]}')
        asyncio.get_event_loop().run_forever()

    except:
        print('Abort wsServer.py', sys.exc_info()[0])
        traceback.print_exc()

#######################################
#              MAIN
#######################################
# Run this module on main thread to unit test with following code

if __name__ == "__main__":
    options = {
        "endpoint": "ws://127.0.0.1:8080/",
        "address": "127.0.0.1",
        "port": "8080",
        "path": "/",
        "queue": None,
        "onEvent": None
        }
        
    start(options)