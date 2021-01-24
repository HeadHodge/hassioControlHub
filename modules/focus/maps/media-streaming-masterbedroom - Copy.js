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
	$case.postCommand({"action": "runSequence", "reference": "media-streaming-masterbedroom", "sequence": [{"remote/turn_on": {"entity_id": "remote.hub_3911_master_bedroom", "activity": "Watch Fire TV"}}]});
};
  
//################
//### keyMap
//################
var	keyMap = {
#		"a": {"key": "upArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionUp", 		          	"device": "Amazon Fire TV Stick"}}]},
#		"b": {"key": "rightArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionRight",	          	"device": "Amazon Fire TV Stick"}}]},
#		"c": {"key": "downArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionDown", 	          	"device": "Amazon Fire TV Stick"}}]},
#		"d": {"key": "leftArrow", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "DirectionLeft", 	          	"device": "Amazon Fire TV Stick"}}]},
		"a": {"key": "upArrow", 	"sequence": [{"androidtv.adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "UP"}}]},
		"b": {"key": "rightArrow", 	"sequence": [{"androidtv.adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "RIGHT"}}]},
		"c": {"key": "downArrow", 	"sequence": [{"androidtv.adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "DOWN"}}]},
		"d": {"key": "leftArrow", 	"sequence": [{"androidtv.adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "LEFT"}}]},
		"e": {"key": "OK", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "OK", 				          	"device": "Amazon Fire TV Stick"}}]},
		"f": {"key": "List", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Home", 				        "device": "Amazon Fire TV Stick"}}]},
		"g": {"key": "Menu", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Menu", 				        "device": "Amazon Fire TV Stick"}}]},
		"i": {"key": "Exit", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Back", 				        "device": "Amazon Fire TV Stick"}}]},
		"A": {"key": "upVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "VolumeUp", 			        "device": "Master Bedroom"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "VolumeDown", 		          	"device": "Master Bedroom"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Mute", 					  	"device": "Master Bedroom"}}]},
		"D": {"key": "Play", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Play", 			            "device": "Amazon Fire TV Stick"}}]},
		"E": {"key": "Pause", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Pause", 			          	"device": "Amazon Fire TV Stick"}}]},
	 	"H": {"key": "Forward", 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "FastForward", "hold_secs": 1,	"device": "Amazon Fire TV Stick"}}]},
	 	"I": {"key": "Back", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Rewind", "hold_secs": 1,      	"device": "Amazon Fire TV Stick"}}]},
		"{": {"key": "Red",	 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "PowerToggle",       			"device": "Vizio TV"}}]},
//		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "PowerToggle", 			      	"device": "Vizio TV"}}]},
//		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", 			          	"device": "Vizio TV"}}]},
		":": {"key": "Blue", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", 		        		"device": "Vizio TV"}}]},
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
