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
	$case.postCommand({"action": "runSequence", "reference": "media-computer-livingroom", "sequence": [{"remote/turn_on": {"entity_id": "remote.hub_3911_living_room", "activity": "Watch HTPC"}}]});
};
   
//################
//### keyMap
//################
var	keyMap = {
		"A": {"key": "upVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeUp", 	"device": "JBL Amp"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeDown", 	"device": "JBL Amp"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Mute", 		"device": "JBL Amp"}}]},
		"{": {"key": "Red",	 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", "device": "LG TV"}}]},
		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Input", 		"device": "LG TV"}}]},
		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", "device": "JBL Amp"}}]},
		":": {"key": "Blue", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "InputNext", 	"device": "Kinivo AV Switch"}}]},
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
