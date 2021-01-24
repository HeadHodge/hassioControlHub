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
	],
	
	"On": [
		{"remote/send_command": {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}},
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}}
	],
	
	"Off": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "SLEEP"}},
		{"remote/send_command" : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}
	]
};
