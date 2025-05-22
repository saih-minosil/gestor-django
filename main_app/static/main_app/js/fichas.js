let nivel=0;

function abrirFicha(Nombre){           
    var ficha=document.getElementById(Nombre)    
    ocultar=document.getElementsByClassName("nivel"+nivel)
    if(ocultar && ocultar[0]){        
        ocultar[0].style.opacity="5%"
    }
    nivel=nivel+10;
    ficha.style.opacity="95%" 
    ficha.style.top="-20px";
    var ancho=""
    if(ficha.className.includes("ancho100"))
        ancho="ancho100"
    else
        ancho="ancho_fijo"
    ficha.style.zIndex=nivel
    ficha.className="Ficha " +ancho +" nivel"+nivel    

}

function cerrarFicha(Nombre){        
    ficha=document.getElementById(Nombre)    
    altura=ficha.offsetHeight;
    console.log(altura);    
    ficha.style.top=String(-altura-400)+"px";
    console.log(String(-altura-400)+"px")
    ficha.className.replace("nivel"+nivel,'');
    //ficha.className="Ficha";
    nivel=nivel-10;
    fichasEnsenar=document.getElementsByClassName("nivel"+nivel)
    if(fichasEnsenar && fichasEnsenar[0]){
        fichasEnsenar[0].style.opacity="95%"
    }
}