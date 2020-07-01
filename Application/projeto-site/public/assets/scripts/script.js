// scroll suave
$(function () {
  $('a[href*="#"]:not([href="#"])').click(function () {

    var target = $(this.hash);

    if (target.length) {
      $('html, body').animate({
        scrollTop: target.offset().top
      }, 500);
      $('.header').css('margin-top', "-80px");
      $('.showcase').css('margin-bottom', "180px");
      // $('.contextualizacao').css('margin-bottom', "180px");
      // $('.conhecendo').css('margin-bottom', "180px");
      // $('#sobreNos').css('margin-bottom', "180px");
      return false;
    }

    // if (url.indexOf('#header') >= 0) {
    //   $('#header').css('margin-top',120);
    //   $('#home').css('margin-top',"-120px");
    //   }

  });
});
// $('.nav-container a[href^="#"]').on('click', function(e) {
//   e.preventDefault();
  
//   var id = $(this).attr('href'), 
//       targetOffset = $(id).offset().top;
  
//   $('html, body').animate({ 
//     scrollTop: targetOffset - 100
//    }, 500);
// });