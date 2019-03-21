<html>
    <head>
        <meta charset="utf-8">
        <title>Гороскоп на сегодня</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
        integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
        crossorigin="anonymous">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    </head>
    <body>
        <div class="container">
            <h1 id="main-header">Что день {{ date }} готовит</h1>
            <div class="row">
                <div class="col" id="p-0"></div>
                <div class="col" id="p-1"></div>
                <div class="col" id="p-2"></div>
                <div class="col" id="p-3"></div>
                <div class="col" id="p-4"></div>
                <div class="col" id="p-5"></div>
            </div>   
        </div>
    </body>
    <script language="javascript">
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
    </script>    
</html>