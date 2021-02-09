////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const debug = require('/controlHub/core/debugLog.js').debug;
const fs = require('fs');
const http = require('http');
const ws = require('/root/node_modules/ws');

var server = null;
var basePath = '/controlHub/html';
//var basePath = __dirname + '/html';

//##########################################
const listenHTTP = function(request, reply) {
//##########################################
console.log(`Enter listenHTTP`);
try {
	fs.readFile(basePath+request.url, function(error, data) {
		if(error) {
			console.log(error);
			reply.writeHead(404);
			reply.end(JSON.stringify(error));
		};
		
		reply.writeHead(200);
		reply.end(data);
	});
} catch (error) {
	console.log(`Abort listenHTTP: ${error}`);
} finally {
	return;
}};

//##########################################
const onInput = function(connection, input, callBack) {
//##########################################
try {
	console.log(`\x20\n\x20`);
	console.log(`==================================================================================================`);
	console.log(`Enter onInput with client input:\n${input}`);

	connection.input = JSON.parse(input);
	if(callBack) return callBack(connection);
	//throw `Invalid input type: ${connection.controlInput.type}`;
}
catch (error) {
	console.log(`Invalid Messag: ${error}`);
	connection.send(`Invalid Messag: ${error}`);
}};
  
//##########################################
const listenWS = function(callBack) {
//##########################################
debug.log(`Enter listenWS for client connections`);

	if(server) return console.log('hubServer already running;');
	server = new ws.Server({ port: 8080 });
	
	server.on('connection', function(connection){
		console.log(`=============================================`);
		console.log(`= Client Connected, waiting for input`);
		console.log(`=============================================`);
		
		connection.on('message', function(message){
			onInput(connection, message, callBack);
		});
	});
};

////////////////////////////////////////////
//                MAIN
//Open server to listen for control clients
////////////////////////////////////////////
console.log(`Loaded hubInput.js`);
var httpServer = http.createServer(listenHTTP);
	
	exports.getInput = listenWS;
	httpServer.listen(80);
