/* -----------------------------------FUNCION PARA AJAX CON HTML ------------------------------------------*/
async function async_html_call(url,htmlelement,errormsg) {
  let myPromise = new Promise(function(resolve) {
    let req = new XMLHttpRequest();
    req.open('GET', url);
    req.onload = function() {
      if (req.status == 200) {
        resolve(req.response);
      } else {
        resolve(req-status + " : " + errormsg);
      }
    };
    req.send();
  });
  htmlelement.innerHTML = await myPromise;
}

async function async_html_call_and_do(url,htmlelement,fun,argument,errormsg) {
  let myPromise = new Promise(function(resolve) {
    let req = new XMLHttpRequest();
    req.open('GET', url);
    req.onload = function() {
      if (req.status == 200) {
        resolve(req.response);
      } else {
        resolve(req-status + " : " + errormsg);
      }
    };
    req.send();
  });
  htmlelement.innerHTML = await myPromise;
  fun(argument);
}



async function async_json_call(url,dataobject,funcion,errormsg) {
  let myPromise = new Promise(function(resolve,reject) {
    let req = new XMLHttpRequest();
    req.open('GET', url);
    req.onload = function() {
      if (req.status == 200) {
        resolve(req.response);
      } else {        
        reject(req.response);
      }
    };
    req.send();
  });
  try {
      json=await myPromise
      
      dataobject= JSON.parse(json);
    } catch (e) {
    
    }
    funcion(dataobject);
  }
