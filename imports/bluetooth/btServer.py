#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
"""
create a bluetooth device to emulate a HID keyboard
"""
#############################################
##            MODULE VARIABLES
#############################################
print("Load btServer")

#from gi.repository import GLib
#from dbus.mainloop.glib import DBusGMainLoop
#DBusGMainLoop(set_as_default=True)
import os, sys, time, traceback, json, socket, threading, asyncio
import btDevice

_deviceAddress = 'DC:A6:32:65:8A:AB'
          
#############################################
async def connect(server, loop, options):
#############################################
    while True:
        try:
            print("***WAIT for a connection")
            connection,  address = await loop.sock_accept(server)
            print(f'***CONNECTED at address: {address}\n')
            
            while True:
                post = await loop.run_in_executor(None, options['agentEvent'])
                print(f'***TRANSFER: {post}')
                await loop.sock_sendall(connection, post)
                await loop.sock_sendall(connection, bytes([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]))
        except:
            print('***ABORT Connection: ', sys.exc_info()[0])
            #traceback.print_exc()
            print(' \n \n')
        
####################################################################################################
def start(channel, options={}): # Note: standard hid channels > "controlPort": 17, "interruptPort": 19
####################################################################################################
    print("Start btServer")
    #systemBus = dbus.SystemBus()

    try:
        if(options.get('agentEvent', None) == None):
            print('Abort btServer, option for "agentEvent" missing')
            return
            
        #_options = options
        #dBusProperty = dbus.Interface(systemBus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
        #deviceAddress = dBusProperty.Get('org.bluez.Adapter1', 'Address')
        deviceAddress = btDevice.getAddress()
        print(f'create server at deviceAddress: {deviceAddress} on hdiChannel: {channel}')
        
        server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((deviceAddress, channel))
        server.setblocking(False)
        server.listen(1)

        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(connect(server, loop, options))
        #_loop.run_forever()
    except:
        print('Abort btServer: ', sys.exc_info()[0])
        traceback.print_exc()
    
#############################################
##                MAIN
#############################################   

# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    P_CTRL = 17 # Service port - must match port configured in SDP record
    P_INTR = 19 # Service port - must match port configured in SDP record#Interrrupt port

    start(P_CTRL)
    start(P_INTR)
