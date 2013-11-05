var redis = require("redis"),
    client = redis.createClient();


var showZSETS = function () {
    client.zrange("test", 0, -1, function (err, replay) {
        console.log(replay);
    });
}

client.on("connect", function () {
    client.flushdb(function (err, replay) {
        var completeFlag = 100;
        for (var i = 0; i < 100; i++) {
            client.zadd("test", i, "key_" + i, function (err, replay) {
                completeFlag--;
                if (!completeFlag) {
                    // client.zrange("test", 0, 20, function (err, replay) {
                    //     console.log(replay);
                    // });                    
                    client.zremrangebyrank("test", 0, 20, function (err, replay) {
                        console.log("What's removed------>", replay);
                        showZSETS();
                    })
                }
            })
        }
    })
})