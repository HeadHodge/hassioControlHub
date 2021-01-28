exports.name = 'MasterBedroom Entertainment Tasks';
exports.zone = 'masterBedroom';
exports.focus = 'Up';

exports.tasks = {
	"Home": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "HOME"}}
	],
	
	"Menu": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "MENU"}}
	],
		
	"Exit": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "BACK"}}
	],
	
	"Up": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "UP"}}
	],
	
	"Down": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "DOWN"}}
	],
	
	"Left": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "LEFT"}}
	],
	
	"Right": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "RIGHT"}}
	],
	
	"Ok": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "CENTER"}}
	],
	
	"Louder": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Louder"}}
	],
	
	"Softer": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Softer"}}
	],
			
	"Sound": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Silence/Sound"}}
	],
			
	"Silence": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Silence/Sound"}}
	],
	
	"Backward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent --longpress 89"}}
	],
	
	"Start/Stop": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent 85"}}
	],
	
	"Forward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent --longpress 90"}}
	],
	
	"Open": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "POWER"}}
	],
	
	"On/Off": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "SLEEP"}},
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}
	]
};

////////////////////////////////////////////
//                MAIN
////////////////////////////////////////////
	console.log('masterBedroom.entertainment.js loaded');
