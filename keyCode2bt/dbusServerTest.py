import os, sys, time
sys.path.insert(1, '/path/to/application/app/folder')
#import dbus, dbus.service
#from dbus.mainloop.glib import DBusGMainLoop
#from gi.repository import GLib
import core.dbusClient as dbusClient


dbusClient.start()
dbusClient.printName('booby')