const express = require('express');
const morgan = require('morgan'); // 디버깅을 위해서 사용한다
const path = require('path');
const bodyParser = require('body-parser') // get , post request 꺼내 올려면 필요한것이다.
const cookieParser = require('cookie-parser');
const fs = require("fs")

const app = express();

app.set('port', process.env.PORT || 8000);
app.set('views', path.join(__dirname, 'public'));
app.set('view engine', 'ejs')
app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

var s3view = require('./routes/s3view.js');
app.use('/', s3view);

app.listen(app.get('port'), () => {
    var dir = './uploadedFiles';
    if(!fs.existsSync(dir)) fs.mkdirSync(dir);
    console.log('8000 Port : Server Started...')
});