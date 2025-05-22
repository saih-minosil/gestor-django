function updateCustomSelect(element){
    var j, ll, selElmnt, a, b, c;
    /* Look for any elements with the class "custom-select": */
    selElmnt = element.getElementsByTagName("select")[0];
    ll = selElmnt.length;
    /* Create a new DIV that will act as the selected item: */
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    var e = selElmnt.options[selElmnt.selectedIndex];
    a.innerHTML = e.innerHTML;
    a.data = e.value;
    //a.style.color="white";
    a.id=selElmnt.id+"_";
    a.className=a.className+" "+ selElmnt.className+"_";
    //element.appendChild(a);
    element.insertBefore(a,null);
    /* Create a new DIV that will contain the option list: */
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    for (j = 0; j < ll; j++) {
        /* For each option in the original select element, create a new DIV that will act as an option item: */
        c = document.createElement("DIV");
        e=selElmnt.options[j];
        c.innerHTML =e.innerHTML;
        c.data=e.value;
        c.style.color=e.style.color;
        c.className=c.className+" "+ e.className+"_";
        c.addEventListener("click", function(e) {
            /* When an item is clicked, update the original select box, and the selected item: */
//            console.log("Event shot: click on option: ")
//            console.log(e)
            var y, i, k, s, h, sl, yl;
            s = this.parentNode.parentNode.getElementsByTagName("select")[0];
            sl = s.length;
            h = this.parentNode.previousSibling;
            for (i = 0; i < sl; i++) {
                if (s.options[i].innerHTML == this.innerHTML) {
                    s.selectedIndex = i;
                    h.innerHTML = this.innerHTML;
                    h.data=this.data;
                    //h.style.color=this.style.color;
                    y = this.parentNode.getElementsByClassName("same-as-selected");
                    yl = y.length;
                    for (k = 0; k < yl; k++) {
                        y[k].removeAttribute("class");
                    }
                    this.setAttribute("class", "same-as-selected");
                    break;
                }
            }
            h.click();
        });
        b.appendChild(c);

    }
    element.appendChild(b);
    a.addEventListener("click", function(e) {
    /* When the select box is clicked, close any other select boxes,
    and open/close the current select box: */
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        
    });
    return a;
}

function closeAllSelect(elmnt) {
  /* A function that will close all select boxes in the document,
  except the current select box: */
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)    
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);