// const express = require('express');
// const morgan = require('morgan');
// const path = require('path');
// const app = express();
// const bodyParse = require('body-parser');
// const cookieParse = require('cookie-parser');
// const router = express.Router();

// app.get('port', process.env.PORT || 8000);
// app.use(morgan('dev')); // 디버깅을위해 에러더 자세하게 보기위해 
// app.use(bodyParse.json()) // parsing은 쪼갠다고 하면 된다 . url에서 정보를찾아내는 작업을 말한다.
// app.use(bodyParse.urlencoded({ extended: false }));
// app.use(cookieParse()); //cookieParse.json()
// app.use(express.static(path.join(__dirname, 'public')));

// var main = require('./routes/main.js');
// app.use('/', main);

// app.listen(app.get('port'), () => {
//     console.log('8000 Port : Server Started~!!');
// });
const express = require('express')
const morgan = require('morgan')
const path = require('path')
const app = express()
const bodyParser = require('body-parser')
const cookieParser = require('cookie-parser')
const router = express.Router()

app.set('port', process.env.PORT || 8000)
app.use(morgan('dev'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cookieParser())
app.use(express.static(path.join(__dirname, 'public')))

var main = require('./routes/main.js')
app.use('/', main)

app.listen(app.get('port'), () => {
    console.log('8000 Port : Server Started...')
});