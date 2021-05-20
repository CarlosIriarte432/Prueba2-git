$('#submit-form').click(function (event) {

    event.preventDefault();

    var capital = $("#capital").val();
    var apikey = "d67866c73e7743798ec25136212005&Q=";
    var url = "http://api.weatherapi.com/v1/forecast.json?key=";
    var final ="&days=3&aqi=no&alerts=no";

    fetch(url + apikey + capital + final)
        .then(response => response.json())
        .then(data =>
            {
                console.log(data);
                var $temperatura_ciudad = $('h1').text(data.current.temp_c);
                var $pronostico1 = $('h2').text(data.forecast.forecastday[0].day.avgtemp_c)
                var $pronostico2 = $('h3').text(data.forecast.forecastday[1].day.avgtemp_c)
                var $pronostico3 = $('h4').text(data.forecast.forecastday[2].day.avgtemp_c)
                



                $('info').empty();
                $('info')
                    .append($temperatura_ciudad)
                    .append($pronostico1)
                    .append($pronostico2)
                    .append($pronostico3)
            






            })

});
