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
		"a": {"key": "upArrow", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "UP"}}]},
		"b": {"key": "rightArrow", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "RIGHT"}}]},
		"c": {"key": "downArrow", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "DOWN"}}]},
		"d": {"key": "leftArrow", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "LEFT"}}]},
		"e": {"key": "OK", 		"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "CENTER"}}]},
		"f": {"key": "List", 		"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "HOME"}}]},
		"g": {"key": "Menu", 		"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "MENU"}}]},
		"i": {"key": "Exit", 		"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "BACK"}}]},
		"A": {"key": "upVolume", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "VOLUME_UP"}}]},
		"B": {"key": "downVolume", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "VOLUME_DOWN"}}]},
		"C": {"key": "muteVolume", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "MUTE"}}]},
		"D": {"key": "Play", 		"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent 85"}}]},
		"E": {"key": "Pause", 		"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": 'sendevent /dev/input/event6 4 4 786637 && sendevent /dev/input/event6 1 164 1 && sendevent /dev/input/event6 0 0 0 && sendevent /dev/input/event6 4 4 786637 && sendevent /dev/input/event6 1 164 0 && sendevent /dev/input/event6 0 0 0'}}]},
	 	"H": {"key": "Forward", 	"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "FAST_FORWARD"}}]},
	 	"I": {"key": "Back", 		"sequence": [{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "REWIND"}}]},
		"{": {"key": "Red",	 	"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", "device": "LG TV"}}]},
		"}": {"key": "Green",		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "Input", "device": "LG TV"}}]},
		"|": {"key": "Yellow", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "PowerToggle", "device": "JBL Amp"}}]},
		":": {"key": "Blue", 		"sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "InputNext", "device": "Kinivo AV Switch"}}]},
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
