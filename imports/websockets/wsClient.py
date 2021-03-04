#############################################
##            GLOBAL VARIABLES
#############################################
print('Load wsClient')
import asyncio
import sys, time, json, websockets, traceback

_options = None
_connection = None

async def onInput(post):
    print(f'received post: {post}')
    
    content = json.loads(post)
    if(content['format'] != 'greeting'): return
    await _connection.send('{"format": "reply", "reply": "Hi There"}')

async def connect():
    global _connection
    
    while True:
        print(f'connect to endpoint: {_options["endpoint"]}')
        
        async with websockets.connect(_options["endpoint"]) as _connection:
            print(f'connected to endpoint: {_options["endpoint"]}')
            
            async for post in _connection:
                await onInput(post)
    
        print('Disconnected')
 
def start(options):
    print('Start wsClient')
    global _options

    try:    
        _options = options
        
        while True:
            asyncio.get_event_loop().run_until_complete(connect())
    except:
        print('Abort wsClient.py', sys.exc_info()[0])
        traceback.print_exc()

