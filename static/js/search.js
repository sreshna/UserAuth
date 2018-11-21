$(".search-button").click(function(e) {
    e.preventDefault();
    var q = $("#search_parameter").val();
    console.log(q);
      $.ajax({
    type: "GET",
    url: '/search/',
    data: {"q": q},
    success: function() {
//      $('#contact_form').html("<div id='message'></div>");
      }
    })
});

$("#suggest_button").click(function(e) {
    e.preventDefault();
    var q = $("#suggest_button").val();
    console.log(q);
      $.ajax({
    type: "GET",
    url: '/search/',
    data: {"q": q},
    success: function() {
//      $('#contact_form').html("<div id='message'></div>");
      }
    })
});