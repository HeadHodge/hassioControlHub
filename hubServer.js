var fs = require('fs');
var http = require('http');
var host, path;

http.createServer(function (req, res) {

	if(req.url == '/webRemote') 
		{host = __dirname + req.url; path = host+'/homePage.htm';}
	else if(req.url == '/webRemote/') 
		{host = __dirname; path = host+'/webRemote/homePage.htm';}
	else
		path = host + req.url;	
	
	fs.readFile(path, function (err,data) {
		if (err) {
			res.writeHead(404);
			res.end(`Abort: Invalid Path Specified.\nUrl: ${req.url}, Host: ${host}, Path: ${path}\nError: ${JSON.stringify(err)}`);
			return;
		};
		
		res.writeHead(200);
		res.end(data);
  });
  
}).listen(80);