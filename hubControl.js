////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/scripts/modules/hubInput.js');
var tasks, clientOptions={};

//##########################################
const performTask = function(inputWord) {
//##########################################
console.log(`Enter performTask with ${inputWord.symbol} in zone ${inputWord.zone}`);
var hubOutput = require('/scripts/modules/hubOutput.js');
var tasks = require('/scripts/modules/masterBedroom.js');

	hubOutput.sendControlTask(tasks.wake);
};

//##########################################
const createCommand = function(inputWord) {
//##########################################
console.log(`Enter createCommand with ${inputWord.symbol} in zone ${inputWord.zone}`);

	inputWord.task = 'wake';
	isCommandMode = false;	
	return performTask(inputWord);
};
  
//##########################################
const decideAction = function(inputWord) {
//##########################################
console.log(`Enter decideAction with ${inputWord.symbol} in zone ${inputWord.zone}`);

	if(inputWord.symbol == 'Set') inputWord.isCommandMode = true;
	if(inputWord.isCommandMode) return createCommand(inputWord);
};
  
//##########################################
const onInput = function(client) {
//##########################################
clientOptions[client.controlWord.id] = require(`/scripts/modules/clients/${client.controlWord.id}.js`);
console.log(`Enter onInput, clientId: ${client.controlWord.id}, clientZone: ${clientOptions[client.controlWord.id].zone}`);
clientOptions[client.controlWord.id].zone = 'livingRoom';

	decideAction(client.controlWord);
};
		
////////////////////////////////////////////
//                MAIN
//Open server to listen for control input
////////////////////////////////////////////
console.log(`Started hubControl on ${os.hostname}`);

	hubInput.listen(onInput);
