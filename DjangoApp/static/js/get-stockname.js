$(function(){
	$.getJSON('http://localhost:8000/static/js/stocksname.json',
		function(json){
			var stockNameSelect = document.getElementById("selectStock");

			for(var i=0;i<json.length;i++){
				stockNameSelect.options[i] = new Option();
				stockNameSelect.options[i].text = json[i].stockname;
				stockNameSelect.options[i].value = json[i].stockname;
			}
		});
})