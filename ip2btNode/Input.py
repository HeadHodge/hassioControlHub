import os, sys, time, asyncio
from gi.repository import GLib
import core.dbusClient as dbusClient
import core.dbusServer as dbusServer
import core.wsServer as wsServer

#import dbus
#import dbus.service
#from dbus.mainloop.glib import DBusGMainLoop
#from core.dbusServer import dbusServer
#import core.dbusClient as dbusClient
#import core.wsServer as wsServer

try:
    try:
        dbusClient.start()
        dbusClient.send_string("moo")
    except:
        print('Abort start dbusClient: ', sys.exc_info()[0])
        
    dbusServer.start('smartKeypads.ip2btInput')
    wsServer.start()

    print('start mainLoop')
    eventloop = asyncio.get_event_loop()
    eventloop.run_forever()

    #print('start mainLoop')
    #loop = GLib.MainLoop()
    #loop.run()
except:
    print('Abort Input.py', sys.exc_info()[0])
