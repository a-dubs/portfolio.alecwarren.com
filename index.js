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
    const all_expand_and_collapse_btns = (".project .collapse-btn, .project .expand-btn, " +
        ".project .secondary-collapse-btn , .project .secondary-expand-btn")
    
    $(".project .btn#c2a a").mouseenter(function () {
        // if (!$(this).is(':animated')) {
        $(this).stop().animate({ "padding": ".55em 6.5em" }, projectBtnAniDur, projectBtnEasing);
        // }
    });
    $(".project .btn#c2a a").mouseleave(function () {
        $(this).stop().animate({ "padding": ".55em 5em" }, projectBtnAniDur, projectBtnEasing);
    });

    $(".project .collapse-btn, .project .expand-btn").click(function () {
        $expand_area = $(this).parent().parent().parent().find(".expand-area"); 

        if (!$expand_area.is(':animated')) {
            $(this).toggleClass("collapse-btn").toggleClass("expand-btn");
            if ($(this).hasClass("collapse-btn")) { // in now collapse button 
                // force custom gallery to resize now that it is no longer "collapsed"
                $expand_area.find(".gallery").trigger("resize");
                $(this).empty().html(COLLAPSE_BTN_HTML);  // so change text to collapse
                $expand_area.stop().animate({ "opacity": "1" }, 350, "easeInOutQuad");
            }
            else {  // is now expand button  
                $(this).empty().html(EXPAND_BTN_HTML);  // so change text to expand
                $expand_area.stop().animate({ "opacity": "0" }, 350, "easeOutCubic");
                
                
            }
        }

        // TODO: make slideshow reset to first slide when expanded/hidden so it starts at the beginning every time
        
        
    });


    $(".project .secondary-collapse-btn .txt-box").click(function () {
        $expand_area = $(this).parent().parent();

        if (!$expand_area.is(':animated')) {
            $expand_area.parent().parent().find(".collapse-btn").toggleClass("collapse-btn").toggleClass("expand-btn");
            $expand_area.parent().parent().find(".expand-btn").empty().html(EXPAND_BTN_HTML);
            $expand_area.parent().parent().find(".expand-btn").stop().animate({ "padding": "0 4em" }, projectBtnAniDur, projectBtnEasing);
            $expand_area.stop().animate({ "opacity": "0" }, 350, "easeOutCubic");
          
        }
        
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


