////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/controlHub/hubInput.js');
const debug = require('/controlHub/hubDebug.js').debug;
var _zones={};


//##########################################
const onOutput = function(zone, command) {
//##########################################
debug.log(`Enter onOutput for command: ${command}`);
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
	debug.log(`For command: ${command}, Send task: ${task}`);
	hubOutput.sendTasks(task);
};

//##########################################
const onSelectTask = function(zone, command) {
//##########################################
debug.log(`Enter onSelectTask with ${command} in zone: ${zone}`);
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
const onCommand = function(input) {
try {
//##########################################
debug.log(`Enter onCommand, command: ${input.command}, zone: ${input.zone}`);
_zones[input.zone] = require(`/controlHub/zones/zone.${input.zone}.js`);

	if(input.command == 'Set') input.command = 'Off/On';
	
	//if(_zones[input.zone].isControllerSelected) {_zones[input.zone].isControllerSelected = null; if(input.command == 'Off/On') input.command = 'Open';};
	if(_zones[input.zone].isFocusSet && input.command == 'Off/On'){input.command = 'Open'; _zones[input.zone].isFocusSet = null;};
	if(_zones[input.zone].isFocusSet) return onSelectFocus(input.zone, input.command);
	if(_zones[input.zone].isTaskSet) return onSelectTask(input.zone, input.command);
		
	if(input.command == 'Focus') {_zones[input.zone].isFocusSet = true; return console.log(`Set Focus Flag`);}

	if(input.command == 'Silence/Sound') {
		if(_zones[input.zone].isSilent)
			{input.command = 'Sound';_zones[input.zone].isSilent=null;}
		else
			{input.command = 'Silence';_zones[input.zone].isSilent=true;}
	};
	
	onOutput(input.zone, input.command);
}
catch(error) {
	console.log(`Unexpected Problem: ${error}`);
	console.error(error);
}};
 
//##########################################
const onFileName = function(client) {
try {
//##########################################
debug.log(`Enter onFileName, fileName: ${client.input.fileName}, filePath: ${__dirname + client.input.fileName}`);
var fs = require('fs');

	fs.readFile(__dirname + client.input.fileName, 'utf8', function(error, content) {
		if(error) return; //client.send(`${error.name}: ${error.message}`);
		client.send(content);
	});
}
catch(error) {
	console.log(`Unexpected Problem: ${error}`);
	console.error(error);
}};
 
//##########################################
const onInput = function(client) {
try {
//##########################################
debug.log(`Enter onInput, inputType: ${client.input.type}`);

	if(client.input.type == 'command') {client.send('Got It');onCommand(client.input);return;};
	if(client.input.type == 'fileName') return onFileName(client);
	
	client.send(`Abort: Invalid Input Recieved`);
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

	hubInput.getInput(onInput);
