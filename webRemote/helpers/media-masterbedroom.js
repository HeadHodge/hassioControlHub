//##############################################
//### Use javascript's XMLHttpRequest Object
//### To Trigger HomeAssistant Events
//### Via the RESTful Integration API
//##############################################

/////////////////////////// BEGIN PRIVATE NAMESPACE //////////////////////	
(function($case, $map){ //invoke anonymous self executing function

//################
//### powerOff
//################
var powerOff = function(keyChar) {
	
	//Turn TV Off and Sonos On
	$case.keyPressed('[');
	$case.keyPressed('3');
	$case.keyPressed('1');
	$case.keyPressed('5'); //Load Audio Map

	//Set Sonos Sleep Volume & Timer
	$case.postCommand({"action": "runSequence", "reference": "media-masterbedroom", "sequence": [
		{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
		{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
		{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.15}},
		{"sonos/set_sleep_timer": {"entity_id": "media_player.master_bedroom", "sleep_time": 3600}}
	]});
};

//################
//### keyPressed
//################
var keyPressed = function(keyChar) {
	if(!$map.keyMap[keyChar]) return;
	if(!$map.keyMap[keyChar].action && $map.keyMap[keyChar].sequence) $map.keyMap[keyChar].action = 'runSequence';
	if(!$map.keyMap[keyChar].reference && $map.keyMap[keyChar].sequence) $map.keyMap[keyChar].reference = 'media-masterbedroom';

	$case.postCommand($map.keyMap[keyChar]);
	if(keyChar == '`') powerOff(keyChar);
};

//################
//### MAIN
//################
var shortcuts = document.querySelector('Shortcuts');
var red = document.querySelector('Shortcuts > .button.red');
var green = document.querySelector('Shortcuts > .button.green');
var yellow = document.querySelector('Shortcuts > .button.yellow');
var blue = document.querySelector('Shortcuts > .button.blue');

	shortcuts.setAttribute('display', '');
	red.innerHTML = 'TV Power';
	green.innerHTML = 'TV Input';

	//Make Variables Public
	$map.keyPressed = keyPressed;
	
	//Turn Sonos On
	$case.postCommand({"action": "runSequence", "reference": "media-masterbedroom", "sequence": [
		{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
		{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
//		{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.3}}
	]});

	//Pin this Map
	$case.saveMap();
	$map.start();
	
/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
