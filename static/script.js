
function init(){
document.getElementById("search").addEventListener("input", search_gene)
}

function search_gene(){
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
        success: function(text) {load_table(text);},
        cache: false
    })
}

function load_table(text){

    let body = document.getElementById('table_body')
    body.innerHTML = ''
    if(text != ''){
    let row = document.createElement('tr');
		row.innerHTML = `
					<td>${text[1].chrom}</td>
					<td>${text[1].pos}</td>
					<td>${text[1].id}</td>
					<td>${text[1].ref}</td>
					<td>${text[1].alt}</td>
					<td>${text[1].format}</td>
					<td>${text[2]}</td>
					<td>${text[3]}</td>
				`
		body.appendChild(row)
    }
}



