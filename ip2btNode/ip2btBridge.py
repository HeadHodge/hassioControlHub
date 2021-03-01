#############################################
##            GLOBAL VARIABLES
#############################################
#from gi.repository import GLib
print('Load ip2btBridge')
from multiprocessing import Process
import os, sys, time, asyncio, traceback, queue

sys.path.append('/inputHub/ip2btNode/modules')
import wsServer
import btServer

_dataOut = queue.Queue()

def ipInput():
    print('Start ipInput')

    try:
        # Start wsServer
        wsServer.start()
       
        # Start event loop
        print('start ipInput eventLoop')
        eventloop = asyncio.get_event_loop()
        eventloop.run_forever()
    except:
        print('Abort ipInput', sys.exc_info()[0])
        traceback.print_exc()

def btOutput():
    print('Start btOutput Module')
    
    try:
        # Start btServer
        btServer.start(_dataOut)

        # Start btOutput event loop
        print('start btOutput eventLoop')
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort btOutput: ', sys.exc_info()[0])
        traceback.print_exc()
   
try:
    state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
    print('send string: ', state)
    _dataOut.put([ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ])
    
    state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]            
    print('send string: ', state)
    _dataOut.put([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ])

    # Start ipInput Module
    try:
        p = Process(target=ipInput)
        p.start()
    except:
        print('Abort start ipInput: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start btOutput Module
    try:
        p = Process(target=btOutput)
        p.start()
    except:
        print('Abort start btOutput: ', sys.exc_info()[0])
        traceback.print_exc()
        

    # Start event loop
    print('start ip2btBridge mainLoop')
    eventloop = asyncio.get_event_loop()
    eventloop.run_forever()
    #loop = GLib.MainLoop()
    #loop.run()
    
except:
    print('Abort ip2btBridge.py', sys.exc_info()[0])
    traceback.print_exc()
