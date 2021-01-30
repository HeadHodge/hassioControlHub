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
	$case.postCommand({"action": "runSequence", "reference": "media-satellite-masterbedroom", "sequence": [
		{"remote/turn_on": {"entity_id": "remote.hub_3911_master_bedroom", "activity": "Watch DirecTV"}}
	]});
};

//################
//### keyMap
//################
var	keyMap = {
		"a": {"key": "upArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionUp", 		"device": "DirecTV Genie"}}]},
		"b": {"key": "rightArrow",	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionRight",	"device": "DirecTV Genie"}}]},
		"c": {"key": "downArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionDown", 	"device": "DirecTV Genie"}}]},
		"d": {"key": "leftArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionLeft", 	"device": "DirecTV Genie"}}]},
		"e": {"key": "OK", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Select", 			"device": "DirecTV Genie"}}]},
		"f": {"key": "List",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "List", 			"device": "DirecTV Genie"}}]},
		"g": {"key": "Menu", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Menu", 			"device": "DirecTV Genie"}}]},
		"h": {"key": "Guide", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Guide", 			"device": "DirecTV Genie"}}]},
		"i": {"key": "Exit", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Exit", 			"device": "DirecTV Genie"}}]},
		"j": {"key": "Info", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Info", 			"device": "DirecTV Genie"}}]},
		"k": {"key": "upCannel",	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "ChannelUp", 		"device": "DirecTV Genie"}}]},
		"l": {"key": "downChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "ChannelDown", 		"device": "DirecTV Genie"}}]},
		"m": {"key": "prevChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "ChannelPrev", 		"device": "DirecTV Genie"}}]},
		"A": {"key": "upVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "VolumeUp", 		"device": "Master Bedroom"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "VolumeDown", 		"device": "Master Bedroom"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Mute", 			"device": "Master Bedroom"}}]},
		"D": {"key": "Play", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Play", 			"device": "DirecTV Genie"}}]},
		"E": {"key": "Pause", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Pause", 			"device": "DirecTV Genie"}}]},
	 	"F": {"key": "Record", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Record", 			"device": "DirecTV Genie"}}]},
	 	"G": {"key": "Stop", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "RedCircle", 		"device": "DirecTV Genie"}}]},
	 	"H": {"key": "Forward", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "FastForward", 		"device": "DirecTV Genie"}}]},
	 	"I": {"key": "Back", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Rewind", 			"device": "DirecTV Genie"}}]},
		"1": {"key": "1", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "1", 				"device": "DirecTV Genie"}}]},
		"2": {"key": "2", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "2", 				"device": "DirecTV Genie"}}]},
		"3": {"key": "3", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "3", 				"device": "DirecTV Genie"}}]},
		"4": {"key": "4", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "4", 				"device": "DirecTV Genie"}}]},
		"5": {"key": "5", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "5", 				"device": "DirecTV Genie"}}]},
		"6": {"key": "6", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "6", 				"device": "DirecTV Genie"}}]},
		"7": {"key": "7", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "7", 				"device": "DirecTV Genie"}}]},
		"8": {"key": "8", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "8", 				"device": "DirecTV Genie"}}]},
		"9": {"key": "9", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "9", 				"device": "DirecTV Genie"}}]},
		"0": {"key": "0", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "0", 				"device": "DirecTV Genie"}}]},
		"-": {"key": "-", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "-", 				"device": "DirecTV Genie"}}]},
		"=": {"key": "=",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Enter", 			"device": "DirecTV Genie"}}]},
		"[": {"key": "Input",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "SelectRemote", 	"device": "Manager"}}]},
		"]": {"key": "Eject", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "RedCircle", 		"device": "DirecTV Genie"}}]},
		"{": {"key": "Red",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "PowerToggle",      "device": "Vizio TV"}}]},
//		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "PowerToggle", 		"device": "Vizio TV"}}]},
//		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", 			"device": "Vizio TV"}}]},
		":": {"key": "Blue", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", 		    "device": "Vizio TV"}}]},
		"`": {"key": "Power", 		"sequence": [{"remote/turn_off": {"entity_id": "remote.hub_3911_master_bedroom"}}]}
	};

//################
//### MAIN
//################

	//Make Variables Public
	$map.keyMap = keyMap;
	$map.start = start;

/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
