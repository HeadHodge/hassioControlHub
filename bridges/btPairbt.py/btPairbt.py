"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
#############################################
##            MODULE VARIABLES
#############################################
print("Load btPairbt")
from gi.repository import GLib
import os, sys, time, traceback, threading
#import dbus

path = os.path.join(os.path.dirname(__file__), '../../imports/bluetooth')
sys.path.append(path)

import btDevice

"""
create a bluetooth device to emulate a HID keyboard
"""
#DBUS_NAME = 'HeadHodge.smartKeypads'

#DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'
#ADAPTER_IFACE = 'org.bluez.Adapter1'

"""
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


"""

def loadServiceRecord():
    """
    Read and return SDP record from a file
    :return: (string) SDP record
    """
    try:
        currentDirectory  = os.path.dirname(os.path.realpath(__file__))
        filePath = os.path.join(currentDirectory, 'sdpRecord.xml')
        print(f'load serviceRecord: {filePath}')
        fh = open(filePath, 'r')
        return fh.read()
        fh.close()
    except OSError:
        sys.exit('Could not open the serviceRecord. Exiting...')

def loadProfile(deviceName='smartRemotes Keypad'):
    #Setup and register HID Profile
    print('loadProfile')

    profileUUID = '00001124-0000-1000-8000-00805f9b34fb'
    
    profileOptions = {
        'Name': 'smartRemotes Profile',
        'Role': 'server',
        'RequireAuthentication': False,
        'RequireAuthorization': False,
        'AutoConnect': True,
        'ServiceRecord': loadServiceRecord()
    }
    
    btDevice.registerProfile(profileUUID, profileOptions)
    
    btDevice.setAlias(deviceName)
    btDevice.setDiscoverable(True)
    btDevice.setDiscoverableTime(300)
    btDevice.setPowered(True)
    
    print(f'Device Name: "{btDevice.getAlias()}"')
    print(f'isDiscoverable: {btDevice.getDiscoverable()}')
    print(f'Discoverable Duration: {btDevice.getDiscoverableTime()}')
    print(f'Devce Powered: {btDevice.getPowered()}')
 
    """
    DBUS_PATH = '/dbus/methods'
    
    dbusName='HeadHodge.smartKeypads'
    dbusPath='/dbus/methods'
    busName = dbus.service.BusName(dbusName, dbus.SystemBus())
    #profile = dbus.service.Object(busName, dbusPath)
    profile = Profile(dbus.SystemBus(), dbusPath)
    """


    #print(f'registered bluez5 profile, UUID: \'{profileUUID}\')
        
##########################
def outControlChannel():
##########################
    try:
        print(' \n***WAIT for controlChannel post')

        #infinite wait to block control channel thread
        while True:
            pass

    except:
        print('Abort outControlChannel', sys.exc_info()[0])
        traceback.print_exc()
        return None
 
##########################
def outDataChannel():
##########################
    try:
        print(' \n***WAIT for dataChannel post')
        
        #infinite wait to block control channel thread
        while True:
            pass
            
    except:
        print('Abort outDataChannel', sys.exc_info()[0])
        traceback.print_exc()
        return None

##########################
def start(options={"controlPort": 17, "interruptPort": 19}):
##########################
    print(f"Start btProfile")

    try:
        #print('get bluez ProfileManager1 interface')
        #dbusObject = dbus.SystemBus().get_object('org.bluez', '/org/bluez')
        #profileManager = dbus.Interface(dbusObject, 'org.bluez.ProfileManager1')
    
        #print('register profile')
        loadProfile()
      
        #controlOptions = {"agentEvent": outControlChannel}
        #threading.Thread(target=btServer.start, args=(options["controlPort"], controlOptions)).start()

        #dataOptions = {"agentEvent": outDataChannel}
        #threading.Thread(target=btServer.start, args=(options["interruptPort"], dataOptions)).start()

        #setDiscoveryTime(timeout=30)
        #self.device.alias = self.MY_DEV_NAME
        #self.device.discoverabletimeout = 0
        #self.device.discoverable = True
    
        # Start btOutput event loop
        print('start btPairbt eventLoop')
        eventloop = GLib.MainLoop()
        eventloop.run()
    except:
        print('Abort btPairbt: ', sys.exc_info()[0])
        traceback.print_exc()
   
#############################################
##                MAIN
#############################################

# Run this module on main thread to unit test with following code
if __name__ == '__main__':

    start()
    """        
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
        
# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    """