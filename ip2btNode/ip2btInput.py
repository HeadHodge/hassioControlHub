import os, sys, time, asyncio
import traceback, threading
#from gi.repository import GLib
import core.dbusClient as dbusClient
import core.dbusInputServer as dbusInputServer
import core.wsServer as wsServer

try:
    print(' \nStart ip2btInput Module')

   # Start dbusInputServer Module for 'smartKeypads.ip2btInput'
    try:
        #dbusInputServer.start('smartKeypads.ip2btInput')
        threading.Thread(target=dbusInputServer.start, args=('smartKeypads.ip2btInput',)).start()
    except:
        print('Abort start dbusServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start wsServer
    try:
        #wsServer.start()
        threading.Thread(target=wsServer.start).start()
    except:
        print('Abort start wsServer: ', sys.exc_info()[0])
        traceback.print_exc()

    # Start dbusClient Module
    try:
        dbusClient.start('smartKeypads.ip2btBridge', 'ip2bt.Input')
        dbusClient.send_string("mewoooing")
        #threading.Thread(target=dbusClient.start, args=('smartKeypads.ip2btBridge', 'ip2bt.Input')).start()
    except:
        print('Abort start dbusClient: ', sys.exc_info()[0])
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
