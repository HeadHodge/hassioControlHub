print('Load dbusExports')
import os, sys, time, traceback
import dbus, dbus.service
import asyncore, socket
from dbus.mainloop.glib import DBusGMainLoop

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        print('handle_read')
        data = self.recv(8192)
        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET)
        self.set_reuse_addr()
        self.bind((host, port))
        print('listen')
        self.listen(1)

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))

        #time.sleep(5)
        
        print('send 11')
        #self.send([ 0xA1, 1, 0, 0, 11, 0, 0, 0, 0, 0 ])
    
        #time.sleep(.35)
        print('send 9')
        #self.send([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ])
        
    def handle_connect():
        print('handle_connect')

    def handle_close():
        print('handle_close')

    def handle_error(err):
        print('handle_error', err)

#server = EchoServer('localhost', 8080)
server17 = EchoServer('DC:A6:32:65:8A:AB', 17)
#server19 = EchoServer('DC:A6:32:65:8A:AB', 19)
asyncore.loop()