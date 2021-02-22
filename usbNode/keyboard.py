#############################################
##            GLOBAL VARIABLES
#############################################
#import paho.mqtt.client as mqtt
import websocket
import sys, time, json, threading, _thread as thread
from evdev import InputDevice, categorize, ecodes

if len(sys.argv) < 3: 
    print('Terminate hubClient, missing required zone and/or event list argument')
    sys.exit()
    
zone = sys.argv[1]
channels = sys.argv[2].split(',')
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

lastCode = 0
lastTime = time.time()

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
def captureInput(connection, channelNum):
###################
    print("Enter captureInput on channel:"+channelNum)
    
    channel = InputDevice(f'/dev/input/event{channelNum}')
    channel.grab()
    
    for event in channel.async_read_loop():
        global lastCode
        global lastTime
        
        if event.type != 1 : continue
        inputEvent = categorize(event)
        print(f'keyState: {inputEvent.keystate}')
        if(inputEvent.keystate != 0): continue
        if(inputEvent.scancode == lastCode and time.time() - lastTime < 0.75): continue
        lastCode = inputEvent.scancode
        lastTime = time.time()
        
        command = getCommand(inputEvent.keycode, inputEvent.scancode)
        
        print(f'Send command from channel: {channelNum}, command: {command}, zone: {zone}')
        connection.send('{' + f'"type": "command", "command": "{command}", "zone": "{zone}", "device": "usb remote"' + '}')

    return
      
###################
def checkConnection(connection):
###################
    print("Enter checkConnection")

    time.sleep(300)
    connection.send('{' + f'"type": "command", "command": "Ping", "zone": "{zone}", "device": "usb remote"' + '}')
    checkConnection(connection)
    
###################
# onMessage
###################
def onMessage(connection, message):
    print("Enter onMessage, received: ", message)

###################
# onError
###################
def onError(connection, error):
    print(f"Enter onError: ", error)
    sys.exit(1)

###################
# onClose
###################
def onClose(connection):
    print("Enter onClose")
         
###################
# onOpen
###################
def onOpen(connection):
    print("Enter onOpen USB Input")
    
    for channel in channels:
        thread.start_new_thread(captureInput, (connection, channel))

    thread.start_new_thread(checkConnection, (connection,))
	
#############################################
##                MAIN
##Open server to listen for control input
#############################################
print('Started mqttClient.py')
websocket.enableTrace(True)

_webSocket = websocket.WebSocketApp("ws://192.168.0.164:8080",
    on_message = onMessage,
    on_error = onError,
    on_close = onClose,
    on_open = onOpen) 

_webSocket.run_forever()
