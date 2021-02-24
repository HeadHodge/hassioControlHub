#############################################
##            GLOBAL VARIABLES
#############################################
import asyncio
import sys, time, json, websockets
#from classes.wsServer import wsServer
#from classes.btKeyboard import *
from btOutput import btOutput

from gi.repository import GLib
#from dbus.mainloop.glib import DBusGMainLoop

async def def1():
    print('def1')


async def def2():
    print('def2')


print('Start Test')

#asyncio.get_event_loop().run_until_complete(wsServer())
#wsServer()
server = btOutput()


#DBusGMainLoop(set_as_default=True)
mainloop = GLib.MainLoop()
mainloop.run()
