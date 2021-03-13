#############################################
##            GLOBAL VARIABLES
#############################################
print('Load usbServer')

#import paho.mqtt.client as mqtt
import websocket
import sys, time, json, threading, traceback
from evdev import InputDevice, categorize, ecodes
              
############################
def captureInput(channel, options):
############################
    #print(f'captureInput on channel: {channel}')
    
    try:
        lastCode = 0
        lastTime = time.time()
        device = InputDevice(f'/dev/input/event{channel}')
        device.grab()
        print(f'grabbed: {device} in zone: {options["zone"]}')
    
        for event in device.async_read_loop():
            #print(event)
            
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
                "zone"    : options['zone'],
                "time"    : time.time()
            }
                        
            #print(f'\n***usbUSER: {eventData}')
            options['userEvent'](eventData)
    except:
        print(f'Abort captureInput: {sys.exc_info()[0]}')
        traceback.print_exc()

###################
# start
###################
def start(options={"zone":"masterBedroom", "channels": [3,4,5,6]}):
    print('Start usbServer')

    try:
        if(options.get('userEvent', None) == None): print('Abort usbServer, no "userEvent" method provided in options'); return
        if(options.get('queue', None) == None): print('Abort usbServer, no "queue" object provided in options'); return
        if(options.get('zone', None) == None): print('Abort usbServer, no "zone" value provided in options'); return
        #_options = options
       
        for channel in options['channels']:
            threading.Thread(target=captureInput, args=(channel, options)).start()

    except:
        print('Abort usbServer', sys.exc_info()[0])
        traceback.print_exc()
    
#############################################
##                MAIN
##Open server to listen for control input
#############################################

if __name__ == "__main__":
# Run this module on main thread to unit test with following code

    start()
