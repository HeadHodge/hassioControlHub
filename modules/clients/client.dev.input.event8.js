exports.zone = 'masterBedroom';
exports.focus = 'Up';
exports.controller = '/scripts/modules/controllers/masterBedroom.entertainment.js';
exports.controllers = {
	"Up"  : {
		"topic"      : 'Entertainment',
		"controller" : {
			"Default"      : "/scripts/modules/controllers/masterBedroom.entertainment.js",
			"Louder"       : null,
			"Softer"       : null,
			"Silence/Sound": null,
			"Louder"       : null
		}
	},

	"Down"  : {
		"topic"      : 'Lights',
		"controller" : {
			"Default"      : null,
			"Louder"       : null,
			"Softer"       : null,
			"Silence/Sound": null,
			"Louder"       : null
		}
	},
	
	"Left"  : {
		"topic"      : 'Covers',
		"controller" : {
			"Default"      : null,
			"Louder"       : null,
			"Softer"       : null,
			"Silence/Sound": null,
			"Louder"       : null
		}
	},

	"Right"  : {
		"topic"      : 'Temperature',
		"controller" : {
			"Default"      : null,
			"Louder"       : null,
			"Softer"       : null,
			"Silence/Sound": null,
			"Louder"       : null
		}
	},
};


