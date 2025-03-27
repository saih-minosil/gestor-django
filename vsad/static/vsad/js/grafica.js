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
    height: 400,
    title:document.getElementById("Cabecera_prediccion").innerHTML,
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
    "label": 'Caudal(m3/s)'     
  }],
    cursor: { drag:  { x: true} }
  };
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

  uplot = new uPlot(options, data, document.getElementById("grafica_container"));
  let ctx=uplot.ctx;
  dibujarAlertas(ctx,senal)
  console.log(uplot);
  abrirFicha("Ficha_senal")
}

function dibujarAlertas(ctx,senal){
}

function downloadImage(){
  let title=document.getElementById("codigo_estacion").innerText;
  let pxRatio = devicePixelRatio;
  let rect = uplot.root.getBoundingClientRect();
  // rect of uPlot's canvas to get y shift due to title above it (if any)
  let rect2 = uplot.ctx.canvas.getBoundingClientRect();
  let htmlContent = uplot.root.outerHTML;
  //NOTE: Use correct index here to address uPlot stylesheet. Needs to be in a separate resource for this to work.
  let uPlotCssRules = document.styleSheets[1].cssRules;
  let cssContent = "";
  for (let { cssText } of uPlotCssRules)
      cssContent += `${cssText} `;
  let width = Math.ceil(rect.width * pxRatio);
  let height = Math.ceil(rect.height * pxRatio);
  let viewBox = `0 0 ${Math.ceil(rect.width)} ${Math.ceil(rect.height)}`;

  // An SVG image is used to draw the HTML elements to an img element and then to a canvas
  let svgText = `
      <svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="${viewBox}">
          <style>
              body { margin: 0; padding: 0; }
              ${cssContent}
          </style>
          <foreignObject width="100%" height="100%">
              <body xmlns="http://www.w3.org/1999/xhtml">${htmlContent}</body>
          </foreignObject>
      </svg>
  `;

  let can = document.createElement('canvas');
  let ctx = can.getContext('2d');
  can.width = width;
  can.height = height;
  can.style.width = Math.ceil(rect.width) + "px";
  can.style.height = Math.ceil(rect.height) + "px";
  let img = new Image();
  img.crossOrigin = "anonymous";
  img.onload = () => {
      /* Once the SVG image is loaded in the img element,
       * we can start drawing on the canvas and download the file afterwards */
      console.log(ctx)
      ctx.fillStyle = "white";
      ctx.fillRect(0, 0, can.width, can.height);
      ctx.drawImage(img, 0, 0);
      ctx.drawImage(uplot.ctx.canvas, 0, (rect2.top - rect.top) * pxRatio);
      var a = document.createElement('a');
      console.log(a)
      a.href = can.toDataURL();
      a.download = title + ".png";
      console.log(a)
      a.click();
      console.log(a)
  };

  let blob = new Blob([svgText], {type: 'image/svg+xml;charset=utf-8'});
  
  /* Using blob.toDataURL() taints the img element due to a bug in Chrome, see
   * https://stackoverflow.com/questions/50824012/why-does-this-svg-holding-blob-url-taint-the-canvas-in-chrome 
   * The workaround here converts the blob to a DataURL which avoids the bug. */
  var reader = new FileReader();
  reader.readAsDataURL(blob);
  reader.onload = function(e) {
      img.src = e.target.result;      
  }
  img.onload();
  console.log(blob)
  console.log(img)
  console.log(reader)
}

function copyImage() {
  let pxRatio = devicePixelRatio;

  let rect = uplot.root.getBoundingClientRect();
  // rect of uPlot's canvas to get y shift due to title above it (if any)
  let rect2 = uplot.ctx.canvas.getBoundingClientRect();

  let htmlContent = uplot.root.outerHTML;
  console.log(htmlContent)
  let uPlotCssRules = document.styleSheets[1].cssRules;
  console.log(document.styleSheets)
  let cssContent = "";
  for (let { cssText } of uPlotCssRules)
    cssContent += `${cssText} `;

  let width = Math.ceil(rect.width * pxRatio);
  let height = Math.ceil(rect.height * pxRatio);

  let viewBox = `0 0 ${Math.ceil(rect.width)} ${Math.ceil(rect.height)}`;
  let svgText = `
    <svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="${viewBox}">
      <style>
        body { margin: 0; padding: 0; }
        ${cssContent}
      </style>
      <foreignObject width="100%" height="100%">
        <body xmlns="http://www.w3.org/1999/xhtml">${htmlContent}</body>
      </foreignObject>
    </svg>
  `;
  console.log(svgText);

  let can = document.createElement('canvas');
  let ctx = can.getContext('2d');
  can.width = width;
  can.height = height;
  can.style.width = Math.ceil(rect.width) + "px";
  can.style.height = Math.ceil(rect.height) + "px";
  document.body.appendChild(can);

  let DOMURL = window.URL || window.webkitURL;

  let img = new Image();
  let blob = new Blob([svgText], {type: 'image/svg+xml;charset=utf-8'});
  console.log(blob)
  let url = DOMURL.createObjectURL(blob);

  ctx.drawImage(uplot.ctx.canvas, 0, (rect2.top - rect.top) * pxRatio);

  img.onload = () => {
    console.log("onload")
    console.log(img)
    ctx.drawImage(img, 0, 0);
    DOMURL.revokeObjectURL(url);
  };

 img.src = url;
 console.log(img)
 //img.onload()
 document.body.appendChild(img);
}