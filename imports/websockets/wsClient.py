#############################################
##            MODULES VARIABLES
#############################################
print('Load wsClient')
import asyncio
import sys, time, json, websockets, traceback

_options = None
_connection = None

##########################
def pname(name):
##########################
    print(name)

##########################
async def onInput(post):
##########################
    try:    
        reply = await _options['onEvent']('post', post)
        print('reply: ', reply)
        if(reply == None): return
        await _connection.send(reply)
    except:
        print('Abort onInput', sys.exc_info()[0])
        traceback.print_exc()

##########################
async def connect():
##########################
    global _connection
    
    while True:
        print(f'connect to endpoint: {_options["endpoint"]}')
        
        async with websockets.connect(_options["endpoint"]) as _connection:
            print(f'connected to endpoint: {_options["endpoint"]}')
            
            async for post in _connection:
                 await onInput(post)
    
        print('Disconnected')
        
##########################
def start(options):
##########################
    print('Start wsClient')
    global _options

    try:    
        _options = options
        asyncio.set_event_loop(asyncio.new_event_loop())

        while True:
            asyncio.get_event_loop().run_until_complete(connect())
        #asyncio.get_event_loop().run_forever()
    except:
        print('Abort wsClient.py', sys.exc_info()[0])
        traceback.print_exc()

##########################
#         MAIN
##########################
# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    pass