#!/usr/bin/node
const { argv } = require('node:process');
function factorial (n) {
  if (n === 0 || n === 1) {
    console.log(1);
  } else {
    let fact = 0;
    for (let i = 2; i <= n; i++) {
      fact *= i;
    }
    console.log(fact);
  }
}
console.log(factorial(parseInt(argv[2])));
