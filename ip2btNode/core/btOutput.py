import traceback
import os, sys, time, asyncio
from gi.repository import GLib
import core.btServer as btServer
print('Load btOutput Module')

def start():
    try:
        print('Start btOutput Module')
    
        # Start btServer
        try:
            btServer.start()
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
