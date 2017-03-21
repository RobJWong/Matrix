var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var spawn = require("child_process").spawn;
var sys   = require('sys');
//var JSONObject = require('gson');

// var spawn = require('child_process').spawn,
//     py    = spawn('python', ['test.py']),
//     data = [1,2,3,4,5,6,7,8,9],
//     dataString = '';

// Create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'));
app.get('/index.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index.html" );

})

app.post('/max_scholarship', urlencodedParser, function (req, res) {
   // Prepare output in JSON format
    // var size = Math.floor((Math.random() * 3) + 1)
    var size = 11 
    //console.log(size)
    var x = new Array(size);
    for (var i = 0; i < size; i++) {
        x[i] = new Array(size);
        for (var j = 0 ; j < size; j++ ){
            x[i][j] = Math.floor((Math.random() * 10));
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
        //res.end(JSON.stringify(data))
    });
    py.stdout.on('end', function(){
    console.log('Processed');
    });
    py.stdin.write(JSON.stringify(emptyObject));
    py.stdin.end();
    //var data = [1,2,3,4,5,6,7,8,9];
    //var dataString = '';
    //var py = spawn('python', ['test.py', emptyObject]);

    //var process = spawn('python',["test.py"]);
    //res.writeHead(200, {'Content-Type': 'application/json'});
    //process.stdout.on('data', function (data){
        // print(data)
    //    sys.print(data.toString());
    //    res.end(JSON.stringify(data))
    // Do something with the data returned from python script
    //});
    //console.log(emptyObject)
    // var process = spawn('python',["MatrixMain.py", emptyObject]);
    // process.stdout.on('data', function (data){
    //     res.writeHead(200, {'Content-Type': 'application/json'});
    //     res.end(JSON.stringify(data))
    // // Do something with the data returned from python script
    // });
    //console.log(process)
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)

})