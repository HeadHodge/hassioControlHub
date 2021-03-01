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
        
def start():
    print("Starting Bluetooth Server")
    listen()
    
def address():
    """Return the adapter MAC address."""
    return 'DC:A6:32:65:8A:AB'
    #return adapter_property.Get(ADAPTER_IFACE, 'Address')
  
def listen():
    """
    Listen for connections coming from HID client
    """
    print(f'Waiting for bluetooth connections on {address()} ports {P_CTRL} and {P_INTR}')

    # Socket server & client objects for hid control
    scontrol = None
    ccontrol = None
        
    # Socket server & client object for hid interrupt
    sinterrupt = None
    cinterrupt = None
    
    while True:
        print('connect to control channel')
        if(scontrol): scontrol.close
        scontrol = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        scontrol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        scontrol.bind((address(), P_CTRL))
        scontrol.listen(1) # Limit of 1 connection
        ccontrol, cinfo = scontrol.accept() # Block until connected
        print(f'{cinfo[0]} connected to control channel')
        
        print('connect to innterupt channel')
        if(sinterrupt): sinterrupt.close
        sinterrupt = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        sinterrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sinterrupt.bind((address(), P_INTR))
        sinterrupt.listen(1) # Limit of 1 connection
        cinterrupt, cinfo = sinterrupt.accept() # Block until connected
        print(f'{cinfo[0]} connected to interrupt channel')
    
        while True:
            try:
                time.sleep(5)
                state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
                print('Send string: ', state)
                cinterrupt.send(bytes(state))
    
                time.sleep(.35)
                state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]            
                print('Send string: ', state)
                cinterrupt.send(bytes(state))
            except:
                print(f'Send string Error: {sys.exc_info()[0]}\n')
                traceback.print_exc()
                break
                
def connect():
    """
    Listen for connections coming from HID client
    """
    print(f'Waiting for bluetooth connections on {address()} ports {P_CTRL} and {P_INTR}')
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