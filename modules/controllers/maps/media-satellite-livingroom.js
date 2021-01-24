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
	$case.postCommand({"action": "runSequence", "reference": "media-directv-livingroom", "sequence": [{"remote/turn_on": {"entity_id": "remote.hub_3911_living_room", "activity": "Watch DirecTV"}}]});
};
   
//################
//### keyMap
//################
var	keyMap = {
		"a": {"key": "upArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionUp", 	"device": "DirecTV Mini-Genie Client"}}]},
		"b": {"key": "rightArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionRight",	"device": "DirecTV Mini-Genie Client"}}]},
		"c": {"key": "downArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionDown", 	"device": "DirecTV Mini-Genie Client"}}]},
		"d": {"key": "leftArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionLeft", 	"device": "DirecTV Mini-Genie Client"}}]},
		"e": {"key": "OK", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Select", 			"device": "DirecTV Mini-Genie Client"}}]},
		"f": {"key": "List", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "List", 			"device": "DirecTV Mini-Genie Client"}}]},
		"g": {"key": "Menu", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Menu", 			"device": "DirecTV Mini-Genie Client"}}]},
		"h": {"key": "Guide", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Guide", 			"device": "DirecTV Mini-Genie Client"}}]},
		"i": {"key": "Exit", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Exit", 			"device": "DirecTV Mini-Genie Client"}}]},
		"j": {"key": "Info", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Info", 			"device": "DirecTV Mini-Genie Client"}}]},
		"k": {"key": "upCannel", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "ChannelUp", 		"device": "DirecTV Mini-Genie Client"}}]},
		"l": {"key": "downChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "ChannelDown", 	"device": "DirecTV Mini-Genie Client"}}]},
		"m": {"key": "prevChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "ChannelPrev", 	"device": "DirecTV Mini-Genie Client"}}]},
		"A": {"key": "upVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeUp", 		"device": "JBL Amp"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeDown", 		"device": "JBL Amp"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Mute", 			"device": "JBL Amp"}}]},
		"D": {"key": "Play", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Play", 			"device": "DirecTV Mini-Genie Client"}}]},
		"E": {"key": "Pause", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Pause", 			"device": "DirecTV Mini-Genie Client"}}]},
	 	"F": {"key": "Record", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Record", 			"device": "DirecTV Mini-Genie Client"}}]},
	 	"G": {"key": "Stop", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "RedCircle", 		"device": "DirecTV Mini-Genie Client"}}]},
	 	"H": {"key": "Forward", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "FastForward", 	"device": "DirecTV Mini-Genie Client"}}]},
	 	"I": {"key": "Back", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Rewind", 			"device": "DirecTV Mini-Genie Client"}}]},
		"1": {"key": "1", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "1", 				"device": "DirecTV Mini-Genie Client"}}]},
		"2": {"key": "2", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "2", 				"device": "DirecTV Mini-Genie Client"}}]},
		"3": {"key": "3", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "3", 				"device": "DirecTV Mini-Genie Client"}}]},
		"4": {"key": "4", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "4", 				"device": "DirecTV Mini-Genie Client"}}]},
		"5": {"key": "5", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "5", 				"device": "DirecTV Mini-Genie Client"}}]},
		"6": {"key": "6", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "6", 				"device": "DirecTV Mini-Genie Client"}}]},
		"7": {"key": "7", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "7", 				"device": "DirecTV Mini-Genie Client"}}]},
		"8": {"key": "8", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "8", 				"device": "DirecTV Mini-Genie Client"}}]},
		"9": {"key": "9", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "9", 				"device": "DirecTV Mini-Genie Client"}}]},
		"0": {"key": "0", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "0", 				"device": "DirecTV Mini-Genie Client"}}]},
		"-": {"key": "-", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "-", 				"device": "DirecTV Mini-Genie Client"}}]},
		"=": {"key": "=",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Enter", 			"device": "DirecTV Mini-Genie Client"}}]},
		"[": {"key": "Input",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "SelectRemote", 	"device": "Manager"}}]},
		"]": {"key": "Eject", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "RedCircle", 		"device": "DirecTV Mini-Genie Client"}}]},
		"{": {"key": "Red",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", 	"device": "LG TV"}}]},
		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Input", 			"device": "LG TV"}}]},
		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", 	"device": "JBL Amp"}}]},
		":": {"key": "Blue", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "InputNext", 		"device": "Kinivo AV Switch"}}]},
		"`": {"key": "Power", 		"sequence": [{"remote/turn_off": 	 {"entity_id": "remote.hub_3911_living_room"}}]}
	};

//################
//### MAIN
//################

	//Make Variables Public
	$map.keyMap = keyMap;
	$map.start = start;

/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
