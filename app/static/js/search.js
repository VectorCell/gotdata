$(document).ready(function() {
    $("#search-form").submit(function(event) {
        var input = $("#search-input")[0].value;
        input = input.split(" ").join("+");
        window.location.replace("/search/" + input);

        event.preventDefault();
    });
});