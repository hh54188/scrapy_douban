var db = require("../db");
var re = require("../myRedis");

exports.response = function (req, res) {
    var keyword = req.body.keyword;
    var key_conv = "";
    for (var i = 0; i < keyword.length; i++) {
        var cha = keyword[i];
        key_conv += cha.charCodeAt(0) + "_";
    }

    // 首先去Redis中查找
    re.find(key_conv, function (replay) {

        console.log("Redis find------>replay length", replay.length);

        // 同时访问次数+1 ，更新热度
        re.incrKeyCount(key_conv);

        // 如果Redis中没有缓存，从MongoDB中查找
        // 虽然返回的数组，但是实际上在Redis中为SET类型
        if (!replay.length) {
            db.find(keyword, function (docs) {
                console.log("docs length------->", docs.length);
                var idArr = []
                docs.forEach(function (doc) {
                    idArr.push(doc.id);
                });

                // 增加缓存索引
                re.add(key_conv, idArr, function (replay) {
                    console.log("Redis save------->", replay);
                });

                // 存入缓存
                re.insertData(docs);

                // 返回结果
                res.send({
                    status: "OK",
                    data: 0
                });  
            })
        } else {
            // 如果缓存中有数据，从缓存中返回
            res.send({
                status: "OK",
                data: 1
            });              
        }
    });
}