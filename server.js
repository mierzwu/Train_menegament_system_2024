const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const cors = require('cors');
const { exec } = require('child_process'); //polecenia systemowe
const path = require('path');

const app = express();
const port = 8787;

app.use(cors());
app.use(express.static(path.join(__dirname, 'strona')));
app.use(bodyParser.json()); //obsługa json
app.use(bodyParser.urlencoded({ extended: true }));

const DB = new sqlite3.Database('resources/railway.db', (err) => {
    if(err){
        console.err('Błąd połączenia z bazą danych:', err);
    } else {
        console.log('Połączono z bazą daych');
    }
});
app.post('/search', (req, res) => {
    const { from_station, to_station, date } = req.body;
    console.log("Dane są gitara",req.body);
    res.send('dane doszły pozdro');
});


app.listen(port, () => {
    console.log('Serwer działa na porcie', port);
});


