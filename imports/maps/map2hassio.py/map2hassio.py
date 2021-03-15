#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassioMap')
import os, sys, importlib, json, traceback

_zones = {}

##########################################
def getCommand(keyCode, zone):
##########################################
    #print(f'Enter getCommand, keyCode: {keyCode}, zone: {zone}')
    controller = None; task = None

    _zones[zone].primaryController = importlib.import_module('controllers.' + _zones[zone].primaryModule)
    controller = _zones[zone].primaryController
    
    #print(f'output task: {json.dumps(controller.tasks[keyCode])}')
    return controller.tasks.get(keyCode, None)
    
##########################################
def getTask(keyCode, zone):
##########################################
    #print(f'Enter onSelectTask with {keyCode} in zone: {zone}')
    task = None

    _zones[zone].isTaskSet = None
    return _zones[zone].tasks.get(keyCode, None)
    
##########################################
def setFocus(keyCode, zone):
##########################################
    #print(f'Enter onSelectFocus with {keyCode} in zone {zone}')

    _zones[zone].isFocusSet = None
    
    if(keyCode == 'Menu'):
        _zones[zone].isTaskSet = True
        print(f'select task for {zone}');return

    def Home()        : return _zones[zone].controllers.get('Home', None)
    def Louder()      : return _zones[zone].controllers.get('Louder', None)
    def Softer()      : return _zones[zone].controllers.get('Softer', None)
    def SoundToggle() : return _zones[zone].controllers.get('SoundToggle', None)
    def Backward()    : return _zones[zone].controllers.get('Backward', None)
    def PlayToggle()  : return _zones[zone].controllers.get('PlayToggle', None)
    def Forward()     : return _zones[zone].controllers.get('Forward', None)

    case = {
        'Home'       : Home,
        'Louder'     : Louder,
        'Softer'     : Softer,
        'SoundToggle': SoundToggle,
        'Backward'   : Backward,
        'PlayToggle' : PlayToggle,
        'Forward'    : Forward
    }
    
    selection = case.get(keyCode, None)
    if(selection == None): return
    _zones[zone].primaryModule = selection()
    print(f'new controller selected: {_zones[zone].primaryModule}')

#############################################
def keyCode2hassio(keyCode, zone='home'):
#############################################
    try:
        #print(f'translate keycode: {key}')
        global _zone
    
        _zones[zone] = importlib.import_module('zones.zone_' + zone)
        
        if(keyCode == 'Set'): keyCode = 'OnToggle'
    
        if(_zones[zone].isFocusSet == True and keyCode == 'OnToggle'): 
            keyCode = 'Open'
            _zones[zone].isFocusSet = None
        
        if(_zones[zone].isFocusSet): return setFocus(keyCode, zone)
        if(_zones[zone].isTaskSet): return getTask(keyCode, zone)
      
        if(keyCode == 'Focus'): _zones[zone].isFocusSet = True; return print('Set Focus Flag')

        if(keyCode == 'SoundToggle'):
            if(_zones[zone].isSilent == True):
                keyCode = 'Sound'
                _zones[zone].isSilent = None
            else:
                keyCode = 'Silence'
                _zones[zone].isSilent = True
    
        return getCommand(keyCode, zone)
    except:
        print('Abort translateKey: ', sys.exc_info()[0])
        traceback.print_exc()

#############################################
##                MAIN
#############################################

