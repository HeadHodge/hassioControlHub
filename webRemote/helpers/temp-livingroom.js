//##############################################
//### Use javascript's XMLHttpRequest Object
//### To Trigger HomeAssistant Events
//### Via the RESTful Integration API
//##############################################

/////////////////////////// BEGIN PRIVATE NAMESPACE //////////////////////	
(function($case, $map){ //invoke anonymous self executing function

//################
//### MAIN
//################
var shortcuts = document.querySelector('Shortcuts');
var red = document.querySelector('Shortcuts > .button.red');
var green = document.querySelector('Shortcuts > .button.green');
var yellow = document.querySelector('Shortcuts > .button.yellow');
var blue = document.querySelector('Shortcuts > .button.blue');

	shortcuts.setAttribute('display', '');
	red.innerHTML = '30 Min';
	green.innerHTML = '60 Min';
	yellow.innerHTML = '90 Min';
	blue.innerHTML = '120 Min';

/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
