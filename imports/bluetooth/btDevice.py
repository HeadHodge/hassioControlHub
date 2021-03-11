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

import os, sys, time
import dbus, dbus.service

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
def setPowered(new_state):
#############################################
    device_property.Set(ADAPTER_IFACE, 'Powered', new_state)

#############################################
def getAlias():
#############################################
    return device_property.Get(ADAPTER_IFACE, 'Alias')

#############################################
def setAlias(new_alias):
#############################################
    device_property.Set(ADAPTER_IFACE, 'Alias', new_alias)

#############################################
def getDiscoveryTime():
#############################################
    """Discoverable timeout of the Adapter."""
    return device_props.Get(ADAPTER_IFACE, 'DiscoverableTimeout')

#############################################
def setDiscoveryTime(new_timeout):
#############################################
    device_property.Set(ADAPTER_IFACE, 'DiscoverableTimeout', dbus.UInt32(new_timeout))

#############################################
def getDiscoveryFlq():
#############################################
    """Discoverable state of the Adapter."""
    return device_property.Get(ADAPTER_IFACE, 'Discoverable')

#############################################
def setDiscoveryFlg(new_state):
#############################################
    device_property.Set(ADAPTER_IFACE, 'Discoverable', new_state)

#############################################
def loadProfile(UUID, options):
#############################################
    device_manager.RegisterProfile('/org/bluez/hidProfile', UUID, options)


#############################################
##                MAIN
#############################################   

# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    print(f'device address: {getAddress()}')