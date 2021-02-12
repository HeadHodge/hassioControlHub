////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const debug = require('/controlHub/core/debugLog.js').debug;
const webSocket = require('/root/node_modules/ws');

var client = null, isConnected = null;

//##########################################
onOpen =  function() {
//##########################################
console.log('Enter client.open');
  //ws.send(Date.now());
};

//##########################################
onClose =  function() {
//##########################################
console.log('Enter client.close');

	createClient();
};

//##########################################
onMessage = function(message) {
//##########################################
console.log(`Enter client.message: ${message}`);
var payload = JSON.parse(message);

	if(payload.type == 'auth_required') return client.send('{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1YmM0ZGYxNGY4ZGE0MTdkYTNhZjdkNjkwYzg0NDQ2ZSIsImlhdCI6MTYxMzAxMDQ4MiwiZXhwIjoxOTI4MzcwNDgyfQ.MffxNYX4VssITLgdZBPilKTq3p4R9RuoQP2yeeoyyPw"}');
	if(payload.type == 'auth_ok') isConnected = true;
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
runService = function(service={}) {
//##########################################
console.log(`Enter runService, service: `, service);
var command;

	if(service.length == 0) return console.log(`Abort runService: invalid service`);
	command = Object.keys(service)[0].split('/');
	console.log(`Domain: ${command[0]}, Action: ${command[1]}`);
};

//##########################################
runTask = function(task=[]) {
//##########################################
console.log(`Enter runTask, contains ${task.length} services`);

	if(task.length == 0) return console.log(`runTask Completed`);
	if(!isConnected) return console.log(`Abort runTask: client not connected to server`);
	
	runService(task[0]);
	task.shift();
	return runTask(task);
	
	task = {
		"id": 24,
		"type": "call_service",
		"domain": "androidtv",
		"service": "adb_command",
		"service_data": {
			"entity_id": "media_player.firetv_livingroom",
			"command": "HOME"
		}
	};		
		
	//client.send(JSON.stringify(task));
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