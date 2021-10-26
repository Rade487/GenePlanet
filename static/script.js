
function init(){
document.getElementById("search").addEventListener("input", ispis)
}

function ispis(){
    //document.getElementById("labela").innerHTML = document.getElementById("search").value
    search = document.getElementById("search").value
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/submit",
        contentType: 'application/json;charset=UTF-8',
        data:{
        	'search' : document.getElementById("search").value
        },
        datatype: 'json',
        success: function(text) {nesto(text);},
        cache: false
    })
}

function nesto(text){
    document.getElementById("labela").innerHTML = text.format
}



