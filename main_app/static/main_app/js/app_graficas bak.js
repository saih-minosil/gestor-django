////////////////////////////////// PARTE DE INTERFAZ DE SELECCION DE SEÑALES ////////////////////////////////    
senalesSeleccionadasDict=new Object();

colores={red:"Rojo",blue:"Azul",green:"Verde",orange:"Naranja"};
lineas={"Continua":"[0]","Discontinua":"[20,5]","Puntos":"[4,4]","Puntos y lineas":"[20,4,4,4]"}

function ajustarFechasIniFin(){
    var now=new Date(Date.now()).toISOString().substring(0,16)
    document.getElementById("Input_fecha_comienzo_grafica").min="2000-06-07T00:00"
    document.getElementById("Input_fecha_comienzo_grafica").max=document.getElementById("Input_fecha_fin_grafica").value
    document.getElementById("Input_fecha_fin_grafica").min=document.getElementById("Input_fecha_comienzo_grafica").value
    document.getElementById("Input_fecha_fin_grafica").max=now
}


function onload(){
    var now=new Date(Date.now()).toISOString().substring(0,16)
    var hace_3_dias=new Date(Date.now()-(3600000*72)).toISOString().substring(0,16)
    document.getElementById("Input_fecha_comienzo_grafica").value=hace_3_dias
    document.getElementById("Input_fecha_fin_grafica").value=now;
    ajustarFechasIniFin()
    mostrarSenales();
}



function anadirSenalSeleccionada(codigo_senal){
    if(senalesSeleccionadasDict[codigo_senal]){
        alert("La señal ya está seleccionada");
    }else{
        senalesSeleccionadasDict[codigo_senal]={codigo:codigo_senal,color:"red",linea:[0]}
        actualizarListaSenalesGrafica();
    }
}

function borrarSenalSeleccionada(codigo_senal){
    delete senalesSeleccionadasDict[codigo_senal];
    actualizarListaSenalesGrafica();
}


function actualizarListaSenalesGrafica(){
    //var divBotones=document.getElementById("Div_botones_graficas");
    var table=document.getElementById("Tabla_senales_seleccionadas");
    var header=table.rows[0];
    table.remove();
    var table_container=document.getElementById("Container_senales_seleccionadas");
    var newTable = document.createElement("TABLE");
    newTable.className="tabla ancho_fijo";
    newTable.id="Tabla_senales_seleccionadas"
    newTable.appendChild(header);
    for(senal in senalesSeleccionadasDict){
        var fila = newTable.insertRow(-1);
        // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
        var celda1 = fila.insertCell(0);
        celda1.className="celdal";
        var celda2 = fila.insertCell(1);
        celda2.className="celdac";
        var celda3 = fila.insertCell(2);
        celda3.className="celdac";
        var celda4 = fila.insertCell(3);
        celda4.className="celdac";
        var celda5 = fila.insertCell(4);
        celda5.className="celdac";
        celda1.innerHTML = senal;
        celda2.appendChild(selectorColor(senal,senalesSeleccionadasDict[senal].color));
        celda3.appendChild(selectorLinea(senal,senalesSeleccionadasDict[senal].linea,celda4));
        //celda3.appendChild(selectorLinea(senal,senalesSeleccionadasDict[senal].linea));
        celda5.innerHTML = "<input type='image' src='static/main_app/img/btn_borrar.png' onclick='borrarSenalSeleccionada(\""+senal+"\")'>";
    }
    table_container.insertBefore(newTable,null);
}


function selectorColor(codigo,value){
    var newDiv=document.createElement("DIV");
    newDiv.style.width="100px";
    newDiv.className="custom-select custom_select_color";
    var newSelect = document.createElement("SELECT");
    newSelect.id='selector_color_'+codigo
    newSelect.className='selector_color'
    for (color in colores){
        newOption=document.createElement("option");
        newOption.value=color;
        newOption.style.color=color;
        newOption.innerHTML=colores[color];
        if(color==value){
            newOption.selected="selected";
        }
        newSelect.add(newOption)
    }
    newDiv.appendChild(newSelect)
    var newCustomSelect=updateCustomSelect(newDiv);
    newCustomSelect.addEventListener("click",(e)=>{
        asignarColor(e.target,codigo);
    });
    newCustomSelect.click();
    return newDiv;
}

