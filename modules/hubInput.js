////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const ws = require('/root/node_modules/ws');
var server = null;
var inputCallback;

//##########################################
const onConnection = function(connection) {
//##########################################
try {
console.log(`\n\n\n\nEnter onConnection for client input`);

	connection.on('message', function(message) {
	console.log(`received: ${message}`);

		connection.controlInput = JSON.parse(message);
		if(connection.controlInput.type != 'hubControl') throw `Invalid input type: ${connection.controlInput.type}`;
		connection.send(`Got It`);
		inputCallback(connection);
	});
}
catch (error) {
	console.log(`Invalid Messag: ${error}`);
	client.send(`Invalid Messag: ${error}`);
}};
  
//##########################################
const listen = function(onInput) {
//##########################################
console.log(`Enter listen for client commands`);

	if(server) return console.log('Error: hubServer already running;');
	inputCallback = onInput;
	server = new ws.Server({ port: 8080 });
	server.on('connection', onConnection);
};

////////////////////////////////////////////
//                MAIN
//Open server to listen for control clients
////////////////////////////////////////////
exports.listen = listen;