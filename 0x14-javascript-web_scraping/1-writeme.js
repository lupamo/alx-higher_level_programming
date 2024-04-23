#!/usr/bin/node
/** A script that writes content of a file**/

const fs = require('fs');

const filePath = process.argv[2];
const str = process.argv[3];

try {
  fs.writeFileSync(filePath, str);
} catch (err) {
  console.error(err);
}
