$(function() {
    $('#status-menu').change(function() {
        if ($('#status-menu').is(':checked')) {
            $('#menu-slide').addClass('muestra');
        } else
            $('#menu-slide').removeClass('muestra');
    })

    $('#status-panel').change(function() {
        if ($('#status-panel').is(':checked')) {
            $('#my-panel').css("margin-left", "0");
        } else
            $('#my-panel').css("margin-left", "-100vw");
    })
});