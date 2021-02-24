#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
import os, sys, time
import dbus, dbus.service

class btDevice:
    DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
    ADAPTER_IFACE = 'org.bluez.Adapter1'

    def __init__(self):
        print("Start btDevice")

        self.dev_path = '/org/bluez/hci0'
        self.bus = dbus.SystemBus()
        self.device_property = dbus.Interface(self.bus.get_object('org.bluez', self.dev_path), self.DBUS_PROP_IFACE)
        self.device_manager = dbus.Interface(self.bus.get_object('org.bluez', '/org/bluez'), 'org.bluez.ProfileManager1')

    @property
    def address(self):
        """Return the device MAC address."""
        return self.device_property.Get(self.ADAPTER_IFACE,
                                         'Address')

    @property
    def powered(self):
        """
        power state of the device.
        """
        return self.device_property.Get(self.ADAPTER_IFACE, 'Powered')

    @powered.setter
    def powered(self, new_state):
        self.device_property.Set(self.ADAPTER_IFACE, 'Powered', new_state)

    @property
    def alias(self):
        return self.device_property.Get(self.ADAPTER_IFACE,
                                         'Alias')

    @alias.setter
    def alias(self, new_alias):
        self.device_property.Set(self.ADAPTER_IFACE,
                                  'Alias',
                                  new_alias)

    @property
    def discoverabletimeout(self):
        """Discoverable timeout of the Adapter."""
        return self.device_props.Get(self.ADAPTER_IFACE,
                                      'DiscoverableTimeout')

    @discoverabletimeout.setter
    def discoverabletimeout(self, new_timeout):
        self.device_property.Set(self.ADAPTER_IFACE,
                                  'DiscoverableTimeout',
                                  dbus.UInt32(new_timeout))

    @property
    def discoverable(self):
        """Discoverable state of the Adapter."""
        return self.device_property.Get(
            self.ADAPTER_INTERFACE, 'Discoverable')

    @discoverable.setter
    def discoverable(self, new_state):
        self.device_property.Set(self.ADAPTER_IFACE,
                                  'Discoverable',
                                  new_state)

    def register_profile(self, UUID, options):
        self.device_manager.RegisterProfile('/org/bluez/hidProfile', UUID, options)


    """    
    def config_hid_profile(self):
        
        #Setup and register HID Profile

        print('Configuring Bluez Profile')
        service_record = self.read_sdp_service_record()

        opts = {
            'Role': 'server',
            'RequireAuthentication': False,
            'RequireAuthorization': False,
            'AutoConnect': True,
            'ServiceRecord': service_record,
        }

        manager = dbus.Interface(self.bus.get_object('org.bluez',
                                                     '/org/bluez'),
                                 'org.bluez.ProfileManager1')

        #HumanInterfaceDeviceProfile(self.bus, BTKbDevice.PROFILE_DBUS_PATH)

        manager.RegisterProfile(BTKbDevice.PROFILE_DBUS_PATH,
                                BTKbDevice.UUID,
                                opts)

        print('Profile registered ')
    """    
