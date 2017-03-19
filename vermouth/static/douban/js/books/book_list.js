/*图片加载事件*/
$('.book_img').imagesLoaded()
    .done(function (image) {
        console.log('all images successfully loaded');
    })
    .fail(function (image) {
        image.img.src = "/static/images/error/404.png";
    })
    .progress(function (instance, image) {
        if (!image.isLoaded) {
            image.img.src = "/static/images/loading/loading1.gif";
        }
    });
jQuery(document).ready(function () {
    /*获取当前url参数，执行选中效果*/
    var current_menu_name = $.getUrlParam("menu_name");
    $(".cbp-filter-item").each(function () {
        var menu_name = $(this).attr("id");
        if (current_menu_name == null) {
            $("#所有图书").addClass("cbp-filter-item-active")
        }
        else {
            if (menu_name == current_menu_name) {
                $(this).addClass("cbp-filter-item-active")
            }
            else {
                $(this).attr("class", "cbp-filter-item")
            }
        }
    });
    /*分类目录的筛选*/
    $(".cbp-filter-item").click(function () {
        var menu_name = $(this).attr("id");
        var url_href = "/douban/index/?menu_name=" + menu_name;
        window.location.href = encodeURI(url_href);
    });

    $(".order_by").click(function () {
        var order_by = $(this).attr("id");
        var menu_name = $("#menu_name_hide").text();
        alert(menu_name);
        var url_href = "/douban/index/?menu_name=" + menu_name+"&order_by="+order_by;
        window.location.href = encodeURI(url_href);
    })
});

/*为jquery扩展一个方法来通过jquery获取url参数*/
(function ($) {
    $.getUrlParam = function (name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) return decodeURI(r[2]);
        return null;
    }
})(jQuery);