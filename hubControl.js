////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const hubInput = require('/scripts/modules/hubInput.js');
var isCommandMode = false;
var tasks;

//##########################################
const performTask = function(controlWord) {
//##########################################
console.log(`Enter performTask with ${controlWord.symbol} in zone ${controlWord.zone}`);
var hubOutput = require('/scripts/modules/hubOutput.js');
var tasks = require('/scripts/modules/masterBedroom.js');

	hubOutput.sendControlTask(tasks.wake);
};

//##########################################
const createCommand = function(controlWord) {
//##########################################
console.log(`Enter createCommand with ${controlWord.symbol} in zone ${controlWord.zone}`);

	controlWord.task = 'wake';
	isCommandMode = false;	
	return performTask(controlWord);
};
  
//##########################################
const decideAction = function(controlWord) {
//##########################################
console.log(`Enter decideAction with ${controlWord.symbol} in zone ${controlWord.zone}`);

	if(controlWord.symbol == 'Set') isCommandMode = true;
	if(isCommandMode) return createCommand(controlWord);
};
  
//##########################################
const onInput = function(controlMsg) {
//##########################################
console.log(`onInput: ${controlMsg}`);

	decideAction(JSON.parse(controlMsg));
};
		
////////////////////////////////////////////
//                MAIN
//Open server to listen for control input
////////////////////////////////////////////
console.log(`Started hubControl on ${os.hostname}`);

	hubInput.listen(onInput);
/*	
const ws = require('/root/node_modules/ws');
var server = new ws.Server({ port: 8080 });

server.on('connection', function connection(client) {
	client.on('message', function incoming(message) {
		console.log(`received: ${message}`);
		decideAction(JSON.parse(message));
		client.send(`Got It`);
	});

});
*/