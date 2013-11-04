var redis = require("redis"),
    client = redis.createClient();


var parseInfo = function(info) {
    var lines = info.split( "\r\n" );
    var obj = { };
    for ( var i = 0, l = info.length; i < l; i++ ) {
        var line = lines[ i ];
        if ( line && line.split ) {
            line = line.split( ":" );
            if ( line.length > 1 ) {
                var key = line.shift( );
                obj[ key ] = line.join( ":" );
            }
        }
    }
    return obj;
}

client.on("connect", function () {
    console.log("Redis connected");
    client.flushdb(function (err, replay, third) {
        if (err) {
            return;
        }
        console.log("Redis Clear");
        client.info(function (err, replay) {
            var info = parseInfo(replay);
        })
    })
})

client.on("error", function (err) {
    console.log("Error " + err);
});    

// LISTS: 记录命中率

// ZSETS: 关键字访问次数+1
exports.incrKeyCount = function (keyword) {
    client.zincrby("HOTDATA", 1, keyword, function (err, replay) {

        // 测试是否已经更新score:
        // 取得所有ZSETS
        client.zrange("HOTDATA", 0, -1, function (err, replay) {
            console.log("Redis all ZSETS------>", replay);
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
// 增加某个SETS
exports.add = function (key, sets, fn) {
    client.sadd(key, sets, function (err, replay) {
        if (fn) fn(replay);
    })
}

// HASH DB: 将数据存入Redis数据库中
exports.insertData = function (docs) {
    docs.forEach(function (data) {
        // 批量设置 key: value
        client.hmset("db:" + data.id, "title", data.title, "url", data.url, function (err, replay) {
            // 获取所有Key/value 验证是否插入成功
            client.hgetall("db:" + data.id, function (err, replay) {
                console.log("Validate Data------>", replay);
            });
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