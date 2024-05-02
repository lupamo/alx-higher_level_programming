$(document).ready(function() {
  $('#btn_translate').click(function() {
	const language = $('#language_code').val();
	const url = 'https://www.fourtonfish.com/hellosalut/hello/' + language;

	$.get(url, function(data) {
		$('#hello').text(data.hello);
	});
  });
});
