#!/usr/bin/node
const { argv } = require('node:process');
let arr = [];
argv.forEach((val) => {
  for (let i = 0; i <= val; i++){
	arr.push(i);
  }
  console.log(arr[1]);
});
