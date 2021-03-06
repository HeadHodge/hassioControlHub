#############################################
##            GLOBAL VARIABLES
#############################################
print('Load usbServer')

#import paho.mqtt.client as mqtt
import websocket
import sys, time, json, threading, traceback
from evdev import InputDevice, categorize, ecodes
commands = {
          1: "Exit",
          2: "1",
          3: "2",
          4: "3",
          5: "4",
          6: "5",
          7: "6",
          8: "7",
          9: "8",
         10: "9",
         11: "0",
         28: "Ok",
         59: "Silence/Sound",
        103: "Up",
        104: "Less",
        105: "Left",
        106: "Right",
        108: "Down",
        109: "More",
        113: "Silence/Sound",
        114: "Softer",
        115: "Louder",
        116: "Off/On",
        127: "Menu",
        158: "Exit",
        163: "Forward",
        164: "Stop/Start",
        165: "Backward",
        172: "Home",
        191: "Set",
        240: "Focus",
        272: "Ok",
        273: "Exit"
}

_zone = None

###################
def getCommand(inputChar, inputCode):
###################
    try:
        print('Enter getCommand', inputCode, commands[inputCode])
        return(commands[inputCode])
        
    except Exception as e:
        print(e)
        return(inputChar)
      
###################
def checkConnection(connection):
###################
    print("Enter checkConnection")

    time.sleep(300)
    connection.send('{' + f'"type": "command", "command": "Ping", "zone": "{zone}", "device": "usb remote"' + '}')
    checkConnection(connection)
    
          
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
            if(inputEvent.scancode == lastCode and time.time() - lastTime < 0.75): continue
            lastCode = inputEvent.scancode
            lastTime = time.time()
        
            print(f'captured scanCode: {inputEvent.scancode}, keyCode: {inputEvent.keycode} on channel: {channel}')
    except:
        print(f'Abort captureInput: {sys.exc_info()[0]}')
        traceback.print_exc()

###################
# start
###################
def start(zone='masterBedroom', channels=[3,4,5,6]):
    print('Start usbServer')
    global _zone

    try:
        _zone = zone
        
        for channel in channels:
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
    
    """
    if len(sys.argv) < 3: 
        print('Terminate hubClient, missing required zone and/or event list argument')
        sys.exit()
    
    zone = sys.argv[1]
    
    channels = sys.argv[2].split(',')
    start(zone, channels)
    """