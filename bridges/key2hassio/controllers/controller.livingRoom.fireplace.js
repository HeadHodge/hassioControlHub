const debug = require('../../../requires/debugLog.js').debug;

exports.name = 'MasterBedroom Entertainment Tasks';
exports.zone = 'masterBedroom';
exports.focus = 'Up';

exports.tasks = {
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
		{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "OFF"}} //Turn off Fireplace
	]
};

////////////////////////////////////////////
//                MAIN
////////////////////////////////////////////
console.log('Loaded controller.livingRoom.fireplace.js');
