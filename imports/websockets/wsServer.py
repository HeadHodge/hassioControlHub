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
        asyncio.get_event_loop().run_until_complete(start_server)

        print(f'wait for connections on address: {options["address"]}, port: {options["port"]}')
        asyncio.get_event_loop().run_forever()

    except:
        print('Abort wsServer.py', sys.exc_info()[0])
        traceback.print_exc()

#######################################
#              MAIN
#######################################
