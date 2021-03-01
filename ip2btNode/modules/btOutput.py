print('Load btOutput Module')
from gi.repository import GLib
import traceback
import os, sys, time, asyncio

sys.path.append('/inputHub/ip2btNode/modules')
import btServer

def start(outputData):
    try:
        print('Start btOutput Module')
    
        # Start btServer
        try:
            btServer.start(outputData)
        except:
            print('Abort start btServer: ', sys.exc_info()[0])
            traceback.print_exc()

    
        # Start event loop for servers
        print('start btOutput mainLoop')
        #eventloop = asyncio.get_event_loop()
        #eventloop.run_forever()
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort btOutput.py', sys.exc_info()[0])
        traceback.print_exc()
