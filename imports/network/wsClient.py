#############################################
##            MODULES VARIABLES
#############################################
print('Load wsClient')
import asyncio
import sys, time, json, websockets, traceback

_options = None
_connection = None

##########################
def getAgentPost(userPost):
##########################
    try:
        print(' \n***WAIT for AGENT post')

        if(_options.get('agentEvent', None) != None):
            post = _options['agentEvent'](userPost)
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
        print(f' \n*************************************************************************')
        print('***WAIT for USER post')
        post = await connection.recv()
        print(f' \n***USER: {post}')
        if(_options.get('userEvent', None) != None): await loop.run_in_executor(None, _options['userEvent'], post)
            
        payload = await loop.run_in_executor(None, getAgentPost, post)
        print(f' \n***TRANSFER AGENT post: {payload}')
        if(payload != 'NOPOST'): await connection.send(payload)
        print(f'*************************************************************************\n \n')
        
##########################
async def userPosts(connection, options):
##########################
    #print(f'get userPosts')
    if(options.get('userEvent', None) == None): print(f'***DISABLE userPosts'); return
    loop = asyncio.get_running_loop()
    
    while True:
        print('\n***WAIT for USER')
        post = await connection.recv()
        print(f'\n***USER: {post}')
        await loop.run_in_executor(None, options['userEvent'], post)
        continue
        
##########################
async def agentPosts(connection, options):
##########################
    #print(f'get agentPosts')
    if(options.get('agentEvent', None) == None): print(f'***DISABLE agentPosts'); return
    loop = asyncio.get_running_loop()

    while True:
        print(f' \n*************************************************************************')
        print('***WAIT for AGENT')
        post = await loop.run_in_executor(None, options['agentEvent'])
        if(post == None): await asyncio.sleep(0); continue
        print(f'\n***TRANSFER POST: {post}')
        await connection.send(post)

##########################
async def connect(options):
##########################
    global _connection
    
    try:    
        print(f' \n***CONNECT: {_options["endpoint"]}')
        
        async with websockets.client.connect(_options["endpoint"]) as connection:
            #userTask = asyncio.create_task(userPosts(connection))
            #agentTask = asyncio.create_task(agentPosts(connection))
            print(f'connected to endpoint: {_options["endpoint"]}')
            await asyncio.gather(
                agentPosts(connection, options),
                userPosts(connection, options)
            )

            #await onConnect(connection)
            #asyncio.get_event_loop().run_forever()
        
        print(' \n***DISCONNECTED')
    except:
        print('Abort onConnect', sys.exc_info()[0])
        traceback.print_exc()
       
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
            asyncio.get_event_loop().run_until_complete(connect(options))
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