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
    if (id === "") {
        res.redirect("/");
        console.log("insert to ID")
    }
    else {
        let result = connection.query('select * from user where userid=?', [id]);
        if (result[0].userid === id) {
            res.writeHead(200);
            var template = `
            <!DOCTYPE html>
            <html>

            <head>
                <meta charset="utf-8">
                <link href="mystyle.css" type="text/css" rel="stylesheet">
                <title>
                    Error
                </title>
            </head>

            <body>
                <div>
                    <h3 style="margin-left:30px">Register Failed</h3>
                    <h4 style="margin-left:30px">이미 존재하는 아이디입니다</h4>
                    
                    <a href="register.html" style="margin-left:30px">다시 시도하기</a>
                </div>
            </body>

            </html>
            `;
            res.end(template);
        } else {
            const result = connection.query("insert into user values (?,?)", [id, pw]);
            console.log(result);
            res.redirect('/');
        }
    }
})

module.exports = app;
