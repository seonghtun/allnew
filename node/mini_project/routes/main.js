const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.get('/netflix', (req, res) => {
    res.sendFile('/allnew/node/mini_project/public/netflix.html')
})

app.get('/justone', (req, res) => {
    res.sendFile('/allnew/node/mini_project/public/analysis.html')
})

app.get('/netflix-total', (req, res) => {

    let result = {
        "ok": "True",
        "data": [],
        "graph_urls": []
    }
    // axios 가 보낼때는 json.stringify 해줘야된다. 문서보면 그렇게해야된다고
    // axios then 하면 이 API가 끝난다?
    Promise.all([axios.get('http://192.168.1.15:3000/col-drop'.concat('?collection=total')), axios.get('http://192.168.1.15:3000/netflix-total'.concat("?title=", req.query.title)),
    axios.post('http://192.168.1.15:3000/total-graph', {
        title: req.query.title,
        countries: ["Argentina", "Australia", "Costa Rica"]
    })])
        .then(response => {
            // console.log(`statusCode : ${response.status}`)
            // console.log(response[0])
            console.log(response[1].data)
            console.log(response[2].data.graph_urls)
            res.send({ "data": response[1].data.data, "graph_urls": response[2].data.graph_urls })
        })
        .catch(error => {
            console.log(error)
            result["ok"] = false
        })
})
app.post('/total-graph', (req, res) => {
    console.log(req.body)
    axios.post('http://192.168.1.15:3000/total-graph', {
        title: req.body.title,
        countries: req.body.countries
    })
        .then(response => {
            // console.log(`statusCode : ${response.status}`)
            // console.log(response.data)
            if (response.data.ok == false)
                res.send()
            else res.send(response.data.graph_urls)
        })
        .catch(error => {
            console.log(error)
        })
})

app.post('/netflix-month', (req, res) => {

    let result = {
        "ok": "True",
        "data": [],
        "graph_urls": []
    }
    // axios 가 보낼때는 json.stringify 해줘야된다. 문서보면 그렇게해야된다고
    // axios then 하면 이 API가 끝난다?
    Promise.all([axios.get('http://192.168.1.15:3000/col-drop'.concat('?collection=period')),
    axios.post('http://192.168.1.15:3000/netflix-month', {
        title: req.body.title,
        period_start: req.body.start,
        period_end: req.body.end
    }),
    axios.post('http://192.168.1.15:3000/month-graph', {
        title: req.body.title,
        countries: ["Argentina", "Australia", "Costa Rica"],
        period_start: req.body.start,
        period_end: req.body.end
    })])
        .then(response => {
            // console.log(`statusCode : ${response.status}`)
            // console.log(response[0])
            console.log(response[1].data.data)
            console.log(response[2].data.ok)
            if (response[1].data.ok == false) res.send({ "ok": -1 })
            else if (response[2].data.ok == false) res.send({ "ok": -2, "data": response[1].data.data })
            else res.send({ "ok": true, "data": response[1].data.data, "graph_urls": response[2].data.graph_urls })
        })
        .catch(error => {
            // console.log(error)
            result["ok"] = false
        })
})

app.post('/month-graph', (req, res) => {
    console.log(req.body)
    let result = {
        "ok": "True",
        "data": [],
        "graph_urls": []
    }
    // axios 가 보낼때는 json.stringify 해줘야된다. 문서보면 그렇게해야된다고
    // axios then 하면 이 API가 끝난다?

    axios.post('http://192.168.1.15:3000/month-graph', {
        title: req.body.title,
        countries: req.body.countries,
        period_start: req.body.start,
        period_end: req.body.end
    })
        .then(response => {
            // console.log(`statusCode : ${response.status}`)
            // console.log(response.data)
            if (response.data.ok == false)
                res.send({ "ok": false })
            else res.send(response.data.graph_urls)
        })
        .catch(error => {
            console.log(error)
        })
})

module.exports = app;