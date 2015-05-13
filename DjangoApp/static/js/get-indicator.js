$(function(){
	$('#send').click(function(event){
		event.preventDefault();
		$(".country").show();
		$(".indicator").show();
		$(".worldbanksubmit").show();
		var topic = $('#selectTopic').val();
		var filter = $("#filter").val();

		$.getJSON('http://localhost:8000/static/js/country.json',
			function(json){
				var country = document.getElementById("selectCountry");
				for(var i=0;i<json.length;i++){
					country.options[i] = new Option();
					country.options[i].text = json[i].name;
					country.options[i].value = json[i].label;
				}
			});

		$.ajax({
			type: "GET",
			url: 'http://localhost:8000/indicator?callback=?',
			data: { topics: topic,filter: filter},
			dataType: 'json',
			traditional: true,
			success: function(json){
				if($("#selectIndicator option").length>0){
					$("#selectIndicator option").remove();
				}
				var indicators = document.getElementById("selectIndicator");
				for(var i=0;i<json.length;i++){
					indicators.options[i] = new Option();
					indicators.options[i].text = json[i].indicator;
					indicators.options[i].value = json[i].indicator;
				}
          	}
		});

		$('.uitip').tooltip();
	});
})