/*async function pruebaFichaje(){
    var url='https://fichajes.tragsa.es/open/j_spring_security_check'
    var data = new FormData();
    data.append('ACTION', 'ACTION_VALIDER_LOGIN');
    data.append('username', 'jnunez2');
    data.append('password', '0KDU1nod__1');
    htmlelement=document.getElementById("loginWrap")
    let myPromise = new Promise(function(resolve) {
        let req = new XMLHttpRequest();
        req.open('POST', url,true);
        req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        req.onload = function() {
          if (req.status == 200) {
            resolve(req.response);
          } else {
            resolve(req-status + " : " + errormsg);
          }
        };
        req.send("ACTION=ACTION_VALIDER_LOGIN&username=jnunez2&password=0KDU1nod__1");
      });
      htmlelement.innerHTML = await myPromise;
      console.log("Recibido");
      console.log(htmlelement);
      }

pruebaFichaje()
*/
// POST https://fichajes.tragsa.es/open/bwpDispatchServlet?1741772501424

/*https://fichajes.tragsa.es/open/webgtp/badge
_csrf_bodet	"1b0f95d1-a873-4be7-a6c9-2984aafd96a7"
ACTION	"BADGER_ES"
ACTION_SWITCH	""
choixApplication	""
application	"1"
choixOption	""
JETON_INTRANET	"1741772752193"
coordonneeLongitude	""
coordonneeLatitude	""
coordonneePrecision	""
coordonneeIndicateur	"-1"
*/