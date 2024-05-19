

$( document ).ready(function() {

     $('.owl-carousel').owlCarousel({
        loop:true,
        margin:0,
        nav:true,
        autoplay: true,
        dots: true,
        autoplayTimeout: 5000,
        navText:['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    })


});


$(document).ready(function(){
    $(".filter-button").click(function(){
        var value = $(this).attr('data-filter');
        
        if(value == "all") {
            $('.gallery_product').show('1000'); // Show all images if "All" is selected
        } else {
            // Hide images not matching the selected filter, and show those matching the filter
            $(".gallery_product").not('.'+value).hide('3000');
            $(".gallery_product").filter('.'+value).show('3000');
        }

        // Update the active class for filter buttons
        $(".filter-button").removeClass("active");
        $(this).addClass("active");
    });
});
