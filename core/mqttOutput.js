////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
const debug = require('/controlHub/core/debugLog.js').debug;
const mqtt = require('/root/node_modules/mqtt')
const brokerUrl = 'mqtt://192.168.0.160:1883'; //test broker: 'mqtt://test.mosquitto.org'
const brokerOptions = {
	username:"admin", 
	password:"pepper"
};

var broker = null;

//##########################################
const connectBroker = function(task) {
//##########################################
console.log(`Enter connectBroker`);

	if(broker) broker.end(); //Close existing broker
	broker = mqtt.connect(brokerUrl, brokerOptions);

	broker.on('connect', function() {
		console.log(`Enter broker connected`);
		if(task) sendTask(task);
	});
 
	broker.on('message', function(topic, message) {
		console.log(`Enter broker replied, topic: ${topic}, message: ${message}`);
		console.log(message.toString());
	});

	broker.on("error", function(error) {
		console.log(`Enter broker failed: ${error.toString()}`);
		if(broker) broker.end();
		broker = null;
	});	

	broker.on("close", function() {
		console.log(`Enter broker closed`);
		broker = null;
	});	
};

//##########################################
const sendTask = function(task) {
//##########################################
console.log(`Enter sendTask`);

	if(!broker) connectBroker(task);
	broker.publish('taskInput', task);
};

////////////////////////////////////////////
//                MAIN
//Open connection with Hub and send request
////////////////////////////////////////////
console.log('Loaded mqttOutput.js');

	exports.sendTask = sendTask;
