var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/test');
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
    console.log('MongoDB connected!');
});

var ItemSchema, ItemModel;

var dataArr = [], count = 100;

(function () {
    for (var i = 0; i < count; i++) {
        dataArr.push({
            id: "id_" + i,
            title: "title_" + i
        })
    }
})()

var save = function (dataArr) {
    ItemModel.create(dataArr, function (err, jellybean, snickers) {
        console.log("-------save complete-------");
        console.log("err------>", err);
        console.log("jellybean------>", jellybean);
        console.log("snickers------>", snickers);
    })
}

var init = function () {
    ItemSchema = mongoose.Schema({
        title: String,
        id: String
    });

    ItemModel = mongoose.model("testHouse", ItemSchema);

    console.log("testHouse init complete!");
};

init();
save(dataArr);






