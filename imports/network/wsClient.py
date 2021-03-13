#############################################
##            MODULES VARIABLES
#############################################
print('Load wsClient')
import asyncio
import sys, time, json, websockets, traceback

##########################
async def onConnection(connection, options):
##########################
    #if(options.get('userEvent', None) == None): print(f'***DISABLE userPosts'); return
    loop = asyncio.get_running_loop()

    if(options['firstPost'] == "Agent"):
        post = await loop.run_in_executor(None, options['userEvent'], None)
        if(post == None): return
        await connection.send(json.dumps(post))
    
    while True:
        #print('\n***wsUSER WAIT')
        
        post = await connection.recv()
        #print(f'\n***wsUSER: {post}')
        post = await loop.run_in_executor(None, options['userEvent'], post)
        
        if(post == None): continue
        #print(f'\n***wsTRANSFER POST: {post}')
        await connection.send(json.dumps(post))
        
##########################
async def agentPosts(connection, options):
##########################
    if(options.get('agentEvent', None) == None): print(f'***DISABLE agentPosts'); return
    loop = asyncio.get_running_loop()

    while True:
        print(f' \n*************************************************************************')
        #print('***wsAGENT WAIT')
        post = await loop.run_in_executor(None, options['agentEvent'])
        if(post == None): await asyncio.sleep(0); continue
        print(f'\n***wsTRANSFER POST: {post}')
        await connection.send(json.dumps(post))

##########################
async def connect(options):
##########################
    try:            
        async with websockets.client.connect(options["endpoint"]) as connection:
            print(f'***USER CONNECTED, endpoint: {options["endpoint"]}')
            await asyncio.gather(
                #agentPosts(connection, options),
                onConnection(connection, options)
            )
        
        print(' \n***DISCONNECTED')
    except:
        print('Abort onConnect', sys.exc_info()[0])
        traceback.print_exc()
       
##########################
def start(options):
##########################
    print('Start wsClient')

    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
        asyncio.get_event_loop().run_until_complete(connect(options))
    except:
        print('Abort: wsClient', sys.exc_info()[0])
        traceback.print_exc()

##########################
#         MAIN
##########################
# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    pass