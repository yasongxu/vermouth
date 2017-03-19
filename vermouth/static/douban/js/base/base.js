jQuery(document).ready(function () {
    /*搜索按钮*/
    $("#search_all").click(function () {
        var search_val = $("#s").val();
        window.location.href = encodeURI("/douban/search/?search=" + search_val);
    });
    $('#s').bind('keypress', function (event) {
        var search_val = $("#s").val();
        if (event.keyCode == "13") {
            window.location.href = encodeURI("/douban/search/?search=" + search_val);
        }
    });
});