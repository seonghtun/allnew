const https = require('axios');

axios
    .post('https://example.com/todos', {
        todo: "Buy the milk"
    })
    .then(res => {
        console.log(`statusCode : ${res.statusCode}`)
        consoel.log(res)
    })
    .catch(error => {
        console.error(error);
    })