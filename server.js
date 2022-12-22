const express = require('express');
const mysql = require('mysql');
const multer = require('multer');
const fs = require('fs');
const app = express();
var router = express.Router();
module.exports = router;

app.use(express.json());
console.log(__dirname + '/uploads');
app.use(express.static(__dirname + '/uploads'));

app.listen(8080, () => {
    console.log("서버시작, 8080번 포트");
});

let storage = multer.diskStorage({
    destination: function(req, file, callback) {
        callback(null, "uploads/");
    },
    filename: function(req, file, callback) {
        callback(null, file.originalname);
    }
});

let upload = multer({
    storage: storage
});

app.post('/api/uploadimage', upload.single("imgfile"), (req, res, next) => {
    let file = req.file;

    console.log("접속함");

    res.json({
        success: true,
        imageurl: `http://127.0.0.1:8080/uploads/'${req.filename}'`
    });
});