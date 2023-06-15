const fs = require('fs');
const env = require('dotenv').config({ path:"../../.env"});

const AWS = require('aws-sdk');
const ID = process.env.ID;
const SECRET = process.env.SECRET;
const BUCKET_name = 'yoon-8394';
const MYREGION = 'ap-northeast-2'
const s3 = new AWS.S3({accessKeyID : ID,
secretAccessKey : SECRET, region: MYREGION});

const uploadFile = (filename) => {
    const fileContent = fs.readFileSync(filename);
    const params = {
        Bucket: BUCKET_name,
        Key : 'axios.png',
        Body: fileContent
    };
    s3.upload(params, function(err, data) {
        if (err) { throw err;}
        console.log(`File uploaded successfully. ${data.Location}`);
    });
}

uploadFile('axios.png')

