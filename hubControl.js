////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/controlHub/hubInput.js');
var _zones={};

//##########################################
const onCommand = function(zone, command) {
//##########################################
console.log(`Enter onCommand for command: ${command}`);
var hubOutput = require('/controlHub/hubOutput.js');
var controller, task;

	if(_zones[zone].popupModule) {
		//module = _zones[zone].popupModule;
		_zones[zone].popupController = require(_zones[zone].popupModule);
		_zones[zone].popupModule = null;
		controller = _zones[zone].popupController;
	} else {
		_zones[zone].primaryController = require(_zones[zone].primaryModule);
		controller = _zones[zone].primaryController;
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
var hubOutput = require('/controlHub/hubOutput.js');
var task;

	_zones[zone].isTaskSet = null;
	if(!_zones[zone].tasks[_zones[zone].focus][command]) return;
	task = `{"action": "runSequence", "sequence": ${JSON.stringify(_zones[zone].tasks[_zones[zone].focus][command])}}`;
	console.log(`Send selected task: ${task}`);
	hubOutput.sendControlTask(task);
};

//##########################################
const onSelectFocus = function(zone, command) {
//##########################################
console.log(`Enter onSelectFocus with ${command} in zone ${zone}`);

	_zones[zone].isFocusSet = null;
	
	if(command == 'Ok') {
		_zones[zone].isTaskSet = true;
		return console.log(`taskList selected for ${zone}`);
	};
	
/*	
	if(_zones[zone].topics[command] && _zones[zone].topics[command].controller[command]) {
		_zones[zone].focus = command;
		_zones[zone].primaryModule = _zones[zone].topics[command].controller[command];
		_zones[zone].isControllerSelected = true;
		return console.log(`primaryModule selected : ${_zones[zone].primaryModule}`);
	};
	
	if(_zones[zone].topics[_zones[zone].focus] && _zones[zone].topics[_zones[zone].focus].controller[command]) {
		_zones[zone].popupModule = _zones[zone].topics[_zones[zone].focus].controller[command];
		return console.log(`popupModule selected: ${_zones[zone].popupModule}`);
	};
*/	
	switch(command) {
	case 'Focus':
		_zones[zone].primaryModule = _zones[zone].controllers['Focus'];
		break;
	case 'Louder':
		_zones[zone].primaryModule = _zones[zone].controllers['Louder'];
		break;
	case 'Softer':
		_zones[zone].primaryModule = _zones[zone].controllers['Softer'];
		break;
	case 'Silence/Sound':
		primaryModule = _zones[zone].controllers['Silence/Sound'];
		break;
	case 'Backward':
		_zones[zone].primaryModule = _zones[zone].controllers['Backward'];
		break;
	case 'Stop/Start':
		_zones[zone].primaryModule = _zones[zone].controllers['Stop/Start'];
		break;
	case 'Forward':
		_zones[zone].primaryModule = _zones[zone].controllers['Forward'];
		break;
	default:
		return;
	}

	return console.log(`defaultController selected: ${_zones[zone].primaryModule}`);
};
 
//##########################################
const onInput = function(hubInput) {
try {
//##########################################
console.log(`Enter onInput, command: ${hubInput.command}, zone: ${hubInput.zone}`);
_zones[hubInput.zone] = require(`/controlHub/zones/zone.${hubInput.zone}.js`);
	
	if(_zones[hubInput.zone].isControllerSelected) {_zones[hubInput.zone].isControllerSelected = null; if(hubInput.command == 'Off/On' || hubInput.command == 'Set') hubInput.command = 'Open';};
	if(_zones[hubInput.zone].isFocusSet) if(hubInput.command == 'Off/On' || hubInput.command == 'Set'){hubInput.command = 'Open'; _zones[hubInput.zone].isFocusSet = null;};
	if(_zones[hubInput.zone].isFocusSet) return onSelectFocus(hubInput.zone, hubInput.command);
	if(_zones[hubInput.zone].isTaskSet) return onSelectTask(hubInput.zone, hubInput.command);
		
	if(hubInput.command == 'Focus') {_zones[hubInput.zone].isFocusSet = true; return console.log(`Set Focus Flag`);}

	if(hubInput.command == 'Set') hubInput.command = 'Off/On';

	if(hubInput.command == 'Silence/Sound') {
		if(_zones[hubInput.zone].isSilent)
			{hubInput.command = 'Sound';_zones[hubInput.zone].isSilent=false;}
		else
			{hubInput.command = 'Silence';_zones[hubInput.zone].isSilent=true;}
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
