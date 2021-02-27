import os, sys, time
from gi.repository import GLib
import core.dbusClient as dbusClient
import core.dbusServer as dbusServer

#import dbus
#import dbus.service
#from dbus.mainloop.glib import DBusGMainLoop
#from core.dbusServer import dbusServer
#import core.dbusClient as dbusClient
#import core.wsServer as wsServer

try:
    dbusClient.start()
    dbusClient.send_string("moo")
    dbusServer.start('smartKeypads.ip2btInput')
    #dbusServer.exportMethods()

    print('start mainLoop')
    loop = GLib.MainLoop()
    loop.run()
except KeyboardInterrupt:
    sys.exit()
