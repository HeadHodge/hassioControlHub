######################################################
##            GLOBAL VARIABLES
#############################################
#import paho.mqtt.client as mqtt
import websocket
import sys, time, json, threading, _thread as thread
from evdev import InputDevice, categorize, ecodes
####################################
##            MODULE VARIABLES
#############################################
print('Load wsServer')
import sys, time, json, traceback, asyncio
from aiohttp import web

async def websocket_handler(request):
    print('s 1')
    
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print('s 2')

    async for msg in ws:
        print(msg)

    print('websocket connection closed')

    return ws
    
#######################################
#              MAIN
#######################################
app = web.Application()
app.add_routes([web.get('/', websocket_handler)])

if __name__ == '__main__':
    web.run_app(app)
