#!/usr/bin/node
const { argv } = required('node:process');
if (argv.length === 3) {
  console.log(`${argv[1]} is ${argv[2]}`);
} else if (argv.length === 2) {
  console.log(`${argv[1]} is undefined`);
} else {
  console.log('undefined is undefined');
}
