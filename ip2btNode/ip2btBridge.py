#############################################
##            GLOBAL VARIABLES
#############################################
#from gi.repository import GLib
print('Load ip2btBridge')
from multiprocessing import Process
import os, sys, time, asyncio, traceback

sys.path.append('/inputHub/ip2btNode/modules')
import ipInput
import btOutput

try:
    # Start ipInput Module
    try:
        p = Process(target=ipInput.start)
        p.start()
    except:
        print('Abort start ipInput: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start btOutput Module
    try:
        p = Process(target=btOutput.start)
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
