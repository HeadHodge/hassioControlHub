////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const ws = require('/root/node_modules/ws');
var server = null;
var inputCallback;

//##########################################
const onConnection = function(client) {
//##########################################
console.log(`Enter onConnection for client input`);

	client.on('message', function(message) {
		console.log(`received: ${message}`);
		client.send(`Got It`);
		inputCallback(message);
	});
};
  
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