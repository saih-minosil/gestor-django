if(i==2){
    var tt2=tt;
    var tt1=tt2.previousElementSibling //tt1 es el 1 y tt es el "2"
    if(parseFloat(tt2.style.top)>=parseFloat(tt1.style.top) && parseFloat(tt2.style.top)<=parseFloat(tt1.style.top) + tt1.offsetHeight){
        console.log("2 por encima de 1")
        tt2.style.top=(parseFloat(tt1.style.top)-tt1.offsetHeight)+"px"
    }else if(parseFloat(tt1.style.top)>=parseFloat(tt2.style.top) && parseFloat(tt2.style.top)<=parseFloat(tt1.style.top) +tt1.offsetHeight){//El 1 mas abajod el 2
        console.log("1 por encima de 2")
        tt1.style.top=(parseFloat(tt2.style.top)-tt2.offsetHeight)+"px"
    }
}
if(i==3){
    var tt3=tt;
    var tt2=tt3.previousElementSibling //tt1 es el 1 y tt es el "2"
    var tt1=tt2.previousElementSibling //tt1 es el 1 y tt es el "2"
    if(parseFloat(tt3.style.top)>=parseFloat(tt1.style.top) && parseFloat(tt3.style.top)<=parseFloat(tt1.style.top) + tt1.offsetHeight){
        console.log("3 por encima de 1")
        tt3.style.top=(parseFloat(tt1.style.top)-tt1.offsetHeight)+"px"
    }else if(parseFloat(tt1.style.top)>=parseFloat(tt3.style.top) && parseFloat(tt3.style.top)<=parseFloat(tt1.style.top) +tt1.offsetHeight){//El 1 mas abajod el 2
        console.log("1 por encima de 3")
        tt1.style.top=(parseFloat(tt3.style.top)-tt3.offsetHeight)+"px"
    }
    if(parseFloat(tt3.style.top)>=parseFloat(tt2.style.top) && parseFloat(tt3.style.top)<=parseFloat(tt2.style.top) + tt2.offsetHeight){
        console.log("3 por encima de 2")
        tt3.style.top=(parseFloat(tt2.style.top)-tt2.offsetHeight)+"px"
    }else if(parseFloat(tt2.style.top)>=parseFloat(tt3.style.top) && parseFloat(tt3.style.top)<=parseFloat(tt2.style.top) +tt2.offsetHeight){//El 1 mas abajod el 2
        console.log("2 por encima de 3")
        tt2.style.top=(parseFloat(tt3.style.top)-tt3.offsetHeight)+"px"
    }
}