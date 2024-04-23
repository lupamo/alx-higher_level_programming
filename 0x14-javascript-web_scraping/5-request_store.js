#!/usr/bin/env node

const request = require('request');
const fs = require('fs');

/** A script that gets the contents of a webpage and stores it in a file**/

const url = process.argv[2];
const fn = process.argv[3];

request({
  url,
  encoding: 'utf-8'
}, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(fn, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    } else {
      console.log(fn);
    }
  });
});
