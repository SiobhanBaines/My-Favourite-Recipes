$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.carousel').carousel();
    $('.modal').modal();
    $('select').formSelect();
    $('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));
});
