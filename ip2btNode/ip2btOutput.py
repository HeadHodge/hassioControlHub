import traceback
import os, sys, time, asyncio
from gi.repository import GLib
import core.dbusClient as dbusClient
import core.dbusServer as dbusServer
import core.btServer as btServer

try:
    print(' \nStart ip2btOutput Module')

    # Start dbusClient Module
    try:
        dbusClient.start()
        dbusClient.send_string("Output moo")
    except:
        print('Abort start dbusClient: ', sys.exc_info()[0])
        traceback.print_exc()
        
    # Start dbusServer Module for 'smartKeypads.ip2btInput'
    try:
        dbusServer.start('smartKeypads.ip2btOutput')
    except:
        print('Abort start dbusServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start btServer
    try:
        btServer.start()
    except:
        print('Abort start btServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start event loop for servers
    print('start mainLoop\n')
    eventloop = asyncio.get_event_loop()
    eventloop.run_forever()

    #print('start mainLoop')
    #loop = GLib.MainLoop()
    #loop.run()
except:
    print('Abort ip2btInput.py', sys.exc_info()[0])
    traceback.print_exc()
