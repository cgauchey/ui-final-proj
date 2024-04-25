$(document).ready(function() {
    $(".prev-slide").click(function() {
        let currentSlide = $(".carousel__item--selected");
        let prevSlide = currentSlide.prev();

        if (prevSlide.length === 0) {
            prevSlide = $(".carousel__item").last();
        }

        currentSlide.removeClass("carousel__item--selected");
        prevSlide.addClass("carousel__item--selected");

        updateNavButtons();
    });

    $(".next-slide").click(function() {
        let currentSlide = $(".carousel__item--selected");
        let index = $(".carousel__item--selected").index();
        let nextSlide = currentSlide.next();
        // if the current slide is the last out of four slides
        if (index === 3) {
            nextSlide = $(".carousel__item").first();
        }

        currentSlide.removeClass("carousel__item--selected");
        nextSlide.addClass("carousel__item--selected");

        updateNavButtons();

    });
    $(".carousel").each(function() {
        let carousel = $(this);
        let items = carousel.find(".carousel__item");
        let buttonsHtml = items.map(function() {
            return '<span class="carousel__button"></span>';
        }).get();

        carousel.append(
            '<div class="carousel__nav">' +
                buttonsHtml.join("") +
            '</div>'
        );

        let buttons = carousel.find(".carousel__button");

        buttons.each(function(i) {
            $(this).on("click", function() {
                // Un-select all items
                items.removeClass("carousel__item--selected");
                buttons.removeClass("carousel__button--selected");

                items.eq(i).addClass("carousel__item--selected");
                $(this).addClass("carousel__button--selected");
            });
        });

        // Select the first item on page load
        items.first().addClass("carousel__item--selected");
        buttons.first().addClass("carousel__button--selected");
    });

    function updateNavButtons() {
        let currentSlideIndex = $(".carousel__item--selected").index();
        let buttons = $(".carousel__button");
        buttons.removeClass("carousel__button--selected");
        buttons.eq(currentSlideIndex).addClass("carousel__button--selected");
    }
});
