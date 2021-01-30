//##############################################
//### Use javascript's XMLHttpRequest Object
//### To Trigger HomeAssistant Events
//### Via the RESTful Integration API
//##############################################

/////////////////////////// BEGIN PRIVATE NAMESPACE //////////////////////	
(function($case, $map){ //invoke anonymous self executing function

//################
//### start
//################
var start = function() {
	if(document.querySelector('Filter').getAttribute('recalled')) return; //Already Powered On
	$case.postCommand({"action": "runSequence", "reference": "media-broadcast-livingroom", "sequence": [{"remote/turn_on": {"entity_id": "remote.hub_3911_living_room", "activity": "Watch Antenna TV"}}]});
};
   
//################
//### keyMap
//################
var	keyMap = {
		"k": {"key": "upCannel", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "ChannelUp", 		"device": "LG TV"}}]},
		"l": {"key": "downChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "ChannelDown", 	"device": "LG TV"}}]},
		"m": {"key": "prevChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Last", 			"device": "LG TV"}}]},
		"A": {"key": "upVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeUp", 		"device": "JBL Amp"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeDown", 		"device": "JBL Amp"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Mute", 			"device": "JBL Amp"}}]},
		"1": {"key": "1", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "1", 				"device": "LG TV"}}]},
		"2": {"key": "2", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "2", 				"device": "LG TV"}}]},
		"3": {"key": "3", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "3", 				"device": "LG TV"}}]},
		"4": {"key": "4", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "4", 				"device": "LG TV"}}]},
		"5": {"key": "5", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "5", 				"device": "LG TV"}}]},
		"6": {"key": "6", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "6", 				"device": "LG TV"}}]},
		"7": {"key": "7", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "7", 				"device": "LG TV"}}]},
		"8": {"key": "8", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "8", 				"device": "LG TV"}}]},
		"9": {"key": "9", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "9", 				"device": "LG TV"}}]},
		"0": {"key": "0", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "0", 				"device": "LG TV"}}]},
		"-": {"key": "-", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "-", 				"device": "LG TV"}}]},
		"=": {"key": "=",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Enter", 			"device": "LG TV"}}]},
		"{": {"key": "Red",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", 	"device": "LG TV"}}]},
		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Input", 			"device": "LG TV"}}]},
		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", 	"device": "LG TV"}}]},
		":": {"key": "Blue", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "InputNext", 		"device": "Kinivo AV Switch"}}]},
		"`": {"key": "Power", 		"sequence": [{"remote/turn_off": {"entity_id": "remote.hub_3911_living_room"}}]}
	};

//################
//### MAIN
//################

	//Make Variables Public
	$map.keyMap = keyMap;
	$map.start = start;

/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
