#############################################
##            GLOBAL VARIABLES
#############################################
import asyncio, threading
import sys, time, json, websockets
#from classes.wsServer import wsServer
#from classes.btKeyboard import *
#from gi.repository import GLib
#from dbus.mainloop.glib import DBusGMainLoop
from btServer import btServer
from wsServer import wsServer

def printName(name):
    print(f'name: {name}')

async def def1():
    print('def1')
    printName('Bobbette')
    wsServer(asyncio.get_event_loop())
    while True:
        print('def1')
        await asyncio.sleep(3)
    print('def1 done')

async def def2(p1=0, p2=0):
    print('def2')
    await asyncio.sleep(5)
    print('def2 done')
    
async def main():
    print('Start Test')
    task1 = asyncio.create_task(def1())
    #task2 = asyncio.create_task(def2())
    print('End Test')
    while True:
        print('main')
        await asyncio.sleep(3)

#task = threading.Thread(target=def1, args=(printName,))
#task.daemon = True
#task.start()
#print('sleep')    
#time.sleep(10)
#print('exit')    
asyncio.run(main())
#print('Continue')
#asyncio.get_event_loop().run_forever()    


#asyncio.get_event_loop().run_forever()
#asyncio.run(def1())  # before blocking call we schedule our coroutine for sending periodic messages
