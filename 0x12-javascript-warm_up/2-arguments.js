#!/usr/bin/node
const { argv } = require('node:process');

argv.forEach((val, index) => {
  let argCount = 0;

  for (let idx = 0; idx <= index; idx++) {
    argCount += idx;
    if (argCount === 1) {
      console.log('No argument');
    } else if (argCount === 2) {
      console.log('Argument found');
    } else {
      console.log('Arguments found');
    }
  }
});
