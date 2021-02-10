#############################################
##            GLOBAL VARIABLES
#############################################
import paho.mqtt.client as mqtt
import sys, time, json, _thread as thread
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
def captureInput(client, channelNum):
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
        #ws.send('{' + f'"type": "command", "command": "{command}", "zone": "{zone}"' + '}')
        payload = '{' + f'"type": "command", "command": "{command}", "zone": "{zone}"' + '}'
        client.publish("remoteInput", payload)

    return

# The callback for when a PUBLISH message is received from the server.
###################
def on_message(client, userdata, msg):
###################
    #print(f'Recieved topic: {msg.topic}, payload: {msg.payload}')
    payload = json.loads(msg.payload)
    print(f'Recieved topic: {msg.topic}, payload: {payload}')

# The callback for when the client receives a CONNACK response from the server.
###################
def on_connect(client, userdata, flags, rc):
###################
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for channel in channels:
        thread.start_new_thread(captureInput, (client, channel))

    client.subscribe("controlInput", 0)
	
#############################################
##                MAIN
##Open server to listen for control input
#############################################
print('Started mqttClient.py')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('admin', password='pepper')
client.connect("192.168.0.160", 1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
