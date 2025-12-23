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
