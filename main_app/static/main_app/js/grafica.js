let datosGrafica=[]
let colores_calidades_treal={"-6":"red","-3":"orange","-1":"white","1":"white","2":"yellow","3":"gray","5":"pink","6":"cyan",7:"whitw",8:"white"}

function mostrarSenal(cod_senal){
  async_html_call_and_do("/senal/"+cod_senal,document.getElementById("Contenido_ficha_senal"),solicitudGraficaSimple,cod_senal,"Error senal no encontrada");
  document.getElementById("cuerpo").scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
}

function solicitudGraficaSimple(cod_senal){
  async_json_call("/grafica_simple/"+cod_senal,datosGrafica,crearGraficaSimple,"No se han encontrado valores de la señal")
}

function crearGraficaSimple(datosRecibidos){
  console.log(datosRecibidos)
  senal=datosRecibidos["senal"]
  var leyenda = Array("",senal["id_senal"]+ " "+ senal["tipo_senal"] + " " + senal["unid_ing_id"]);
  data=[datosRecibidos["etiquetas"],datosRecibidos["valores"]]
  calidades=datosRecibidos["calidades"]
  var options = {
    width: 1000,
    height: 400,
    tzDate:data => uPlot.tzDate(new Date(data * 1e3), 'CET'),
    fmtDate: tpl => {
                        tpl=tpl.replace("{M}/{D}","{D}/{MM}")
                        tpl=tpl.replace("{h}{aa}","{H}:00")
                        tpl=tpl.replace("{h}:{mm}{aa}","{H}:{mm}")
                        tpl=tpl.replace("{YYYY}-{MM}-{DD}","{DD}/{MM}/{YYYY}")
                        return uPlot.fmtDate(tpl)
    },
    plugins: [
      tooltipsPlugin({
        cursorMemo,
      }),
    ],

    series: [
    {},
    {
      show: true,
      label: leyenda[1],
      stroke: "blue",
      fill: "rgba(16, 16, 255, 0.4)",
      dash: [5, 5],
      tag: senal["id_senal"],
      unidad:senal["unid_ing_id"]
    }
    ],
    scales:{
    "x":{},
    "y":{}
  },
    axes:[
      {},
      {
        label: senal["unid_ing_id"]
      }
    ]
  ,
    cursor: { drag:  { x: true, y: true } }
  };

  let uplot = new uPlot(options, data, document.getElementById("grafica_container"));
  console.log(uplot);
  crearTabla(data,calidades,options);
  abrirFicha("Ficha_senal")
}

function crearTabla(datosRecibidos,calidades,options){
  console.log(datosRecibidos)
  tabla=document.getElementById("tabla_valores_grafica")
  for(i=0;i<datosRecibidos[0].length;i++){
    var fila=tabla.insertRow(-1);
    var cell1=fila.insertCell(0);
    var cell2=fila.insertCell(1);
    cell1.innerHTML=options.tzDate(datosRecibidos[0][i]).toLocaleString();
    cell2.innerHTML=datosRecibidos[1][i];
    cell1.style.backgroundColor=colores_calidades_treal[calidades[i]] //SOLO VALE ^PARA TREAL; HAY QUE CAMBIARLO PARA CONSOLIDADOS!!
    cell2.style.backgroundColor=colores_calidades_treal[calidades[i]] //SOLO VALE ^PARA TREAL; HAY QUE CAMBIARLO PARA CONSOLIDADOS!!
  }

}

function verTabla(){

}
