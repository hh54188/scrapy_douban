var request = require("request");

request({
    uri: "http://127.0.0.1:8000/ping",
}, function(error, res, body) {
    console.log(res.body);
})