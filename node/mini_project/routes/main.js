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

    result = {
        "ok": "True",
        "data": [],
        "graph_urls": []
    }

    axios
        .get('http://192.168.1.15:3000/netflix-total'.concat("?title=", req.query.title))
        .then(response => {
            console.log(`statusCode : ${response.status}`)
            console.log(response.data)
            result["data"] = response.data
        })
        .catch(error => {
            console.log(error)
            result["ok"] = false
        })

    // axios
    //     .post('http://192.168.1.15:3000/total-graph')
    //     .then(response => {
    //         console.log(`statusCode : ${response.status}`)
    //         console.log(response.data)
    //         result["data"] = response.data
    //     })
    //     .catch(error => {
    //         console.log(error)
    //         result["ok"] = False
    //     })
    res.send(result)
})
app.get('/randomUUID', (req, res) => {
    axios
        .get('http://192.168.1.12:3000/randomUUID')
        .then(response => {
            console.log(`statusCode : ${response.status}`)
            console.log(response.data)
            res.send(response.data)
        })
        .catch(error => {
            console.log(error)
        })
})

app.get('/users', (req, res) => {
    axios
        .get('http://192.168.1.12:5000/users')
        .then(response => {
            console.log(`statusCode : ${response.status}`)
            console.log(response.data)
            res.send(response.data)
        })
        .catch(error => {
            console.log(error)
        })
})
// app.get('', (req, res) => {
//     axios
//         .get('http://192.168.1.15:3000/')
//         .then(reqponse => {

//         })
//         .catch(error => {
//             console.log(error)
//         })
// })

// app.post('', (req, res) => {
//     axios
//         .get('http://192.168.1.15:3000/')
//         .then(reqponse => {

//         })
//         .catch(error => {
//             console.log(error)
//         })
// })

// app.post('', (req, res) => {
//     axios
//         .get('http://192.168.1.15:3000/')
//         .then(reqponse => {

//         })
//         .catch(error => {
//             console.log(error)
//         })
// })

module.exports = app;