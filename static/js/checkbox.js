function addClassCheck(element){

    if(element.checked){
        element.classList.add("marked");
    }else{
        element.classList.remove("marked");
    }

    if(document.getElementsByClassName("marked").length>1){
      alert("Veuillez ne séléctionner qu'un fichier à la fois !");
        element.checked=false;
        element.classList.remove("marked");
    }

}