function mostrar()
{
    mostrarEstaciones();
}

function mostrarEstaciones()
{
     var allEstaciones = document.getElementsByClassName("fila_estacion");
     for (const estacion of allEstaciones){
                estacion.hidden=true;
     }
     visibles_tipo=Array();
     visibles_zona=Array();
     for (const tipo of tipos){
        visibles_tipo.push.apply(visibles_tipo,document.getElementsByClassName("fila_estacion_"+tipo));
     }
     for (const zona of zonas){
        visibles_zona.push.apply(visibles_zona,document.getElementsByClassName("fila_estacion_"+zona));
     }
     for (visible of visibles_tipo){
            if(visibles_zona.includes(visible))
                visible.hidden=false;
     }    
     document.getElementById("Selector_filtro_tipo_estacion_piezo").hidden=true;    
}

function mostrarEstacion(codigo_estacion){
    async_html_call_and_do("/estacion/"+codigo_estacion,document.getElementById("Contenido_ficha_estacion"),abrirFicha,"Ficha_estacion","Error: no se ha encontrado la estacion");
    document.getElementById("cuerpo").scroll({
        top: 0,
        left: 0,
        behavior: "smooth",
      });
}

