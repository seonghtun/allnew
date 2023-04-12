const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });


var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
})

const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// request 1, query 0

app.post('/login', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query('select * from user where userid=? and passwd=?', [id, pw]);
    // if (result.length === 0) {
    //     res.sendFile('/allnew/node/member/public/error.html');
    // }
    // if (result.affectedRows > 0) {
    //     console.log(result);
    //     if (id === 'root' || id === 'admin') {
    //         res.sendFile('/allnew/node/member/public/member.html');
    //     } else {
    //         res.sendFile('/allnew/node/member/public/main.html');
    //     }

    // }
    // else {
    //     res.sendFile('/allnew/node/member/public/error.html');
    // }
    if (result.length === 0) {
        res.redirect('error.html');
    }
    else {
        console.log(result);
        if (id === 'root' || id === 'admin') {
            res.redirect('member.html');
        } else {
            res.redirect('main.html');
        }
    }
})

app.post('/register', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("insert into user values (?,?)", [id, pw]);
    console.log(result);
    res.redirect('/');
})

module.exports = app;
