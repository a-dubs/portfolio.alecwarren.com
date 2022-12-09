$(function () {

function tetris_ai_simulation_gallery() {
    var slidewidth = $("#tetris_ai_simulation_gallery").width()
    var animationduration =600;
    // Comment the line below out if you do not want the automatic slide changing 
    var currentslide = 1;
    var tetris_ai_simulation_gallery_hidden = $("#tetris_ai_simulation_gallery").is(":visible");
    var tetris_ai_simulation_gallery_timer = setInterval(goToSlide, 5000);
    // edit the number above to change how often (in milliseconds) the slides change
    var tempbar = document.createElement("li");
    tempbar.className = "bar";
    $("#tetris_ai_simulation_gallery #bar_island_ul").get(0).appendChild(tempbar);
    var bar_opacity = $("#tetris_ai_simulation_gallery .bar").css("opacity");
    $("#tetris_ai_simulation_gallery .bar").remove()
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
        if ($("#tetris_ai_simulation_gallery").is(":visible")) {
            
            if (tetris_ai_simulation_gallery_hidden)
            {
                clearInterval(tetris_ai_simulation_gallery_timer);
                tetris_ai_simulation_gallery_timer = setInterval(goToSlide, 5000);
                tetris_ai_simulation_gallery_hidden = false;
            }    
            else {
                if (slideNumber > numofslides) {
                    slideNumber = 1;
                }
                if (!$(jQuery(slides[oldslide - 1])).is(':animated')) {
                    clearInterval(tetris_ai_simulation_gallery_timer);
                    tetris_ai_simulation_gallery_timer = setInterval(goToSlide, 5000);
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
            tetris_ai_simulation_gallery_hidden = true;
            clearInterval(tetris_ai_simulation_gallery_timer);
            tetris_ai_simulation_gallery_timer = setInterval(goToSlide, 100);
        }

    }

    var oldslide = 1;
    var slides = document.getElementById("tetris_ai_simulation_gallery").querySelectorAll(".slide");

    var numofslides = $('#tetris_ai_simulation_gallery #carousel').children().length;
    var min = 0;

    var gallery_btn_hovered = false;

    //$("#tetris_ai_simulation_gallery .slide").css("width", slidewidth);

    // start slideshow on "second slide" or the first non-clone slide
    $(slides[0]).css({
        width: slidewidth,
        opacity: 1
    })

    // click button to advance to the left
    $("#tetris_ai_simulation_gallery .gallery-btn#left").click(function () {
        tetris_ai_simulation_gallery_hidden = false;
        if (!$(jQuery(slides[oldslide - 1])).is(':animated')) {
            if (currentslide == 1) {
                goToSlide(numofslides)
            } else {
                goToSlide(currentslide - 1)
            }
        }
    });

    // click button to advance to the right
    $("#tetris_ai_simulation_gallery .gallery-btn#right").click(function () {
        tetris_ai_simulation_gallery_hidden = false;
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
        $("#tetris_ai_simulation_gallery #bar_island_ul").get(0).appendChild(newbar);
    }

    // create inner bars
    var bars = document.getElementById("tetris_ai_simulation_gallery").querySelectorAll(".bar")
    for (i = 0; i < bars.length; i++) {
        var newinnerbar = document.createElement("div")
        newinnerbar.className = "innerbar"
        bars[i].appendChild(newinnerbar)
    }


    // set first bar as selected bar	
    bars[0].classList.add("selected")
    // animate bars when hovered
    $("#tetris_ai_simulation_gallery .bar").hover(function() {
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
    var gallery_btn_opacity = $("#tetris_ai_simulation_gallery .gallery-btn").css("opacity");

    // animate slider buttons when hovered
    $("#tetris_ai_simulation_gallery .gallery-btn").hover(function() {
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
    $("#tetris_ai_simulation_gallery .bar").click(function () {
        tetris_ai_simulation_gallery_hidden = false;
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
        slidewidth = document.getElementById("tetris_ai_simulation_gallery").offsetWidth;
        farthest = ((slides - 1) * slidewidth);
        clearInterval(tetris_ai_simulation_gallery_timer);
        tetris_ai_simulation_gallery_timer = setInterval(goToSlide, 5000);
        slideduration = slidewidth * .75;
        $("#tetris_ai_simulation_gallery .slide").css("width", slidewidth);
        $("#tetris_ai_simulation_gallery #carousel").css("width", slidewidth * slides);
        for (i = 0; i < slides.length; i++) {
            if (i + 1 != currentslide)
                jQuery(slides[i]).css("width", 0);
        }

    }
    // adjust width of slides if browser window resizes
    $(window).resize(resizeGallery);
    $("#tetris_ai_simulation_gallery").resize(resizeGallery);
    document.getElementById("tetris_ai_simulation_gallery").addEventListener("resize", resizeGallery);
}
tetris_ai_simulation_gallery();

});