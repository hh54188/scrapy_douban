var mongoose = require('mongoose');
var redis = require("redis");

//connect to mongo
exports.connectToDB = function (callback) {
    mongoose.connect('mongodb://localhost/test');
    var db = mongoose.connection;
    db.on('error', console.error.bind(console, 'connection error:'));
    db.once('open', function () {
        console.log('MongoDB connected!');
        if (callback) {
            callback();
        }
    });
};

var ItemSchema, ItemModel;

exports.saveAll = function (dataArr) {

    // 也可使用此方法进行批量添加，但一旦出错，整批数据无效
    // ItemModel.create(dataArr, function (error) {

    //     if (error) {
    //         console.log("DB saveAll error------>", error);
    //         return;
    //     }
    //     console.log(dataArr.length + " datas have saved!");
    // });

    var notCompleteLen = dataArr.length;
    var errLength = 0, saveLength = 0;
    dataArr.forEach(function (data, index) {

        var item = new ItemModel({
            url: data.href,
            title: data.title,
            id: data.id
        }).save(function (err) {
            if (!--notCompleteLen) {
                console.log(errLength + " ignored!");
                console.log(saveLength + " saved!");
            }
            
            if (err) {
                errLength++;
                return;
            }

            saveLength++;
        });

    })
}

exports.getSingle = function (id) {

}

exports.init = function () {
    ItemSchema = mongoose.Schema({
        url: String,
        title: String,
        id: {
            type: [String],
            index: {
                unique: true
            }
        }
    });

    ItemModel = mongoose.model("MasterHouse", ItemSchema);
    console.log("Master init complete!");
};






