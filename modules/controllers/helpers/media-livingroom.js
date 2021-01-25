//##############################################
//### Use javascript's XMLHttpRequest Object
//### To Trigger HomeAssistant Events
//### Via the RESTful Integration API
//##############################################

/////////////////////////// BEGIN PRIVATE NAMESPACE //////////////////////	
(function($case, $map){ //invoke anonymous self executing function

//################
//### remoteKeyPressed
//################
var keyPressed = function(keyChar) {
	if(!$map.keyMap[keyChar]) return;
	if(!$map.keyMap[keyChar].action && $map.keyMap[keyChar].sequence) $map.keyMap[keyChar].action = 'runSequence';
	if(!$map.keyMap[keyChar].reference) $map.keyMap[keyChar].reference = 'media-livingroom';

	$case.postCommand($map.keyMap[keyChar]);
	if(keyChar == '`') $case.removeMap();
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
	yellow.innerHTML = 'AV Power';
	blue.innerHTML = 'AV Input';

	//Make Variables Public
	$map.keyPressed = keyPressed;
	
	//Save this Map
	$case.saveMap();
	$map.start();
	
/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
