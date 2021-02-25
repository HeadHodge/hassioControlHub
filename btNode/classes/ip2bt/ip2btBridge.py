#############################################
##            GLOBAL VARIABLES
#############################################
import threading, asyncio
import sys, time, json
#from classes.wsServer import wsServer
#from classes.btKeyboard import *
#from gi.repository import GLib
#from dbus.mainloop.glib import DBusGMainLoop
from wsServer import wsServer
#from btServer import btServer


def def1():
    print('def1')
    server = wsServer()
    #asyncio.set_event_loop(asyncio.new_event_loop())        
    #asyncio.get_event_loop().run_forever()

async def def2():
    print('def2')
    server = btServer()


print('Start Test')
#asyncio.get_event_loop().run_until_complete(def1())
#asyncio.get_event_loop().run_until_complete(wsServer)
#asyncio.run(def1())
#asyncio.get_event_loop().run_forever()

x = threading.Thread(target=def1())
x.start()
##asyncio.get_event_loop().run_until_complete(def1())
print('End Test')
asyncio.get_event_loop().run_forever()
