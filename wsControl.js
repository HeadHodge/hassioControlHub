////////////////////////////////////////////
//            GLOBAL VARIABLES
////////////////////////////////////////////
//api/websock'
//var W3CWebSocket = require('/root/node_modules/websocket').w3cwebsocket;
var mqtt = require('/root/node_modules/mqtt')
//var client  = mqtt.connect('mqtt://test.mosquitto.org')
var client  = mqtt.connect('mqtt://192.168.0.160:1883', {username:"admin", password:"pepper"})

client.on('connect', function () {
  client.subscribe('presence', function (err) {
    if (!err) {
      client.publish('presence', 'Hello mqtt')
    }
  })
})
 
client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  client.end()
})

client.on("error",function(error) {
  console.log(error.toString())
  client.end()
})