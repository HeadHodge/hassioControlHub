#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassioMap')
import importlib, json

_zones = {}

##########################################
def onCommand(zone, command):
##########################################
    #print(f'Enter onCommand, command: {command}, zone: {zone}')
    controller = None; task = None

    if(_zones[zone].popupModule):
        _zones[zone].popupController = importlib.import_module('controllers.' + _zones[zone].popupModule)
        _zones[zone].popupModule = None
        controller = _zones[zone].popupController
    else:
        _zones[zone].primaryController = importlib.import_module('controllers.' + _zones[zone].primaryModule)
        controller = _zones[zone].primaryController
    
    if(not controller.tasks[command]): return print(f'Abort: Invalid command: {command}')
    
    #print(f'output task: {json.dumps(controller.tasks[command])}')
    return json.dumps(controller.tasks[command])
    
##########################################
def onSelectTask(zone, command):
##########################################
    #print(f'Enter onSelectTask with {command} in zone: {zone}')
    task = None

    _zones[zone]['isTaskSet'] = None
    if(not _zones[zone][tasks['command']]): print(f'Abort: Invalid command: {command}'); return
    return JSON.stringify(_zones[zone].tasks[command])
    
##########################################
def onSelectFocus(zone, command):
##########################################
    #print(f'Enter onSelectFocus with {command} in zone {zone}')

    _zones[zone]['isFocusSet'] = None
    
    if(command == 'Ok'):
        _zones[zone].isTaskSet = True
        return console.log('taskList selected for ${zone}')

    def Home()        : return _zones[zone][controllers['Home']]
    def Louder()      : return _zones[zone][controllers['Louder']]
    def Softer()      : return _zones[zone][controllers['Softer']]
    def SilenceSound(): return _zones[zone][controllers['Silence/Sound']]
    def Backward()    : return _zones[zone][controllers['Backward']]
    def StopStart()   : return _zones[zone][controllers['Stop/Start']]
    def Forward()     : return _zones[zone][controllers['Forward']]

    case = {
        'Home': Home,
        'Louder': Louder,
        'Softer': Softer,
        'Silence/Sound': SilenceSound,
        'Backward': Backward,
        'Stop/Start': StopStart,
        'Forward': Forward,
    }
    
    _zones[zone]['primaryModule'] = case.get(command, None)()
    print('defaultController selected: ${_zones[zone].primaryModule}')

#############################################
def translateKey(key):
#############################################
    #print(f'translate keycode: {key}')
    global _zone
    
    _zones[key["zone"]] = importlib.import_module('zones.zone_' + key["zone"])

    #if(key["code"] == 'Echo'): reply('Echo'); return
        
    if(key["code"] == 'Set'): key["code"] = 'Off/On'
    
    if(_zones[key["zone"]].isFocusSet == True and key["code"] == 'Off/On'): 
        key["code"] = 'Open'
        _zones[key["zone"]].isFocusSet = None
        
    if(_zones[key["zone"]].isFocusSet): return onSelectFocus(key["zone"], key["code"])
    if(_zones[key["zone"]].isTaskSet or key["code"] == 'Ping'): return onSelectTask(key["zone"], key["code"], reply)

        
    if(key["code"] == 'Focus'): _zones[key["zone"]].isFocusSet = True; return console.log('Set Focus Flag')

    if(key["code"] == 'Silence/Sound'):
        if(_zones[key["zone"]].isSilent):
            key["code"] = 'Sound'
            _zones[key["zone"]].isSilent=null
        else:
            key["code"] = 'Silence'
            _zones[key["zone"]].isSilent=True
    
    return onCommand(key["zone"], key["code"])

#############################################
##                MAIN
#############################################

