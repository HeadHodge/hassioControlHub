var fs = require('fs');
var http = require('http');
var host, path;

http.createServer(function (req, res) {

	if(req.url == '/html') 
		{host = __dirname ; path = host+'/homePage.htm';}
	else if(req.url == '/html/') 
		{host = __dirname; path = host+'/html/homePage.htm';}
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