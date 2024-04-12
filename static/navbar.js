
$(document).ready(function() {
  // Get current page URL and split by '/'
  var pathSegments = window.location.pathname.split('/').filter(Boolean);

  // Get only the first segment of the path
  var mainSection = pathSegments.length > 0 ? '/' + pathSegments[0] : '/';

  // Loop through nav links
  $('.nav-link').each(function() {
      var $this = $(this);
      // Split the href attribute of the link and get the first segment
      var hrefSegments = $this.attr('href').split('/').filter(Boolean);
      var mainHrefSection = hrefSegments.length > 0 ? '/' + hrefSegments[0] : '/';

      // If main section of href matches main section of current path, add active class
      if(mainHrefSection === mainSection) {
          $this.addClass('active');
      }
  });
});
