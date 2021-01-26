////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/scripts/modules/hubInput.js');
var _hub={};
var primaryController={}, popupController={};

//##########################################
const onCommand = function(zone, command) {
//##########################################
console.log(`Enter onCommand for command: ${command}`);
var hubOutput = require('/scripts/modules/hubOutput.js');
var controller, task;

	if(_hub[zone].popupModule) {
		//module = _hub[zone].popupModule;
		//_hub[zone].popupModule = null;
		popupController = require(_hub[zone].popupModule);
		controller = popupModule;
	} else {
		primaryController = require(_hub[zone].primaryModule);
		controller = primaryController;
	};
	
	if(!controller.tasks[command]) return console.log(`Abort: Invalid command: ${command}`);
	
	task = `{"action": "runSequence", "sequence": ${JSON.stringify(controller.tasks[command])}}`;
	hubOutput.sendControlTask(task);
};

//##########################################
const onFunction = function(zone, command) {
//##########################################
console.log(`Enter onFunction with ${command} in zone: ${_hub[zone].zone}`);

	_hub[zone].isFunctionSet = null;
};
 
//##########################################
const onFocus = function(zone, command) {
//##########################################
console.log(`Enter onFocusChange with ${command} in zone ${_hub[zone].zone}`);

	_hub[zone].isFocusSet = null;
	
	if(command == 'Focus' || command == 'On/Off' || command == 'Set') return console.log(`Cancel onFocus`);
	
	if(command == 'Ok') return onCommand(zone, 'Off');
	
	if(!_hub[zone].topics[command]) {
		_hub[zone].popupController = _hub[zone].topics[_hub[zone].focus].controller[command];
		return console.log(`popupController selected: ${_hub[zone].popupController}`);
	};
	
	_hub[zone].primaryController = _hub[zone].topics[command].controller[command];
	console.log(`primaryController changed to: ${_hub[zone].primaryController}`);
	return onCommand(zone, 'Open');
 };
 
//##########################################
const onInput = function(hubInput) {
try {
//##########################################
console.log(`Enter onInput, command: ${hubInput.command}, zone: ${hubInput.zone}`);
_hub[hubInput.zone] = require(`/scripts/modules/hubs/hub.zone.${hubInput.zone}.js`);
//var controller = _hub[hubInput.zone].topics[_hub[hubInput.zone].focus].controller[_hub[hubInput.zone].focus];
	
	if(_hub[hubInput.zone].isFocusSet) return onFocus(hubInput.zone, hubInput.command);
	if(_hub[hubInput.zone].isFunctionSet) return onFunction(hubInput.zone, hubInput.command);

	if(hubInput.command == 'Focus' || hubInput.command == 'On/Off') {_hub[hubInput.zone].isFocusSet = true; return console.log(`Set Focus Flag`);}
	if(hubInput.command == 'Enter') {_hub[hubInput.zone].isFunctionSet = true; return console.log(`Set Function Flag`);}
	if(hubInput.command == 'Set') hubInput.command = 'Off';

/*
	if(hubInput.command == 'On/Off' || hubInput.command == 'Set') {
		if(_hub[hubInput.zone].isOn)
			{hubInput.command = 'Off';_hub[hubInput.zone].isOn=false;}
		else
			{hubInput.command = 'On';_hub[hubInput.zone].isOn=true;}
	};
*/	
	if(hubInput.command == 'Silence/Sound') {
		if(_hub[hubInput.zone].isSilent)
			{hubInput.command = 'Sound';_hub[hubInput.zone].isSilent=false;}
		else
			{hubInput.command = 'Silence';_hub[hubInput.zone].isSilent=true;}
	};
	
	onCommand(hubInput.zone, hubInput.command);
}
catch(error) {
	console.log(`Unexpected Problem: ${error}`);
	console.error(error);
}};
		
////////////////////////////////////////////
//                MAIN
//Open server to listen for control input
////////////////////////////////////////////
console.log(`Started hubControl on ${os.hostname}`);

	hubInput.listen(onInput);
