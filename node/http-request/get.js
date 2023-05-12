// express를 안쓰고 https 로 request 하기
// 요청하기만 인가 그러면 
const https = require('https');

const options = {
    hostname: '192.168.1.80',
    port: 8000,
    path: '/todos',
    method: 'GET'
}

const data = JSON.stringify({
    todo: 'Buy the milk'
})


const req = https.request(options, res => {
    console.log(`statusCode : ${res.statusCode}`);
    res.on('data', d => {
        process.stdout.write(d);
    })
})

req.on('error', error => {
    console.log(error);
})

req.write(data);
req.end();