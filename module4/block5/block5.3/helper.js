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

obj_hours=document.getElementById("main-header");
name_month = new Array ("января", "февраля", "марта", "апреля", "мая", "июня",
"июля", "августа", "сентября", "октября", "ноября", "декабря");

function wr_hours() {
    time=new Date;
    time_date=time.getDate();
    time_wr=((time_date<10)?'0':'')+time_date;
    time_wr="Сегодня "+time_wr+" "+name_month[time.getMonth()]+" "+time.getFullYear()+" г. чтобы получить предсказание кликните на меня";
    obj_hours.innerHTML=time_wr;
}
wr_hours();
setInterval("wr_hours();",1000);