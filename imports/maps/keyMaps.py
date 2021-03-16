#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassio')
    
import os, sys, time, json, traceback

_zone = 'home'
_keyDuration = .35

_keyCode = {
    "a" 			: {"name": "alpha letter",       "keyNum":4,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "b" 			: {"name": "alpha letter",       "keyNum":5,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "c" 			: {"name": "alpha letter",       "keyNum":6,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "d" 			: {"name": "alpha letter",       "keyNum":7,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "e" 			: {"name": "alpha letter",       "keyNum":8,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "f" 			: {"name": "alpha letter",       "keyNum":9,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "g" 			: {"name": "alpha letter",       "keyNum":10,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "h" 			: {"name": "alpha letter",       "keyNum":11,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "i" 			: {"name": "alpha letter",       "keyNum":12,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "j" 			: {"name": "alpha letter",       "keyNum":13,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "k" 			: {"name": "alpha letter",       "keyNum":14,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "l" 			: {"name": "alpha letter",       "keyNum":15,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "m" 			: {"name": "alpha letter",       "keyNum":16,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "n" 			: {"name": "alpha letter",       "keyNum":17,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "o" 			: {"name": "alpha letter",       "keyNum":18,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "p" 			: {"name": "alpha letter",       "keyNum":19,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "q" 			: {"name": "alpha letter",       "keyNum":20,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "r" 			: {"name": "alpha letter",       "keyNum":21,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "s" 			: {"name": "alpha letter",       "keyNum":22,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "t" 			: {"name": "alpha letter",       "keyNum":23,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "u" 			: {"name": "alpha letter",       "keyNum":24,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "v" 			: {"name": "alpha letter",       "keyNum":25,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "w" 			: {"name": "alpha letter",       "keyNum":26,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "x" 			: {"name": "alpha letter",       "keyNum":27,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "y" 			: {"name": "alpha letter",       "keyNum":28,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "z" 			: {"name": "alpha letter",       "keyNum":29,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "1" 			: {"name": "alpha number",       "keyNum":30,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "2" 			: {"name": "alpha number",       "keyNum":31,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "3" 			: {"name": "alpha number",       "keyNum":32,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "4" 			: {"name": "alpha number",       "keyNum":33,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "5" 			: {"name": "alpha number",       "keyNum":34,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "6" 			: {"name": "alpha number",       "keyNum":35,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "7" 			: {"name": "alpha number",       "keyNum":36,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "8" 			: {"name": "alpha number",       "keyNum":37,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "9" 			: {"name": "alpha number",       "keyNum":38,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "0" 			: {"name": "alpha number",       "keyNum":39,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Ok" 			: {"name": "dpad select",        "keyNum":40,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Back" 			: {"name": "previos page",       "keyNum":41,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Home" 			: {"name": "home page",          "keyNum":41,  "keyMod": 4, "keyDuration": _keyDuration, "zone": _zone},
    "Focus" 		: {"name": "set context",        "keyNum":74,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Less" 			: {"name": "page backward",      "keyNum":75,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "More" 			: {"name": "page forward",       "keyNum":78,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Right" 		: {"name": "dpad right",         "keyNum":79,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Left" 			: {"name": "dpad left",          "keyNum":80,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Down" 			: {"name": "dpad down",          "keyNum":81,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Up" 			: {"name": "dpad up",            "keyNum":82,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Set" 			: {"name": "set options",        "keyNum":88,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Menu" 			: {"name": "options menu",       "keyNum":101, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "OnToggle" 		: {"name": "power toggle",       "keyNum":102, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "SoundToggle" 	: {"name": "volume mute",        "keyNum":127, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Louder" 		: {"name": "volume up",          "keyNum":128, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Softer" 		: {"name": "volume down",        "keyNum":129, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "PlayToggle" 	: {"name": "play/pause",         "keyNum":232, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Backward" 		: {"name": "skip back",          "keyNum":234, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Forward" 		: {"name": "skip forward",       "keyNum":235, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
}

_usbNum = {
    1: "Back",
    28: "Ok",
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
    