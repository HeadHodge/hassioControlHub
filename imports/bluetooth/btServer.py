"""
Bluetooth HID keyboard emulator DBUS Service

Original idea taken from:
http://yetanotherpointlesstechblog.blogspot.com/2016/04/emulating-bluetooth-keyboard-with.html

Moved to Python 3 and tested with BlueZ 5.43
"""
"""
create a bluetooth device to emulate a HID keyboard
"""
#############################################
##            MODULE VARIABLES
#############################################
print("Load btServer")

import os, sys, time, traceback, json, socket, threading, asyncio
import btDevice

#myDeviceAddress = 'DC:A6:32:65:8A:AB'

##########################
async def transfer(post, options):
##########################
    #print(f' \n***TRANSFER {post}')
    if(options.get('connection', None) == None): print('Abort transfer, no active connecton available'); return
    if(post.get('keyCode', None) == None): print('Abort transfer, "keyCode" missing'); return
    if(post.get('hidCode', None) == None): print('Abort transfer, "hidCode" missing'); return
    if(post.get('hidMod', None) == None): print('Abort transfer, "hidMod" missing'); return
    
    repeat = post.get('hidRepeat', 0)    
    wait = post.get('hidWait', .75)
    loop = asyncio.get_event_loop()
    await loop.sock_sendall(options['connection'], bytes([ 0xA1, 1, post['hidMod'], 0, post['hidCode'], 0, 0, 0, 0, 0 ]))
    
    for x in range(repeat): 
        #print(x)
        await loop.sock_sendall(options['connection'], bytes([ 0xA1, 1, post['hidMod'], 0, post['hidCode'], 0, 0, 0, 0, 0 ]))
        await asyncio.sleep(wait)
  
    await loop.sock_sendall(options['connection'], bytes([ 0xA1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]))
        
          
#############################################
async def connect(server, loop, options):
#############################################
    while True:
        try:
            print("***WAIT for a connection")
            connection,  address = await loop.sock_accept(server)
            options['connection'] = connection
            print(f' \n***CONNECTED at address: {address}\n')
            
            while True:
                print(f'***WAIT btPOST')
                post = await loop.sock_recv(connection, 2048)
                if(options.get('userEvent', None) != None): await options['userEvent'](post, options); continue
                print(f' \n***RECEIVED POST: {post}')
                
        except:
            print('***ABORT Connection: ', sys.exc_info()[0])
            traceback.print_exc()
            print(' \n \n')
        
####################################################################################################
def start(options={}): # Note: standard hid channels > "controlPort": 17, "interruptPort": 19
####################################################################################################
    print("Start btServer")

    try:
        if(options.get('channel', None) == None): print('Abort btServer: "channel" option missing'); return
        if(options.get('userEvent', None) == None): print('Abort btServer: "userEvent" option missing'); return
            
        options['address'] = btDevice.getAddress()
        options['transfer'] = transfer
        options['connection'] = None
        
        if(options.get('address', None) == None): print('Abort btServer: "address" option missing'); return
       
        print(f'create server at btAddress: {options["address"]} on hidChannel: {options["channel"]}')
        
        server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((options['address'], options['channel']))
        server.setblocking(False)
        server.listen(1)

        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(connect(server, loop, options))
    except:
        print('Abort btServer: ', sys.exc_info()[0])
        traceback.print_exc()
    
#############################################
##                MAIN
#############################################   

# Run this module on main thread to unit test with following code
if __name__ == '__main__':
    P_CTRL = 17 # Service port - must match port configured in SDP record
    P_INTR = 19 # Service port - must match port configured in SDP record#Interrrupt port

    start(P_CTRL)
    start(P_INTR)
