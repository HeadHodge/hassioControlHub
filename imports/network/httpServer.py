####################################
##            MODULE VARIABLES
#############################################
print('Load httpServer')
import sys, time, json, traceback, asyncio
from aiohttp import web

def start(port=80):
    asyncio.set_event_loop(asyncio.new_event_loop())
    app = web.Application()
    app.add_routes([web.static('/', '/smartRemotes/bridges/html2key.html')])
    web.run_app(app, port=port, handle_signals=False)
  
#######################################
#              MAIN
#######################################

if __name__ == '__main__':
    start()