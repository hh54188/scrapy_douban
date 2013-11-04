var redis = require("redis"),
    client = redis.createClient();

client.on("connect", function () {
    console.log("Redis connected");
    client.flushdb(function (err, replay, third) {
        if (err) {
            return;
        }
        console.log("Redis Clear");
        client.info(function (err, replay) {

        })
    })
})

client.on("error", function (err) {
    console.log("Error " + err);
});    

// INFO

// HASH DB:
exports.insertDocData = function (data) {
    client.hset("db:" + data.id, "title", data.title, "link", data.link, redis.print);
}

exports.getDocData = function (id, fn) {
    client.hgetall("db:" + id, fn);
}

exports.isDocExist = function (id) {
    client.hexist("db:" + id, title, redis.print);
}

exports.delDocData = function (id) {
    client.del("db:" + id, redis.print);
}

// ZSET HOT

exports.insertHotData = function (id) {
    client.zincrby("HOTDATA", id, redis.print);
}

exports.delHotData = function (id) {
    client.zrem("HOTDATA", id, redis.print);
}