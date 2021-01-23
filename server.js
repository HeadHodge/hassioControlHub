////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const os = require('os');
const ws = require('/root/node_modules/ws');
var server = new ws.Server({ port: 8080 });
var isCommandMode = false;
var tasks;

//##########################################
const performTask = function(controlWord) {
//##########################################
console.log(`Enter performTask with ${controlWord.symbol} in zone ${controlWord.zone}`);
var hubClient = require('/scripts/modules/hubClient.js');
var tasks = require('/scripts/modules/masterBedroom.js');

	hubClient.sendTask(tasks.wake);
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
  
////////////////////////////////////////////
//                MAIN
//Open server to listen for control input
////////////////////////////////////////////
console.log(`Started Server on ${os.hostname}`);

server.on('connection', function connection(client) {
	client.on('message', function incoming(message) {
		console.log(`received: ${message}`);
		decideAction(JSON.parse(message));
		client.send(`Got It`);
	});

});