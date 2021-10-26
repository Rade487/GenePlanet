
function init(){
document.getElementById("search").addEventListener("input", ispis)
}

function ispis(){
    search = document.getElementById("search").value
    let re = new RegExp('^[0-9]{1,2} [0-9]+');
    if(search.startsWith('rs') || search.match(re))
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

    let body = document.getElementById('table_body')
    body.innerHTML = ''
    if(text != ''){
    let row = document.createElement('tr');
		row.innerHTML = `
					<td>${text.chrom}</td>
					<td>${text.pos}</td>
					<td>${text.id}</td>
					<td>${text.ref}</td>
					<td>${text.alt}</td>
					<td>${text.format}</td>
				`
		body.appendChild(row)
    }
}



