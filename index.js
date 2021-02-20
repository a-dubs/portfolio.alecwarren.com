$(function () {
    // $(".gallery").mouseenter(function ()
    // {
    //     $(this).find(".btn#fs").addClass("visible").removeClass("invisible");
    // });

    // $(".gallery").mouseleave(function ()
    // {
    //     $(this).find(".btn#fs").removeClass("visible").addClass("invisible");
    // });
    
    $(".project .btn#github a").mouseenter(function () {
        $(this).stop().animate({ "padding": ".55em 6.5em"}, 200);
    });
    $(".project .btn#github a").mouseleave(function () {
        $(this).stop().animate({ "padding": ".55em 5em" }, 200);
    });

    // $(".gallery #fs.btn").click(function () {
    //     console.log($(this).parent());
    //     $(this).removeClass("visible").addClass("invisible");
    //     $(this).parent().stop().animate({ "width": (2200.0 / 24.0 + "%") }, 600);
    //     // $(this).parent().find(".slide").stop().animate({ "width": "100%" }, 600);
    //     $(this).parent().delay(600).addClass("col-22 col-sm-22 col-md-22 col-lg-22 col-xl-22 col-xxl-22"); 
    //     $(this).parent().delay(650).trigger("resize");
    //     $(this).delay(1000).removeClass("visible").addClass("invisible");
    // });

});

$(document).scroll(function() {
    //console.log("scrolled " + $(document).scrollTop());
});

