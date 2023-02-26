async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json',
        "X-CSRFToken": 'mrcNwMnfjoldLAhvR8MZLtIRmpKxtR17LD9QxpFepLOKlnFIAW6ksH6CGio8pkBg'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }





function lights(){
    var lig = document.getElementById('a')
    if (lig.checked == true){
                  
          postData('http://192.168.80.20:8000/lights-update/',  {
        "id": 0,
        "testlight": true
    })
            .then(data => {
              console.log(data);
// JSON data parsed by `data.json()` call
            });
    }
    else if(lig.checked == false){
        postData('http://192.168.80.20:8000/lights-update/',  {
        "id": 0,
        "testlight": false
    })
    }

}
