let uplot;

let datosGrafica=[];

/*
function mostrarSenal(cod_senal){
  async_html_call_and_do("/senal/"+cod_senal,document.getElementById("Contenido_ficha_senal"),solicitudGraficaSimple,cod_senal,"Error senal no encontrada");
  document.getElementById("cuerpo").scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
}
*/
function solicitudGraficaSimple(cod_estacion){
  async_json_call("/vsad/datos/"+cod_estacion,datosGrafica,crearGraficaSimple,"No se han encontrado valores de la señal")
}

function crearGraficaSimple(datosRecibidos){
  console.log(datosRecibidos)
  //senal=datosRecibidos["senal"]
  //var leyenda = Array("",senal["id_senal"]+ " "+ senal["tipo_senal"] + " " + senal["unid_ing"]);
  data=datosRecibidos["grafica"]  
  senal=datosRecibidos["senal"]
  num_datos=data[0].length
  


  var options = {
    width: window.innerWidth-200,
    height: 600,
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
      label: "Caudal SAIH",//leyenda[1],
      stroke: "gray",
      width: 2,      
      dash: [0],
      unidad:'m3/s'
    },
    {
      show: false,
      label: "Caudal Aportacion SAIH",//leyenda[1],
      stroke: "darkblue",
      width: 2,      
      dash: [0],
      unidad:'m3/s'
    },
    {
      show: true,
      label: "Caudal Simulado",//leyenda[1],
      stroke: "cyan",      
      width: 2,      
      dash: [0],
      unidad:'m3/s'
    },
    {
      show: true,
      label: "Caudal pronóstico",//leyenda[1],
      stroke: "magenta",
      width: 2,      
      dash: [0],
      unidad:'m3/s'
    },
  
    ],
    scales:{
    "x":{},
    "y":{}
  },axes:[{
    "space":90,    
  },{
    "space":50,
    "label": 'm3/s'     
  }],
    cursor: { drag:  { x: true} }
  };
console.log(senal)
if(senal['tipo']=='E'){
  options.series[2].show=true;
}  
if(senal["activacion"]!=-777){
  data.push(new Array(num_datos).fill(senal["activacion"]))
  options.series.push({
    show: true,
    label: "Activacion",
    stroke: "yellow",
    width: 1,      
    dash: [4,2],
    unidad:'m3/s'
  })
}
if(senal["prealerta"]!=-777){ 
  data.push(new Array(num_datos).fill(senal["prealerta"]))
  options.series.push(  {
  show: true,
  label: "Pre-alerta",
  stroke: "orange",
  width: 1,      
  dash: [4,2],
  unidad:'m3/s'
  })
}
if(senal["alerta"]!=-777){ 
    data.push(new Array(num_datos).fill(senal["alerta"]))
    options.series.push({show: true,
    label: "Alerta",
    stroke: "red",
    width: 1,      
    dash: [4,2],
    unidad:'m3/s'
    }) 
  } 

  let uplot = new uPlot(options, data, document.getElementById("grafica_container"));
  let ctx=uplot.ctx;
  dibujarAlertas(ctx,senal)
  console.log(uplot);
  abrirFicha("Ficha_senal")
}

function dibujarAlertas(ctx,senal){
}
