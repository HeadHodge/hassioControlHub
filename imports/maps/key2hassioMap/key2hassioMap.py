#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassioMap')
import importlib, json

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

    _zones[zone]['isTaskSet'] = None
    if(not _zones[zone][tasks['code']]): print(f'Abort: Invalid code: {code}'); return None
    return _zones[zone].tasks[code]
    
##########################################
def setFocus(zone, code):
##########################################
    #print(f'Enter onSelectFocus with {code} in zone {zone}')

    _zones[zone].isFocusSet = None
    
    if(code == 'Ok'):
        _zones[zone].isTaskSet = True
        return console.log('taskList selected for ${zone}')

    def Home()        : return _zones[zone].controllers['Home']
    def Louder()      : return _zones[zone].controllers['Louder']
    def Softer()      : return _zones[zone].controllers['Softer']
    def SoundToggle() : return _zones[zone].controllers['SoundToggle']
    def Backward()    : return _zones[zone].controllers['Backward']
    def PlayToggle()  : return _zones[zone].controllers['PlayToggle']
    def Forward()     : return _zones[zone].controllers['Forward']

    case = {
        'Home'       : Home,
        'Louder'     : Louder,
        'Softer'     : Softer,
        'SoundToggle': SoundToggle,
        'Backward'   : Backward,
        'PlayToggle' : PlayToggle,
        'Forward'    : Forward
    }
    
    _zones[zone].primaryModule = case.get(code, None)()
    print(f'primaryController selected: {_zones[zone].primaryModule}')

#############################################
def translateKey(key):
#############################################
    #print(f'translate keycode: {key}')
    global _zone
    
    _zones[key["zone"]] = importlib.import_module('zones.zone_' + key["zone"])

    #if(key["code"] == 'Echo'): reply('Echo'); return
        
    if(key["code"] == 'Set'): key["code"] = 'OffOn'
    
    if(_zones[key["zone"]].isFocusSet == True and key["code"] == 'OffOn'): 
        key["code"] = 'Open'
        _zones[key["zone"]].isFocusSet = None
        
    if(_zones[key["zone"]].isFocusSet): return setFocus(key["zone"], key["code"])
    if(_zones[key["zone"]].isTaskSet or key["code"] == 'Ping'): return getTask(key["zone"], key["code"], reply)

        
    if(key["code"] == 'Focus'): _zones[key["zone"]].isFocusSet = True; return print('Set Focus Flag')

    if(key["code"] == 'Silence/Sound'):
        if(_zones[key["zone"]].isSilent):
            key["code"] = 'Sound'
            _zones[key["zone"]].isSilent=null
        else:
            key["code"] = 'Silence'
            _zones[key["zone"]].isSilent=True
    
    return getCommand(key["zone"], key["code"])

#############################################
##                MAIN
#############################################

