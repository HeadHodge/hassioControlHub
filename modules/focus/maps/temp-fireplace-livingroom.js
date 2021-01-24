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
	if(!keyMap[keyChar].reference) keyMap[keyChar].reference = 'temp-fireplace-livingroom';
	$case.postCommand(keyMap[keyChar]);
};

//################
//### keyMap
//################
var	keyMap = {
	 	"F": {"key": "Record",		"sequence": [{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "120 Minutes"}}]},
	 	"G": {"key": "Stop", 		"sequence": [{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "OFF"}}]},
		"{": {"key": "Red",	 		"sequence": [{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "30 Minutes"}}]},
		"}": {"key": "Green",		"sequence": [{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "60 Minutes"}}]},
		"|": {"key": "Yellow", 		"sequence": [{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "90 Minutes"}}]},
		":": {"key": "Blue", 		"sequence": [{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "120 Minutes"}}]}
	};

//################
//### MAIN
//################

	//Make Variables Public
	$map.keyMap = keyMap;
	$map.keyPressed = keyPressed;
	$map.loadHelper = true;

/////////////////////////// END PRIVATE NAMESPACE //////////////////////	
})(ipRemote.case, ipRemote.map);
