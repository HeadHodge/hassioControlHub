####################################
##            MODULE VARIABLES
####################################
print('Load wsServer')

import sys, time, json, traceback, asyncio
from aiohttp import web

_options = {}

#############################################
async def websocket_handler(request):
#############################################
    global _options
    
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(f'Connected to wsServer on port: {_options["port"]}')

    async for hostPost in ws:
        if(_options.get('hostEvent', None) != None): _options['hostEvent'](json.loads(hostPost[1])); continue
        print(f'wsServer received hostPost: {hostPost}')

    print('wsServer connection closed')
    return ws
    
#############################################
def start(options={"port": 8080}):
#############################################
    global _options
    
    _options = options
    asyncio.set_event_loop(asyncio.new_event_loop())
    app = web.Application()
    app.add_routes([web.get('/', websocket_handler)])
    web.run_app(app, port=options['port'], handle_signals=False)
    
#######################################
#              MAIN
#######################################

if __name__ == '__main__':
    start()