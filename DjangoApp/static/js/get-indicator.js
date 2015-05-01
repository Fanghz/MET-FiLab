$(function(){
	$('#send').click(function(event){
		event.preventDefault();
		$(".country").show();
		$(".indicator").show();
		$(".worldbanksubmit").show();
		var topic = $('#selectTopic').val();

		$.getJSON('http://localhost:8000/static/js/country.json',
			function(json){
				var country = document.getElementById("selectCountry");
				for(var i=0;i<json.length;i++){
					country.options[i] = new Option();
					country.options[i].text = json[i].name;
					country.options[i].value = json[i].label;
				}
			});
/*
		$.getJSON("http://localhost:8000/indicator?callback=?",
			{ ids: [1, 2, 3], stocked: [true, false] },
			function(data){
				if (data["HTTPRESPONSE"] == 1){
          			alert("success2");
          		}
          	}); 
		*/
		$.ajax({
			type: "GET",
			url: 'http://localhost:8000/indicator?callback=?',
			data: { topics: topic},
			dataType: 'json',
			traditional: true,
			success: function(json){
				var indicators = document.getElementById("selectIndicator");
				for(var i=0;i<json.length;i++){
					indicators.options[i] = new Option();
					indicators.options[i].text = json[i].indicator;
					indicators.options[i].value = json[i].indicator;
				}
          	}
		});
	});
})