var mongoose = require('mongoose');

//connect to mongo
exports.connectToDB = function (callback) {
    mongoose.connect('mongodb://localhost/test');
    var db = mongoose.connection;
    db.on('error', console.error.bind(console, 'connection error:'));
    db.once('open', function () {
        console.log('mongoDB connected!');
        if (callback) {
            callback();
        }
    });
};

var ItemSchema, ItemModel;

exports.init = function () {
    ItemSchema = mongoose.Schema({
        url: String,
        title: String,
        id: Number
    });

    ItemModel = mongoose.model("MasterHouse", ItemSchema);

    console.log("Master init complete!");

    // var item = new ItemModel({
    //     url: "test_url",
    //     title: "test_title",
    //     id: 110
    // }).save(function (err) {
    //     if (err) {
    //         console.log("Error!", err);
    //     }

    //     console.log("Item save complete!");
    // });
};






