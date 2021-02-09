////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const http = require('http');
const debug = require('/controlHub/core/debugLog.js').debug;

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
debug.log(`Enter onReply, statusCode: ${reply.statusCode}`);
var buffer = '';

	reply.on('data', function(reply) {
		console.log('Task server reply: ' + reply);
		console.log(`==================================================================================================`);
		buffer += reply;
	});

	reply.on('end', function () {
		//console.log(buffer);
	});
};

//##########################################
const sendTask = function(task) {
//##########################################
debug.log(`Enter sendTask`);
var request = http.request(options, onReply);	

	request.on('error', function (error) {
		console.error(`Encountered an error trying to make a request: ${error.message}`);
	});

	console.log(`\x20\n${task}\n\x20`);
	request.write(task);
	request.end();
};

////////////////////////////////////////////
//                MAIN
//Open connection with Hub and send request
////////////////////////////////////////////
console.log('Loaded hubOutput.js');

	exports.sendTask = sendTask;