#!/usr/bin/node
const { argv } = require('node:process');
function factorial (n) {
  if (n === 0 || n === 1) {
    return (1);
  } else {
    let fact = 1;
    for (let i = 2; i <= n; i++) {
      fact *= i;
    }
    return (fact);
  }
}
console.log(factorial(parseInt(argv[2])));
