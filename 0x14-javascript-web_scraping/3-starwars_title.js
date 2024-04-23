#!/usr/bin/node
/** A script that displays prints the title of a
 * Star Wars movie where the episode number matches a given integer**/

const request = require('request');

const part = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${part}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  if (data.detail === 'Not found') {
    console.log('Movie does not exist');
  } else {
    console.log(`${data.title}`);
  }
});
