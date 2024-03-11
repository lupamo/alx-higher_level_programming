#!/usr/bin/node
const { argv } = require('node:process');
if (typeof(argv[1]) === Number) {
  console.log(`My number: ${int(argv[1])}`);
} else {
	console.log('Not a number');
}
