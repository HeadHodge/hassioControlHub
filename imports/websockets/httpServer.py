#############################################
##            MODULE VARIABLES
#############################################
print('Load wsServer')
import sys, time, json
import traceback, asyncio
from aiohttp import web

_options = None       

#######################################
def start(options):
#######################################
    print('Start wsServer')
    global _options
    
    try:
        _options = options
        
        start_server = websockets.serve(onConnect, options["address"], options["port"])
        asyncio.get_event_loop().run_until_complete(start_server)

        print(f'wait for connections on address: {options["address"]}, port: {options["port"]}')
        asyncio.get_event_loop().run_forever()

    except:
        print('Abort wsServer.py', sys.exc_info()[0])
        traceback.print_exc()

#######################################
#              MAIN
#######################################
import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = '../'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
#handler_object = http.server.SimpleHTTPRequestHandler
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()