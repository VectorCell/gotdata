$(document).ready(function() {
  var $item = $('.carousel .item');

  $item.height($(window).height());
  $item.addClass('fill');

  $('.carousel img').each(function() {
    var $src = $(this).attr('src');
    $(this).parent().css({
      'background-image': 'url('+$src+')'
    });
    $(this).remove();
  });

  $(window).on('resize', function() {
    $item.height($(window).height());
  });

  $('.carousel').carousel({
    interval: 5000,
    pause: "false"
  });
});
