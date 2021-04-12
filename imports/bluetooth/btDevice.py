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
from xml.etree import ElementTree

#Connect to Bluez5 API on the dbus system bus
DBusGMainLoop(set_as_default=True)

#############################################
# Global Variables
#############################################
_options = {}
    
#############################################
def getPowered():
#############################################
    """
    power state of the device.
    """
    return _options['hciProperties'].Get('org.bluez.Adapter1', 'Powered')

#############################################
def setPowered(state=True):
#############################################
    value = dbus.Boolean(state)
    _options['hciProperties'].Set('org.bluez.Adapter1', 'Powered', value)

#############################################
def getAlias():
#############################################
    return _options['hciProperties'].Get('org.bluez.Adapter1', 'Alias')

#############################################
def setAlias(alias):
#############################################
    _options['hciProperties'].Set('org.bluez.Adapter1', 'Alias', alias)

#############################################
def getDiscoverableTime():
#############################################
    """Discoverable timeout of the Adapter."""
    return _options['hciProperties'].Get('org.bluez.Adapter1', 'DiscoverableTimeout')

#############################################
def setDiscoverableTime(timeout=300):
#############################################
    duration = dbus.UInt32(timeout)
    _options['hciProperties'].Set('org.bluez.Adapter1', 'DiscoverableTimeout', duration)

#############################################
def getDiscoverable():
#############################################
    """Discoverable state of the Adapter."""
    return _options['hciProperties'].Get('org.bluez.Adapter1', 'Discoverable')

#############################################
def setDiscoverable(new_state):
#############################################
    _options['hciProperties'].Set('org.bluez.Adapter1', 'Discoverable', new_state)

#############################################
def registerProfile(uuid, options):
#############################################
    print(f'Register bluetooth profile, uuid: {uuid}')
    _options['bluezManager'].RegisterProfile('/org/bluez/hidProfile', uuid, options)
    
#############################################
def enableConnectSignal(notify):
#############################################
    print(f'enableConnectSignal')

    _options['systemBus'].add_signal_receiver(notify, signal_name = 'PropertiesChanged', path = _options['devicePath'])
        
    # Start btOutput event loop
    print('start connectSignal eventLoop')
    eventloop = GLib.MainLoop()
    eventloop.run()

#############################################
def getAddress():
#############################################
    """Return the device MAC address."""
    return _options['hciProperties']['interface'].Get(_options['hciProperties']['adapter'], 'Address')

#############################################
def isConnected():
#############################################
    """Return the device connection state."""
    return _options['deviceProperties']['interface'].Get(_options['deviceProperties']['device'], 'Connected')
     
#############################################
def start():
#############################################
    print(f'start btDevice')
    global _options
    interface = {}
    
    systemBus = dbus.SystemBus()

    #get dbus introspect interface
    #busctl tree
    interface['dbusIntrospect'] = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Introspectable')

    #get 1st paired device name
    devicePath = None
    for child in ElementTree.fromstring(interface['dbusIntrospect'].Introspect()):
        if child.tag != 'node': continue
        deviceName = child.attrib['name']
        devicePath = '/org/bluez/hci0/' + deviceName
        print('devicePath', devicePath)
        break

    #get bluez interfaces
    interface['bluezManager'] = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez'), 'org.bluez.ProfileManager1')
    interface['hciProperties'] = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
    interface['deviceProperties'] = dbus.Interface(systemBus.get_object('org.bluez', devicePath), 'org.freedesktop.DBus.Properties')
    
    _options['systemBus'] = systemBus
    
    _options['devicePath'] = devicePath
    
    _options['dbusIntrospect'] = {
            'interface': interface['dbusIntrospect'],
            'introspect': 'org.freedesktop.DBus.Introspectable'
        }
    
    _options['bluezManager'] = {
            'interface': interface['bluezManager'],
            'manager': 'org.bluez.ProfileManager1'
        }
        
    _options['hciProperties'] = {
            'interface': interface['hciProperties'],
            'properties': 'org.freedesktop.DBus.Properties',
            'adapter': 'org.bluez.Adapter1'
        }
        
    _options['deviceProperties'] = {
            'interface': interface['deviceProperties'],
            'properties': 'org.freedesktop.DBus.Properties',
            'device': 'org.bluez.Device1'
        }

    _options['hciAddress'] = getAddress()
    print('hciAddress', _options['hciAddress'])
    print('isConnected', isConnected())
    
#############################################
##                MAIN
#############################################   
start()

#Run this module on main thread to unit test with following code
if __name__ == '__main__':
    import threading
  
    #############################################
    def onConnectSignal(interface, changed, path):
    #############################################
        print(f'****CONNECTION ALERT****, interface: {interface}, connected: {changed["Connected"]}')
    
    threading.Thread(target=enableConnectSignal, args=(onConnectSignal,)).start()
