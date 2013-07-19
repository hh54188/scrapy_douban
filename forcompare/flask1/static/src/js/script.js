;(function () {
    var KEYWORD_LIMIT = 10, count = 0;
    function search(keywords) {
        $.ajax({
            type: "get",
            url: '/fetch',
            data: {
                param: keywords.join("&"),
                name: 'lee'
            },
            error: function () {
                alert("后台出错，轻稍后再试，抱歉");
                $('.btn-search').attr("disabled", false).text("搜索");
            },
            success: function (data) {
                var result = $.parseJSON(data);
                $('.btn-search').attr("disabled", false).text("搜索");
                
                if (result.status !== "ok") {
                    alert("后台出错，轻稍后再试，抱歉");
                    return
                }
                result = result.data;
                if (result.length === 0) {
                    alert("暂无这些关键字的房屋信息，抱歉");
                    return;
                }
                
                $('#model_search').modal('show')
                $('.smodel_search-list').empty();
                for (var i = 0; i < result.length; i++) {
                    var item = result[i];
                    var $li = $('<li><a target="_blank" href="' + item.link + '">' + item.title + '</a></li>');
                    $('.smodel_search-list').append($li);
                }
            }
        })
    }


    $('.btn-keyword').click(function () {
        var searchBtn = $('.btn-search');
        // 最多只允许20个关键字
        count++;
        if (count === KEYWORD_LIMIT) {
            count--;
            return;
        }
        searchBtn.attr("disabled", false).text("搜索");

        var text = $(this).text();
        var label = $('<div class="label-word-copy alert in alert-info"><strong>' + text + '</strong><a class="close" data-dismiss="alert" href="#">×</a></div>');
        label.bind('closed', function () {
            // HACK:
            count = $('.label-word-copy').length - 1;
            if (count === 0) {
                searchBtn.attr("disabled", true).text("请先选择关键词");
            }
        })
        $('.side_bar').append(label);
    })

    $('.btn-search').click(function () {
        var keywords = $('.label-word-copy');
        if (keywords.length === 0) return;
        var collectKeywords = function () {
            var result = []
            keywords.each(function (index, el) {
                result.push($(el).find("strong").text());
            })
            return result;
        }
        var result = collectKeywords();
        search(result);
        $(this).attr("disabled", true).text("正在查找，请稍后");
    })

    function refresh() {
        $.ajax({
            type: "get",
            url: '/refresh',
            success: function (data) {

            }
        })        
    }
    refresh();
})();