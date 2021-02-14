const debug = require('/inputHub/core/debugLog.js').debug;

exports.focus = 'Up';
exports.popupController = {};
exports.primaryController = {};
exports.popupModule;
exports.primaryModule;

exports.controllers = {
	"Home" 			: "/inputHub/controllers/controller.masterBedroom.entertainment.js",
	"Softer" 		: "/inputHub/controllers/controller.masterBedroom.video.js",
	"Silence/Sound"	: "/inputHub/controllers/controller.masterBedroom.sound.js",
	"Louder" 		: "/inputHub/controllers/controller.masterBedroom.entertainment.js",
	"Backward"		: "/inputHub/controllers/controller.masterBedroom.fireplace.js",
	"Stop/Start"	: "/inputHub/controllers/controller.masterBedroom.covers.js",
	"Forward"		: "/inputHub/controllers/controller.masterBedroom.entertainment.js"
};

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

exports.tasks = {
		//Keep FireTV awake	
		"Ping"  : [
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "PING"}}
		],
		
		//Wake Up	
		"Left"  : [
			//Turn Music On
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.25}},

			//Turn Fireplace On
			{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "90 Minutes"}},

			//Open Shade
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 15},

			{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 5},

			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}}
		],
	
		//Morning	
		"Up"  : [
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
			//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "WAKEUP"}},
			{"sleep": 3},
			{"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}},
	
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"sonos/join": {"entity_id": "media_player.bathroom", "master": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
			{"media_player/volume_set": {"entity_id": "media_player.bathroom", "volume_level": 0.45}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.3}},

			{"sleep": 30},
			{"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}}
		],
	
		//Daytime	
		"Right"  : [
			//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}},
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Home"]}},
			{"remote/send_command" : {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
			{"sleep": 3},

			{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.25}}
		],
	
		//Night	
		"Down"  : [
			//Turn TV On
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
			{"sleep": 3},
			{"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}},
			//{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "WAKEUP"}},

			//Turn Sound On
			{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.45}},

			//Turn Fireplace On
			{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "90 Minutes"}},

			//Close Shades
			{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 15},
			
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 2},
			
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
 		]
};

////////////////////////////////////////////
//                MAIN
//             hubControl
////////////////////////////////////////////
console.log(`Loaded zone.masterBedroom.js`);

	exports.primaryModule = exports.controllers['Home'];