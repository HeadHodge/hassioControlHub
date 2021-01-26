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

		
////////////////////////////////////////////
//                MAIN
//             hubControl
////////////////////////////////////////////
console.log(`Started hubControl`);

