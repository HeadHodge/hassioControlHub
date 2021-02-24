#!/usr/bin/python3
"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
import os, sys, time, json, socket
from gi.repository import GLib

class btServer:
    """
    create a bluetooth device to emulate a HID keyboard
    """
    P_CTRL = 17 # Service port - must match port configured in SDP record
    P_INTR = 19 # Service port - must match port configured in SDP record#Interrrupt port
        
    def __init__(self):
        print("Starting Bluetooth Server")

        # Socket server & client objects for hid control
        self.scontrol = None
        self.ccontrol = None
        
        # Socket server & client object for hid interrupt
        self.sinterrupt = None
        self.cinterrupt = None

        print('Start Server')
        self.listen()
    
    @property
    def address(self):
        """Return the adapter MAC address."""
        return 'DC:A6:32:65:8A:AB'
        return self.adapter_property.Get(self.ADAPTER_IFACE, 'Address')
  
    def listen(self):
        """
        Listen for connections coming from HID client
        """

        print('Waiting for connections')
        self.scontrol = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        self.scontrol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.sinterrupt = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        self.sinterrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.scontrol.bind((self.address, self.P_CTRL))
        self.sinterrupt.bind((self.address, self.P_INTR))

        # Start listening on the server sockets
        # Limit of 1 connection
        self.scontrol.listen(1)
        self.sinterrupt.listen(1)

        # Block until connected
        self.ccontrol, cinfo = self.scontrol.accept()
        print('{} connected on the control socket'.format(cinfo[0]))

        # Block until connected
        self.cinterrupt, cinfo = self.sinterrupt.accept()
        print('{} connected on the interrupt channel'.format(cinfo[0]))

    # send a string to the bluetooth host machine
    def send_string(self, message):
        try:
            print('Send Message: ', message)
            self.cinterrupt.send(bytes(message))
        except OSError as err:
            print('Send Error: ', error(err))
            error(err)
        
if __name__ == '__main__':
    # The sockets require root permission
    if not os.geteuid() == 0:
        sys.exit('Only root can run this script')

    device = btServer()
    
    time.sleep(10)
    state = [ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ]
    device.send_string(state)
    
    time.sleep(.35)
    state = [ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]
    device.send_string(state)

    mainloop = GLib.MainLoop()
    mainloop.run()
