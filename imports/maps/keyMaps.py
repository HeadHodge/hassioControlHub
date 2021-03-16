#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassio')
    
import os, sys, time, json, traceback

_zone = 'home'
_keyDuration = .1

_keyCode = {
    "a" 			: {"name": "alpha letter",       "hidCode":4,   "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "b" 			: {"name": "alpha letter",       "hidCode":5,   "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "c" 			: {"name": "alpha letter",       "hidCode":6,   "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "d" 			: {"name": "alpha letter",       "hidCode":7,   "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "e" 			: {"name": "alpha letter",       "hidCode":8,   "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "f" 			: {"name": "alpha letter",       "hidCode":9,   "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "g" 			: {"name": "alpha letter",       "hidCode":10,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "h" 			: {"name": "alpha letter",       "hidCode":11,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "i" 			: {"name": "alpha letter",       "hidCode":12,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "j" 			: {"name": "alpha letter",       "hidCode":13,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "k" 			: {"name": "alpha letter",       "hidCode":14,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "l" 			: {"name": "alpha letter",       "hidCode":15,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "m" 			: {"name": "alpha letter",       "hidCode":16,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "n" 			: {"name": "alpha letter",       "hidCode":17,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "o" 			: {"name": "alpha letter",       "hidCode":18,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "p" 			: {"name": "alpha letter",       "hidCode":19,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "q" 			: {"name": "alpha letter",       "hidCode":20,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "r" 			: {"name": "alpha letter",       "hidCode":21,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "s" 			: {"name": "alpha letter",       "hidCode":22,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "t" 			: {"name": "alpha letter",       "hidCode":23,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "u" 			: {"name": "alpha letter",       "hidCode":24,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "v" 			: {"name": "alpha letter",       "hidCode":25,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "w" 			: {"name": "alpha letter",       "hidCode":26,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "x" 			: {"name": "alpha letter",       "hidCode":27,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "y" 			: {"name": "alpha letter",       "hidCode":28,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "z" 			: {"name": "alpha letter",       "hidCode":29,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "1" 			: {"name": "alpha number",       "hidCode":30,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "2" 			: {"name": "alpha number",       "hidCode":31,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "3" 			: {"name": "alpha number",       "hidCode":32,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "4" 			: {"name": "alpha number",       "hidCode":33,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "5" 			: {"name": "alpha number",       "hidCode":34,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "6" 			: {"name": "alpha number",       "hidCode":35,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "7" 			: {"name": "alpha number",       "hidCode":36,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "8" 			: {"name": "alpha number",       "hidCode":37,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "9" 			: {"name": "alpha number",       "hidCode":38,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "0" 			: {"name": "alpha number",       "hidCode":39,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Ok" 			: {"name": "dpad select",        "hidCode":40,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Back" 			: {"name": "previos page",       "hidCode":41,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Home" 			: {"name": "home page",          "hidCode":41,  "hidMod": 4, "keyDuration": _keyDuration, "zone": _zone},
    "Space" 		: {"name": "alpa space",         "hidCode":44,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Focus" 		: {"name": "set context",        "hidCode":74,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Less" 			: {"name": "page backward",      "hidCode":75,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "More" 			: {"name": "page forward",       "hidCode":78,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Right" 		: {"name": "dpad right",         "hidCode":79,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Left" 			: {"name": "dpad left",          "hidCode":80,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Down" 			: {"name": "dpad down",          "hidCode":81,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Up" 			: {"name": "dpad up",            "hidCode":82,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Set" 			: {"name": "set options",        "hidCode":88,  "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Menu" 			: {"name": "options menu",       "hidCode":101, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "OnToggle" 		: {"name": "power toggle",       "hidCode":102, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "SoundToggle" 	: {"name": "volume mute",        "hidCode":127, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Louder" 		: {"name": "volume up",          "hidCode":128, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Softer" 		: {"name": "volume down",        "hidCode":129, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "PlayToggle" 	: {"name": "play/pause",         "hidCode":232, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Backward" 		: {"name": "skip back",          "hidCode":234, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Forward" 		: {"name": "skip forward",       "hidCode":235, "hidMod": 0, "keyDuration": _keyDuration, "zone": _zone},
}

_usbNum = {
    1: "Back",
    28: "Ok",
    57: "Space",
    59: "SoundToggle",
    103: "Up",
    104: "Less",
    105: "Left",
    106: "Right",
    108: "Down",
    109: "More",
    113: "SoundToggle",
    114: "Softer",
    115: "Louder",
    116: "PowerToggle",
    127: "Menu",
    158: "Exit",
    163: "Forward",
    164: "PlayToggle",
    165: "Backward",
    172: "Home",
    191: "Set",
    240: "Focus",
    272: "Ok",
    273: "Back",
}

_keyMod = {
    "1":   {"name": "leftShift"},
    "2":   {"name": "leftCtrl"},
    "4":   {"name": "leftAlt"},
    "8":   {"name": "leftCmd"},
    "16":  {"name": "rightShift"},
    "32":  {"name": "rightCtrl"},
    "64":  {"name": "rightAlt"},
    "128": {"name": "rightCmd"},
}

#############################################
def keyNum2key(keyCode, zone='home'):
#############################################
    #print(f'getKey, keyCode:{keyCode}, duration:{duration}, zone:{zone}')
    key = _keyCode.get(keyCode, None)
    if(key == None): return None
    
    key['keyCode'] = keyCode
    key['zone'] = zone
    return key

#############################################
def usbNum2keyCode(usbNum):
#############################################
    #print(f'getKeyCode, usbNum:{usbNum}')
    return _usbNum.get(usbNum, None)
    
#############################################
##               MAIN
#############################################
    