#############################################
##            MODULE VARIABLES
#############################################
print('Load usb2bt')

from multiprocessing import Process
from dbus.mainloop.glib import DBusGMainLoop
import os, sys, time, json, asyncio, traceback, queue, threading, importlib
if len(sys.argv) < 3: 
    print('Terminate usb2hassio, missing required zone name and/or event list arguments')
    print('Example: python3 usb2hassio.py masterBedroom 3,4,5,6')
    sys.exit()

path = os.path.join(os.path.dirname(__file__), '../../imports/usb')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/bluetooth')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/network')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/dbus')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps/map2hassio.py')
sys.path.append(path)

import usbServer, btServer, httpServer, wsioServer, wsClient, btDevice, btProfile, keyMaps, map2hassio

_transferNum = 0

_usbInputOptions = {
    "zone": sys.argv[1],
    "channels": sys.argv[2].split(','),
    "userEvent": None,
}

_wssInputOptions = {
    "port": "8080",
    "firstPost": "User",
    "userEvent" : None,
    "agentEvent" : None
   }

_btControlOptions = {
    "userEvent" : None,
}

_btTransferOptions = {
    "userEvent" : None,
}

_wsTransferOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "firstPost": "User",
    "ack": True,
    "userEvent": None,
    "agentEvent": None
   }
   
#############################################
async def translateInput(keyCode, zone):
#############################################
    print(f' \n***TRANSLATE: {keyCode}, {zone}')
    global _transferNum

    hassioSequence = map2hassio.keyCode2hassio(keyCode, zone)
    
    if(hassioSequence == None): return
    
    if(hassioSequence == 'RELOAD'): 
        print('reload')
        importlib.reload(keyMaps)
        importlib.reload(map2hassio)
        return
    
    for task in hassioSequence:
        key = list(task.keys())[0]
        data = task[key]
        command = key.split('/')
        
        if(command[0] == 'sleep'): print(f' \n***SLEEP: {data} seconds'); time.sleep(data); continue
            
        _transferNum += 1
        
        payload = {
            "id": _transferNum, 
            "type": "call_service",	
            "domain": command[0],
            "service": command[1],
            "service_data": data
        }
        
        #Route Payload to proper destination
        if(payload['domain'] == 'script'):
            print(f' \n***btTRANSFER: {payload}')
            await _btTransferOptions['transfer'](payload, _btTransferOptions)
        else:
            print(f' \n***wsTRANSFER: {payload}')
            _wsTransferOptions['ack'] = False
            await _wsTransferOptions['transfer'](payload, _wsTransferOptions)
    
        print(f'************************************************************************* \n')
        print(f' \n*************************************************************************')
        print('******INPUT: WAIT')
        
#############################################
async def usbInputEvent(post):
#############################################
    print(f'***usbIN: {post}')
    global _transferNum
    
    usbNum = post.get('scanCode', 0)
    zone = post.get('zone', 'home')
    keyCode = keyMaps.usbNum2keyCode(usbNum)
    if(keyCode == None): print(f'Abort inPosts, invalid keyCode: {keyCode}'); return

    await translateInput(keyCode, zone)
 
#############################################
async def wssInputEvent(post):
#############################################
    print(f' \n***wssIN: {post}')
    global _ioQueue, _sessionId
    
    keyCode = post.get('keyCode', None)
    zone = post.get('zone', 'home')
    if(keyCode == None): print(f'Abort inPosts, invalid keyCode: {keyCode}'); return
    
    await translateInput(keyCode, zone)
       
##########################
async def btControlEvent(post, options):
##########################
    return
    print(f' \n***btCONTROL: RECEIVED POST: {post}')
    print(f' \n***btCONTROL: WAIT')
    print(f'************************************************************************* \n')
    
##########################
async def btTransferEvent(post, options):
##########################
    print(list(bytes(post)), len(post))
    print(f' \n*************************************************************************')
    print(f' \n***btOUT: RECEIVED POST: {post}')
    print(f' \n***btOUT: WAIT')
        
#############################################
async def wsTransferEvent(post, options):
#############################################
    print(f' \n***wsOUT: {post}')
    options['ack'] = True
    
    content = json.loads(post)
    if(content['type'] == "auth_required"):
        payload = {
            "type": "auth",
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"
        }
        
        print(f' \n***wsTRANSFER: {payload}')
        #asyncio.run(options['transfer'](payload, options))
        await options['transfer'](payload, options)
        print(f' \n***********************************************************************')
        print(f'***wsOUT: WAIT')
   
#############################################
def onConnectSignal(interface, changed, path):
#############################################
    print(f'****CONNECTION ALERT****, interface: {interface}, connected: {changed["Connected"]}')
   
#############################################
def start(options={"controlPort": 17, "interruptPort": 19}):
#############################################
    print('Start usb2bt')

    try:
        # Start httpServer Module
        try:
            threading.Thread(target=httpServer.start).start()
            time.sleep(1)
        except:
            print('Abort httpServer: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start wsServer Module
        try:
            _wssInputOptions['userEvent'] = wssInputEvent
            threading.Thread(target=wsioServer.start, args=(_wssInputOptions,)).start()
            time.sleep(1)
        except:
            print('Abort wsServer: ', sys.exc_info()[0])
            traceback.print_exc()

        # Enable ConnectSignal
        try:
            threading.Thread(target=btDevice.enableConnectSignal, args=(onConnectSignal,)).start()
            threading.Thread(target=btProfile.start).start()
            time.sleep(1)
        except:
            print('Abort enableConnectSignal: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start bt output module
        try:            
            _btControlOptions['userEvent'] = btControlEvent
            _btControlOptions['channel'] = options["controlPort"]
            threading.Thread(target=btServer.start, args=(_btControlOptions,)).start()

            _btTransferOptions['userEvent'] = btTransferEvent
            _btTransferOptions['channel'] = options["interruptPort"]
            threading.Thread(target=btServer.start, args=(_btTransferOptions,)).start()

            time.sleep(1)
        except:
            print('Abort btServer: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start ws output module
        try:            
            _wsTransferOptions['userEvent'] = wsTransferEvent
            threading.Thread(target=wsClient.start, args=(_wsTransferOptions,)).start()

            time.sleep(1)
        except:
            print('Abort btServer: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start input module
        try:
            _usbInputOptions['userEvent'] = usbInputEvent
            threading.Thread(target=usbServer.start, args=(_usbInputOptions,)).start()
            time.sleep(1)
            print(f' \n***********************************************************************')
            print(f'***INPUT: WAIT')
        except:
            print('Abort wsClient: ', sys.exc_info()[0])
            traceback.print_exc()
    except:
        print('Abort usb2bt: ', sys.exc_info()[0])
        traceback.print_exc()
  
#############################################
##                MAIN
#############################################   

# Run this module on main thread to unit test with following code
if __name__ == '__main__':

    start()
