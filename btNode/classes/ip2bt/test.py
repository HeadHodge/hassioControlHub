#############################################
##            GLOBAL VARIABLES
#############################################
import asyncio
import sys, time, json, websockets
#from classes.wsServer import wsServer
#from classes.btKeyboard import *
#from gi.repository import GLib
#from dbus.mainloop.glib import DBusGMainLoop
from btAPI import btAPI


async def def1():
    print('def1')


async def def2():
    print('def2')


print('Start Test')

device = btAPI()
print(device.address)
