var redis = require("redis"),
    client = redis.createClient();


var lock = false;

// 删除SETS索引
var removeIndex = function (key) {
    // 首先取得该索引下的所有id
    client.smembers(key, function (err, replay) {

        if (err || replay.length == 0) return;
        var completeFlag = replay.length;
        replay.forEach(function (id) {
            // 删除对应HASH数据库
            client.del("db:" + id, function (err, replay) {

                completeFlag--;

                // 如果SET中的所有数据库删除完成，则删除这个SET
                if (!completeFlag) {
                    client.del(key, function (res, replay) {
                        // console.log("Redis del index sets------>", key);
                    })
                }
            });
        })

    })
}

function reset(total, max) {
    lock = true;
    console.log("LOCK locked------>", lock, "total------>", total);
    client.zrange("HOTDATA", 0, total - max, function (err, members) {
        // 首先找到多余的members
        var memberCounter = members.length;
        members.forEach(function (member, member_index) {
            // 找到每个member对应的set
            client.smembers(member, function (err, set) {
                if (set.length > 0) {
                    set.forEach(function (id, set_index) {
                        // 找到每个对应的数据库并且删除
                        client.del("db:" + id, function (err, replay) {
                            if(set_index == set.length - 1) {
                                // 如果该set下的所有数据都已经删除完毕
                                // 删除该member
                                client.del(member, function (err, replay) {
                                    memberCounter--;
                                    if (!memberCounter) {
                                        // 删除所有多余members
                                        client.zremrangebyrank("HOTDATA", 0, total - max, function (err, replay) {
                                            lock = false;
                                            check();
                                        })                        
                                    }                                    
                                })
                            }
                        })
                    })
                } else {
                    client.del(member, function (err, replay) {
                        memberCounter--;
                        if (!memberCounter) {
                            lock = false;
                            check();
                        }
                    })
                }
            });
        })

    })
}


// function check() {
//     while(true) {
//         // console.log("check lock------->", lock);
//         if (!lock) {
//             var max = 50;
//             // LFU:
//             client.zrange("HOTDATA", 0, -1, function (err, replay) {
//                 var total = replay.length;
//                 console.log("total------>", total);
//                 if (total > max) {
//                     reset(total, max);
//                 } else {
//                     check();
//                 }
//             }); 
//             break;
//         }
//     }   
// };

function check() {
    while (true) {
        console.log("Redis used_memory------>", client.server_info.used_memory);
    }
}

check();