function selectorLinea(codigo,value,celda_canvas){
    var newDiv=document.createElement("DIV");
    newDiv.style.width="160px";
    newDiv.className="custom-select custom_select_color";
    var newSelect = document.createElement("SELECT");
    newSelect.id='selector_linea_'+codigo
    newSelect.className='selector_linea'
    for (linea in lineas){
        newOption=document.createElement("option");
        newOption.value=lineas[linea];
        //newOption.style.color=color;
        newOption.innerHTML=linea;
        if(linea==value){
            newOption.selected="selected";
        }
        newSelect.add(newOption)
    }
    newDiv.appendChild(newSelect)
    var newCustomSelect=updateCustomSelect(newDiv);
    var newCanvas=document.createElement("CANVAS");
    newCanvas.width=100;
    newCanvas.height=20;
    newCanvas.className="canvas_tipo_lineas_graficas";
    celda_canvas.appendChild(newCanvas)
    newCustomSelect.addEventListener("click",(e)=>{
        asignarLinea(e.target,codigo,newCanvas);
    });
    newCustomSelect.click();
    return newDiv;
}


function asignarColor(input,codigo_senal){
    senalesSeleccionadasDict[codigo_senal].color=input.data;
    input.style.backgroundColor=input.data;
}

function asignarLinea(input,codigo_senal,canvas){
    var dash = JSON.parse(input.data);
    senalesSeleccionadasDict[codigo_senal].linea=dash;
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.setLineDash(Array.from(dash));/*dashes are 5px and spaces are 3px*/
    ctx.lineWidth=1.0;
    ctx.beginPath();
    ctx.moveTo(0,10);
    ctx.lineTo(100, 10);
    ctx.stroke();
    //ctx.clearRect(0, 0, canvas.width, canvas.height);
}

/////////////////////////////////  PARTE DE GENERACION DE LA GRAFICA ////////////////////////////////////////////

let datosGrafica=[],uplot,datosSenales={},etiquetas=[],longitud_total=0;recibidas=0;numsenales=0;avisos="";infoSenales={};


function generarGrafica() {
    fecha_ini=document.getElementById("Input_fecha_comienzo_grafica").value
    fecha_fin=document.getElementById("Input_fecha_fin_grafica").value
    if(Date.parse(fecha_ini) > Date.parse(fecha_fin)){
        alert("La fecha inicial debe ser anterior a la fecha final" ) //ESTO NO PUEDE PASAR
    }else{
        origen=document.getElementById("Select_origen_datos_grafica").value
        valores=[];        
        datosSenales={};
        infoSenales={};
        longitud_total=0;
        num_senales=0;
        recibidas=0;
        etiquetas=null;
        avisos="";
        for (codigo in senalesSeleccionadasDict){
            num_senales++;
            async_json_call("/datos_senal/"+origen+","+codigo+","+fecha_ini+","+fecha_fin,valores,anadirValores,"Error en la peticion de datos");        
            }
        //Animacion "Espere a que carguen los datos de la BD"        
    }
}

