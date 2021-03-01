print('Load ipInput Module')
import os, sys, time, asyncio
import traceback, threading

sys.path.append('/inputHub/ip2btNode/modules')
import wsServer

def start():
    try:
        print('Start ipInput Module')

        # Start wsServer
        try:
            wsServer.start()
        except:
            print('Abort start wsServer: ', sys.exc_info()[0])
            traceback.print_exc()
       
        # Start event loop for servers
        print('start btInput mainLoop')
        eventloop = asyncio.get_event_loop()
        eventloop.run_forever()

        #eventloop = GLib.MainLoop()
        #eventloop.run()
    except:
        print('Abort ipInput.py', sys.exc_info()[0])
        traceback.print_exc()
