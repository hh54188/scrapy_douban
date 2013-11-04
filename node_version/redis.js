var redis = require("redis"),
    client = redis.createClient();

client.on("connect", function () {
    console.log("Redis connected");
    client.flushdb(function (err, status, third) {
        if (err) {
            return;
        }
        console.log("Redis Clear");
    })
})

client.on("error", function (err) {
    console.log("Error " + err);
});    