function anadirValores(valores){    
    if(!valores["etiquetas"] || valores["etiquetas"].length==0){                  //SI NO TIENE VALORES
        avisos=avisos.concat("<li>La señal "+ valores["senal"]["id_senal"]+ " no tiene datos para el origen y las fechas indicadas</li>")
    }else{
        if(!etiquetas){ //undefined? o null? o que? empty?  //SI AUN NO HABIA ETIQUETAS O ERAN UNDEFINED (Primera señal con datos)
            etiquetas=valores["etiquetas"] //rellena etiquetas
        }else if(etiquetas.length==0){            //SI ESTAN EN BLANCO (NO TENDIRA QUE PASAR NUNCA)
            console.error("LAS etiquetas estaban vacias. Esto no deberia pasar")
        }else{                                                  //RESTO DE SEÑALES CON DATOS
            if(etiquetas.length!=valores["etiquetas"].length){
                console.error("Las señales tienen un distinto numero de etiquetas(faltan datos?)")
                avisos=avisos.concat("<li>La señal "+ valores["codigo_senal"]+ " tiene un unmero incorrecto de datos.</li>")
            }            
        }        
        datosSenales[valores["senal"]["id_senal"]]=valores["valores"]
        infoSenales[valores["senal"]["id_senal"]]=valores["senal"]
        longitud_total+=valores["valores"].length
    }
    recibidas++;
    console.log(datosSenales)
    console.log(etiquetas)
    //Comprobas si se ha recibido todo
    if(recibidas>=num_senales){ //Si ya se han recibido todas        
        if(longitud_total){ //Si hay al menos una señal
            datosGrafica=[etiquetas];
            series=[{}];
            for(senal in datosSenales){ //PARA CADA SEÑAL
                datosGrafica.push(datosSenales[senal]) //DATOS
                series.push(({show:true,                //METADATOS (titulo, color, linea)
                    label:senal + " - " + infoSenales[senal]["descripcion"] +" (" + infoSenales[senal]["unid_ing"] +")",
                    stroke:senalesSeleccionadasDict[senal].color,
                    width:1,
                    dash:senalesSeleccionadasDict[senal].linea}))
            }
            crearGrafica(datosGrafica);
        }else{
            alert("No se ha obtenido ningun dato");
        }
    }
}

function crearGrafica(datosGrafica){    
    var options = {
	    width: 1000,
	    height: 500,
	    tzDate:data => uPlot.tzDate(new Date(data * 1e3), 'CET'),
	    fmtDate: tpl => {
	                    tpl=tpl.replace("{M}/{D}","{D}/{MM}")
	                    tpl=tpl.replace("{h}{aa}","{H}:00")
	                    tpl=tpl.replace("{h}:{mm}{aa}","{H}:{mm}")
	                    tpl=tpl.replace("{YYYY}-{MM}-{DD}","{DD}/{MM}/{YYYY}")
	                    return uPlot.fmtDate(tpl)},
        series: series,
        scales:{
            "x":{},
            "y":{}
        },
          cursor: { drag:  { x: true, y: true } }
    }; 
    if(uplot){
        uplot.destroy();
    }   
    uplot = new uPlot(options, datosGrafica, document.getElementById("Div_panel_grafica"));
    abrirFicha("Ficha_grafica");
    console.log(avisos)
    if(avisos.length){
        document.getElementById("Lista_avisos_grafica").innerHTML=avisos;
        document.getElementById("Div_panel_avisos_grafica").hidden=false;
    }  
}
/*
function abrirGrafica(){       
    document.getElementById("tabla_senales_container").hidden=true;
    document.getElementById("filtro_senales").hidden=true;  
    document.getElementById("Div_panel_grafica").hidden=false;
    if(avisos.length){
        console.log(avisos)
        document.getElementById("Lista_avisos_grafica").innerHTML=avisos;
        document.getElementById("Div_panel_avisos_grafica").hidden=false;
    }  
}

function cerrarGrafica(){    
    document.getElementById("tabla_senales_container").hidden=false;
    document.getElementById("filtro_senales").hidden=false;
    document.getElementById("Div_panel_grafica").hidden=true;
    document.getElementById("Div_panel_avisos_grafica").hidden=true;
}*/


function abrirAvisosGrafica(){    
    document.getElementById("Div_panel_avisos_grafica").hidden=false;
}

function cerrarAvisosGrafica(){    
    document.getElementById("Div_panel_avisos_grafica").hidden=true;
}