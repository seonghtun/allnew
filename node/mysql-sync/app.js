var mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

let result = connection.query('select * from st_info');
console.log(result);

//make insert data
let data = {
    st_id: "202345",
    name: "Moon",
    dept: "Computer"
}

// async 랑 다른 방식이라 몇번이든 만들수 있다.
// inserted data 

// inserted data's id
let insertId = data.st_id;

// insert query
// result = connection.query("insert into st_info values (?,?,?)", [insertId, data.name, data.dept]);

// select query for inserted data
result = connection.query(`select * from st_info where st_id=${insertId}`);
console.log(result);

// update query
result = connection.query("update st_info set dept = ? where st_id = ? ", ["Game", insertId]);
console.log("data is Updated~!!");

// select query for updated data
result = connection.query("select * from st_info where st_id = ?", [insertId]);
console.log(result);

// delete row
result = connection.query(`delete from st_info where st_id = ${insertId}`);
console.log(result);

// select query all data
result = connection.query("select * from st_info");
console.log(result);