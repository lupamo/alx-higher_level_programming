#!/usr/bin/node
const { argv } = require('node:process');
if (!isNaN(argv[2])) {
  if (argv[2] === 0 || argv[2] === 1) {
    console.log(1);
  } else {
	let fact = 1;
    for (let i = 2 ; i <= argv[2]; i++) {
      fact *= i;
	}
    console.log(fact);
  }
}
