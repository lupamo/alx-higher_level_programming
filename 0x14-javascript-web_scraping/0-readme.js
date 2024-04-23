#!/usr/bin/node
/** A script that reads content of a file in utf-8**/

const fs = require('fs');

const fileRead = process.argv[2];

try {
  const data = fs.readFileSync(fileRead, 'utf-8');
  console.log(data);
} catch (err) {
  console.error(err);
}
