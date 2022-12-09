$(function () {

function 3d_modelling_gallery() {
    var slidewidth = $("#3d_modelling_gallery").width()
    var animationduration =600;
    // Comment the line below out if you do not want the automatic slide changing 
    var currentslide = 1;
    var 3d_modelling_gallery_hidden = $("#3d_modelling_gallery").is(":visible");
    var 3d_modelling_gallery_timer = setInterval(goToSlide, 5000);
    // edit the number above to change how often (in milliseconds) the slides change
    var tempbar = document.createElement("li");
    tempbar.className = "bar";
    $("#3d_modelling_gallery #bar_island_ul").get(0).appendChild(tempbar);
    var bar_opacity = $("#3d_modelling_gallery .bar").css("opacity");
    $("#3d_modelling_gallery .bar").remove()
    // update which bar is the selected bar based on the given slide
    function updateBars(slideNumber) { // must come before currentslide value is updated
    
        //bars[oldslide - 1].classList.remove("selected");
        jQuery(bars[oldslide - 1]).removeClass("selected");
        jQuery(bars[currentslide - 1]).addClass("selected");
        jQuery(bars[oldslide - 1]).animate({
            "opacity": bar_opacity
        }, 150)
        //bars[slideNumber - 1].classList.add("selected")
        jQuery(bars[slideNumber - 1]).animate({
            "opacity": 1
        }, 150)
    }

    // jump to specified slide number (including clones)
    function goToSlide(slideNumber = currentslide + 1) {
        if ($("#3d_modelling_gallery").is(":visible")) {
            
            if (3d_modelling_gallery_hidden)
            {
                clearInterval(3d_modelling_gallery_timer);
                3d_modelling_gallery_timer = setInterval(goToSlide, 5000);
                3d_modelling_gallery_hidden = false;
            }    
            else {
                if (slideNumber > numofslides) {
                    slideNumber = 1;
                }
                if (!$(jQuery(slides[oldslide - 1])).is(':animated')) {
                    clearInterval(3d_modelling_gallery_timer);
                    3d_modelling_gallery_timer = setInterval(goToSlide, 5000);
                    oldslide = currentslide;
                    currentslide = slideNumber;
                    jQuery(slides[oldslide - 1]).css("z-index", 3);
                    jQuery(slides[currentslide - 1]).css("z-index", 2);
    
                    jQuery(slides[currentslide - 1]).css("width", slidewidth);
                    jQuery(slides[currentslide - 1]).css({
                        "opacity": 1
                    });
                    jQuery(slides[oldslide - 1]).animate({
                        "opacity": 0
                    }, animationduration, "easeOutCubic");
    
                    setTimeout(function () {
                        jQuery(slides[oldslide - 1]).css("width", 0);
                    }, animationduration, "easeOutCubic")
                    updateBars(currentslide)
                }
            }
        }
        else {
            3d_modelling_gallery_hidden = true;
            clearInterval(3d_modelling_gallery_timer);
            3d_modelling_gallery_timer = setInterval(goToSlide, 100);
        }

    }

    var oldslide = 1;
    var slides = document.getElementById("3d_modelling_gallery").querySelectorAll(".slide");

    var numofslides = $('#3d_modelling_gallery #carousel').children().length;
    var min = 0;

    var gallery_btn_hovered = false;

    //$("#3d_modelling_gallery .slide").css("width", slidewidth);

    // start slideshow on "second slide" or the first non-clone slide
    $(slides[0]).css({
        width: slidewidth,
        opacity: 1
    })

    // click button to advance to the left
    $("#3d_modelling_gallery .gallery-btn#left").click(function () {
        3d_modelling_gallery_hidden = false;
        if (!$(jQuery(slides[oldslide - 1])).is(':animated')) {
            if (currentslide == 1) {
                goToSlide(numofslides)
            } else {
                goToSlide(currentslide - 1)
            }
        }
    });

    // click button to advance to the right
    $("#3d_modelling_gallery .gallery-btn#right").click(function () {
        3d_modelling_gallery_hidden = false;
        if (!$(jQuery(slides[oldslide - 1])).is(':animated')) {
            if (currentslide == numofslides) {
                goToSlide(1)
            } else {
                goToSlide(currentslide + 1)
            }
        }
    });

    // create outer bar containers automatically based off of number slides
    for (i = 0; i < numofslides; i++) {
        var newbar = document.createElement("li");
        newbar.className = "bar";
        $("#3d_modelling_gallery #bar_island_ul").get(0).appendChild(newbar);
    }

    // create inner bars
    var bars = document.getElementById("3d_modelling_gallery").querySelectorAll(".bar")
    for (i = 0; i < bars.length; i++) {
        var newinnerbar = document.createElement("div")
        newinnerbar.className = "innerbar"
        bars[i].appendChild(newinnerbar)
    }


    // set first bar as selected bar	
    bars[0].classList.add("selected")
    // animate bars when hovered
    $("#3d_modelling_gallery .bar").hover(function() {
        $(this).stop().animate({
            "opacity": 1
        }, 150)
    }, function() {
        if (!($(this).hasClass("selected"))) {
            
            $(this).stop().animate({
                "opacity": bar_opacity
            }, 100)
        }
    });

    // original opacity of slider button
    var gallery_btn_opacity = $("#3d_modelling_gallery .gallery-btn").css("opacity");

    // animate slider buttons when hovered
    $("#3d_modelling_gallery .gallery-btn").hover(function() {
        gallery_btn_hovered = true;

        $(this).stop().animate({
            "opacity": 1
        }, 100)
    }, function() {
        gallery_btn_hovered = false;
        $(this).animate({
            "opacity": gallery_btn_opacity
        }, 140)
    });



    // change highlighted bar & move slideshow
    $("#3d_modelling_gallery .bar").click(function () {
        3d_modelling_gallery_hidden = false;
        if (!$(jQuery(slides[oldslide - 1])).is(':animated')) {
            if (!$(this).hasClass("selected")) {
                $(this).toggleClass("selected")
                for (i = 0; i < bars.length; i++) {
                    if ($(this)[0] === bars[i]) {
                        goToSlide(i + 1);
                    }
                }
            }
        }
    });
    function resizeGallery() {
        slidewidth = document.getElementById("3d_modelling_gallery").offsetWidth;
        farthest = ((slides - 1) * slidewidth);
        clearInterval(3d_modelling_gallery_timer);
        3d_modelling_gallery_timer = setInterval(goToSlide, 5000);
        slideduration = slidewidth * .75;
        $("#3d_modelling_gallery .slide").css("width", slidewidth);
        $("#3d_modelling_gallery #carousel").css("width", slidewidth * slides);
        for (i = 0; i < slides.length; i++) {
            if (i + 1 != currentslide)
                jQuery(slides[i]).css("width", 0);
        }

    }
    // adjust width of slides if browser window resizes
    $(window).resize(resizeGallery);
    $("#3d_modelling_gallery").resize(resizeGallery);
    document.getElementById("3d_modelling_gallery").addEventListener("resize", resizeGallery);
}
3d_modelling_gallery();

});