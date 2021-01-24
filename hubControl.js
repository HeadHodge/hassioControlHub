////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/scripts/modules/hubInput.js');
var tasks, clientOptions={}, focusOptions={};

//##########################################
const onCommand = function(clientId, clientCommand) {
//##########################################
console.log(`Enter onCommand for clientCommand: ${clientCommand}`);
var hubOutput = require('/scripts/modules/hubOutput.js');
//var tasks = require('/scripts/modules/masterBedroom.js');
var sequence, task;

	//focusOptions = require(`/scripts/modules/controllers/masterBedroom.entertainment.js`);
	focusOptions = require(`/scripts/modules/controllers/masterBedroom.entertainment.js`);
	sequence = focusOptions.tasks[clientCommand];
	if(!sequence) return console.log(`Abort: Ivalid clientCommand: ${clientCommand}`);
	
	task = `{"action": "runSequence", "sequence": ${JSON.stringify(focusOptions.tasks[clientCommand])}}`;
	//console.log(`Send Task: ${task}`);
	hubOutput.sendControlTask(task);
	//$case.postCommand({"action": "runSequence", "sequence": [{"remote/send_command": {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}, {"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}}]});
};

//##########################################
const onFunction = function(clientId, clientCommand) {
//##########################################
console.log(`Enter onFunction with ${clientCommand} in zone: ${clientOptions[clientId].zone}`);

	clientOptions[clientId].isFunctionSet = null;
	//inputWord.task = 'wake';
	//isCommandMode = false;	
	//return sendTask(inputWord);
};
 
//##########################################
const onFocus = function(clientId, clientCommand) {
//##########################################
console.log(`Enter onFocusChange with ${clientCommand} in zone ${clientOptions[clientId]}`);

	clientOptions[clientId].isFocusSet = null;
	//inputWord.task = 'wake';
	//isCommandMode = false;	
	//return sendTask(inputWord);
};
 
//##########################################
const onInput = function(client) {
//##########################################
clientOptions[client.controlInput.id] = require(`/scripts/modules/clients/${client.controlInput.id}.js`);
var controller = clientOptions[client.controlInput.id].topics[clientOptions[client.controlInput.id].focus].controller.Default;
console.log(controller);
console.log(`Enter onInput, clientId: ${client.controlInput.id}, clientZone: ${clientOptions[client.controlInput.id].zone}`);

	if(client.controlInput.command == 'Focus') {clientOptions[client.controlInput.id].isFocusSet = true; return console.log(`Set Focus Flag`);}
	if(client.controlInput.command == 'Enter') {clientOptions[client.controlInput.id].isFunctionSet = true; return console.log(`Set Function Flag`);}
	
	if(clientOptions[client.controlInput.id].isFocusSet) return onFocus(client.controlInput.id, client.controlInput.command);
	if(clientOptions[client.controlInput.id].isFunctionSet) return onFunction(client.controlInput.id, client.controlInput.command);

	if(client.controlInput.command == 'Set') client.controlInput.command = 'On';
	if(client.controlInput.command == 'Silence/Sound') client.controlInput.command = 'Silence';
	if(client.controlInput.isCommandMode) return createCommand(client.controlInput);
	onCommand(client.controlInput.id, client.controlInput.command);
};
		
////////////////////////////////////////////
//                MAIN
//Open server to listen for control input
////////////////////////////////////////////
console.log(`Started hubControl on ${os.hostname}`);

	hubInput.listen(onInput);
