#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
import os, sys, time, json, threading
import dbus, dbus.service, socket

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

class btAPI:
    """
    create a bluetooth device to emulate a HID keyboard
    MY_DEV_NAME = 'X_Keyboard'
    # Service port - must match port configured in SDP record
    P_CTRL = 17
    # Service port - must match port configured in SDP record#Interrrupt port
    P_INTR = 19
    # BlueZ dbus
    PROFILE_DBUS_PATH = '/bluez/yaptb/btkb_profile'
    ADAPTER_IFACE = 'org.bluez.Adapter1'
    DEVICE_INTERFACE = 'org.bluez.Device1'
    DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
    DBUS_OM_IFACE = 'org.freedesktop.DBus.ObjectManager'

    # file path of the sdp record to laod
    install_dir  = os.path.dirname(os.path.realpath(__file__))
    SDP_RECORD_PATH = os.path.join(install_dir,
                                   'btProfile.xml')
    # UUID for HID service (1124)
    # https://www.bluetooth.com/specifications/assigned-numbers/service-discovery
    UUID = '00001124-0000-1000-8000-00805f9b34fb'
    """
    DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
    ADAPTER_IFACE = 'org.bluez.Adapter1'
    UUID = '00001124-0000-1000-8000-00805f9b34fb'

    def __init__(self):
        print("Start btAPI")

        self.dev_path = '/org/bluez/hci0'
        self.bus = dbus.SystemBus()
        self.adapter_property = dbus.Interface(self.bus.get_object('org.bluez', self.dev_path), self.DBUS_PROP_IFACE)

    @property
    def address(self):
        """Return the adapter MAC address."""
        return self.adapter_property.Get(self.ADAPTER_IFACE,
                                         'Address')

    @property
    def powered(self):
        """
        power state of the Adapter.
        """
        return self.adapter_property.Get(self.ADAPTER_IFACE, 'Powered')

    @powered.setter
    def powered(self, new_state):
        self.adapter_property.Set(self.ADAPTER_IFACE, 'Powered', new_state)

    @property
    def alias(self):
        return self.adapter_property.Get(self.ADAPTER_IFACE,
                                         'Alias')

    @alias.setter
    def alias(self, new_alias):
        self.adapter_property.Set(self.ADAPTER_IFACE,
                                  'Alias',
                                  new_alias)

    @property
    def discoverabletimeout(self):
        """Discoverable timeout of the Adapter."""
        return self.adapter_props.Get(self.ADAPTER_IFACE,
                                      'DiscoverableTimeout')

    @discoverabletimeout.setter
    def discoverabletimeout(self, new_timeout):
        self.adapter_property.Set(self.ADAPTER_IFACE,
                                  'DiscoverableTimeout',
                                  dbus.UInt32(new_timeout))

    @property
    def discoverable(self):
        """Discoverable state of the Adapter."""
        return self.adapter_property.Get(
            self.ADAPTER_INTERFACE, 'Discoverable')

    @discoverable.setter
    def discoverable(self, new_state):
        self.adapter_property.Set(self.ADAPTER_IFACE,
                                  'Discoverable',
                                  new_state)

    def config_hid_profile(self):
        """
        Setup and register HID Profile
        """

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
if __name__ == '__main__':
    # The sockets require root permission
    if not os.geteuid() == 0:
        sys.exit('Only root can run this script')

    #thread.start_new_thread(checkConnection)

    DBusGMainLoop(set_as_default=True)
    myservice = BTKbDevice()
    mainloop = GLib.MainLoop()
    mainloop.run()
"""