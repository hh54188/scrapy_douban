var mongoose = require('mongoose');

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

exports.save = function (data) {
    
    var item = new ItemModel({
        url: data.href,
        title: data.title,
        id: data.id
    }).save(function (err) {
        if (err) {
            console.log("Error!", err);
        }

        console.log(data.id + " saved");
    });
}

exports.init = function () {
    ItemSchema = mongoose.Schema({
        url: String,
        title: String,
        id: Number
    });

    ItemModel = mongoose.model("MasterHouse", ItemSchema);

    console.log("Master init complete!");
};






