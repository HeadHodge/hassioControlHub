//##############################################
//### Use javascript's XMLHttpRequest Object
//### To Trigger HomeAssistant Events
//### Via the RESTful Integration API
//##############################################

/////////////////////////// BEGIN PRIVATE NAMESPACE //////////////////////	
(function($case, $map){ //invoke anonymous self executing function

//################
//### keyPressed
//################
var keyPressed = function(keyChar) {
	if(!keyMap[keyChar]) return;
	if(!keyMap[keyChar].action && keyMap[keyChar].sequence) keyMap[keyChar].action = 'runSequence';
	if(!keyMap[keyChar].reference) keyMap[keyChar].reference = 'media-audio-masterbedroom';

	$case.postCommand(keyMap[keyChar]);
};

//################
//### start
//################
var start = function() {
var shortcuts = document.querySelector('Shortcuts');
var red = document.querySelector('Shortcuts > .button.red');
var green = document.querySelector('Shortcuts > .button.green');
var yellow = document.querySelector('Shortcuts > .button.yellow');
var blue = document.querySelector('Shortcuts > .button.blue');

	shortcuts.setAttribute('display', '');
	red.innerHTML = 'Rock';
	green.innerHTML = 'Blues';
	yellow.innerHTML = 'Club';
	blue.innerHTML = 'TV';
	
	$case.postCommand({"action": "runSequence", "reference": "media-audio-masterbedroom-sleep", "sequence": [
		{"remote/turn_off": {"entity_id": "remote.hub_3911_master_bedroom"}},
//		{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
		{"sleep": 5},
		{"media_player/media_play": {"entity_id": "media_player.master_bedroom"}}
	]});

	$case.saveMap();
};
   
//################
//### keyMap
//################
var	keyMap = {
		"A": {"key": "upVolume",   "sequence": [{"media_player/volume_up":     {"entity_id": "media_player.master_bedroom"}}]},
		"B": {"key": "downVolume", "sequence": [{"media_player/volume_down":   {"entity_id": "media_player.master_bedroom"}}]},
		"D": {"key": "Play", 	   "sequence": [{"media_player/volume_mute":   {"entity_id": "media_player.master_bedroom", "is_volume_muted": false}}]},
		"C": {"key": "muteVolume", "sequence": [{"media_player/volume_mute":   {"entity_id": "media_player.master_bedroom", "is_volume_muted": true}}]},
		"{": {"key": "Red",	   "sequence": [{"remote.rm4_ir_hub_remote":   {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}]},
		"}": {"key": "Green",	   "sequence": [{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}}]},
		"|": {"key": "Yellow", 	   "sequence": [{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Club"}}]},
		":": {"key": "Blue", 	   "sequence": [{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}}]},
		"`": {"key": "Power", 	   "sequence": [{"media_player/media_stop":    {"entity_id": "media_player.master_bedroom"}}]}
	};

//################
//### MAIN
//################

	//Make Variables Public
	$map.keyMap = keyMap;
	$map.keyPressed = keyPressed;
	start();

/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
