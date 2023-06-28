const express = require('express');
const bodyParser = require('body-parser');

const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const users = [
        {id:1, name:"User1"},
        {id:2, name:"User2"},
        {id:3, name:"User3"},
        {id:4, name:"User4"},
        {id:5, name:"User5"}
]


app.get('/hello', (req, res) => {
    res.send("Hello World~!!\n");
})


// request X , response O
app.get("/api/users", (req, res) => {
    res.json({ok:true, users:users});
})

// Query param, request O, response O
app.get("/api/users/user", (req, res) => {
    const user_id = req.query.user_id
    const user = users.filter(data => data.id == user_id)
    res.json({ok:false, users:user});
})

// Query param, request O, response O
app.get("/api/users/useridname", (req, res) => {
    const {user_id, name }= req.query
    const user = users.filter(data => data.id == user_id && data.name == name)
    res.json({ok:false, users:user});
})


// Path param, request O, response O
app.get("/api/users/:user_id", (req, res) => {
    const user_id = req.params.user_id
    const user = users.filter(data => data.id == user_id)
    res.json({ok:false, users:user});
});


// post, request body O, response O
app.post("/api/users/userBody", (req, res) => {
    const user_id = req.body.id
    console.log(user_id)
    const user = users.filter(data => data.id == user_id)
    res.json({ok:false, users:user});
});

app.post("/api/users/add", (req, res) => {
    const { id, name } = req.body
    const user = users.concat({ id, name })
    res.json({ok:false, users:user});
});

app.put("/api/users/update", (req, res) => {
    const { id, name } = req.body
    const user = users.map(data=> {
        if (data.id == id) data.name = name 
        return {
            id : data.id,
            name : data.name 
        }
    })
    res.json({ok:true, users:user});
});

app.patch("/api/users/update/:user_id", (req, res) => {
    const { user_id }= req.params
    const { name } = req.body
    const user = users.map(data => {
        if (data.id == user_id) data.name = name
        return {
            id: data.id,
            name: data.name
        }
    })
    res.json({ok:true , users:user})
})

app.delete("/api/users/delete", (req, res) => {
    const { user_id } = req.body
    console.log(user_id)
    const user = users.filter(data => data.id != user_id)
    res.json({ok:false, users:user});
});


module.exports = app;
