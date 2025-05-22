codigo_estacion="";
codigo_tipo="";
texto_busqueda="";

function abrirFiltroPorEstacion(){
        document.getElementById("Filtrado_por_estacion").hidden=false;
        document.getElementById("filtro_senales").hidden=true;
        tabla_senales=document.getElementById("tabla_senales");
        if(tabla_senales==null){
            tabla_senales=document.getElementById("tabla_senales_graficas_container");
        }
        //if(tabla_senales){ 
            tabla_senales.hidden=true;
        //}
        buscarEstaciones();
        }

function cerrarFiltroPorEstacion(){
        document.getElementById("Filtrado_por_estacion").hidden=true;
        document.getElementById("filtro_senales").hidden=false;
        tabla_senales=document.getElementById("tabla_senales")
        if(tabla_senales==null){
            tabla_senales=document.getElementById("tabla_senales_graficas_container");
        }
        //if(tabla_senales){ //SOLO PARA PAGINA DE GRAFICAS
        tabla_senales.hidden=false;
        //}
}

function buscarEstaciones(){
        var element=document.getElementById("Contenedor_estaciones");
        var tipo = document.getElementById("select_tipo_estacion").value;
        var zona = document.getElementById("select_zona_estacion").value;
        async_html_call("/estaciones_tabla/"+tipo+","+zona,element,"No hay estaciones");
    }


function filtrarSenalesEstacion(cod_estacion){
    codigo_estacion=cod_estacion;
    cerrarFiltroPorEstacion();
    mostrarSenales();
}

function mostrarSenales(){   
    codigo_tipo=document.getElementById("select_tipo_senal").value;
    texto_busqueda=document.getElementById("input_buscar_senal").value;
    tipo_busqueda=document.getElementById("select_buscar_senal").value;//1 en el codigo 2 en el nombre
    if(codigo_estacion){
        document.getElementById("Label_codigo_estacion").innerHTML=codigo_estacion;
        }else{
        document.getElementById("Label_codigo_estacion").innerHTML="TODAS";
    }
    var todas=document.getElementsByClassName("fila_senal");
    for (cada of todas){
        cada.hidden=true;
    }
    visibles_tipo=Array.from(document.getElementsByClassName("fila_senal"+codigo_tipo));
    visibles_estacion=Array.from(document.getElementsByClassName("fila_senal"+codigo_estacion));
    visibles_busqueda=Array()
    if(texto_busqueda){
        for (cada of todas){
            if(tipo_busqueda==1){ //busqueda en codigo, buscar en id
                buscarEn=cada.id.toLowerCase();
            }else{ //busqueda en nombre, buscar en el contenido
                buscarEn=cada.cells[1].childNodes[1].innerText.toLowerCase();
            }
            if (buscarEn.includes(texto_busqueda.toLowerCase())){
                visibles_busqueda.push(cada)
            }
        }
    }else{
        visibles_busqueda=Array.from(todas);
    }    
    for (visible of visibles_tipo){
        if(visibles_estacion.includes(visible) && visibles_busqueda.includes(visible)){
            visible.hidden=false;
            }
    }
}

