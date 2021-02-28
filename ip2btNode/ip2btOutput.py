import traceback
import os, sys, time, asyncio
from gi.repository import GLib
import core.btServer as btServer
print(' \nLoad ip2btOutput Module')

def start():
    try:
        print(' \nStart ip2btOutput Module')
    
        # Start btServer
        try:
            btServer.start()
        except:
            print('Abort start btServer: ', sys.exc_info()[0])
            traceback.print_exc()

    
        # Start event loop for servers
        print('start ip2btOutput mainLoop\n')
        #eventloop = asyncio.get_event_loop()
        #eventloop.run_forever()
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort ip2btInput.py', sys.exc_info()[0])
        traceback.print_exc()
