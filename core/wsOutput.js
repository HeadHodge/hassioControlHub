////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const debug = require('/controlHub/core/debugLog.js').debug;
const webSocket = require('/root/node_modules/ws');

var client = null, isConnected = null, messageId = 1;

//##########################################
onOpen =  function() {
//##########################################
console.log('Enter onOpen');
  //ws.send(Date.now());
};

//##########################################
onClose =  function() {
//##########################################
console.log('Enter onClose');

	createClient();
};

//##########################################
onMessage = function(message) {
//##########################################
console.log(`Enter onMessage: Received server message`);
var payload = JSON.parse(message);

	if(payload.type == 'auth_required') return client.send('{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1YmM0ZGYxNGY4ZGE0MTdkYTNhZjdkNjkwYzg0NDQ2ZSIsImlhdCI6MTYxMzAxMDQ4MiwiZXhwIjoxOTI4MzcwNDgyfQ.MffxNYX4VssITLgdZBPilKTq3p4R9RuoQP2yeeoyyPw"}');
	if(payload.type == 'auth_ok') return isConnected = true;
	if(payload.type == 'result') return console.log(`Server result: messageId: ${payload.id}, status: ${payload.success}`);
};

//##########################################
createClient = function() {
//##########################################
console.log(`Enter createClient`);

	isConnected = false;
	if(client) client.close();
	client = new webSocket('ws://192.168.0.160:8123/api/websocket', {});
	client.on('open', onOpen);
	client.on('close', onClose);
	client.on('message', onMessage);
};

//##########################################
runTask = function(input) {
//##########################################
console.log(`Enter runTask`);
var task = JSON.parse(input);
var service, key, command, payload={"id": messageId, "type": "call_service"};

	if(!isConnected) return console.log(`Abort runTask: client not connected to server`);
	if(task.length == 0) return console.log(`runTask Completed`);

	service = task[0];
	key = Object.keys(service)[0];
	command = key.split('/');
	if(command.length == 1) return console.log(`Abort runService: ignore command: `, command);

	payload.domain = command[0];
	payload.service = command[1];
	payload.service_data = service[key];
	console.log(`Send payload, domain: ${payload.domain}, service: ${payload.service}`);
	
	++messageId;
	client.send(JSON.stringify(payload));
		
	task.shift();
	return runTask(JSON.stringify(task));
};

////////////////////////////////////////////
//                MAIN
//Open connection with Hub and send request
////////////////////////////////////////////
console.log('Loaded wsOutput.js');

	exports.runTask = runTask;
	createClient();	
/*
	setTimeout(function timeout() {
		ws.send(Date.now());
	}, 500);
*/