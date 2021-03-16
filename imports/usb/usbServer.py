#############################################
##            GLOBAL VARIABLES
#############################################
print('Load usbServer')

import sys, time, json, threading, traceback, asyncio
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
        postTime = 0
        
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
        
        for event in device.async_read_loop():
            if event.type != 1 : continue
            if(postTime != 0 and time.time()-postTime < .3): continue
            postTime = time.time()

            inputEvent = categorize(event)

            eventData = {
                "keyCode" : inputEvent.keycode,
                "scanCode": inputEvent.scancode,
                "channel" : channel,
                "device"  : device.name,
                "zone"    : options['zone'],
                "time"    : time.time()
            }
                        
            asyncio.run(options['userEvent'](eventData))

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
        #if(options.get('queue', None) == None): print('Abort usbServer, no "queue" object provided in options'); return
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
