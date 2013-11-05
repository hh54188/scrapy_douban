var redis = require("redis"),
    client = redis.createClient();

client.on("connect", function () {
    console.log("Redis connected");
    client.flushdb(function (err, replay, third) {
        if (err) {
            return;
        }
        console.log("Redis Clear");
        console.log("Redis used_memory_human------>", client.server_info.used_memory_human);
        console.log("Redis used_memory------>", client.server_info.used_memory);
        
        var maxMemory = 1024 * 1024 * 1;
        client.config("set", "maxmemory", maxMemory, function (err, replay) {
            if (replay) console.log("Reset maxmemory------->", maxMemory / (1024 * 1024) + "mb");
        });

        var maxMemoryPolicy = "allkeys-lru";
        client.config("set", "maxmemory-policy", maxMemoryPolicy, function (err, replay) {
            if (replay) console.log("Reset memorypolicy------->", maxMemoryPolicy);
        });        

        // volatile-lru remove a key among the ones with an expire set, trying to remove keys not recently used.
        // volatile-ttl remove a key among the ones with an expire set, trying to remove keys with short remaining time to live.
        // volatile-random remove a random key among the ones with an expire set.
        // allkeys-lru like volatile-lru, but will remove every kind of key, both normal keys or keys with an expire set.
        // allkeys-random like volatile-random, but will remove every kind of keys, both normal keys and keys with an expire set.


    })
})

client.on("error", function (err) {
    console.log("Error " + err);
});

// ZSETS: 关键字访问次数+1
exports.incrKeyCount = function (keyword) {
    client.zincrby("HOTDATA", 1, keyword, function (err, replay) {

        // 测试是否已经更新score:
        // 取得所有ZSETS
        client.zrange("HOTDATA", 0, -1, function (err, replay) {
            console.log("Redis all ZSETS length------>", replay.length);
            // 如果超过100则进行整理
            if (replay.length > 100) {
                // ZSETS 为升序排序，只保留最热的100个
                // client.zrange("HOTDATA", 0, -100, function (err, replay) {

                // });
            }
        });

        // 验证指定关键字是否已经增加
        client.zscore("HOTDATA", keyword, function (err, replay) {
            console.log(keyword, "'s score: ", replay);            
        });

    });
}

// SETS：某个关键字缓存的所有索引
// 查找是否有该关键字
exports.find = function (key, fn) {
    client.smembers(key, function (err, replay) {
        if (fn) fn(replay);
    })
}
// 增加索引SETS
exports.add = function (key, sets, fn) {
    client.sadd(key, sets, function (err, replay) {
        if (fn) fn(replay);
    })
}

// 删除SETS索引
var removeIndex = function (key) {
    // 首先取得该索引下的所有id
    client.smembers(key, function (err, replay) {

        if (err || replay.length == 0) return;
        var completeFlag = replay.length;
        replay.forEach(function (id) {
            // 删除对应HASH数据库
            client.del("db:" + id, function (err, replay) {
                console.log("Redis del hash------>", "db:" + id);
                completeFlag--;

                // 如果SET中的所有数据库删除完成，则删除这个SET
                if (!completeFlag) {
                    client.del(key, function (res, replay) {
                        console.log("Redis del index sets------>", key);
                    })
                }
            });
        })

    })
}






// HASH DB: 将数据存入Redis数据库中
exports.insertData = function (docs) {
    docs.forEach(function (data) {
        // 批量设置 key: value
        client.hmset("db:" + data.id, "title", data.title, "url", data.url, function (err, replay) {
            // 获取所有Key/value 验证是否插入成功
            // client.hgetall("db:" + data.id, function (err, replay) {
            //     console.log("Validate Data------>", replay);
            // });

        });
    });
}

exports.getDocData = function (key, fn) {
    client.smembers(key, function (err, replay) {
        if (err) {
            console.log("Redis------>err", err);
            return;
        }
        fn(replay);
    })
    // client.hgetall("db:" + id, fn);
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