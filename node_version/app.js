// Basic
var express = require('express'),
    ejs = require('ejs');

// Route

var app = express();

app.set('port', process.env.PORT || 8000);

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(__dirname + "/media"));

app.get('/', function (req, res) {
    res.render("index");
});

app.get("/fetch", function (req, res) {
    res.send({
        name: req.query.name
    })
});

app.listen(process.env.VCAP_APP_PORT || 8000);