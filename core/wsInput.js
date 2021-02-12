////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const debug = require('/controlHub/core/debugLog.js').debug;
const ws = require('/root/node_modules/ws');

var server = null;

//##########################################
const onMessage = function(message) {
//##########################################
try {
	console.log(`\x20\n\x20`);
	console.log(`==================================================================================================`);
	console.log(`Enter onMessage from ws client:\n${message}`);
	global.onInput(JSON.parse(message));
}
catch (error) {
	console.log(`Invalid Messag: ${error}`);
}};
  
//##########################################
const onConnect = function(connection) {
//##########################################
debug.log(`Enter onConnect`);
		
	console.log(` \n`);
	console.log(`===================================================`);
	console.log(`= WebSocket Client Connected, waiting for input`);
	console.log(`===================================================`);
		
	connection.on('message', onMessage);
};

////////////////////////////////////////////
//                MAIN
//Open server to listen for control clients
////////////////////////////////////////////
console.log(`Loaded wsInput.js`);

	server = new ws.Server({port: 8080});
	server.on('connection', onConnect);
