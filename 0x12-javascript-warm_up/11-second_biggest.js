#!/usr/bin/node
const { argv } = require('node:process');
const nums = argv.slice(2).map(Number).filter(num => Number.isInteger(num));

if (nums.length < 2) {
  console.log('0');
} else {
  const sortedNums = numbers.sort((a, b) => b - a);
  console.log(`${sortedNums[1]}`);
}
