#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassioMap')
import os, sys, importlib, json, traceback

_zones = {}

##########################################
def getCommand(zone, code):
##########################################
    #print(f'Enter getCommand, code: {code}, zone: {zone}')
    controller = None; task = None

    _zones[zone].primaryController = importlib.import_module('controllers.' + _zones[zone].primaryModule)
    controller = _zones[zone].primaryController
    
    #print(f'output task: {json.dumps(controller.tasks[code])}')
    return controller.tasks.get(code, None)
    
##########################################
def getTask(zone, code):
##########################################
    #print(f'Enter onSelectTask with {code} in zone: {zone}')
    task = None

    _zones[zone].isTaskSet = None
    return _zones[zone].tasks.get(code, None)
    
##########################################
def setFocus(zone, code):
##########################################
    #print(f'Enter onSelectFocus with {code} in zone {zone}')

    _zones[zone].isFocusSet = None
    
    if(code == 'Menu'):
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
    
    selection = case.get(code, None)
    if(selection == None): return
    _zones[zone].primaryModule = selection()
    print(f'new controller selected: {_zones[zone].primaryModule}')

#############################################
def translateKey(key):
#############################################
    try:
        #print(f'translate keycode: {key}')
        global _zone
    
        _zones[key["zone"]] = importlib.import_module('zones.zone_' + key["zone"])
        
        if(key["code"] == 'Set'): key["code"] = 'OnToggle'
    
        if(_zones[key["zone"]].isFocusSet == True and key["code"] == 'OnToggle'): 
            key["code"] = 'Open'
            _zones[key["zone"]].isFocusSet = None
        
        if(_zones[key["zone"]].isFocusSet): return setFocus(key["zone"], key["code"])
        if(_zones[key["zone"]].isTaskSet): return getTask(key["zone"], key["code"])
      
        if(key["code"] == 'Focus'): _zones[key["zone"]].isFocusSet = True; return print('Set Focus Flag')

        if(key["code"] == 'Silence/Sound'):
            if(_zones[key["zone"]].isSilent):
                key["code"] = 'Sound'
                _zones[key["zone"]].isSilent=null
            else:
                key["code"] = 'Silence'
                _zones[key["zone"]].isSilent=True
    
        return getCommand(key["zone"], key["code"])
    except:
        print('Abort translateKey: ', sys.exc_info()[0])
        traceback.print_exc()

#############################################
##                MAIN
#############################################

