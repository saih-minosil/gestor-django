function mostrarEstacion(codigo_estacion){
    async_html_call_and_do("/vsad/"+codigo_estacion,document.getElementById("Contenido_ficha_senal"),mostrarGrafica,codigo_estacion,"Error: no se ha encontrado la estacion");
    document.getElementById("cuerpo").scroll({
        top: 0,
        left: 0,
        behavior: "smooth",
      });
}

function mostrarGrafica(codigo_estacion){
    solicitudGraficaSimple(codigo_estacion);    
}
