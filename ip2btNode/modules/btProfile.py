#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
print("Load btProfile")
import os, sys, time, traceback
import dbus
from btDevice import btDevice

"""
create a bluetooth device to emulate a HID keyboard
"""
DBUS_NAME = 'HeadHodge.smartKeypads'
PROFILE_UUID = '00001124-0000-1000-8000-00805f9b34fb'

DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
ADAPTER_IFACE = 'org.bluez.Adapter1'
CURRENT_DIR  = os.path.dirname(os.path.realpath(__file__))
SERVICE_RECORD_PATH = os.path.join(CURRENT_DIR, 'sdpRecord.xml')

class Profile(dbus.service.Object):
	fd = -1

	@dbus.service.method("org.bluez.Profile1",
					in_signature="", out_signature="")
	def Release(self):
		print("Release")
		mainloop.quit()

	@dbus.service.method("org.bluez.Profile1",
					in_signature="", out_signature="")
	def Cancel(self):
		print("Cancel")

	@dbus.service.method("org.bluez.Profile1",
				in_signature="oha{sv}", out_signature="")
	def NewConnection(self, path, fd, properties):
		self.fd = fd.take()
		print("NewConnection(%s, %d)" % (path, self.fd))
		for key in properties.keys():
			if key == "Version" or key == "Features":
				print("  %s = 0x%04x" % (key, properties[key]))
			else:
				print("  %s = %s" % (key, properties[key]))

	@dbus.service.method("org.bluez.Profile1",
				in_signature="o", out_signature="")
	def RequestDisconnection(self, path):
		print("RequestDisconnection(%s)" % (path))

		if (self.fd > 0):
			os.close(self.fd)
			self.fd = -1




def start():
    print(f"Start btProfile")

    try:
        print('get bluez ProfileManager1 interface')
        dbusObject = dbus.SystemBus().get_object('org.bluez', '/org/bluez')
        profileManager = dbus.Interface(dbusObject, 'org.bluez.ProfileManager1')
    
        print('register profile')
        register_profile(profileManager)
    except:
        print('Abort btProfile: ', sys.exc_info()[0])
        traceback.print_exc()

def read_sdp_service_record():
    """
    Read and return SDP record from a file
    :return: (string) SDP record
    """
    try:
        fh = open(SERVICE_RECORD_PATH, 'r')
    except OSError:
        sys.exit('Could not open the sdp record. Exiting...')

    return fh.read()   

def register_profile(profileManager):
    #Setup and register HID Profile

    #service_record = read_sdp_service_record()
    PROFILE_OPTIONS = {
        'Name': 'smartKeypads ip2bt keypad',
        'Role': 'server',
        'RequireAuthentication': False,
        'RequireAuthorization': False,
        'AutoConnect': True,
        'ServiceRecord': read_sdp_service_record()
    }
    
    DBUS_PATH = '/dbus/methods'
    
    dbusName='HeadHodge.smartKeypads'
    dbusPath='/dbus/methods'
    busName = dbus.service.BusName(dbusName, dbus.SystemBus())
    #profile = dbus.service.Object(busName, dbusPath)
    profile = Profile(dbus.SystemBus(), dbusPath)
    
    profileManager.RegisterProfile(dbusPath, PROFILE_UUID, PROFILE_OPTIONS)

    #self.device.alias = self.MY_DEV_NAME
    #self.device.discoverabletimeout = 0
    #self.device.discoverable = True

    print(f'registered bluez5 profile, UUID: \'{PROFILE_UUID}\', dbus pathName: \'{DBUS_PATH}\'')
        
# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    if not os.geteuid() == 0: sys.exit('Only root can run this script')
    from dbus.mainloop.glib import DBusGMainLoop
    from gi.repository import GLib

    try:    
        DBusGMainLoop(set_as_default=True) #Run before starting any dbus service
        
        start()
        
        print('start btProfile main loop')
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort btProfile.py', sys.exc_info()[0])
        traceback.print_exc()
