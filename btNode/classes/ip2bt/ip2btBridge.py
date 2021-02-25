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
from btServer import btServer

class ip2btBridge:
    print('Load ip2btBridge')
    """
    """  
    def __init__(self):
        print('Starting ip2btBridge')
        threading.Thread(target=self.def1()).start()

        #loop = asyncio.get_event_loop()
        #loop.create_task(self.def1())

        print('End Test')
        asyncio.get_event_loop().run_forever()
        
    def myName(self, name):
        print(f'my name is: {name}')
        
    def def1(self):
        print('def1')
        server = wsServer(self)

    async def def2(self):
        print('def2')
        server = btServer()
        
    """
    #asyncio.set_event_loop(asyncio.new_event_loop())        
    #asyncio.get_event_loop().run_forever()
    print('Start Test')
    #asyncio.get_event_loop().run_until_complete(def1())
    #asyncio.get_event_loop().run_until_complete(wsServer)
    #asyncio.run(def1())
    #asyncio.get_event_loop().run_forever()

    threading.Thread(target=def1()).start()
    ##asyncio.get_event_loop().run_until_complete(def1())
    print('End Test')
    asyncio.get_event_loop().run_forever()
    """
myclass = ip2btBridge()