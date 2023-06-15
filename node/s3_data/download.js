const fs = require('fs');
const env = require('dotenv').config({ path:"../../.env"});

const AWS = require('aws-sdk');
const ID = process.env.ID;
const SECRET = process.env.SECRET;
const BUCKET_name = 'yoon-8394';
const MYREGION = 'ap-northeast-2'
const s3 = new AWS.S3({accessKeyID : ID,
secretAccessKey : SECRET, region: MYREGION});

const downloadFile = (filename) => {
    const params = {
        Bucket: BUCKET_name,
        Key : 'axios.png',
    };
    s3.getObject(params, function(err, data) {
        if (err) { throw err;}
        fs.writeFileSync(filename, data.Body)
    });
};

downloadFile('axios.png');
