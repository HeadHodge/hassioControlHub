import os
import sys
import time
import dbus
import dbus.service
import dbus.mainloop.glib
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

class ipInput(dbus.service.Object):
    print("Load ipInput")

    def __init__(self):
        print("Start ipInput")
