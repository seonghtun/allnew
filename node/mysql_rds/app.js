var express = require('express');
var mysql = require('mysql');
const env = require('dotenv').config({ path: ".env" });

var connection = mysql.createConnection({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

var app = express();

connection.connect(function (err) {
    if (!err) {
        console.log("Database is connected.............\n\n");
    } else {
        console.log(err);
        console.log("Error connecting Database......\n\n ");
    }
});

app.get('/', function (rep, res) {
    connection.query('select * from st_info', function (err, rows, fields) {
        if (!err) {
            console.log(rows)
            var template=`
                <table border=1 style="border: 1px solid #444444;
    border-collapse: collapse; margin:auto; text-align:center; font-size: 20px;
    font-family: Sans-serif;">
                    <tr>
                        <th> ID </th>
                        <th> NAME </th>
                        <th> DEPT </th>
                    <tr>
            `
            rows.forEach((row) => {
                template += `
                    <tr>
                        <td> ${row.ST_ID} </td>
                        <td> ${row.NAME} </td>
                        <td> ${row.DEPT} </td>
                    </tr>
                `
            })
            template += '</table>'
            console.log('The solution is : ', rows);
            res.send(template);
        } else {
            console.log('Error while performing Query');
        }
    });
});

app.listen(8000, function () {
    console.log('8000 Port : Server Started...');
})