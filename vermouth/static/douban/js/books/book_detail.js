jQuery(document).ready(function () {
    /*限制图片的宽高*/
    $(".book_detail_pic").each(function () {
         $(this).css("height", 256);
         $(this).css("width", 186);
    })
});