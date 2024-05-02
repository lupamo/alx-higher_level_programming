$(document).ready(function () {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
		const helloTrans = JSON.parse(data).hello;
		$('#hello').text(helloTrans);
	});
});
