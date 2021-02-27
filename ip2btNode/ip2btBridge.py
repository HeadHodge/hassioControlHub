#############################################
##            GLOBAL VARIABLES
#############################################
import traceback, threading
import os, sys, time, asyncio
#import core.dbusClient as dbusClient
#import core.dbusBridgeServer as dbusBridgeServer
#import ip2btOutput
import core.wsServer as wsServer
import core.btServer as btServer
from gi.repository import GLib
from multiprocessing import Process

print('Load ip2btBridge')

def callback(func):
    func('hellooooooo')


try:
    # Start dbusBridgeServer Module for 'smartKeypads.ip2btBridge'

    try:
        p = Process(target=wsServer.start)
        p.start()
        print('hello1')
    except:
        print('Abort start dbusBridgeServer: ', sys.exc_info()[0])
        traceback.print_exc()

    try:
        p = Process(target=btServer.start)
        p.start()
        print('hello2')
    except:
        print('Abort start dbusBridgeServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start event loop for servers
    print('start ip2btBridge mainLoop\n')
    eventloop = asyncio.get_event_loop()
    eventloop.run_forever()
    #loop = GLib.MainLoop()
    #loop.run()
    
except:
    print('Abort ip2btBridge.py', sys.exc_info()[0])
    traceback.print_exc()
