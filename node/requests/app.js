const express = require('express');
const request = require('request');
const CircularJSON = require('circular-json');
const app = express();

let option = "http://192.168.1.158:8000/Hello"

// hostname: '192.168.1.76',
// port: 8000,
// path: '/Hello',
// method: 'GET'
app.get('/', (req, res) => {
    res.send("Web Server Started.....");
})

app.get('/Hello', (req, res) => {
    res.send("Hello World - Yoon");
})

app.post('/todos', (req, res) => {
    console.log(req.body)
    res.send(req.body);
})

app.get("/rhello", function (req, res) {
    request(option, { json: true }, (err, result, body) => {
        if (err) { return console.log(err) }
        res.send(CircularJSON.stringify(body));
    });

    // const req = https.request(option, res => {
    //     console.log(`statusCode : ${res.statusCode}`);
    //     res.on('data', d => {
    //         process.stdout.write(d);
    //     })
    // });
})

const data = JSON.stringify({ todo: 'Buy the milk - Yoon' });
app.get("/data", function (req, res) {
    res.send(data);
});

option = "http://192.168.1.76:8000/data"
// r이 붙은건 자기꺼
app.get("/rdata", (req, res) => {
    request(option, { json: true }, (err, result, body) => {
        if (err) return console.log(err)
        res.send(CircularJSON.stringify(body));
    })
})

app.listen(8000, function () {
    console.log('8000 Port : Server Started....');
})

module.exports = app;