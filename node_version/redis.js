var redis = require("redis"),
    client = redis.createClient();

client.on("connect", function () {
    console.log("Redis connected");
})

client.on("error", function (err) {
    console.log("Error " + err);
});    