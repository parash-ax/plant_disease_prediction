$(document).ready(function () {

	function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function (e) {
				$('#selected_image')
					.attr('src', e.target.result)
					.width(176)
					.height(176);
			}
			reader.readAsDataURL(input.files[0]);
		}
	}

	$('#imagefile').change(function () {
		readURL(this);
	});

	$("form#analysis-form").submit(function (event) {
		event.preventDefault();

		var analyze_button = $("button#analyze-button");
		var imagefile = $('#imagefile')[0].files;

		if (!imagefile.length > 0) {
			alert("Please select a file to analyze!");
			return;
		}

		analyze_button.html("Analyzing..");
		analyze_button.prop("disabled", true);

		var fd = new FormData();
		fd.append('file', imagefile[0]);

		// Get CSRF Token from the page
		var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();  

		var loc = window.location;

		$.ajax({
			method: 'POST',
			async: true,
			url: loc.protocol + '//' + loc.hostname + ':' + loc.port + '/analyze/',
			data: fd,
			processData: false,
			contentType: false,
			beforeSend: function (xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);  // Include CSRF token
			}
		}).done(function (data) {
			console.log("Done Request!");
			$("#result").html("Result: " + data.result);
		}).fail(function (e) {
			console.log("Fail Request!");
			console.log(e);
		}).always(function () {
			analyze_button.prop("disabled", false);
			analyze_button.html("Analyze");
		});

		console.log("Submitted!");
	});
});
