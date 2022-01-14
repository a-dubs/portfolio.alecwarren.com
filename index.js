$(function () {
    // $(".gallery").mouseenter(function ()
    // {
    //     $(this).find(".btn#fs").addClass("visible").removeClass("invisible");
    // });

    // $(".gallery").mouseleave(function ()
    // {
    //     $(this).find(".btn#fs").removeClass("visible").addClass("invisible");
    // });

    var projectBtnAniDur = 250;
    var projectBtnEasing = "easeOutBack";
    var COLLAPSE_BTN_HTML = "<p>&nbsp;Collapse&nbsp;</p>";
    var EXPAND_BTN_HTML = "<p>&nbsp;Expand&nbsp;</p>";


    $(".project .btn#c2a a").mouseenter(function () {
        // if (!$(this).is(':animated')) {
        $(this).stop().animate({ "padding": ".55em 6.5em" }, projectBtnAniDur, projectBtnEasing);
        // }
    });
    $(".project .btn#c2a a").mouseleave(function () {
        $(this).stop().animate({ "padding": ".55em 5em" }, projectBtnAniDur, projectBtnEasing);
    });

    $(".project .collapse-btn, .project .expand-btn").click(function () {
        if (!$(this).is(':animated')) {
            $(this).toggleClass("collapse-btn").toggleClass("expand-btn");
            if ($(this).html().replace(/\s/g, "") == COLLAPSE_BTN_HTML)  // COLLAPSE 
                $(this).empty().html(EXPAND_BTN_HTML);
            else  // EXPAND 
            {
                $(this).empty().html(COLLAPSE_BTN_HTML);
                // force custom gallery to resize now that it is no longer "collapsed"
                
            }
        }
        $expand_area = $(this).parent().parent().parent().find(".expand-area");
        $expand_area.find(".gallery").trigger("resize");
    });

    // $(".taskbar .filter").click(function () {
    //     $(this).toggleClass("selected").toggleClass("unselected");
    //     var selected = []
    //     $(".taskbar .filter").each(function () {
    //         if ($(this).hasClass("selected"))
    //             selected.push($(this).attr('id'));
    //     });

    //     if (selected.length == 0) {
    //         $(".project").show()
    //     }

    //     else {
    //         selected.forEach(function (id) {
    //             $(".projec#" + id).show(300);
    //         })
    //     }

    // })

    $(".project .collapse-btn, .project .expand-btn").mouseenter(function () {
        if ($(this).html() == COLLAPSE_BTN_HTML) { // COLLAPSE 
            if (!$(this).is(':animated')) {
                $(this).stop().animate({ "padding": "0 4em" }, projectBtnAniDur, projectBtnEasing);
            }
        }
        else  // EXPAND 
            $(this).stop().animate({ "padding": "0 6.5em" }, projectBtnAniDur, projectBtnEasing);
    });
    $(".project .collapse-btn, .project .expand-btn").mouseleave(function () {
        if ($(this).html() == COLLAPSE_BTN_HTML) { // COLLAPSE 
            // if (!$(this).is(':animated')) {
                $(this).stop().animate({ "padding": "0 6.5em" }, projectBtnAniDur, projectBtnEasing);
            // }
        }
        else  // EXPAND 
            $(this).stop().animate({ "padding": "0 4em" }, projectBtnAniDur, projectBtnEasing);
    });
    /* $(".gallery #fs.btn").click(function () {
        console.log($(this).p arent());
        $(this).removeClass("visible").addClass("invisible");
        $(this).parent().stop().animate({ "width": (2200.0 / 24.0 + "%") }, 600);
        // $(this).parent().find(".slide").stop().animate({ "width": "100%" }, 600);
        $(this).parent().delay(600).addClass("col-22 col-sm-22 col-md-22 col-lg-22 col-xl-22 col-xxl-22"); 
        $(this).parent().delay(650).trigger("resize");
        $(this).delay(1000).removeClass("visible").addClass("invisible");
        }); */

    $(".expand-area .secondary-collapse-btn .txt-box").mouseenter(function () {
        $(this).find(".bg").stop().animate({
            "width": "100%"
        }, projectBtnAniDur, projectBtnEasing);
    });
    $(".expand-area .secondary-collapse-btn .txt-box").mouseleave(function () {
        $(this).find(".bg").stop().animate({
            "width": "0%"
        }, projectBtnAniDur, projectBtnEasing);
    });
    
});

$(document).scroll(function () {
    //console.log("scrolled " + $(document).scrollTop());
});


