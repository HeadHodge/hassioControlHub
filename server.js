//var WebSocketServer = require('/root/node_modules/websocket').server;
const WebSocket = require('/root/node_modules/ws')
const http = require('http');
///////////////////////////////////////////////////////
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

const request = http.request(options, (res) => {
  if (res.statusCode !== 201) {
    console.error(`Did not get a Created from the server. Code: ${res.statusCode}`);
    res.resume();
    return;
  }

  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
    console.log('Data chunk: '+chunk);
  });

  res.on('close', () => {
    console.log('Added new user');
    console.log(JSON.parse(data));
  });
});

const requestData = {
  name: 'New User',
  username: 'digitalocean',
  email: 'user@digitalocean.com',
  address: {
    street: 'North Pole',
    city: 'Murmansk',
    zipcode: '12345-6789',
  },
  phone: '555-1212',
  website: 'digitalocean.com',
  company: {
    name: 'DigitalOcean',
    catchPhrase: 'Welcome to the developer cloud',
    bs: 'cloud scale security'
  }
};

const requestString = '{"action": "runSequence", "reference": "media-streaming-masterbedroom", "sequence": [{"remote/send_command": {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}, {"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}}]}';
request.write(requestString);
//request.write(JSON.stringify(requestData));
request.end();

request.on('error', (err) => {
  console.error(`Encountered an error trying to make a request: ${err.message}`);
});

/////////////////////////////////////////////////////
const wss = new WebSocket.Server({ port: 8080 })

wss.on('connection', ws => {
  ws.on('message', message => {
    console.log(`Received message => ${message}`)
  })
  ws.send('ho!')
})