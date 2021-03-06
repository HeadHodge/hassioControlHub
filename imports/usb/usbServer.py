#############################################
##            GLOBAL VARIABLES
#############################################
print('Load usbServer')

#import paho.mqtt.client as mqtt
import websocket
import sys, time, json, threading, traceback
from evdev import InputDevice, categorize, ecodes

_zone = None
_onInput = None
               
############################
def captureInput(channel):
############################
    print(f'captureInput on channel: {channel}')
    
    try:
        lastCode = 0
        lastTime = time.time()
        device = InputDevice(f'/dev/input/event{channel}')
        device.grab()
        print(f'grabbed channel: {channel} from device: {device} in zone: {_zone}')
    
        for event in device.async_read_loop():
            if event.type != 1 : continue
            
            inputEvent = categorize(event)
            #print(f'keyState: {inputEvent.keystate}')
            
            if(inputEvent.keystate != 0): continue
            if(inputEvent.scancode == lastCode and time.time() - lastTime < 0.80): continue
            lastCode = inputEvent.scancode
            lastTime = time.time()
        
            #print(f'captured scanCode: {inputEvent.scancode}, keyCode: {inputEvent.keycode} on channel: {channel}')

            eventData = {
                "keyCode" : inputEvent.keycode,
                "scanCode": inputEvent.scancode,
                "keyState": inputEvent.keystate,
                "channel" : channel,
                "device"  : device.name,
                "zone"    : _zone,
                "time"    : time.time()
            }

            _onInput('key', json.dumps(eventData))
    except:
        print(f'Abort captureInput: {sys.exc_info()[0]}')
        traceback.print_exc()

###################
# start
###################
def start(options={"zone":"masterBedroom", "channels": [3,4,5,6]}):
    print('Start usbServer')
    global _zone, _onInput

    try:
        _zone = options['zone']
        _onInput = options['onEvent']
        
        for channel in options['channels']:
            threading.Thread(target=captureInput, args=(channel,)).start()

    except:
        print('Abort usbServer', sys.exc_info()[0])
        traceback.print_exc()

    """
    websocket.enableTrace(True)

    _webSocket = websocket.WebSocketApp(endpoint,
        on_message = onMessage,
        on_error = onError,
        on_close = onClose,
        on_open = onOpen) 

    _webSocket.run_forever()
    """
    
#############################################
##                MAIN
##Open server to listen for control input
#############################################

if __name__ == "__main__":
# Run this module on main thread to unit test with following code

    start()
