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
path = os.path.join(os.path.dirname(__file__), '../../imports/dbus')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps')
sys.path.append(path)

import usbServer, btServer, btDevice, btProfile, keyMaps

_ioQueue = queue.Queue()

_inOptions = {
    "zone": sys.argv[1],
    "channels": sys.argv[2].split(','),
    "userEvent": None,
}

_outControlOptions = {
    "userEvent" : None,
}

_outDataOptions = {
    "userEvent" : None,
}
        
#############################################
async def inUserEvent(post):
#############################################
    print(f'***inUSER: {post}')
    global _ioQueue, _sessionId
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

##########################
async def outDataEvent(post, options):
##########################
    print(f' \n*************************************************************************')
    print(f' \n***dataUSER: RECEIVED POST: {post}')
    print(f' \n***dataUSER: WAIT')
    
##########################
async def outControlEvent(post, options):
##########################
    print(f' \n*************************************************************************')
    print(f' \n***controlUSER: RECEIVED POST: {post}')
    print(f' \n***controlUSER: WAIT')
   
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

        # Start output module
        try:            
            _outControlOptions['userEvent'] = outControlEvent
            _outControlOptions['channel'] = options["controlPort"]
            threading.Thread(target=btServer.start, args=(_outControlOptions,)).start()

            _outDataOptions['userEvent'] = outDataEvent
            _outDataOptions['channel'] = options["interruptPort"]
            threading.Thread(target=btServer.start, args=(_outDataOptions,)).start()

            time.sleep(1)
        except:
            print('Abort btServer: ', sys.exc_info()[0])
            traceback.print_exc()

        # Start input module
        try:
            _inOptions['userEvent'] = inUserEvent
            threading.Thread(target=usbServer.start, args=(_inOptions,)).start()
            time.sleep(1)
            print(f' \n*************************************************************************')
            print('***WAIT usbUSER')
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
