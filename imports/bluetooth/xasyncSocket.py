import asyncore
import socket
import time
import logging
import json


class Server(asyncore.dispatcher):

    def __init__(self, host, port):

        self.logger = logging.getLogger('SERVER')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(confjson.get('SERVER_QUEUE_SIZE', None))
        self.logger.debug('binding to {}'.format(self.socket.getsockname()))

    def handle_accept(self):
        socket, address = self.accept()
        self.logger.debug('new connection accepted')
        EchoHandler(socket)


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):

        msg = self.recv(confjson.get('RATE', None))
        self.out_buffer = msg
        self.out_buffer += ' server recieve: {}'.format(time.time())
        if not self.out_buffer:
            self.close()


if __name__ == "__main__":

    try:
        print('Server start')
        server = Server('DC:A6:32:65:8A:AB', 19)
        asyncore.loop()
    except:
        logging.error('Something happened,\n'
                      'if it was not a keyboard break...\n'
                      'check if address taken, '
                      'or another instance is running. Exit')
    finally:
        print('Goodbye')