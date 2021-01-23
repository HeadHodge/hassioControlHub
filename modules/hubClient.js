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
    'Content-Type': 'application/json; charset=UTF-8'
  }
};

//##########################################
const getReply = function(reply) {
//##########################################
console.log(`Enter getReply, statusCode: ${reply.statusCode}`);
var buffer = '';

	reply.on('data', function (chunk) {
		buffer += chunk;
	});

	reply.on('end', function () {
		console.log(buffer);
	});
};

//##########################################
const sendTask = function(task) {
//##########################################
console.log(`Enter sendTask: ${task}`);
var request = http.request(options, getReply);	

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
	console.log('hubClient loaded');
	exports.sendTask = sendTask;