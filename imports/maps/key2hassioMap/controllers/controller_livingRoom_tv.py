const debug = require('../../requires/debugLog.js').debug;
exports.name = 'MasterBedroom Entertainment Tasks';
exports.zone = 'masterBedroom';
exports.focus = 'Up';

exports.tasks = {
	"On/Off": [
		{"remote/send_command" : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}
	],
	
	"On": [
		{"remote/send_command": {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}
	],
	
	"Off": [
		{"remote/send_command" : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}
	],
	
	"Start/Stop": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "MENU"}}
	]
};

////////////////////////////////////////////
//                MAIN
////////////////////////////////////////////
	console.log('masterBedroom.tv.js loaded');
