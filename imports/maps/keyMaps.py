#############################################
##            MODULE VARIABLES
#############################################
print('Load key2hassio')
    
import os, sys, time, json, traceback

_zone = 'home'
_keyDuration = .1

_keyCode = {
    "a" 			: {"name": "alpha letter",       "hidCode":4,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "b" 			: {"name": "alpha letter",       "hidCode":5,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "c" 			: {"name": "alpha letter",       "hidCode":6,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "d" 			: {"name": "alpha letter",       "hidCode":7,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "e" 			: {"name": "alpha letter",       "hidCode":8,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "f" 			: {"name": "alpha letter",       "hidCode":9,   "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "g" 			: {"name": "alpha letter",       "hidCode":10,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "h" 			: {"name": "alpha letter",       "hidCode":11,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "i" 			: {"name": "alpha letter",       "hidCode":12,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "j" 			: {"name": "alpha letter",       "hidCode":13,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "k" 			: {"name": "alpha letter",       "hidCode":14,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "l" 			: {"name": "alpha letter",       "hidCode":15,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "m" 			: {"name": "alpha letter",       "hidCode":16,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "n" 			: {"name": "alpha letter",       "hidCode":17,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "o" 			: {"name": "alpha letter",       "hidCode":18,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "p" 			: {"name": "alpha letter",       "hidCode":19,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "q" 			: {"name": "alpha letter",       "hidCode":20,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "r" 			: {"name": "alpha letter",       "hidCode":21,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "s" 			: {"name": "alpha letter",       "hidCode":22,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "t" 			: {"name": "alpha letter",       "hidCode":23,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "u" 			: {"name": "alpha letter",       "hidCode":24,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "v" 			: {"name": "alpha letter",       "hidCode":25,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "w" 			: {"name": "alpha letter",       "hidCode":26,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "x" 			: {"name": "alpha letter",       "hidCode":27,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "y" 			: {"name": "alpha letter",       "hidCode":28,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "z" 			: {"name": "alpha letter",       "hidCode":29,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "1" 			: {"name": "alpha number",       "hidCode":30,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "2" 			: {"name": "alpha number",       "hidCode":31,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "3" 			: {"name": "alpha number",       "hidCode":32,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "4" 			: {"name": "alpha number",       "hidCode":33,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "5" 			: {"name": "alpha number",       "hidCode":34,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "6" 			: {"name": "alpha number",       "hidCode":35,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "7" 			: {"name": "alpha number",       "hidCode":36,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "8" 			: {"name": "alpha number",       "hidCode":37,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "9" 			: {"name": "alpha number",       "hidCode":38,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "0" 			: {"name": "alpha number",       "hidCode":39,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Ok" 			: {"name": "dpad select",        "hidCode":40,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Back" 			: {"name": "previos page",       "hidCode":41,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Home" 			: {"name": "home page",          "hidCode":41,  "keyMod": 4, "keyDuration": _keyDuration, "zone": _zone},
    "Focus" 		: {"name": "set context",        "hidCode":74,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Less" 			: {"name": "page backward",      "hidCode":75,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "More" 			: {"name": "page forward",       "hidCode":78,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Right" 		: {"name": "dpad right",         "hidCode":79,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Left" 			: {"name": "dpad left",          "hidCode":80,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Down" 			: {"name": "dpad down",          "hidCode":81,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Up" 			: {"name": "dpad up",            "hidCode":82,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Set" 			: {"name": "set options",        "hidCode":88,  "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Menu" 			: {"name": "options menu",       "hidCode":101, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "OnToggle" 		: {"name": "power toggle",       "hidCode":102, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "SoundToggle" 	: {"name": "volume mute",        "hidCode":127, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Louder" 		: {"name": "volume up",          "hidCode":128, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Softer" 		: {"name": "volume down",        "hidCode":129, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "PlayToggle" 	: {"name": "play/pause",         "hidCode":232, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Backward" 		: {"name": "skip back",          "hidCode":234, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
    "Forward" 		: {"name": "skip forward",       "hidCode":235, "keyMod": 0, "keyDuration": _keyDuration, "zone": _zone},
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
    