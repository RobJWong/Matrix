var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var spawn = require("child_process").spawn;
var sys   = require('sys');
var urlencodedParser = bodyParser.urlencoded({ extended: false })
//basic libraries

app.use(express.static('public'));
app.get('/', function (req, res) {
   res.sendFile( __dirname + "/" );
})

//updates page showing the matrix sequence and total as requested from requirements
app.post('/max_scholarship', urlencodedParser, function (req, res) {
    var size = Math.floor(Math.random() * (1000 - 100) + 100);
    //creates a random size from 100-1000 for the nxn matrix
    var x = new Array(size);
    for (var i = 0; i < size; i++) {
        x[i] = new Array(size);
        for (var j = 0 ; j < size; j++ ){
            //randomly picks a number from 0-100 and assigns it to that matrix
            x[i][j] = Math.floor(Math.random() * (101));
        }
    }
    var emptyObject = {}
    emptyObject['data'] = []
    for (var p = 0; p < size; p++)
    {
        emptyObject['data'].push(x[p])
    }
    //make the JSON object to be sent to Python to calculate
    console.log(emptyObject)

    var py = spawn('python', ['MatrixMain.py']);
    py.stdout.on('data', function(data){
        //when data comes back from the python script, it displays onto the web page
        sys.print(data.toString());
        res.writeHead(200, {'Content-Type': 'application/json; charset=utf-8'});
        res.end(data.toString())
    });
    py.stdout.on('end', function(){
    console.log('Processed');
    });
    py.stdout.on('error', function(data){
        //error catching
        console.log("Error with Python")
    })
    //writes results to node.js command prompt
    py.stdin.write(JSON.stringify(emptyObject));
    py.stdin.end();
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log('Server running at http://127.0.0.1:8081/');
})