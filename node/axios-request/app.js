const axios = require('axios');

// 요청을 하면 된다 . 서버를 띄워서
axios
    .post('http://192.168.1.80:8000/todos', {})
    .then((res) => {
        console.log(`statusCode : ${res.status}`);
        console.log(res)
        // console.log(req)
    })
    .catch(error => {
        console.log(error);
    })