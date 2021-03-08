const debug = require('../../../requires/debugLog.js').debug;
const eventNum = 4;

const adbEvents = {
	"Home"		: `sendevent /dev/input/event${eventNum} 4 4 786979 && sendevent /dev/input/event${eventNum} 1 172 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 786979 && sendevent /dev/input/event${eventNum} 1 172 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Menu"		: `sendevent /dev/input/event${eventNum} 4 4 786496 && sendevent /dev/input/event${eventNum} 1 139 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 786496 && sendevent /dev/input/event${eventNum} 1 139 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Exit"		: `sendevent /dev/input/event${eventNum} 4 4 458993 && sendevent /dev/input/event${eventNum} 1 158 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 458993 && sendevent /dev/input/event${eventNum} 1 158 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Up"		: `sendevent /dev/input/event${eventNum} 4 4 458834 && sendevent /dev/input/event${eventNum} 1 103 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 458834 && sendevent /dev/input/event${eventNum} 1 103 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Down"		: `sendevent /dev/input/event${eventNum} 4 4 458833 && sendevent /dev/input/event${eventNum} 1 108 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 458833 && sendevent /dev/input/event${eventNum} 1 108 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Left"		: `sendevent /dev/input/event${eventNum} 4 4 458832 && sendevent /dev/input/event${eventNum} 1 105 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 458832 && sendevent /dev/input/event${eventNum} 1 105 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Right"		: `sendevent /dev/input/event${eventNum} 4 4 458831 && sendevent /dev/input/event${eventNum} 1 106 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 458831 && sendevent /dev/input/event${eventNum} 1 106 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Ok"		: `sendevent /dev/input/event${eventNum} 4 4 458840 && sendevent /dev/input/event${eventNum} 1 96 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 458840 && sendevent /dev/input/event${eventNum} 1 96 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Stop/Start": `sendevent /dev/input/event${eventNum} 4 4 786637 && sendevent /dev/input/event${eventNum} 1 164 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 786637 && sendevent /dev/input/event${eventNum} 1 164 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Backward"	: `sendevent /dev/input/event${eventNum} 4 4 786612 && sendevent /dev/input/event${eventNum} 1 168 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 786612 && sendevent /dev/input/event${eventNum} 1 168 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Forward"	: `sendevent /dev/input/event${eventNum} 4 4 786611 && sendevent /dev/input/event${eventNum} 1 208 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 786611 && sendevent /dev/input/event${eventNum} 1 208 0 && sendevent /dev/input/event${eventNum} 0 0 0`,
	"Off/On"	: `sendevent /dev/input/event${eventNum} 4 4 458854 && sendevent /dev/input/event${eventNum} 1 116 1 && sendevent /dev/input/event${eventNum} 0 0 0 && sendevent /dev/input/event${eventNum} 4 4 458854 && sendevent /dev/input/event${eventNum} 1 116 0 && sendevent /dev/input/event${eventNum} 0 0 0`
};

exports.name = 'MasterBedroom Entertainment Tasks';
exports.zone = 'masterBedroom';
exports.focus = 'Up';
exports.tasks = {
	"Home": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Home"]}}
	],
	
	"Menu": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "MENU"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Menu"]}}
	],
		
	"Exit": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "BACK"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Exit"]}}
	],
	
	"Up": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "UP"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Up"]}}
	],
	
	"Down": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "DOWN"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Down"]}}
	],
	
	"Left": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "LEFT"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Left"]}}
	],
	
	"Right": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "RIGHT"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Right"]}}
	],
	
	"Ok": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "CENTER"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Ok"]}}
	],
	
	"Louder": [
		{"media_player/volume_up"  : {"entity_id": "media_player.master_bedroom"}},
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}
	],
	
	"Softer": [
		{"media_player/volume_down": {"entity_id": "media_player.master_bedroom"}},
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}
	],
			
	"Sound": [
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}
	],
			
	"Silence": [
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": true}}
	],
	
	"Backward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 89"}}
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Backward"]}}
	],
	
	"Stop/Start": [
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent 85"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Stop/Start"]}}
	],
	
	"Forward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 90"}}
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Forward"]}}
	],
	
	"Open": [
		//Turn on TV
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "WAKEUP"}},
	    //{"sleep": 3},
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 3"}},
		//{"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}},

		//Turn on Sound
		{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
		{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
		{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
		{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.45}}
	],
		
	"Off/On": [
		//Turn off TV
		//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}},
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Home"]}},
	    {"sleep": 3},
		{"remote/send_command" : {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
	    //{"sleep": 2},

		//Turn on Sleep Timer with Music
		{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
		{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
		{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.18}},
		{"sonos/set_sleep_timer": {"entity_id": "media_player.master_bedroom", "sleep_time": 3600}}
	]
};

////////////////////////////////////////////
//                MAIN
////////////////////////////////////////////
console.log('Loaded controller.masterBedroom.entertainment.js');
