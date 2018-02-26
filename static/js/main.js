var theMaxHeight = 0;
$('body div.container .row .thumbnail > div').each(function () {
    if($(this).height() > theMaxHeight) {
        theMaxHeight = $(this).height();
    }
});

$('body div.container .row .thumbnail > div').height(theMaxHeight);