    var direccion_intranet = "http://peares2/" ;
    /*---------------------------------------------------------------------------------------------------------*/
	function visualizacionFotos(estacion){
	/*---------------------------------------------------------------------------------------------------------*/
		url = direccion_intranet + "intraphpminhosil/desarrollo/apps/visor_fotos.php?CODREM=" + estacion;
		window.open(url, "fotos1", "scrollbars=1, width=1000, height=600");
	}

		/*---------------------------------------------------------------------------------------------------------*/
	function curvasEstacion(estacion, area){
	/*---------------------------------------------------------------------------------------------------------*/
		if(area == "CAL"){
			area = "CALIDAD";
		}
		else {
			area = "HIDROLOGIA";
			area = "HIDROLOGIA";
		}

		url = direccion_intranet + "tendsminhosil/main/curvas_estacion.php?estacion=" + estacion + "&area=" + area;
		window.open(url, "curvas", "width=100, height=100");
	}

	/*---------------------------------------------------------------------------------------------------------*/
	function curvasGenerales(){
	/*---------------------------------------------------------------------------------------------------------*/
		url = direccion_intranet + "tendsminhosil/main/principal.php";
		window.open(url, "curvas2", "width=100, height=100");
	}

	function abrirAppGraficas(){
		url = "/graficas_app";
		window.open(url, "http://belesar:8000/graficas", "width=1100, height="+screen.height);
	}

	/*---------------------------------------------------------------------------------------------------------*/
	function extraccionDatos(){
	/*---------------------------------------------------------------------------------------------------------*/
		url = direccion_intranet + "intraphpminhosil/desarrollo/apps/extraccion_datos.php";
		window.open(url, "extraccion", "scrollbars=1, width=835, height=830");
	}


  function range(start, stop, step) {
    var a = [start], b = start;
    while (b < stop) {
        a.push(b += step || 1);
    }
    return a;
}