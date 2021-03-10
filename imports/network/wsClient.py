#############################################
##            MODULES VARIABLES
#############################################
print('Load wsClient')
import asyncio
import sys, time, json, websockets, traceback

_options = None
_connection = None

##########################
def getGuestPost(hostPost):
##########################
    try:
        print(' \n***WAIT for GUEST post')

        if(_options.get('guestEvent', None) != None):
            post = _options['guestEvent'](hostPost)
            if(post != None): return post
            
        while True:
            if(_options['queue'].empty()): continue

            post = _options['queue'].get()
            return json.dumps(post)
            
    except:
        print('Abort getPayload', sys.exc_info()[0])
        traceback.print_exc()
        
##########################
async def onConnect(connection):
##########################
    loop = asyncio.get_running_loop()

    while True:
        try:    
            print(f' \n*************************************************************************')
            print('***WAIT for HOST post')
            post = await connection.recv()
            print(f' \n***HOST: {post}')
            if(_options.get('hostEvent', None) != None): await loop.run_in_executor(None, _options['hostEvent'], post)
            
            payload = await loop.run_in_executor(None, getGuestPost, post)
            print(f' \n***TRANSFER GUEST post: {payload}')
            await connection.send(payload)
            print(f'*************************************************************************\n \n')
        except:
            print('Abort onConnect', sys.exc_info()[0])
            traceback.print_exc()
            return

##########################
async def connect():
##########################
    global _connection
    
    print(f'connect to host: {_options["endpoint"]}')
        
    async with websockets.client.connect(_options["endpoint"]) as connection:
        print(f'connected to endpoint: {_options["endpoint"]}')
        await onConnect(connection)
        
    print(' \n***DISCONNECTED')
        
##########################
def start(options):
##########################
    print('Start wsClient')
    global _options

    try:    
        _options = options

        asyncio.set_event_loop(asyncio.new_event_loop())

        #while True:
        try:
            asyncio.get_event_loop().run_until_complete(connect())
        except:
            print('Abort: run_until_complete(connect()', sys.exc_info()[0])
            traceback.print_exc()
    except:
        print('Abort wsClient.py', sys.exc_info()[0])
        traceback.print_exc()

##########################
#         MAIN
##########################
# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    pass