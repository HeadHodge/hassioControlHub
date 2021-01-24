////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const http = require('http');
const options = {
  host: '192.168.0.160',
  port: 5050,
  path: '/api/appdaemon/ipRemoteCommand',
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/text; charset=UTF-8'
  }
};

//##########################################
const onReply = function(reply) {
//##########################################
console.log(`Enter onReply, statusCode: ${reply.statusCode}`);
var buffer = '';

	reply.on('data', function(chunk) {
		console.log('chunk: ' + chunk);
		buffer += chunk;
	});

	reply.on('end', function () {
		//console.log(buffer);
	});
};

//##########################################
const sendControlTask = function(task) {
//##########################################
console.log(`Enter sendControlTask: ${task}`);
var request = http.request(options, onReply);	

	request.on('error', function (error) {
		console.error(`Encountered an error trying to make a request: ${error.message}`);
	});

	request.write(task);
	request.end();
};

////////////////////////////////////////////
//                MAIN
//Open connection with Hub and send request
////////////////////////////////////////////
	console.log('hubOutpt loaded');
	exports.sendControlTask = sendControlTask;