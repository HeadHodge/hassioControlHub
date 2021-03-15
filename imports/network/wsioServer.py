####################################
##            MODULE VARIABLES
####################################
print('Load wsServer')

import sys, time, json, traceback, asyncio
from aiohttp import web

_options = {}

#############################################
async def connect(request):
#############################################
    global _options
    if(_options.get('userEvent', None) == None): print('Abort connect, userEvent method missing in options'); return

    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(f' \n***wssCONNECTED on port: {_options["port"]}')

    async for userPost in ws:
        #print(f'wsServer received userPost: {userPost}')
        await _options['userEvent'](json.loads(userPost[1])); continue

    print(' \n***wssCLOSED')
    return ws
    
#############################################
def start(options={"port": 8080}):
#############################################
    global _options
    
    _options = options
    asyncio.set_event_loop(asyncio.new_event_loop())
    app = web.Application()
    app.add_routes([web.get('/', connect)])
    web.run_app(app, port=options['port'], handle_signals=False)
    
#######################################
#              MAIN
#######################################

if __name__ == '__main__':
    start()