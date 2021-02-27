#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
import os, sys, time
from btDevice import btDevice

"""
create a bluetooth device to emulate a HID keyboard
"""
class btPair:
    print(f"Starting btPair")
    MY_DEV_NAME = 'XXX_Keyboard'
    DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
    ADAPTER_IFACE = 'org.bluez.Adapter1'
    UUID = '00001124-0000-1000-8000-00805f9b34fb'
    WORKING_DIR  = os.path.dirname(os.path.realpath(__file__))
    SDP_RECORD_PATH = os.path.join(WORKING_DIR, 'btProfile.xml')

    def __init__(self):
        print(f"Starting btPair for: {self.MY_DEV_NAME}")

        self.device = btDevice()
        
        # set the Bluetooth device configuration
        self.config_hid_profile()
        print(f"Pairing enabled, {self.MY_DEV_NAME} is now visible for 5 minutes")
        time.sleep(360)
        print(f"Pairing Mode Disabled")

    def read_sdp_service_record(self):
        """
        Read and return SDP record from a file
        :return: (string) SDP record
        """
        try:
            fh = open(self.SDP_RECORD_PATH, 'r')
        except OSError:
            sys.exit('Could not open the sdp record. Exiting...')

        return fh.read()   

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

        self.device.register_profile(self.UUID, opts)

        self.device.alias = self.MY_DEV_NAME
        self.device.discoverabletimeout = 0
        self.device.discoverable = True

        print('Profile registered ')
        
if __name__ == '__main__':
    # The sockets require root permission
    if not os.geteuid() == 0:
        sys.exit('Only root can run this script')

    myservice = btPair()
