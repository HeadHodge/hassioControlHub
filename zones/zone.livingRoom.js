const debug = require('/controlHub/core/debugLog.js').debug;

exports.focus = 'Up';
exports.popupController = {};
exports.primaryController = {};
exports.popupModule;
exports.primaryModule;

exports.controllers = {
	"Home" 			: "/controlHub/controllers/controller.livingRoom.entertainment.js",
	"Softer" 		: "/controlHub/controllers/controller.livingRoom.video.js",
	"Silence/Sound"	: "/controlHub/controllers/controller.livingRoom.sound.js",
	"Louder" 		: "/controlHub/controllers/controller.livingRoom.entertainment.js",
	"Backward"		: "/controlHub/controllers/controller.livingRoom.fireplace.js",
	"Stop/Start"	: "/controlHub/controllers/controller.livingRoom.covers.js",
	"Forward"		: "/controlHub/controllers/controller.livingRoom.entertainment.js"
};

exports.tasks = {
	"Up": {
		//Wake Up	
		"Left"  : [
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}, //Turn TV On
			{"cover/set_cover_position": {"entity_id": "cover.springs_window_fashions_graber_csz1_cellular_shade_level", "position": 45}}, //Partial Open Livingroom Shade
			{"cover/set_cover_position": {"entity_id": "cover.downstairs_slider", "position": 40}}, //Partial Open Dining Room Shade
			{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "90 Minutes"}}, //Turn Fireplace On
			{"media_player/select_source": {"entity_id": "media_player.firetv_livingroom", "source": "com.att.tv"}}
		],

		//Morning	
		"Up"  : [
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}, //Turn TV On
			{"cover/set_cover_position": {"entity_id": "cover.springs_window_fashions_graber_csz1_cellular_shade_level", "position": 45}}, //Partial Open Livingroom Shade
			{"cover/set_cover_position": {"entity_id": "cover.downstairs_slider", "position": 40}}, //Partial Open Dining Room Shade
			{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "90 Minutes"}}, //Turn Fireplace On
			{"media_player/select_source": {"entity_id": "media_player.firetv_livingroom", "source": "com.att.tv"}}
		],
	
		//Daytime	
		"Right"  : [
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
console.log(`Loaded zone.livingRoom.js`);

	exports.primaryModule = exports.controllers['Home'];