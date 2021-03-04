#!/usr/bin/python3
#
# thanhle Bluetooth keyboard/Mouse emulator DBUS Service
#

print('Load dbusExports')
import os, sys, time, traceback
import dbus, dbus.service
from dbus.mainloop.glib import DBusGMainLoop

def start():
    print("Start dbusExports")
    DBusGMainLoop(set_as_default=True) #Run before starting any dbus service
    exportMethods()

class exportMethods(dbus.service.Object):
    print("Load exportMethods")

    def __init__(self, dbusName='HeadHodge.smartKeypads', dbusPath='/dbus/methods'):
        print(f"Start exportMethods for dbusName: '{dbusName}', dbusPath: '{dbusPath}'")
        
        # connect methods to dbus
        busName = dbus.service.BusName(dbusName, dbus.SystemBus())
        dbus.service.Object.__init__(self, busName, dbusPath)

    @dbus.service.method('ip2btBridge.InputMethods', in_signature='s')
    def send_string(self, string):
        print("Get send_string request through dbus")
        print("key msg: ", string)

    @dbus.service.method('ip2btBridge.InputMethods', in_signature='yay')
    def send_keys(self, modifier_byte, keys):
        print("Get send_keys request through dbus")
        print("key msg: ", keys)
        state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]
        state[2] = int(modifier_byte)
        count = 4
        for key_code in keys:
            if(count < 10):
                state[count] = int(key_code)
            count += 1
        #self.device.send_string(state)

    @dbus.service.method('ip2btBridge.InputMethods', in_signature='yay')
    def send_mouse(self, modifier_byte, keys):
        print("Get send_keys request through dbus")
        state = [0xA1, 2, 0, 0, 0, 0]
        count = 2
        for key_code in keys:
            if(count < 6):
                state[count] = int(key_code)
            count += 1
        self.device.send_string(state)
        
    """
    BlueZ D-Bus Profile for HID
    """
    fd = -1

    @dbus.service.method('org.bluez.Profile1',
                         in_signature='', out_signature='')
    def Release(self):
        print('Release')
        mainloop.quit()

    @dbus.service.method('org.bluez.Profile1',
                         in_signature='oha{sv}', out_signature='')
    def NewConnection(self, path, fd, properties):
        print('NewConnection({}, {})'.format(path, self.fd))
        self.fd = fd.take()
        for key in properties.keys():
            if key == 'Version' or key == 'Features':
                print('  {} = 0x{:04x}'.format(key, properties[key]))
            else:
                print('  {} = {}'.format(key, properties[key]))

    @dbus.service.method('org.bluez.Profile1',
                         in_signature='o', out_signature='')
    def RequestDisconnection(self, path):
        print('RequestDisconnection {}'.format(path))

        if self.fd > 0:
            os.close(self.fd)
            self.fd = -1


# Run this module on main thread to unit test with following code
if __name__ == "__main__":
    from gi.repository import GLib

    try:
        if not os.geteuid() == 0:
            sys.exit("Only root can run this script")

        start()
        print('start dbusExports main loop')
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort dbusExports.py', sys.exc_info()[0])
        traceback.print_exc()
