$(function() {
    "use strict";




    /* ==========================================================================
   Preload
   ========================================================================== */
    
    $(window).load(function() {
        $("#status").fadeOut();
        $("#preloader").delay(1000).fadeOut("slow");
    });


  

    /* ==========================================================================
   On Scroll animation
   ========================================================================== */
    
    if ($(window).width() > 240) {
        new WOW().init();
    };
    

    /* ==========================================================================
   Fade On Scroll
   ========================================================================== */
    
 
    

    



});
