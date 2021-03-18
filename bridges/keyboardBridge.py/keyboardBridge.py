#############################################
##            MODULE VARIABLES
#############################################
print('Load usb2bt')

from multiprocessing import Process
from dbus.mainloop.glib import DBusGMainLoop
import os, sys, time, json, asyncio, traceback, queue, threading
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

import usbServer, btServer, wsClient, btDevice, btProfile, keyMaps, map2hassio

_transferNum = 0

_inOptions = {
    "zone": sys.argv[1],
    "channels": sys.argv[2].split(','),
    "userEvent": None,
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
    "userEvent": None,
    "agentEvent": None
   }
        
#############################################
async def inUserEvent(post):
#############################################
    print(f'***inUSER: {post}')
    global _transferNum
    
    usbNum = post.get('scanCode', 0)
    zone = post.get('zone', 'home')
    keyCode = keyMaps.usbNum2keyCode(usbNum)
    if(keyCode == None): print(f'Abort inPosts, invalid keyCode: {keyCode}'); return

    print(f' \n***TRANSLATE: {keyCode}')
    hassioSequence = map2hassio.keyCode2hassio(keyCode, zone)
    if(hassioSequence == None): return
    
    for task in hassioSequence:
        key = list(task.keys())[0]
        data = task[key]
        command = key.split('/')
        
        if(command[0] == 'sleep'):
            payload = {
                "id": 0, 
                "type": "sleep",	
                "service_data": data
            }
            
            _ioQueue.put(payload)
            continue
            
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
            await _btTransferOptions['transfer'](payload, _wsTransferOptions)
    
        print(f'************************************************************************* \n')
        print(f' \n*************************************************************************')
        print('******inUSER: WAIT')
   
    
    
    
    
    
    
    
    """
    usbNum = post.get('scanCode', 0)
    zone = post.get('zone', 'home')

    keyCode = keyMaps.usbNum2keyCode(usbNum)
    print(f'***TRANSLATE: usbNum: {usbNum} == keyCode: {keyCode}')

    key = keyMaps.keyNum2key(keyCode, zone)
    if(key == None): print(f'Abort inUserEvent, invalid keyCode {keyCode}'); return
    
    print(f'***TRANSFER: {key}')
    await _outDataOptions['transfer'](key, _outDataOptions)

    print(f'************************************************************************* \n')
    print(f' \n*************************************************************************')
    print('******inUSER: WAIT')
    """
    
##########################
async def btControlEvent(post, options):
##########################
    print(f' \n*************************************************************************')
    print(f' \n***btCONTROL: RECEIVED POST: {post}')
    print(f' \n***btCONTROL: WAIT')
    
##########################
async def btTransferEvent(post, options):
##########################
    print(f' \n*************************************************************************')
    print(f' \n***btUSER: RECEIVED POST: {post}')
    print(f' \n***btUSER: WAIT')
        
#############################################
async def wsTransferEvent(post, options):
#############################################
    print(f' \n***wsUSER: {post}')
    print(f' \n***********************************************************************')
    print(f'***wsUSER WAIT')

    content = json.loads(post)
    if(content['type'] == "auth_required"):
        payload = {
            "type": "auth",
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"
        }
        
        print(f' \n***outTRANSFER: {payload}')
        #asyncio.run(options['transfer'](payload, options))
        await options['transfer'](payload, options)
   
#############################################
def onConnectSignal(interface, changed, path):
#############################################
    print(f'****CONNECTION ALERT****, interface: {interface}, connected: {changed["Connected"]}')
   
#############################################
def start(options={"controlPort": 17, "interruptPort": 19}):
#############################################
    print('Start usb2bt')

    try:
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
            _inOptions['userEvent'] = inUserEvent
            threading.Thread(target=usbServer.start, args=(_inOptions,)).start()
            time.sleep(1)
            print(f' \n***********************************************************************')
            print(f'***inUSER WAIT')
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
