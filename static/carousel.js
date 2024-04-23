$(document).ready(function() {
    $(".carousel").each(function() {
        var carousel = $(this);
        var items = carousel.find(".carousel__item");
        var buttonsHtml = items.map(function() {
            return '<span class="carousel__button"></span>';
        }).get();

        carousel.append(
            '<div class="carousel__nav">' +
                buttonsHtml.join("") +
            '</div>'
        );

        var buttons = carousel.find(".carousel__button");
        var prevButton = carousel.find(".prev");
        var nextButton = carousel.find(".next");

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

        // Event listener for next button
        nextButton.on("click", function() {
            var current = carousel.find(".carousel__item--selected");
            var next = current.next(".carousel__item");

            if (next.length === 0) {
                next = items.first(); // Loop back to the first item
            }

            current.removeClass("carousel__item--selected");
            next.addClass("carousel__item--selected");

            // Update button selection if needed
            buttons.removeClass("carousel__button--selected");
            buttons.eq(next.index()).addClass("carousel__button--selected");
        });

        // Event listener for previous button
        prevButton.on("click", function() {
            var current = carousel.find(".carousel__item--selected");
            var prev = current.prev(".carousel__item");

            if (prev.length === 0) {
                prev = items.last(); // Loop back to the last item
            }

            current.removeClass("carousel__item--selected");
            prev.addClass("carousel__item--selected");

            // Update button selection if needed
            buttons.removeClass("carousel__button--selected");
            buttons.eq(prev.index()).addClass("carousel__button--selected");
        });
    });
});
