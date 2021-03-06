#############################################
##            MODULE VARIABLES
#############################################
print('Load usb2keyMap')
import importlib, json

scan2key = {
    1: "Exit",
    2: "1",
    3: "2",
    4: "3",
    5: "4",
    6: "5",
    7: "6",
    8: "7",
    9: "8",
    10: "9",
    11: "0",
    28: "Ok",
    59: "Silence/Sound",
    103: "Up",
    104: "Less",
    105: "Left",
    106: "Right",
    108: "Down",
    109: "More",
    113: "Silence/Sound",
    114: "Softer",
    115: "Louder",
    116: "Off/On",
    127: "Menu",
    158: "Exit",
    163: "Forward",
    164: "Stop/Start",
    165: "Backward",
    172: "Home",
    191: "Set",
    240: "Focus",
    272: "Ok",
    273: "Exit"
}

#############################################
def translateKey(input, reply):
#############################################
    print(f'translate keycode: {input}')

    key = {
        "context": "multiMedia",
        "code": scan2key.get(input['keyCode'], None),
        "zone": input['zone'],
        "device": "usb"
    }

    return json.dumps(key)

#############################################
##                MAIN
#############################################

