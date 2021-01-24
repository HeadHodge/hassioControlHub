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
	$case.postCommand({"action": "runSequence", "reference": "media-streaming-masterbedroom", "sequence": [{"remote/send_command": {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}, {"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}}]});
};
  
//################
//### keyMap
//################
var	keyMap = {
		"a": {"key": "upArrow",    "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "UP"}}]},
		"b": {"key": "rightArrow", "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "RIGHT"}}]},
		"c": {"key": "downArrow",  "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "DOWN"}}]},
		"d": {"key": "leftArrow",  "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "LEFT"}}]},
		"e": {"key": "OK", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "CENTER"}}]},
		"f": {"key": "List", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}}]},
		"g": {"key": "Menu", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "MENU"}}]},
		"i": {"key": "Exit", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "BACK"}}]},
		"A": {"key": "upVolume",   "sequence": [{"media_player/volume_up"  : {"entity_id": "media_player.master_bedroom"}}, {"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}]},
		"B": {"key": "downVolume", "sequence": [{"media_player/volume_down": {"entity_id": "media_player.master_bedroom"}}, {"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}]},
		"C": {"key": "muteVolume", "sequence": [{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": true}}]},
		"D": {"key": "Play/Pause", "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent 85"}}]},
	 	"H": {"key": "Forward",    "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 90"}}]},
	 	"I": {"key": "Back",       "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 89"}}]},
		"{": {"key": "Red",	   "sequence": [{"remote/send_command"	   : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}]},
		"}": {"key": "Green",	   "sequence": [{"remote/send_command"     : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "Input"}}]},
//		"|": {"key": "Yellow", 	   "sequence": [{"remote/send_command"     : {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", "device": "Vizio TV"}}]},
//		":": {"key": "Blue", 	   "sequence": [{"remote/send_command"     : {"entity_id": "remote.hub_3911_master_bedroom", "command": "Input", "device": "Vizio TV"}}]},
		"`": {"key": "Off", 	   "sequence": [{"androidtv/adb_command"   : {"entity_id": "media_player.firetv_masterbedroom", "command": "SLEEP"}}, {"remote/send_command" : {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}]}
	};

//################
//### MAIN
//################

	//Make Variables Public
	$map.keyMap = keyMap;
	$map.start = start;

/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
