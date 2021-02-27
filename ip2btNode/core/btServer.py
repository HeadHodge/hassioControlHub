#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
import traceback
import os, sys, time, json, socket
import asyncio
from gi.repository import GLib

"""
create a bluetooth device to emulate a HID keyboard
"""
P_CTRL = 17 # Service port - must match port configured in SDP record
P_INTR = 19 # Service port - must match port configured in SDP record#Interrrupt port
ccontrol = None
cinterrupt = None
        
def start():
    print("Starting Bluetooth Server")
    # Socket server & client objects for hid control
    scontrol = None
    ccontrol = None
        
    # Socket server & client object for hid interrupt
    sinterrupt = None
    cinterrupt = None

    listen()
        
    time.sleep(10)
    state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
    send_string(state)
    
    time.sleep(.35)
    state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]
    send_string(state)
        
    #mainloop = GLib.MainLoop()
    #mainloop.run()
    
#@property
def address():
    """Return the adapter MAC address."""
    return 'DC:A6:32:65:8A:AB'
    #return adapter_property.Get(ADAPTER_IFACE, 'Address')
  
def listen():
    """
    Listen for connections coming from HID client
    """
    print(f'Waiting for connections on {address()} ports {P_CTRL} and {P_INTR}')
    global ccontrol, cinterrupt
    
    scontrol = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
    scontrol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    sinterrupt = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
    sinterrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    scontrol.bind((address(), P_CTRL))
    sinterrupt.bind((address(), P_INTR))

    # Start listening on the server sockets
    # Limit of 1 connection
    scontrol.listen(1)
    sinterrupt.listen(1)

    # Block until connected
    ccontrol, cinfo = scontrol.accept()
    print('{} connected on the control socket'.format(cinfo[0]))

    # Block until connected
    cinterrupt, cinfo = sinterrupt.accept()
    print('{} connected on the interrupt channel'.format(cinfo[0]))
 
# send a string to the bluetooth host machine
def send_string(state):
    try:
        print('Send string: ', state)
        cinterrupt.send(bytes(state))
    except:
        print('Send string Error: ', sys.exc_info()[0])
        traceback.print_exc()

"""
if __name__ == '__main__':
    # The sockets require root permission
    if not os.geteuid() == 0:
        sys.exit('Only root can run this script')

    try:
        device = btServer()
    
        time.sleep(10)
        state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
        device.send_string(state)
    
        time.sleep(.35)
        state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]
        device.send_string(state)

        mainloop = GLib.MainLoop()
        mainloop.run()
    except:
        print('\n! Received keyboard interrupt, quitting threads.\n')
"""