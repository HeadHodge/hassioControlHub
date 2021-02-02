////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const ws = require('/root/node_modules/ws');
var server = null;
var onInput;

//##########################################
const sendReply = function(reply) {
//##########################################
try {
console.log(`\n\n\n\nEnter sendReply: ${reply}`);

	connection.on('message', function(message) {
	console.log(`received: ${message}`);

		connection.controlInput = JSON.parse(message);
		connection.send(`Got It`);
		if(connection.controlInput.type == 'command') return commandCallback(connection.controlInput);
		if(connection.controlInput.type == 'fileName') return fileNameCallback(connection.controlInput);
		throw `Invalid input type: ${connection.controlInput.type}`;
	});
}
catch (error) {
	console.log(`Invalid Messag: ${error}`);
	connection.send(`Invalid Messag: ${error}`);
}};
//##########################################
const onConnection = function(connection) {
//##########################################
try {
console.log(`\n\n\n\nEnter onConnection waiting for client input`);

	connection.on('message', function(input) {
	console.log(`received client input: ${input}`);

		connection.input = JSON.parse(input);
		//connection.send(`Got It`);
		//if(connection.controlInput.type == 'command') return commandCallback(connection);
		if(onInput) return onInput(connection);
		//throw `Invalid input type: ${connection.controlInput.type}`;
	});
}
catch (error) {
	console.log(`Invalid Messag: ${error}`);
	connection.send(`Invalid Messag: ${error}`);
}};
  
//##########################################
const listen = function(callBack) {
//##########################################
console.log(`Enter listen for client commands`);

	onInput = callBack;
	if(server) return console.log('hubServer already running;');
	server = new ws.Server({ port: 8080 });
	server.on('connection', onConnection);
};

////////////////////////////////////////////
//                MAIN
//Open server to listen for control clients
////////////////////////////////////////////
console.log(`Started hubInput`);
exports.getInput = listen;