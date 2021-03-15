#############################################
##            GLOBAL VARIABLES
#############################################
print('Load usbServer')

#import paho.mqtt.client as mqtt
import websocket
import sys, time, json, threading, traceback, asyncio
from evdev import InputDevice, categorize, ecodes

############################
def monitor(keyData,):
############################
    print('***********monitor**********')
    lastCode = 0
    lastTime = 0
    startTime = 0

    while True:
        if(keyData["scanTime"] == lastTime):
            if(lastCode == 0 or time.time() - keyData["scanTime"] < .3): continue
            #print(f'****Dump {keyData["scanCode"]} Duration: {time.time() - startTime}*******')
            lastCode = 0
            continue
       
        if(lastCode == 0): 
            eventData = {
                "keyCode" : keyData["keyCode"],
                "scanCode": keyData["scanCode"],
                "channel" : keyData["channel"],
                "device"  : keyData["device"],
                "zone"    : keyData["zone"],
                "duration": .3
            }
                        
            #print(f'\n***usbUSER: {eventData}')
            keyData['userEvent'](eventData)
                
            startTime = keyData["scanTime"];
            lastCode = keyData["scanCode"]

        #print(keyData["scanTime"] - lastTime, keyData["scanTime"] - startTime)
        lastTime = keyData["scanTime"]
        
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

        keyData = {
            "scanTime" : 0,
            "scanCode" : 0,
            "keyCode"  : 0,
            "channel"  : channel,
            "device"   : device.name,
            "zone"     : options['zone'],
            "userEvent": options['userEvent']
        }
        
        threading.Thread(target=monitor, args=(keyData,)).start()    
        
        for event in device.async_read_loop():
            if event.type != 1 : continue
            
            inputEvent = categorize(event)
            #print(f'keyState: {inputEvent.keystate}')
            
            
            #print(event, time.time() - lastTime)
            keyData['scanTime'] = time.time()
            keyData['scanCode'] = inputEvent.scancode
            keyData['keyCode']  = inputEvent.keycode
            continue
            
            """
            lastTime = time.time()
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
            """
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
