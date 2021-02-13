////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const debug = require('/inputHub/core/debugLog.js').debug;
const os = require('os');
const htmlServer = require('/inputHub/core/htmlServer.js');
const wsInput = require('/inputHub/core/wsInput.js');
const wsOutput = require('/inputHub/core/wsOutput.js');
var _zones={};

//##########################################
const onCommand = function(zone, command, reply) {
//##########################################
console.log(`Enter onCommand, command: ${command}, zone: ${zone}`);
var controller, task;

	if(_zones[zone].popupModule) {
		_zones[zone].popupController = require(_zones[zone].popupModule);
		_zones[zone].popupModule = null;
		controller = _zones[zone].popupController;
	} else {
		_zones[zone].primaryController = require(_zones[zone].primaryModule);
		controller = _zones[zone].primaryController;
	};
	
	if(!controller.tasks[command]) return console.log(`Abort: Invalid command: ${command}`);
	
	console.log(`Run Task: ${JSON.stringify(controller.tasks[command])}`);
	global.onOutput(JSON.stringify(controller.tasks[command]), reply);
};

//##########################################
const onSelectTask = function(zone, command, reply) {
//##########################################
debug.log(`Enter onSelectTask with ${command} in zone: ${zone}`);
var task;

	_zones[zone].isTaskSet = null;
	if(!_zones[zone].tasks[command]) return console.log(`Abort: Invalid command: ${command}`);
	global.onOutput(JSON.stringify(_zones[zone].tasks[command]), reply);
};

//##########################################
const onSelectFocus = function(zone, command) {
//##########################################
debug.log(`Enter onSelectFocus with ${command} in zone ${zone}`);

	_zones[zone].isFocusSet = null;
	
	if(command == 'Ok') {
		_zones[zone].isTaskSet = true;
		return console.log(`taskList selected for ${zone}`);
	};
	
	switch(command) {
	case 'Home':
		_zones[zone].primaryModule = _zones[zone].controllers['Home'];
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
const onInput = function(input, reply) {
try {
//##########################################
debug.log(`Enter onInput, command: ${input.command}, zone: ${input.zone}`);
_zones[input.zone] = require(`/inputHub/zones/zone.${input.zone}.js`);

	if(input.command == 'Set') input.command = 'Off/On';
	
	if(_zones[input.zone].isFocusSet && input.command == 'Off/On'){input.command = 'Open'; _zones[input.zone].isFocusSet = null;};
	if(_zones[input.zone].isFocusSet) return onSelectFocus(input.zone, input.command);
	if(_zones[input.zone].isTaskSet || input.command == 'Ping') return onSelectTask(input.zone, input.command, reply);
		
	if(input.command == 'Focus') {_zones[input.zone].isFocusSet = true; return console.log(`Set Focus Flag`);}

	if(input.command == 'Silence/Sound') {
		if(_zones[input.zone].isSilent)
			{input.command = 'Sound';_zones[input.zone].isSilent=null;}
		else
			{input.command = 'Silence';_zones[input.zone].isSilent=true;}
	};
	
	onCommand(input.zone, input.command, reply);
}
catch(error) {
	console.log(`Unexpected Problem: ${error}`);
	console.error(error);
}};

////////////////////////////////////////////
//                MAIN
//Open server to listen for control input
////////////////////////////////////////////
debug.log(`Started hubControl on ${os.hostname}`);

	global.onInput = onInput;