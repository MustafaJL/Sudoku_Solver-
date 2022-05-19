
function myFunction() {
    var element = document.getElementsByTagName("input");
    for(let i=0; i<element.length; i++){
    val = i+1
    name = "inp"+val
    element[i].setAttribute("name",name)
    element[i].setAttribute("maxlength", "1")
}
}

window.addEventListener('load', function(){

    var element = document.getElementsByTagName("input");
    for(let i=0; i<element.length; i++){
    
    element[i].maxLength = "1"
    element[i].setAttribute("oninput","this.value = this.value.replace(/[^1-9.]/g, '').replace(/(\..*?)\..*/g, '$1');" );
    // element[i].oninput = this.value.replace(/[0-9]/g,'');
    }
    console.log(2)
})



 