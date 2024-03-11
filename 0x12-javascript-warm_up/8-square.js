#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 3 || isNaN(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    let row = '';
    for (let j = 0; j < argv[2]; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
