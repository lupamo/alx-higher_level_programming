#!/usr/bin/node
/** A script that prints the number
 *  of movies where the character “Wedge Antilles” is present.**/
const request = require('request');

const url = process.argv[2];
const id = 18;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const movies = JSON.parse(body).results;

  const moviesIn = movies.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`));
  console.log(moviesIn.length);
});
