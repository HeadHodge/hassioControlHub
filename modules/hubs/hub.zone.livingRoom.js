exports.focus = 'Up';
exports.popupController = {};
exports.primaryController = {};
exports.popupModule = null;
exports.primaryModule = "/controlHub/modules/controllers/livingRoom.entertainment.js";
exports.topics = {
	"Up"  : {
		"topic"      : 'Entertainment',
		"controller" : {
			"Up"      	: "/controlHub/modules/controllers/livingRoom.entertainment.js",
			"Softer"    : "/controlHub/modules/controllers/livingRoom.tv.js",
			"Louder"    : "/controlHub/modules/controllers/livingRoom.stereo.js",
			"Backward"	: "/controlHub/modules/controllers/livingRoom.fireplace.js"
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
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}, //Turn TV On
			{"cover/set_cover_position": {"entity_id": "cover.springs_window_fashions_graber_csz1_cellular_shade_level", "position": 55}}, //Partial Open Livingroom Shade
			{"cover/set_cover_position": {"entity_id": "cover.downstairs_slider", "position": 30}}, //Partial Open Dining Room Shade
			{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "90 Minutes"}} //Turn Fireplace On
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
			{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "SLEEP"}},
			{"remote/send_command" : {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
			{"sleep": 5},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.3}}
		],
	
		//Night	
		"Down"  : [
		]
	}
};
		
////////////////////////////////////////////
//                MAIN
//             hubControl
////////////////////////////////////////////
console.log(`Started hubControl`);

