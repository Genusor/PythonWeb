advice_url = "http://localhost:8080/api/forecasts";
$("#main-header").click(function() {

    $.getJSON(advice_url, function(data){
        advice = data['prophecies']
        set_content_in_divs(advice);
    });
    
});

function set_content_in_divs(paragraphs) {
    $.each(paragraphs, function(i, d) {
      p = $("#p-" + i);
      p.html("<p>" + d + "</p>");
    })
}