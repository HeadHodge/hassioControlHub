#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassioMap')
import importlib, json

_zones = {}

##########################################
def onCommand(zone, command, reply):
##########################################
    print(f'Enter onCommand, command: {command}, zone: {zone}')
    controller = None; task = None

    if(_zones[zone].popupModule):
        _zones[zone].popupController = importlib.import_module('controllers.' + _zones[zone].popupModule)
        _zones[zone].popupModule = None
        controller = _zones[zone].popupController
    else:
        _zones[zone].primaryController = importlib.import_module('controllers.' + _zones[zone].primaryModule)
        controller = _zones[zone].primaryController
    
    if(not controller.tasks[command]): return print(f'Abort: Invalid command: {command}')
    
    print(f'output task: {json.dumps(controller.tasks[command])}')
    return json.dumps(controller.tasks[command])
    
##########################################
def onSelectTask(zone, command, reply):
##########################################
    print(f'Enter onSelectTask with {command} in zone: {zone}')
    task = None

    _zones[zone]['isTaskSet'] = None
    if(not _zones[zone][tasks['command']]): print(f'Abort: Invalid command: {command}'); return
    return JSON.stringify(_zones[zone].tasks[command])
    
##########################################
def onSelectFocus(zone, command):
##########################################
    print(f'Enter onSelectFocus with {command} in zone {zone}')

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
    
    _zones[zone]['primaryModule'] = case.get(command, lambda: None)()
    print('defaultController selected: ${_zones[zone].primaryModule}')

#############################################
def translateKey(key, reply):
#############################################
    print(f'translate keycode: {key}')
    global _zone
    
    _zones[key["zone"]] = importlib.import_module('zones.zone_' + key["zone"])
    print(_zones[key["zone"]])

    if(key["command"] == 'Echo'): reply('Echo'); return
        
    if(key["command"] == 'Set'): key["command"] = 'Off/On'
    
    if(_zones[key["zone"]].isFocusSet == True and key["command"] == 'Off/On'): 
        key["command"] = 'Open'
        _zones[key["zone"]].isFocusSet = None
        
    if(_zones[key["zone"]].isFocusSet): return onSelectFocus(key["zone"], key["command"])
    if(_zones[key["zone"]].isTaskSet or key["command"] == 'Ping'): return onSelectTask(key["zone"], key["command"], reply)

        
    if(key["command"] == 'Focus'): _zones[key["zone"]].isFocusSet = true; return console.log('Set Focus Flag')

    if(key["command"] == 'Silence/Sound'):
        if(_zones[key["zone"]].isSilent):
            key["command"] = 'Sound'
            _zones[key["zone"]].isSilent=null
        else:
            key["command"] = 'Silence'
            _zones[key["zone"]].isSilent=true
    
    return onCommand(key["zone"], key["command"], reply)

#############################################
##                MAIN
#############################################

