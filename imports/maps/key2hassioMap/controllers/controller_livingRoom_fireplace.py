#############################################
##            MODULE VARIABLES
#############################################
print('Load controller_livingRoom_fireplace')

name = 'Fireplace Tasks';
zone = 'livingRoom';

tasks = {
	"Left": [
		{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "30 Minutes"}}
	],
	
	"Up": [
		{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "60 Minutes"}}
	],
	
	"Right": [
		{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "90 Minutes"}}
	],
	
	"Down": [
		{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "120 Minutes"}}
	],
	
	"Ok": [
		{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "OFF"}}
	]
};

#######################################
#                MAIN
#######################################
