#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 4) {
  console.log(argv[2] + argv[3]);
} else if (argv.length === 3) {
  console.log('NaN');
} else {
  console.log('NaN');
}
