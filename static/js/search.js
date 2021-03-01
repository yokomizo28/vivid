$(document).ready(function () {
    //何か操作されるたびに動く .on() 今回はclick
    $('#search-form').children().on('click', function(){
        $('#search-form').submit();
    });
});