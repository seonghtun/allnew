const express = require('express');
const app = express.Router();
const multer = require("multer");
const fs = require('fs');
const path = require('path');

var storage = multer.diskStorage({
    destination(req, file ,cb) {
        cb(null , 'uploadedFiles/');
    },
    filename(req, file, cb) {
        cb(null, `${Date.now()}__${file.originalname}`);
    }
})

var upload = multer({dest: 'uploadedFiles/'});
var uploadWithOriginalFilename = multer({ storage : storage});

app.get('/', function(req, res) {
    res.render('upload');
})

app.post('/uploadFile', upload.single('attachment'),function(req, res) {
    res.render('confirmation', {file:req.file, files:null})
})

app.post('/uploadFileWithOriginalFilename', uploadWithOriginalFilename.single('attachment'),function(req, res) {
    res.render('confirmation', {file:req.file, files:null})
})

app.post('/uploadFiles', upload.array('attachments'),function(req, res) {
    res.render('confirmation', {file:null, files:req.files})
})

app.post('/uploadFilesWithOriginalFilename', uploadWithOriginalFilename.array('attachments'),function(req, res) {
    res.render('confirmation', {file:null, files:req.files})
})  

// app.get('/fileList', (req, res) => {
//     fs.readdir('uploadedFiles/',function(err, filelist) {
//         if (err) return console.error(err);
// 	    console.log(filelist);
// 	    res.send(filelist);
//     })
// })

app.get('/list', (req, res) => {
    const fullPath = process.cwd() + '/uploadedFiles'// not __dirname
    const dir = fs.opendirSync(fullPath);
    let entity
    
    // let listing = []
    res.writeHead(200);
    var template = `
        <!doctype html>
        <html>
            <head>
                <title>
                Result
                </title>
                <meta charset='utf-8'>
            </head>
            <body>
                <table border="1" style="margin: auto; text-align: center; width:100%">
                    <thead>
                        <tr>
                            <th> Type </th>
                            <th> Name </th>
                            <th> Down </th>
                            <th> Del </th>
                        </tr>
                    </thead>
                    <tbody>`;
    
    // while ((entity = dir.readSync()) !== null) {
    //     if(entity.isFile()) {
    //         listing.push({type:'f', name:entity.name});
    //     } else if (entity.isDirectory()){
    //         listing.push({type:'d', name:entity.name})
    //     }
    // }
    while ((entity = dir.readSync()) !== null) {
        let type;
        if(entity.isFile()) {
            type = 'f'
        } else if (entity.isDirectory()){
            type = 'd'
        }
        template += `
                <tr>
                    <td> ${type} </td>
                    <td> ${entity.name} </td>
                    <td>
                    <form method="post" action='/downloadFile'>
                    <button type="submit" name='dlKey' value=${entity.name}>
                    Down</button>
                    </form>
                    </td>
                    <td>
                    <form method="post" action='/deleteFile'>
                    <button type="submit" name='dlKey' value=${entity.name}>
                    Del</button>
                    </form>
                    </td>
                </tr>`
    }
    
        template+= `
                    </tbody>
                </table>
            </body>
        </html>
    `
    dir.closeSync()
    res.end(template);
})


app.post('/downloadFile',function(req,res){
  res.download(path.join(process.cwd(), '/uploadedFiles/', req.body.dlKey),req.body.dlKey)
//   const stream = fs.createReadStream(path.join(process.cwd(), '/uploadedFiles/', req.body.dlKey));
//   res.setHeader('Content-Disposition', `attachment; filename=${req.body.dlKey}`); // 이게 핵심 
//   stream.pipe(res);
//   res.sendFile(path.join(process.cwd(), '/uploadedFiles/', filename));
})

app.post('/deleteFile',function(req,res){
    console.log(req.body.dlKey);
    fs.unlink(process.cwd(), '/uploadedFiles/', req.body.dlKey, 
    (err) => err ? console.log(err) : console.log(`File delete successfully. ${req.body.dlKey}`))
    res.redirect('/list');
})

module.exports = app;