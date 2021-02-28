import os, sys, time, asyncio
import traceback, threading
#from gi.repository import GLib
import core.wsServer as wsServer
print(' \nLoad ip2btInput Module')

def start():
    try:
        print(' \nStart ip2btInput Module')

        # Start wsServer
        try:
            wsServer.start()
        except:
            print('Abort start wsServer: ', sys.exc_info()[0])
            traceback.print_exc()
       
        # Start event loop for servers
        print('start ip2btInput mainLoop\n')
        eventloop = asyncio.get_event_loop()
        eventloop.run_forever()

        #eventloop = GLib.MainLoop()
        #eventloop.run()
    except:
        print('Abort ip2btInput.py', sys.exc_info()[0])
        traceback.print_exc()
