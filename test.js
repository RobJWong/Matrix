var spawn = require('child_process').spawn,
    py    = spawn('python', ['test.py']),
    data1 = [1,2,3,4,5,6,7,8,9],
    dataString = '';

py.stdout.on('data', function(data){
  dataString += data.toString();
});
py.stdout.on('end', function(){
  console.log('Sum of numbers=',dataString);
});
py.stdin.write(JSON.stringify(data1));
py.stdin.end();