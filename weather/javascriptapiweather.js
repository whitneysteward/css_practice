$.ajax({
      url:"http://api.openweathermap.org/data/2.5/weather?q="+ "Portland,OR" +"&appid=9ef3311b380d2586bf47ff522529e7a9",
      method: 'GET',
      success:function(data) {

    console.log (data.weather[0].main);
        var weather = (data.main.temp);
        // get temp from kelvin to *F
        var temp = Math.round((data.main.temp * 1.8 - 459.87) * 100) / 100 ;
        if (data.weather[0].main=="Clouds"){
    console.log("if")
          $("#imagediv").html("<img src='cloud.jpg'>");
          alert("FEELIN CLOUDY!")
        }
        else if (data.weather[0].main=="Rain"){
          $("#imagediv").html("<img src='rain.png'");
          alert("Rain... typical");
        }
        else{$("#imagediv").html("<img src='sun.png'");
        alert("Woah... Sun!");
        }

      }
   });
