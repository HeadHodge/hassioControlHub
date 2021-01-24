exports.name = 'MasterBedroom Entertainment Tasks';
exports.zone = 'masterBedroom';
exports.focus = 'Up';

exports.tasks = {
	"Home": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}}
	],
	
	"Menu": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "MENU"}}
	],
		
	"Exit": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "BACK"}}
	],
	
	"Up": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "UP"}}
	],
	
	"Down": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "DOWN"}}
	],
	
	"Left": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "LEFT"}}
	],
	
	"Right": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "RIGHT"}}
	],
	
	"Ok": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "CENTER"}}
	],
	
	"Louder": [
		{"media_player/volume_up"  : {"entity_id": "media_player.master_bedroom"}},
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}
	],
	
	"Softer": [
		{"media_player/volume_down": {"entity_id": "media_player.master_bedroom"}},
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}
	],
			
	"Mute": [
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": true}}
	],
	
	"Backward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 89"}}
	],
	
	"Play/Pause": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent 85"}}
	],
	
	"Forward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 90"}}
	]
};

/*
		"g": {"key": "Menu", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "MENU"}}]},
		"D": {"key": "Play/Pause", "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent 85"}}]},
	 	"H": {"key": "Forward",    "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 90"}}]},
	 	"I": {"key": "Back",       "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 89"}}]},
		"f": {"key": "List", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}}]},
		"{": {"key": "Red",	   "sequence": [{"remote/send_command"	   : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}]},
		"}": {"key": "Green",	   "sequence": [{"remote/send_command"     : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "Input"}}]},
//		"|": {"key": "Yellow", 	   "sequence": [{"remote/send_command"     : {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", "device": "Vizio TV"}}]},
//		":": {"key": "Blue", 	   "sequence": [{"remote/send_command"     : {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", "device": "Vizio TV"}}]},
		"`": {"key": "Off", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "SLEEP"}}, {"remote/send_command" : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}]}
*/