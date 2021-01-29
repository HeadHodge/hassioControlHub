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
	$case.postCommand({"action": "runSequence", "reference": "media-broadcast-masterbedroom", "sequence": [{"remote/turn_on": {"entity_id": "remote.hub_3911_master_bedroom", "activity": "Watch Antenna TV"}}]});
};
   
//################
//### keyMap
//################
var	keyMap = {
		"k": {"key": "upCannel", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "ChannelUp", 		"device": "Vizio TV"}}]},
		"l": {"key": "downChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "ChannelDown", 		"device": "Vizio TV"}}]},
		"m": {"key": "prevChannel", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Last", 			"device": "Vizio TV"}}]},
		"A": {"key": "upVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "VolumeUp", 			"device": "Master Bedroom"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "VolumeDown", 		"device": "Master Bedroom"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Mute", 				"device": "Master Bedroom"}}]},
		"1": {"key": "1", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "1", 				"device": "Vizio TV"}}]},
		"2": {"key": "2", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "2", 				"device": "Vizio TV"}}]},
		"3": {"key": "3", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "3", 				"device": "Vizio TV"}}]},
		"4": {"key": "4", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "4", 				"device": "Vizio TV"}}]},
		"5": {"key": "5", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "5", 				"device": "Vizio TV"}}]},
		"6": {"key": "6", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "6", 				"device": "Vizio TV"}}]},
		"7": {"key": "7", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "7", 				"device": "Vizio TV"}}]},
		"8": {"key": "8", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "8", 				"device": "Vizio TV"}}]},
		"9": {"key": "9", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "9", 				"device": "Vizio TV"}}]},
		"0": {"key": "0", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "0", 				"device": "Vizio TV"}}]},
		"-": {"key": "-", 			"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "-", 				"device": "Vizio TV"}}]},
		"=": {"key": "=",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Enter", 			"device": "Vizio TV"}}]},
		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "PowerToggle", 		"device": "Vizio TV"}}]},
		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", 			"device": "Vizio TV"}}]},
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
