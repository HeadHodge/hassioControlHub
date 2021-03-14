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
    273: "Exit"
}

seqNum = 3

#############################################
def translate(input):
#############################################
    #print(f'translate keycode: {input}')
    global seqNum
    
    if(input['scanCode'] == 1):   code = 1 #back
    if(input['scanCode'] == 105): seqNum -= 1;  code = seqNum  #left
    if(input['scanCode'] == 106): seqNum += 1;  code = seqNum  #right
    if(input['scanCode'] == 28):  code = seqNum  #ok
        
    print(f'code: {code}')
    key =  [ 0xA1, 1, 12, 0, code, 0, 0, 0, 0, 0 ]

    return key

#############################################
##                MAIN
#############################################
