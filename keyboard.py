############################
#
# Capture Control Input
#
############################
import asyncio, evdev, sys, websockets
from evdev import InputDevice, categorize, ecodes

async def hello():
    try:
        async with websockets.connect("ws://localhost:8080") as websocket:
            #print(websocket)
            #name = input("What's your name? ")

            await websocket.send('Bob')
            #print(f"> {name}")

            greeting = await websocket.recv()
            print(greeting)
    except Exception as e:
        print('Oopps')
        print(e)
    else:
        print('Done')
        
###################
# Capture Input
###################
async def captureInput(device):
    async for event in device.async_read_loop():
        if event.type != 1 : continue
        inputEvent = categorize(event)
        if inputEvent.keystate != 0 : continue
        print(device.path, inputEvent.keycode, inputEvent.scancode)
        #asyncio.get_event_loop().run_until_complete(hello())
        await hello()

###################
#      MAIN
###################
if len(sys.argv) == 1:
  location = 'home'
else:
  location = sys.argv[1]
  
## Open Control Input Channels
chan1 = evdev.InputDevice('/dev/input/event3')
chan2 = evdev.InputDevice('/dev/input/event4')
chan3 = evdev.InputDevice('/dev/input/event5')
chan4 = evdev.InputDevice('/dev/input/event6')

## Make Control Input Channels Private
chan1.grab()
chan2.grab()
chan3.grab()
chan4.grab()

## Listen for Contrrol Input
print(location, chan1.name, chan1.info.vendor, chan1.info.product, chan1.info.bustype)

for device in chan1, chan2, chan3, chan4:
    asyncio.ensure_future(captureInput(device))

loop = asyncio.get_event_loop()
loop.run_forever()