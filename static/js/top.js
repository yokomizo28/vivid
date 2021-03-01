$(document).ready(function () {
    var windowWidth = $(window).width();

    $('.arrow1').click(function() {
        var pos = $(this).next().children('.slide').position();
        if(pos.left < 0){
            if(windowWidth < 768){
                $(this).next().children('.slide').animate(
                    {'left': '+=220px'},500,
                )
            }else{
                $(this).next().children('.slide').animate(
                    {'left': '+=220px'},500,
                )
            }
        }
    });


    $('.arrow2').click(function() {
        var pos = $(this).prev().children('.slide').position();
        var slideWidth = $(this).prev().children('.slide').width();
        slideWidth -= 220;
        if(pos.left > -(slideWidth)) {
            if (windowWidth < 768) {
                $(this).prev().children('.slide').animate(
                    {'left': '-=220px'}, 500,
                )
            } else {
                $(this).prev().children('.slide').animate(
                    {'left': '-=220px'}, 500,
                )
            }
        }
    });

});