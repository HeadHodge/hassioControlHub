#!/usr/bin/python3
import os  # used to all external commands
import sys  # used to exit the script
import time
import dbus
import dbus.service
import dbus.mainloop.glib

class dbusClient():
    print("Loading dbusClient")

    def __init__(self):
        print("Starting dbusClient")
        self.bus = dbus.SystemBus()
        self.client = self.bus.get_object('org.thanhle.btkbservice', '/org/thanhle/btkbservice')
        self.iface = dbus.Interface(self.client, 'org.thanhle.btkbservice')
    
    def send_key_state(self):
        """sends a single frame of the current key state to the emulator server"""
        bin_str = ""
        element = self.state[2]
        for bit in element:
            bin_str += str(bit)
        self.iface.send_keys(int(bin_str, 2), self.state[4:10])
    
    def send_string(self, string=''):
        """sends a single frame of the current key state to the emulator server"""
        self.iface.send_string(string)

if __name__ == "__main__":
    dc = dbusClient()
    string_to_send = 'Hello World'
    print("Sending " + string_to_send)
    dc.send_string(string_to_send)
    print("Done.")
