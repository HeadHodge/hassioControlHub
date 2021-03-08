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
        payload = await _options['onEvent']('post', post)
        #print(' \nsend payload: ', payload)
        #if(payload == None): return
        await _connection.send(payload)
    except:
        print('Abort onInput', sys.exc_info()[0])
        traceback.print_exc()
        
##########################
async def onConnect(connection):
##########################
    while True:
        try:    
            post = await connection.recv()
            print(f'POST: {post}')
            
            #payload = await _options['onEvent']('post', post)
            payload = await asyncio.get_running_loop().run_in_executor(None, _options['onEvent']('post', post))

            await connection.send(payload)
            
        except:
            print('Abort onInput', sys.exc_info()[0])
            traceback.print_exc()
            return

##########################
async def connect():
##########################
    global _connection
    
    print(f'connect to endpoint: {_options["endpoint"]}')
        
    async with websockets.client.connect(_options["endpoint"]) as connection:
        print(f'connected to endpoint: {_options["endpoint"]}')
            
        post = await connection.recv()
        print(f'POST: {post}')
        content = json.loads(post)

        if(content['type'] == "auth_required"): print('auth_required')
        await connection.send('{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"}')       
        print('auth_sent')

        await onConnect(connection)
        
    print('Disconnected')
        
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