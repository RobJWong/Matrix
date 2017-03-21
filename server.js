var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var spawn = require("child_process").spawn;
var sys   = require('sys');
var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'));
app.get('/', function (req, res) {
   res.sendFile( __dirname + "/" );

})

app.post('/max_scholarship', urlencodedParser, function (req, res) {
    var size = Math.floor(Math.random() * (1000 - 100) + 100);
    var x = new Array(size);
    for (var i = 0; i < size; i++) {
        x[i] = new Array(size);
        for (var j = 0 ; j < size; j++ ){
            x[i][j] = Math.floor(Math.random() * (101));
        }
    }
    var emptyObject = {}
    emptyObject['data'] = []
    for (var p = 0; p < size; p++)
    {
        emptyObject['data'].push(x[p])
    }
    console.log(emptyObject)

    var py = spawn('python', ['MatrixMain.py']);
    py.stdout.on('data', function(data){
        sys.print(data.toString());
        res.writeHead(200, {'Content-Type': 'application/json; charset=utf-8'});
        res.end(data.toString())
    });
    py.stdout.on('end', function(){
    console.log('Processed');
    });
    py.stdin.write(JSON.stringify(emptyObject));
    py.stdin.end();
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)

})