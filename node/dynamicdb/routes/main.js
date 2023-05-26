const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });
const request = require('request');

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

function template_nodata(res) {
    res.writeHead(200);
    let template = `<!DOCTYPE html>
    <html>
        <head>
            <title>Result</title>
            <link type="text/css" rel="stylesheet" href="dynamic.css">
            <meta charset="utf-8">
        </head>
        <body>
            <h3>데이터가 존재하지 않습니다.</h3>
        </body>
    </html>
    `;
    res.end(template);
}

function template_result(result, res) {
    res.writeHead(200);
    let template = `<!DOCTYPE html>
    <html>
        <head>
            <title>Result</title>
            <link type="text/css" rel="stylesheet" href="dynamic.css">
            <meta charset="utf-8">
        </head>
        <body>
        <table style="margin:auto">
            <thead>
                <tr><th>USERID</th><th>PASSWORD</th></tr>
            </thead>
            <tbody>`;
    for (var i = 0; i < result.length; i++) {
        template += `
        <tr><td>${result[i]['userid']}</td><td>${result[i].passwd}</td>
    `;
    }
    template += `
            </tbody>
        </table>
    </body>
    </html>
    `;
    res.end(template);
}


app.get('/select', (req, res) => {
    const result = connection.query('select * from user');
    console.log(result);
    if (result.length === 0) {
        template_nodata(res);
    } else {
        template_result(result, res);
    }
})

app.post('/test', (req, res) => {
    let result = req.body
    console.log(result)
    request({
        uri: 'http://192.168.1.3:3000/contents_country_graph',
        method: "POST",
        body: {
            countries: result['countries']
        },
        json: true,
        function(error, response, body) {
            console.error('error', error);
            console.log('stausCode :', response && response.statusCode);
            console.log('body :', body);
        }
    })
})
// 비동기함수로 만들어야 보내고 바로 끊긴다. 안하면 response 기다리고있는거다
// 비동기 
// sync 굳이 종료를 어플리케이션 이 종료되는 순간에 종료가 된다
// async 어플리케이션 종료되는 순간이 아니게 할려는거니 연결 종료를 해줘야된다.
// 기본적으로 함수 자체도 비동기 함수로 쓰게 
// 서버 자체가 비동기 란 뜻이지 함수 자체가 비동기란 뜻은 아니다. 비동기로 쓴다는건 함수자체도 비동기로 하겠다는 뜻이다.

app.get('/selectQuery', (req, res) => {
    // const { id , password } = req.query;
    const id = req.query.id;
    if (id === "") {
        res.write("<script>alert('User-id를 입력하세요.')</script>");
    }
    else {
        // const result = connection.query(`select * from user where id = ${id}`);
        const result = connection.query("select * from user where userid=?", [id]);
        if (result.length === 0) {
            template_nodata(res);
        } else {
            template_result(result, res);
        }
    }
})

/*
app.post('/selectQuery', (req, res) => {
    // const { id , password } = req.query;
    const id = req.body.id;
    if (id === "") {
        res.end(`ID 를 입력해주세요!`)
    } else {
        // const result = connection.query(`select * from user where id = ${id}`);
        const result = connection.query("select * from user where userid=?", [id]);
        res.writeHead(200);
        if (result.length === 0) {
            template_nodata(res);
        } else {
            template_result(result, res);
        }
    }
})
*/

app.post('/insert', (req, res) => {
    const { id, pw } = req.body;
    if (id === "" && pw === "") {
        res.write("<script>alert('User-id와 Password를 입력해주세요.')</script>");
    }
    else if (id === "") {
        res.write("<script>alert('User-id를 입력하세요.')</script>");
    }
    else if (pw === "") {
        res.write("<script>alert('Password 를 입력하세요.')</script>");
    }
    else {
        let result = connection.query("select * from user where userid=?", [id]);
        if (result.length > 0) {
            let template = `
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Error</title>
                    <meta charset="utf-8">
                </head>
                <body>
                    <div>
                        <h3 style="margin-left : 30px">Register Failed</h3>
                        <h4 style="margin-left : 30px">이미 존재하는 아이디입니다.</h4>
                    </div>
                </body>
                </html>
            `;
            res.end(template);
        } else {
            result = connection.query("insert into user values (?,?)", [id, pw]);
            console.log(result);
            res.redirect('/selectQuery?id=' + id);
        }
    }
})

app.post('/update', (req, res) => {
    const { id, pw } = req.body;
    if (id === "" && pw === "") {
        res.write("<script>alert('User-id와 Password를 입력해주세요.')</script>");
    }
    else if (id === "") {
        res.write("<script>alert('User-id를 입력하세요.')</script>");
    }
    else if (pw === "") {
        res.write("<script>alert('Password를 입력하세요.')</script>");
    }
    else {
        result = connection.query("update user set passwd=? where userid=?", [pw, id]);
        console.log(result);
        res.redirect('/selectQuery?id=' + id);
    }
})

app.post('/delete', (req, res) => {
    const id = req.body.id;
    if (id === "") {
        res.write("<script>alert('User-id를 입력하세요.')</script>");
    } else {
        let result = connection.query("select * from user where userid=?", [id]);

        if (result.length === 0) {
            template_nodata(res);
        } else {
            result = connection.query("delete from user where userid=?", [id]);
            console.log(result);
            res.redirect('/select');
        }
    }
})

app.post('/login', (req, res) => {
    const { id, pw } = req.body;
    if (id === "" && pw === "") {
        res.write("<script>alert('User-id를 입력하세요.')</script>");
        // res.redirect('/login-page');
    }
    else if (id === "") {
        sss
        // res.send("ID를 입력해주세요.");
        res.write("<script>alert('User-id를 입력하세요.')</script>");
        // res.write("<script>alert('User-id를 입력하세요.')</script>");
    }
    else if (pw === "") {
        // res.send("Password를 입력해주세요.");
        res.write("<script>alert('User-id를 입력하세요.')</script>");
        // res.write("<script>alert('Password를 입력하세요.')</script>");
    }
    else {
        const result = connection.query('select * from user where userid=? and passwd=?', [id, pw]);
        if (result.length === 0) {
            res.redirect('error.html');
        }
        else {
            console.log(result);
            if (id === 'root' || id === 'admin') {
                console.log(id + " => Administrator Logined");
                res.redirect('admin.html?id=' + id);
            } else {
                console.log(id + " => User Logined");
                res.redirect('user.html?id=' + id);
            }
        }
    }
})

app.get('/login-page', (req, res) => {
    res.sendFile('/allnew/node/dynamicdb/public/login.html');
})

app.post('/register', (req, res) => {
    const { id, pw } = req.body;
    if (id === "") {
        res.redirect("/register.html");
        console.log("insert to ID")
    }
    else {
        let result = connection.query('select * from user where userid=?', [id]);
        console.log("result :", result);
        if (result.length > 0) {
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
            res.redirect('/login-page');
        }
    }
})



module.exports = app;