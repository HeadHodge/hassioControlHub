#############################################
##            GLOBAL VARIABLES
#############################################
import traceback
import threading
import os, sys, time, asyncio
import core.dbusClient as dbusClient
import core.dbusBridgeServer as dbusBridgeServer
from gi.repository import GLib

print('Load ip2btBridge')

try:
    # Start dbusBridgeServer Module for 'smartKeypads.ip2btBridge'
    try:
        #dbusBridgeServer.start()
        threading.Thread(target=dbusBridgeServer.start).start()
    except:
        print('Abort start dbusBridgeServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start event loop for servers
    print('start mainLoop\n')
    eventloop = asyncio.get_event_loop()
    eventloop.run_forever()
    #loop = GLib.MainLoop()
    #loop.run()
    
except:
    print('Abort ip2btBridge.py', sys.exc_info()[0])
    traceback.print_exc()
