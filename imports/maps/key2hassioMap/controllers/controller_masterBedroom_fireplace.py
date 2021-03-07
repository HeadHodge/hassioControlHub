#############################################
##            GLOBAL VARIABLES
#############################################
print('Load controller_masterBedroom_fireplace');
name = 'MasterBedroom Firepllace Tasks';
zone = 'masterBedroom';

tasks = {
	"Left": [
		{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "30 Minutes"}}
	],
	
	"Up": [
		{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "60 Minutes"}}
	],
	
	"Right": [
		{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "90 Minutes"}}
	],
	
	"Down": [
		{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "120 Minutes"}}
	],
	
	"Ok": [
		{"switch/turn_off": {"entity_id": "switch.31485653bcddc23a2807"}}
	]
};

#############################################
##                MAIN
#############################################
