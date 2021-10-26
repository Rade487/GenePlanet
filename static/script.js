
function init(){
document.getElementById("search").addEventListener("input", ispis)
}

function ispis(){
    document.getElementById("labela").innerHTML = document.getElementById("search").value
    search = document.getElementById("search").value
    if(search == "rs")
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/proba",
        data:{
        	search:document.getElementById("search").value
        },
        success: function(text) {nesto(text);},
        dataType: "html",
        cache: false
    })
}

function nesto(text){
    document.getElementById("labela").innerHTML = text
}



