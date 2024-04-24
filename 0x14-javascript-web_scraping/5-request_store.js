#!/usr/bin/node

const request = require('request');
const fs = require('fs');

/** A script that gets the contents of a webpage and stores it in a file**/

const url = process.argv[2];
const fn = process.argv[3];

request.get(url, function(error, response, data) {
	if (error){
		console.error(error);
	} else {
		fs.writeFile(fn, data, 'utf-8', (err, res) => {
			if (error){
				console.log(error);
			}
		});
	}
});
