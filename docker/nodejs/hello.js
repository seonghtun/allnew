var express = require('express')
var app = express()

app.get('/', function (req, res) {
<<<<<<< HEAD
    res.send('Hello Node JS~!!');
});
=======
    res.send("Hello Node JS~!!")
})
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb

app.listen(8000, function () {
    console.log("8000 Port : Server Started~!!")
})