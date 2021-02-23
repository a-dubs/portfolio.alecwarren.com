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

    $(".project .btn#github a").mouseenter(function () {
        $(this).stop().animate({ "padding": ".55em 6.5em"}, projectBtnAniDur, projectBtnEasing);
    });
    $(".project .btn#github a").mouseleave(function () {
        $(this).stop().animate({ "padding": ".55em 5em" }, projectBtnAniDur, projectBtnEasing);
    });

    
    $(".project .collapse-btn, .project .expand-btn").click(function () {

        $expand_area = $(this).parent().parent().parent().find(".expand-area")

        $(this).toggleClass("collapse-btn").toggleClass("expand-btn");
        if ($(this).html() == "Collapse")  // COLLAPSE 
            $(this).empty().html("&nbsp;Expand&nbsp;");
        else  // EXPAND 
        {
            $(this).empty().html("Collapse");
            $expand_area.find(".gallery").trigger("resize");
            // var w = $expand_area.width();
            // console.log("w: " + w)
            // $(this).parent().parent().find(".expand-area").css({"width":w,"height":"auto", "opacity": "0", "pointer-events": "none", "overflow" : "hidden", "position":"absolute", "padding": "2em 0 .5em 0" });
            // console.log($expand_area.height());
            // var h = parseFloat($expand_area.css("height")) + 2.5 * parseInt($expand_area.css("font-size")) + "px";
            // console.log(h);
            // $(this).parent().parent().find(".expand-area").css({"height": "0", "width":"100%", "position": "relative", "visibility": "visible", "pointer-events": "auto", "padding": "0" });
            
            // $(this).parent().parent().find(".expand-area").stop().animate({
            //     "height": h, "paddingTop": "2em", "paddingRight": "0", "paddingBottom": "0.5em", "PaddingLeft": "0"
            // }, dur, function () {
            //     console.log($(this).height());
            //     $(this).delay(10000).height('auto');
            //     console.log($(this).height());
            // });
        }
    });


    $(".taskbar .filter").click(function () {
        $(this).toggleClass("selected").toggleClass("unselected");
        var selected = []
        $(".taskbar .filter").each(function () {
            if ($(this).hasClass("selected"))
                selected.push($(this).attr('id'));
        });
        
        if (selected.length == 0) {
            $(".project").show()
        }
        
        else {
            selected.forEach(function (id) {
                $(".projec#" + id).show(300);
            })
        }

    })

    $(".project .collapse-btn, .project .expand-btn").mouseenter(function () {
        if ($(this).html() == "Collapse")  // COLLAPSE 
            $(this).stop().animate({  "padding": ".75em 3em"}, projectBtnAniDur, projectBtnEasing);
        else  // EXPAND 
            $(this).stop().animate({ "padding": ".75em 4.5em"}, projectBtnAniDur, projectBtnEasing);
    });
    $(".project .collapse-btn, .project .expand-btn").mouseleave(function () {
        if ($(this).html() == "Collapse")  // COLLAPSE 
            $(this).stop().animate({  "padding": ".75em 4.5em"}, projectBtnAniDur, projectBtnEasing);
        else  // EXPAND 
            $(this).stop().animate({  "padding": ".75em 3em"}, projectBtnAniDur, projectBtnEasing);
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

});

$(document).scroll(function() {
    //console.log("scrolled " + $(document).scrollTop());
});


