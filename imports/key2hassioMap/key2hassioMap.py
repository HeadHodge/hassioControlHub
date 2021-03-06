#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassioMap')
import importlib

_zones = {}

#############################################
def translateKey(key, reply):
#############################################
    print(f'translate keycode: {key}')
    global _zone
    
    _zones[key["zone"]] = importlib.import_module('zones.zone_' + key["zone"])

    if(key["command"] == 'Echo'): reply('Echo'); return
        
    if(key["command"] == 'Set'): key["command"] = 'Off/On'
    
    if(_zones[key["zone"]].isFocusSet and key["command"] == 'Off/On'): key["command"] = 'Open'; _zones[key["zone"]].isFocusSet = null
        
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
    
    onCommand(key["zone"], key["command"], reply)

#############################################
##                MAIN
#############################################

