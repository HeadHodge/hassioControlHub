#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
print("Load btServer")
import traceback
import os, sys, time, json, socket
import asyncio, queue
from gi.repository import GLib

"""
create a bluetooth device to emulate a HID keyboard
"""
_dataOut = None
P_CTRL = 17 # Service port - must match port configured in SDP record
P_INTR = 19 # Service port - must match port configured in SDP record#Interrrupt port
        
def start(dataOut):
    global _dataOut
    
    print("Start btServer")
    _dataOut = dataOut
    
    connect()
    
def address():
    """Return the adapter MAC address."""
    return 'DC:A6:32:65:8A:AB'
    #return adapter_property.Get(ADAPTER_IFACE, 'Address')
  
def connect():
    """
    Listen for connections coming from HID client
    """

    # Socket server & client objects for hid control
    scontrol = None
    ccontrol = None
        
    # Socket server & client object for hid interrupt
    sinterrupt = None
    cinterrupt = None
    
    while True:
        print(f' \nwait for bluetooth connections on {address()} ports {P_CTRL} and {P_INTR}')

        if(scontrol): scontrol.close
        scontrol = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        scontrol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        scontrol.bind((address(), P_CTRL))
        scontrol.listen(1) # Limit of 1 connection
        ccontrol, cinfo = scontrol.accept() # Block until connected
        print(f'{cinfo[0]} connected to control channel')
        
        if(sinterrupt): sinterrupt.close
        sinterrupt = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        sinterrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sinterrupt.bind((address(), P_INTR))
        sinterrupt.listen(1) # Limit of 1 connection
        cinterrupt, cinfo = sinterrupt.accept() # Block until connected
        print(f'{cinfo[0]} connected to interrupt channel')
        
        time.sleep(5)
        
        while True:
            if(_dataOut.empty() == True): continue
            dataOut = _dataOut.get()
            print('sendData: ', dataOut)
             
            try:
               cinterrupt.send(bytes(dataOut))
            except:
                print(f'send dataOut error: {sys.exc_info()[0]}')
                traceback.print_exc()
                break

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