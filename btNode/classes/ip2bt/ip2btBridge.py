#############################################
##            GLOBAL VARIABLES
#############################################
import threading, asyncio
import sys, time, json
from wsServer import wsServer
from btServer import btServer
from gi.repository import GLib

class ip2btBridge:
    print('Load ip2btBridge')
    """
    """  
    ipIN = None
    btOUT = None
    
    def __init__(self):
        print('Starting ip2btBridge')
        task = threading.Thread(target=self.def1())
        task.daemon = True
        task.start()
        
        task1 = threading.Thread(target=self.def2())
        task1.daemon = True
        #task1.start()

        mainloop = GLib.MainLoop()
        mainloop.run()
        print('Exit ip2btBridge')
        
    def printName(self, name):
        print(f'my name is: {name}')
        
    def def1(self):
        print('enter def1')
       
        #self.printName('Robby')
        btIN = btServer(self)
        
        while True:
            time.sleep(5)
        #eventloop = asyncio.get_event_loop()
        #eventloop.run_forever()

        print('exit def1')

    def def2(self):
        print('enter def2')
        btOUT = btServer(self)
        print('exit def2')

#try:
myclass = ip2btBridge()
    
#except:
#    print('Abort 1p2btBridge', sys.exc_info()[0])
