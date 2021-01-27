//exports.zone = 'masterBedroom';
exports.focus = 'Up';
exports.popupController = {};
exports.primaryController = {};
exports.popupModule = null;
exports.primaryModule = "/scripts/modules/controllers/masterBedroom.entertainment.js";
exports.topics = {
	"Up"  : {
		"topic"      : 'Entertainment',
		"controller" : {
			"Up"      	: "/scripts/modules/controllers/masterBedroom.entertainment.js",
			"Softer"    : "/scripts/modules/controllers/masterBedroom.tv.js",
			"Louder"    : "/scripts/modules/controllers/masterBedroom.stereo.js",
			"Backward"	: "/scripts/modules/controllers/masterBedroom.fireplace.js"
		}
	},

	"Down"  : {
		"topic"      : 'Lights',
		"controller" : {
			"Down"         : null,
			"Louder"       : null,
			"Softer"       : null,
			"Silence/Sound": null,
			"Louder"       : null
		}
	},
	
	"Left"  : {
		"topic"      : 'Covers',
		"controller" : {
			"Left"         : null,
			"Louder"       : null,
			"Softer"       : null,
			"Silence/Sound": null,
			"Louder"       : null
		}
	},

	"Right"  : {
		"topic"      : 'Temperature',
		"controller" : {
			"Right"        : null,
			"Louder"       : null,
			"Softer"       : null,
			"Silence/Sound": null,
			"Louder"       : null
		}
	},
};

exports.tasks = {
	"Up": {
		//Wake Up	
		"Left"  : [
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.3}},
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
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
			{"sonos/join": {"entity_id": "media_player.bathroom", "master": "media_player.master_bedroom"}},
			{"media_player/volume_set": {"entity_id": "media_player.bathroom", "volume_level": 0.45}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.4}}
		],
	
		//Daytime	
		"Right"  : [
		],
	
		//Night	
		"Down"  : [
		]
	},
		
	"Left": {
	},
		
	"Right": {
	},
		
	"Down": {
	}
};
		
////////////////////////////////////////////
//                MAIN
//             hubControl
////////////////////////////////////////////
console.log(`Started hubControl`);

