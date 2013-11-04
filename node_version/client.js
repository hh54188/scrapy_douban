var request = require("request");

var keywords = {
    hot: [],
    cold: []
}

request({
    "Content-type": "application/json",
    "uri": "http://127.0.0.1:8000/query",
    "json": {
        "keyword": "知春路"
    }
}, function(error, res, body) {
    console.log(res.body);
})