exports.response = function (req, res) {
    console.log(req.body);
    res.send({
        status: "OK",
        data: "test"
    });
}