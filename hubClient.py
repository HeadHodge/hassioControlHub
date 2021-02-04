############################
#
# Capture Control Input
#
############################
import asyncio, evdev, sys, websocket, websockets
import _thread as thread
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

###################
# getCommand
###################
def getCommand(inputChar, inputCode):
    #global commands
    try:
        print('Enter getCommand', inputCode, commands[inputCode])
        return(commands[inputCode])
        
    except Exception as e:
        print(e)
        return(inputChar)
   
###################
# captureInput
###################
def captureInput(ws, channelNum):
    print("Enter captureInput on channel:"+channelNum)
    
    channel = evdev.InputDevice(f'/dev/input/event{channelNum}')
    channel.grab()

    for event in channel.async_read_loop():
        if event.type != 1 : continue
        inputEvent = categorize(event)
        if inputEvent.keystate != 0 : continue

        command = getCommand(inputEvent.keycode, inputEvent.scancode)
        #ws.send('{"type": "command", "command": "Ok", "zone": "masterBedroom"}')
        print(f'Send command from channel: {channelNum}, command: {command}, zone: {zone}')
        ws.send('{' + f'"type": "command", "command": "{command}", "zone": "{zone}"' + '}')
   
    return

###################
# onMessage
###################
def onMessage(ws, message):
    print("Enter onMessage: ", message)

###################
# onError
###################
def onError(ws, error):
    print(f"Enter onError: ", error)
    sys.exit(1)

###################
# onClose
###################
def onClose(ws):
    print("Enter onClose")
         
###################
# onOpen
###################
def onOpen(ws):
    print("Enter on_open")

    for channel in channels:
        thread.start_new_thread(captureInput, (ws, channel, ))
    
###################
#      MAIN
###################
    
websocket.enableTrace(True)

_ws = websocket.WebSocketApp("ws://192.168.0.164:8080",
    on_message = onMessage,
    on_error = onError,
    on_close = onClose,
    on_open = onOpen) 

_ws.run_forever()
