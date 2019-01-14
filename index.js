'use strict';

$(() => {
  $('a[href*="#"]').click(event => {
    console.log('clicked');
    event.preventDefault();
    var targetHash = (($(event.target).length) ? $(event.target)[0] : $(event.target)).hash;
    var targetScroll = $(targetHash).offset().top;
    console.log(targetScroll);
    var bottomLimit = $(document).height() - $(window).height();
    console.log(((targetScroll > bottomLimit) ? bottomLimit : targetScroll) + "px");
    $('html, body').animate({
      scrollTop: ((targetScroll > bottomLimit) ? bottomLimit : targetScroll) + "px"
    }, 800, 'easeOutCubic', () => {
      window.location = targetHash;
    });
  });
});