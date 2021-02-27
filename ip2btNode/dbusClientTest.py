import os, sys, time
#import dbus, dbus.service
#from dbus.mainloop.glib import DBusGMainLoop
#from gi.repository import GLib
import core.dbusClient as dbusClient


dbusClient.start()
dbusClient.printName('booby')