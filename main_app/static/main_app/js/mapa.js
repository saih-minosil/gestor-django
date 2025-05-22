tipos=Array()//'A','N','E','M','P', 'CH','R')
markers=Array()
var EstacionIcon = L.Icon.extend({
    options: {
        iconSize:     [16, 16],
        iconAnchor:   [8, 8],
        popupAnchor:  [0, -10]
    }
});
var iconos={
    iconoAforo : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_a.png'}),
    iconoNivel : new EstacionIcon({iconUrl:'main_app/static/main_app/img/ico_n.png'}),
    iconoEmbalse : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_e.png'}),
    iconoMeteo : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_m.gif'}),
    iconoPluvio : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_p.gif'}),
    iconoCalidad : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_q.gif'}),
    iconoVertido : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_v.gif'}),
    iconoRiego : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_r.png'}),
    iconoPiezo : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_pz.gif'}),
    iconoAforoActivacion : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_a_a.gif'}),
    iconoNivelActivacion : new EstacionIcon({iconUrl:'main_app/static/main_app/img/ico_n_a.gif'}),
    iconoAforoPrealerta : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_a_aa.gif'}),
    iconoNivelPrealerta : new EstacionIcon({iconUrl:'main_app/static/main_app/img/ico_n_aa.gif'}),
    iconoAforoAlerta : new EstacionIcon({iconUrl: 'main_app/static/main_app/img/ico_a_aaa.gif'}),
    iconoNivelAlerta : new EstacionIcon({iconUrl:'main_app/static/main_app/img/ico_n_aaa.gif'}),
}
let map;

function cargarMapa(){
    map = L.map('map').setView([42.58, -7.09], 8);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        minZoom:8,
        maxZoom: 13,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
}


function cargarPopup(event){
    console.log(event)
   var element=event.target._popup._contentNode;
   var id_estacion = event.target.options.id.substring(7);
   console.log(id_estacion);
   async_html_call("/estacion_popup/"+id_estacion,element,"No hay datos de la estación")
}


function mostrarMarcadores(estaciones)
{
    for(i=0;i<markers.length;i++){
      markers[i].remove()
    }
    for (estacion of estaciones){
        var tipo = estacion.tipo;
        if(tipos.includes(tipo)){
            console.log(estacion.icono);
            var marker = L.marker([estacion.x,estacion.y],{icon: iconos[estacion.icono], id:"marker_"+estacion.codigo}).addTo(map);
            //console.log(marker);
            marker.bindPopup();
            marker.addEventListener("click",cargarPopup,false);
            markers.push(marker);
        }
    }
    document.getElementById("div_selectorzonas").hidden=true;
    document.getElementById("Fila_titulo_filtro_tipo_estacion").hidden=true;
}

function mostrar(){
    mostrarMarcadores(estaciones);
}


