var request = require("request");

var keywords = {
    hot: [],
    cold: []
}

request({
    "Content-type": "application/json",
    "uri": "http://127.0.0.1:8000/ping",
    "json": {
        "hello": "world"
    }
}, function(error, res, body) {
    console.log(res.body);
})