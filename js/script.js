/* global $*/

$(function() {
  $('.menu-trigger').on('click', function(event) {
    $(this).toggleClass('active');
    $('#sp-menu').fadeToggle();
    event.preventDefault();
  });
  $('#back a').on('click',function(event){
    $('body, html').animate({
      scrollTop:0
    }, 800);
    event.preventDefault();
  });
});