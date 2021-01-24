////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/scripts/modules/hubInput.js');
var tasks, clientOptions={}, zoneOptions={}, focusOptions={};

//##########################################
const sendTask = function(command) {
//##########################################
console.log(`Enter sendTask for command: ${command}`);
var hubOutput = require('/scripts/modules/hubOutput.js');
var tasks = require('/scripts/modules/masterBedroom.js');
var task;

	focusOptions = require(`/scripts/modules/focus/masterBedroom.up.js`);
	task = `{"action": "runSequence", "sequence": ${JSON.stringify(focusOptions.tasks[command])}}`;
	console.log(`Send Task: ${task}`);
	hubOutput.sendControlTask(task);
	//$case.postCommand({"action": "runSequence", "sequence": [{"remote/send_command": {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}, {"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}}]});
};

//##########################################
const createCommand = function(inputWord) {
//##########################################
console.log(`Enter createCommand with ${inputWord.symbol} in zone ${inputWord.zone}`);

	inputWord.task = 'wake';
	isCommandMode = false;	
	return sendTask(inputWord);
};
  
//##########################################
const onInput = function(client) {
//##########################################
clientOptions[client.controlInput.id] = require(`/scripts/modules/clients/${client.controlInput.id}.js`);
console.log(`Enter onInput, clientId: ${client.controlInput.id}, clientZone: ${clientOptions[client.controlInput.id].zone}`);

	if(client.controlInput.command == 'Set') client.controlInput.isCommandMode = true;
	if(client.controlInput.isCommandMode) return createCommand(client.controlInput);
	sendTask(client.controlInput.command);
};
		
////////////////////////////////////////////
//                MAIN
//Open server to listen for control input
////////////////////////////////////////////
console.log(`Started hubControl on ${os.hostname}`);

	hubInput.listen(onInput);
