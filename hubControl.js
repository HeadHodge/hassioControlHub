////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/controlHub/modules/hubInput.js');
var _hub={};
//var primaryController={}, popupController={};

//##########################################
const onCommand = function(zone, command) {
//##########################################
console.log(`Enter onCommand for command: ${command}`);
var hubOutput = require('/controlHub/modules/hubOutput.js');
var controller, task;

	if(_hub[zone].popupModule) {
		//module = _hub[zone].popupModule;
		_hub[zone].popupController = require(_hub[zone].popupModule);
		_hub[zone].popupModule = null;
		controller = _hub[zone].popupController;
	} else {
		_hub[zone].primaryController = require(_hub[zone].primaryModule);
		controller = _hub[zone].primaryController;
	};
	
	if(!controller.tasks[command]) return console.log(`Abort: Invalid command: ${command}`);
	
	task = `{"action": "runSequence", "sequence": ${JSON.stringify(controller.tasks[command])}}`;
	console.log(`For command: ${command}, Send task: ${task}`);
	hubOutput.sendControlTask(task);
};

//##########################################
const onSelectTask = function(zone, command) {
//##########################################
console.log(`Enter onSelectTask with ${command} in zone: ${zone}`);
var hubOutput = require('/controlHub/modules/hubOutput.js');
var task;

	_hub[zone].isTaskSet = null;
	if(!_hub[zone].tasks[_hub[zone].focus][command]) return;
	task = `{"action": "runSequence", "sequence": ${JSON.stringify(_hub[zone].tasks[_hub[zone].focus][command])}}`;
	console.log(`Send selected task: ${task}`);
	hubOutput.sendControlTask(task);
};

//##########################################
const onSelectFocus = function(zone, command) {
//##########################################
console.log(`Enter onSelectFocus with ${command} in zone ${zone}`);

	_hub[zone].isFocusSet = null;
	
	if(command == 'Ok') {
		_hub[zone].isTaskSet = true;
		return console.log(`taskList selected for ${zone}`);
	};
	
	if(_hub[zone].topics[command] && _hub[zone].topics[command].controller[command]) {
		_hub[zone].focus = command;
		_hub[zone].primaryModule = _hub[zone].topics[command].controller[command];
		_hub[zone].isControllerSelected = true;
		return console.log(`primaryModule selected : ${_hub[zone].primaryModule}`);
	};
	
	if(_hub[zone].topics[_hub[zone].focus] && _hub[zone].topics[_hub[zone].focus].controller[command]) {
		_hub[zone].popupModule = _hub[zone].topics[_hub[zone].focus].controller[command];
		return console.log(`popupModule selected: ${_hub[zone].popupModule}`);
	};
 };
 
//##########################################
const onInput = function(hubInput) {
try {
//##########################################
console.log(`Enter onInput, command: ${hubInput.command}, zone: ${hubInput.zone}`);
_hub[hubInput.zone] = require(`/controlHub/modules/hubs/hub.zone.${hubInput.zone}.js`);
	
	if(_hub[hubInput.zone].isControllerSelected) {_hub[hubInput.zone].isControllerSelected = null; if(hubInput.command == 'On/Off' || hubInput.command == 'Set') hubInput.command = 'Open';};
	if(_hub[hubInput.zone].isFocusSet) if(hubInput.command == 'On/Off' || hubInput.command == 'Set'){hubInput.command = 'Open'; _hub[hubInput.zone].isFocusSet = null;};
	if(_hub[hubInput.zone].isFocusSet) return onSelectFocus(hubInput.zone, hubInput.command);
	if(_hub[hubInput.zone].isTaskSet) return onSelectTask(hubInput.zone, hubInput.command);
		
	if(hubInput.command == 'Focus') {_hub[hubInput.zone].isFocusSet = true; return console.log(`Set Focus Flag`);}

	if(hubInput.command == 'Set') hubInput.command = 'On/Off';

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
