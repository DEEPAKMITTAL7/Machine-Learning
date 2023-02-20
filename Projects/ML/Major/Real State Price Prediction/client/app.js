function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

  function getBalconyValue() {
    var uiBalcony = document.getElementsByName("uiBalcony");
    for(var i in uiBalcony) {
      if(uiBalcony[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var balcony = getBalconyValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var areas = document.getElementById("uiareas");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    //var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        balcony:balcony,
        location: location.value,
        areas : areas.value

    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded for locations" );
    //var url = "http://127.0.0.1:5000/locations"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/locations"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for locations request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });

    console.log( "document loaded for area" );
    //var url = "http://127.0.0.1:5000/areas"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/areas"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for areas request");
        if(data) {
            var areas = data.areas;
            var uiareas = document.getElementById("uiareas");
            $('#uiareas').empty();
            for(var i in areas) {
                var opt = new Option(areas[i]);
                $('#uiareas').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;