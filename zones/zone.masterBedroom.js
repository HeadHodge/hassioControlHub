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

exports.tasks = {
		//Keep FireTV awake	
		"Ping"  : [
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}}
		],
		
		//Wake Up	
		"Left"  : [
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.25}},
			{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "90 Minutes"}},
			{"sleep": 10},
			{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 5},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}}
		],
	
		//Morning	
		"Up"  : [
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}},
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
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}},
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
			{"sleep": 5},
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}},

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
			{"sleep": 10},
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 2},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},

			{"sleep": 30},
			{"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}}
 		]
};

////////////////////////////////////////////
//                MAIN
//             hubControl
////////////////////////////////////////////
console.log(`Loaded zone.masterBedroom.js`);

	exports.primaryModule = exports.controllers['Home'];