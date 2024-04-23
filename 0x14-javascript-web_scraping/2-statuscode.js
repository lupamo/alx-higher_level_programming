#!/usr/bin/node
/** A script that displays status code of a Request**/
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
