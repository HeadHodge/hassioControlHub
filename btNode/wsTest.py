#############################################
##            GLOBAL VARIABLES
#############################################
import asyncio
import sys, time, json, websockets
#from classes.wsServer import wsServer
from classes.btKeyboard import *

async def def1():
    print('def1')


async def def2():
    print('def2')


print('Start Test')

#asyncio.get_event_loop().run_until_complete(wsServer())
#wsServer()
btKeyboard()