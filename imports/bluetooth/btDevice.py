"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
#############################################
##            MODULE VARIABLES
#############################################
print('Load btDevice')

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
import os, sys, time, dbus


#Connect to Bluez5 API on the dbus system bus
DBusGMainLoop(set_as_default=True)
systemBus = dbus.SystemBus()
device_property = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
device_manager = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez'), 'org.bluez.ProfileManager1')
ADAPTER_IFACE = 'org.bluez.Adapter1'

#############################################
def getAddress():
#############################################
    """Return the device MAC address."""
    return device_property.Get(ADAPTER_IFACE, 'Address')
    
#############################################
def getPowered():
#############################################
    """
    power state of the device.
    """
    return device_property.Get(ADAPTER_IFACE, 'Powered')

#############################################
def setPowered(state=True):
#############################################
    value = dbus.Boolean(state)
    device_property.Set(ADAPTER_IFACE, 'Powered', value)

#############################################
def getAlias():
#############################################
    return device_property.Get(ADAPTER_IFACE, 'Alias')

#############################################
def setAlias(alias):
#############################################
    device_property.Set(ADAPTER_IFACE, 'Alias', alias)

#############################################
def getDiscoverableTime():
#############################################
    """Discoverable timeout of the Adapter."""
    return device_property.Get(ADAPTER_IFACE, 'DiscoverableTimeout')

#############################################
def setDiscoverableTime(timeout=300):
#############################################
    duration = dbus.UInt32(timeout)
    device_property.Set(ADAPTER_IFACE, 'DiscoverableTimeout', duration)

#############################################
def getDiscoverable():
#############################################
    """Discoverable state of the Adapter."""
    return device_property.Get(ADAPTER_IFACE, 'Discoverable')

#############################################
def setDiscoverable(new_state):
#############################################
    device_property.Set(ADAPTER_IFACE, 'Discoverable', new_state)

#############################################
def registerProfile(uuid, options):
#############################################
    print(f'Register bluetooth profile, uuid: {uuid}')
    device_manager.RegisterProfile('/org/bluez/hidProfile', uuid, options)
    
#############################################
def enableConnectSignal(notify):
#############################################
    print(f'enableConnectSignal')

    systemBus.add_signal_receiver(notify, signal_name='PropertiesChanged', path='/org/bluez/hci0/dev_80_FD_7A_4A_DB_39')
        
    # Start btOutput event loop
    print('start connectSignal eventLoop')
    eventloop = GLib.MainLoop()
    eventloop.run()

#############################################
##                MAIN
#############################################   

# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    import threading
  
    #############################################
    def onConnectSignal(interface, changed, path):
    #############################################
        print(f'****CONNECTION ALERT****, interface: {interface}, connected: {changed["Connected"]}')
    
    print(f'device address: {getAddress()}')
    threading.Thread(target=enableConnectSignal, args=(onConnectSignal,)).start()
