//##############################################
//### Use javascript's XMLHttpRequest Object
//### To Trigger HomeAssistant Events
//### Via the RESTful Integration API
//##############################################remote.hub_3911_living_room

/////////////////////////// BEGIN PRIVATE NAMESPACE //////////////////////	
(function($case, $map){ //invoke anonymous self executing function

//################
//### start
//################
var start = function() {
	if(document.querySelector('Filter').getAttribute('recalled')) return; //Already Powered On
	$case.postCommand({"action": "runSequence", "reference": "media-amazontv-livingroom", "sequence": [{"remote/turn_on": {"entity_id": "remote.hub_3911_living_room", "activity": "Watch FireTV"}}]});
};
  
//################
//### keyMap
//################
var	keyMap = {
		"a": {"key": "upArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionUp", 		            "device": "Amazon Fire TV Stick"}}]},
		"b": {"key": "rightArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionRight",	            "device": "Amazon Fire TV Stick"}}]},
		"c": {"key": "downArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionDown", 	            "device": "Amazon Fire TV Stick"}}]},
		"d": {"key": "leftArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "DirectionLeft", 	            "device": "Amazon Fire TV Stick"}}]},
		"e": {"key": "OK", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "OK", 				            "device": "Amazon Fire TV Stick"}}]},
		"f": {"key": "List", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Home", 			            "device": "Amazon Fire TV Stick"}}]},
		"g": {"key": "Menu", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Menu", 			            "device": "Amazon Fire TV Stick"}}]},
		"i": {"key": "Exit", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Back", 			            "device": "Amazon Fire TV Stick"}}]},
		"A": {"key": "upVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeUp", 		            "device": "JBL Amp"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeDown", 		            "device": "JBL Amp"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Mute", 			            "device": "JBL Amp"}}]},
		"D": {"key": "Play", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Play", 			            "device": "Amazon Fire TV Stick"}}]},
		"E": {"key": "Pause", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Pause", 			            "device": "Amazon Fire TV Stick"}}]},
	 	"H": {"key": "Forward", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "FastForward", "hold_secs": .65,"device": "Amazon Fire TV Stick"}}]},
	 	"I": {"key": "Back", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Rewind", "hold_secs": .65, 		"device": "Amazon Fire TV Stick"}}]},
		"{": {"key": "Red",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", 		    	"device": "LG TV"}}]},
		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Input", 			            "device": "LG TV"}}]},
		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", 				"device": "JBL Amp"}}]},
		":": {"key": "Blue", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "InputNext", 					"device": "Kinivo AV Switch"}}]},
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
