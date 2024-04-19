var express = require('express');
var app = express();

var http     = require('http').Server(app);
var io       = require('socket.io')(http);

var SerialPort = require('serialport').SerialPort;

var ReadlineParser = require('@serialport/parser-readline').ReadlineParser;

var parsers    = SerialPort.parsers;
//시리얼통신부분
var sp = new SerialPort( {

  path:'COM3',

  baudRate: 115200
});

const parser = sp.pipe(new ReadlineParser({ delimiter: '\r\n' }));

sp.on('open', () => console.log('Port open'));

parser.on('data', function (data) {
  var rcv = data.toString();
  if (rcv.substring(0, 1) == 'H') {
    var humi = parseInt(rcv.substring(1, 3)); // 습도 값을 숫자로 변환
    console.log('humidity: ' + humi);
    io.emit('humidity', humi);

  }
  if (rcv.substring(0, 1) == 'C') {
    var cds = parseInt(rcv.substring(1, 4)); // 습도 값을 숫자로 변환
    console.log('cds: ' + cds);
    io.emit('cds', cds);
  }
  /*if (rcv.substring(0, 3) == 'adc') {
    var adc = parseInt(rcv.substring(3)); // 습도 값을 숫자로 변환
    console.log('adc: ' + adc);
    io.emit('adc', adc);
  }*/
  if (rcv.substring(0, 1) == 'T') {
    var temp = parseInt(rcv.substring(1,3)); // 습도 값을 숫자로 변환
    console.log('temp: ' + temp);
    io.emit('temp', temp);
  }
});

app.use(express.static(__dirname + '/public'));

const port = 3000;
http.listen(port, function () {
  console.log('Server listening on http://localhost:' + port);
});

