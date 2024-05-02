$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  const mv = data.results;
  $.each(mv, function(index, movie) {
	$('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
