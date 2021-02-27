import os, sys, time, asyncio
from gi.repository import GLib
import core.dbusClient as dbusClient
import core.dbusServer as dbusServer
import core.wsServer as wsServer

try:
    print(' \nStart ip2btInput Module')

    # Start dbusClient Module
    try:
        dbusClient.start()
        #dbusClient.send_string("moo")
    except:
        print('Abort start dbusClient: ', sys.exc_info()[0])
        
    # Start dbusServer Module for 'smartKeypads.ip2btInput'
    try:
        dbusServer.start('smartKeypads.ip2btInput')
    except:
        print('Abort start dbusServer: ', sys.exc_info()[0])

    # Start wsServer
    try:
        wsServer.start()
    except:
        print('Abort start wsServer: ', sys.exc_info()[0])

    # Start event loop for servers
    print('start mainLoop\n')
    eventloop = asyncio.get_event_loop()
    eventloop.run_forever()

    #print('start mainLoop')
    #loop = GLib.MainLoop()
    #loop.run()
except:
    print('Abort ip2btInput.py', sys.exc_info()[0])
