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

#DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
ADAPTER_IFACE = 'org.bluez.Adapter1'

systemBus = dbus.SystemBus()
device_property = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
device_manager = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez'), 'org.bluez.ProfileManager1')

    
#@property
def getAddress():
    print('address property')
    """Return the device MAC address."""
    return device_property.Get(ADAPTER_IFACE, 'Address')
    
@property
def powered():
    """
    power state of the device.
    """
    return device_property.Get(ADAPTER_IFACE, 'Powered')

@powered.setter
def powered(new_state):
    device_property.Set(ADAPTER_IFACE, 'Powered', new_state)

#@property
def getAlias():
    return device_property.Get(ADAPTER_IFACE,
                               'Alias')

#@alias.setter
def setAlias(new_alias):
    device_property.Set(ADAPTER_IFACE,
                        'Alias',
                        new_alias)

@property
def discoverabletimeout():
    """Discoverable timeout of the Adapter."""
    return device_props.Get(ADAPTER_IFACE,
                            'DiscoverableTimeout')

@discoverabletimeout.setter
def discoverabletimeout(new_timeout):
    device_property.Set(ADAPTER_IFACE,
                        'DiscoverableTimeout',
                        dbus.UInt32(new_timeout))

@property
def discoverable():
    """Discoverable state of the Adapter."""
    return device_property.Get(
        ADAPTER_IFACE, 'Discoverable')

@discoverable.setter
def discoverable(new_state):
    device_property.Set(ADAPTER_IFACE,
                        'Discoverable',
                        new_state)

def register_profile(UUID, options):
    device_manager.RegisterProfile('/org/bluez/hidProfile', UUID, options)
