let datosGrafica=[]

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
  var leyenda = Array("",senal["id_senal"]+ " "+ senal["tipo_senal"] + " " + senal["unid_ing"]);
  data=datosRecibidos["grafica"]
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
      //width: 1,
      fill: "rgba(16, 16, 255, 0.4)",
      dash: [5, 5],
      tag: senal["id_senal"],
      unidad:senal["unid_ing"]
    }
    ],
    scales:{
    "x":{},
    "y":{}
  },
    cursor: { drag:  { x: true, y: true } }
  };

  let uplot = new uPlot(options, data, document.getElementById("grafica_container"));
  console.log(uplot);
  abrirFicha("Ficha_senal")
}
