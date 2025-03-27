    tipos=Array()
    function on_check(check)
    {
        switch(check.className){
            case 'chkTiposTodos':
                var inputs = document.getElementsByClassName("chkFiltrarTipos");
                for (input of inputs){
                    input.checked=check.checked;
                }
                break;
            case 'chkZonasTodas':
                var inputs = document.getElementsByClassName("chkFiltrarZonas");
                for (input of inputs){
                    input.checked=check.checked;
                }
                break;
            case 'chkFiltrarTipos':
                document.getElementById("chkTiposTodos").checked=false;
                break;
            case 'chkFiltrarZonas':
                document.getElementById("chkZonasTodas").checked=false;
                break;
            default:
        }
        /*console.log(check.value);*/
        filtrar()
    }

    function filtrar()
    {
        tipos=Array();
        zonas=Array();
        inputs=document.getElementsByClassName('chkFiltrarTipos');
        for(input of inputs){
            if(input.checked){
                tipos.push(input.value)
            }
        }
        inputs=document.getElementsByClassName('chkFiltrarZonas');
        for(input of inputs){
            if(input.checked){
                zonas.push(input.value)
            }
        }
        mostrar()
    }

  


function filtrarEstaciones(e){       
    var texto_busqueda=e.target.value
    var todas=document.getElementsByClassName("option_estacion_");
    console.log(todas)
    for (cada of todas){
        cada.hidden=true;
    }
    visibles_busqueda=Array()
    if(texto_busqueda){
        for (cada of todas){
            //buscar en el contenido
            buscarEn=cada.innerText.toLowerCase();            
            if (buscarEn.includes(texto_busqueda.toLowerCase())){
                visibles_busqueda.push(cada)
            }
        }
    }else{
        visibles_busqueda=Array.from(todas);
    }
    console.log(visibles_busqueda)
    for (visible of visibles_busqueda){    
        if (visibles_busqueda.includes(visible)){
                visible.hidden=false;
        }
    }
    
}
