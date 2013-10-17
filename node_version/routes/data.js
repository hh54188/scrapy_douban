var request = require("request");
var cheerio = require("cheerio");

var FETCH_URLS = [
    // "http://www.douban.com/group/beijingzufang/discussion",
    // "http://www.douban.com/group/fangzi/discussion",
    // "http://www.douban.com/group/262626/discussion",
    // "http://www.douban.com/group/276176/discussion",
    // "http://www.douban.com/group/26926/discussion",
    // "http://www.douban.com/group/sweethome/discussion",
    // "http://www.douban.com/group/242806/discussion",
    // "http://www.douban.com/group/257523/discussion",
    // "http://www.douban.com/group/279962/discussion",
    "http://www.douban.com/group/334449/discussion"
];

var FETCH_PAGE_NUM = 2;
var COMPLETE_FLAG = 0;
var RES = {};

var pageRequest = function (res, url) {

    COMPLETE_FLAG++;

    request({
        uri: url,
    }, function(error, response, body) {

        if (error) {
            COMPLETE_FLAG--;
            return;
        }

        var $ = cheerio.load(body);
        var links = $("table.olt td.title a");

        links.map(function (i, link) {
            var href = $(link).attr('href');
            var title = $(link).attr('title');
            var id = href.split('/')[5];

            RES[id] = href;
            console.log(id);
        });

        COMPLETE_FLAG--;

        if (!COMPLETE_FLAG) {
            res.send(RES);
        }
    });
};

exports.fetch = function (req, res) {

    // Loop 1
    FETCH_URLS.forEach(function (url, index) {

        // Loop 2
        for (var i = 0; i < FETCH_PAGE_NUM; i++) {
            var temp_url = url + "?start=" + 25 * i;
            pageRequest(res, temp_url);
        }
    });
};