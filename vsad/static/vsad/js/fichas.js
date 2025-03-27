let nivel=0;

function abrirFicha(Nombre){           
    var ficha=document.getElementById(Nombre)    
    ocultar=document.getElementsByClassName("nivel"+nivel)
    console.log(ocultar)
    if(ocultar && ocultar[0]){        
        ocultar[0].style.opacity="1%"
    }
    nivel=nivel+10;
    ficha.style.opacity="100%" 
    ficha.style.top="0px";
    document.getElementById(Nombre).style.zIndex=nivel
    document.getElementById(Nombre).className=document.getElementById(Nombre).className+" nivel"+nivel    
}

function cerrarFicha(Nombre){    
    //document.getElementById("Contenido_principal").hidden=false;
    ficha=document.getElementById(Nombre)
    altura=ficha.clientHeight;
    //ficha.hidden=true;      
    ficha.style.top=String(-altura-400)+"px";
    ficha.className.replace("nivel"+nivel,'');
    //ficha.className="Ficha";
    nivel=nivel-10;
    fichasEnsenar=document.getElementsByClassName("nivel"+nivel)
    if(fichasEnsenar && fichasEnsenar[0]){
        fichasEnsenar[0].style.opacity="100%"
    }
}