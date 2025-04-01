// app.js
document.getElementById('predict-form').addEventListener('submit', function (e) {
    e.preventDefault();
    formData = new FormData();
    formData.append('location', document.getElementById('location').value);
    formData.append('type', document.getElementById('type').value);
    formData.append('beds', document.getElementById('beds').value);
    formData.append('baths', document.getElementById('baths').value);
    formData.append('sq_feet', document.getElementById('sq_feet').value);
    formData.append('furnishingb', document.getElementById('furnishingb').value);
    formData.append('smokingb', document.getElementById('smokingb').value);
    formData.append('catsb', document.getElementById('catsb').value);
    formData.append('dogsb', document.getElementById('dogsb').value);

    fetch("/api/get_estimated_price", {method: "POST", body: formData}).then(response => response.json()).then(data => {
        document.getElementById('result').innerText = `Average rent should be: $${data['estimated_price']}`;
    }).catch (err => {
        console.log("Encountered Error: " ,err)
        document.getElementById('result').innerText = "Encountered Error. Try again.";
    })
  });
  
  

  function get_location(){
    return document.getElementById('location').value;
  }
  function get_type(){
    return document.getElementById('type').value;
  }
  function get_beds(){
    return document.getElementById('beds').value;
  }
  function get_baths(){
    return document.getElementById('baths').value;
  }
  function get_sq_feet(){
    return document.getElementById('sq_feet').value;
  }
  function get_furnishingb(){
    return document.getElementById('furnishingb').value;
  }
  function get_smokingb(){
    return document.getElementById('smokingb').value;
  }
  function get_catsb(){
    return document.getElementById('catsb').value;
  }
  function get_dogsb(){
    return document.getElementById('dogsb').value;
  }
