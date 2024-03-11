#!/usr/bin/node
const { argv } = require('node:process');

argv.forEach((val, index) => {
  for (let idx = 0; idx <= index; idx++ ){
    if (idx === 1) {
       console.log('No argument');
    } else if (idx === 2) {
      console.log('Argument found');
    } else {
      console.log('Arguments found');
    }
  }
})
