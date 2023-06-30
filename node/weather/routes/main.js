const express = require("express")
const app = express.Router();
const mongoose = require("mongoose");
const request = require("request");
const moment = require("moment");  
const dateutil = require("data-utils");
const mongoClient = require("mongodb").MongoClient

let day = new Date().toLocaleDateString('sv').replaceAll('-','');

var keys = "koV896YEPjzMVvktqNptcMO4LNQeS6kERRUsN%2FOVwEpN0IXlIE9sAWiGgaZd%2Bz8ddSDb21Ml%2F3JE7eCUV03VQg%3D%3D"
var url = "https://apis.data.go.kr/1360000/WthrChartInfoService/getSurfaceChart"

var queryParams = "?" + encodeURIComponent('serviceKey') + "=" + keys;
queryParams += "&" + encodeURIComponent('pageNo') + "=" + encodeURIComponent('1');
queryParams += "&" + encodeURIComponent('numOfRows') + "=" + encodeURIComponent('10');
queryParams += "&" + encodeURIComponent('dataType') + "=" + encodeURIComponent('JSON');
queryParams += "&" + encodeURIComponent('code') + "=" + encodeURIComponent('3');
queryParams += "&" + encodeURIComponent('time') + "=" + encodeURIComponent(day);

var DataSchema = mongoose.Schema({
    day_v : String,
    imgSrc1_v : String,
    imgSrc2_v : String
})

var Data = mongoose.model('weathers', DataSchema);

app.get('/getdata', (req,res, next) => {
    request({
        url: url + queryParams,
        method : 'GET'
    }, function (error, response, body) {
        Data.find({}).remove().exec();
        if (error) console.log(error);
        // console.log(body)
        let data = JSON.parse(body);
        let imgSrcArr = data['response']['body']['items']['item'][0]['man-file'].split(',');
        let imgSrc1 = imgSrcArr[0].slice(1)
        let imgSrc2 = imgSrcArr[1].slice(1)
        console.log("imgSrc1 :",imgSrc1);
        console.log("imgSrc2 :",imgSrc2);
        
        res.writeHead(200);
        var template =`
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>
                Result
            </title>
        </head>
        <body>
        <img src="${imgSrc1}" width="500" height="500"></img>
        <img src="${imgSrc2}" width="500" height="500"></img>
        </body>
        </html>
        `;
        res.end(template);
        
        var newData = new Data({day_v:day, imgSrc1_v : imgSrc1, imgSrc2_v : imgSrc2})
        newData.save(function(err, result) {
            if(err) return console.error(err);
            console.log(new Date(), result);
        })
        // console.log('resultCode', response.resultCode);
        // console.log('Headers',
        // JSON.stringify(response.headers))
    })
})

app.get('/list', function(req, res, next) {
    Data.findOne({}, function(err, docs) {
        if (err) console.log('err');
        console.log(docs);
        res.writeHead(200);
        var template =`
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>
                Result
            </title>
        </head>
        <body>
        <img src="${docs['imgSrc1_v']}" width="500px" height="500px"></img>
        <img src="${docs['imgSrc2_v']}" width="500px" height="500px"></img>
        </body>
        </html>
        `;
        res.end(template);
    })
})

module.exports = app;
