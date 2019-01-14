'use strict';

$(() => {
  $('a[href*="#"]').click(event => {
    console.log('clicked');
    event.preventDefault();
    var targetHash = (($(event.target).length) ? $(event.target)[0] : $(event.target)).hash;
    var targetScroll = $(targetHash).offset().top;
    var bottomLimit = $(document).height() - $(window).height();
    $('html, body').stop().animate({
      scrollTop: ((targetScroll > bottomLimit) ? bottomLimit : targetScroll) + "px"
    }, 800, 'easeOutCubic', () => {
      window.location = targetHash;
    });
  });
});