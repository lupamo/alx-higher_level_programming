#!/usr/bin/node
/** A script that displays status code of a Request**/

const url = process.argv[2];

fetch(`${url}`)
  .then(response => {
    console.log(`code: ${response.status}`);
  });
