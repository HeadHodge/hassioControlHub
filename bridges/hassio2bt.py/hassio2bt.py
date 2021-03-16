#############################################
##            MODULE VARIABLES
#############################################
print('Load hassio2bt')

import os, sys, time, json, asyncio, traceback, queue, threading

path = os.path.join(os.path.dirname(__file__), '../../imports/network')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/bluetooth')
sys.path.append(path)
path = os.path.join(os.path.dirname(__file__), '../../imports/maps')
sys.path.append(path)

import wsClient, btServer, btDevice, btProfile, keyMaps

_inOptions = {
    "endpoint": "ws://192.168.0.160:8123/api/websocket",
    "address": "192.168.0.160",
    "port": "8123",
    "path": "/api/websocket",
    "userEvent": None,
}

_outControlOptions = {
    "userEvent" : None,
}

_outDataOptions = {
    "userEvent" : None,
}
        
#############################################
async def inUserEvent(post, options):
#############################################
    content = json.loads(post)
    print(f' \n***inUSER: {post}, {content["type"]}')
    global _sessionId

    if(content['type'] == "auth_required"):
        payload = {
            "type": "auth",
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1NmVhNzU3ODkzMDE0MTMzOTJhOTZiYmY3MTZiOWYyOCIsImlhdCI6MTYxNDc1NzQ2OSwiZXhwIjoxOTMwMTE3NDY5fQ.K2WwAh_9OjXZP5ciIcJ4lXYiLcSgLGrC6AgTPeIp8BY"
        }
        
        print(f' \n***inTRANSFER: {payload}')
        await options['transfer'](payload, options)

    elif(content['type'] == "auth_ok"):
        payload = {
            "id": 1, 
            "type": "subscribe_events",	
            "event_type": "postPublished"
        }
        
        print(f' \n***inTRANSFER: {payload}')
        await options['transfer'](payload, options)

    elif(content['type'] == "event" and content['event']['event_type'] == 'postPublished'):
        payload = content['event']['data']['post']
        
        print(f' \n***inTRANSFER: {payload}')
        await _outDataOptions['transfer'](payload, _outDataOptions)
   
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
    print('Start hassio2bt')

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
            print(f' \n*************************************************************************')
            print('***inUSER: WAIT')
            _inOptions['userEvent'] = inUserEvent
            threading.Thread(target=wsClient.start, args=(_inOptions,)).start()
            time.sleep(1)
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
