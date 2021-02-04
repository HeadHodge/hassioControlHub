////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const ws = require('/root/node_modules/ws');
var server = null;
var callBack;

//##########################################
const onInput = function(connection, input, callBack) {
//##########################################
try {
	console.log(`==================================================================================================`);
	console.log(`= Enter onInput with client input: ${input}`);
	console.log(`==================================================================================================`);

	connection.input = JSON.parse(input);
	if(callBack) return callBack(connection);
	//throw `Invalid input type: ${connection.controlInput.type}`;
}
catch (error) {
	console.log(`Invalid Messag: ${error}`);
	connection.send(`Invalid Messag: ${error}`);
}};
  
//##########################################
const listen = function(callBack) {
//##########################################
console.log(`Enter listen for client connections`);

	//callBack = callBack;
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
console.log(`Started hubInput`);
exports.getInput = listen;