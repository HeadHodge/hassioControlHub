#############################################
##            GLOBAL VARIABLES
#############################################
print('Load keyCode2hassio')
from gi.repository import GLib
from multiprocessing import Process
import os, sys, time, json, traceback, queue

path = os.path.join(os.path.dirname(__file__), '../imports/websockets')
sys.path.append(path)
import wsClient, wsServer

_inputOptions = {
    "endpoint": "ws://127.0.0.1:8181",
    "address": "127.0.0.1",
    "port": "8181"
   }
   
_outputOptions = {
    "endpoint": "ws://127.0.0.1:8181",
    "address": "127.0.0.1",
    "port": "8181"
   }
   
try:
    # Start wsServer Module
    try:
        wsServer = Process(target=wsServer.start, args=(_outputOptions,))
        wsServer.start()
    except:
        print('Abort run wsServer: ', sys.exc_info()[0])
        traceback.print_exc()
   
    # Start wsClient Module
    try:
        wsClient = Process(target=wsClient.start, args=(_inputOptions,))
        wsClient.start()
    except:
        print('Abort run wsClient: ', sys.exc_info()[0])
        traceback.print_exc()
    
except:
    print('Abort keyCode2hassio.py', sys.exc_info()[0])
    traceback.print_exc()
