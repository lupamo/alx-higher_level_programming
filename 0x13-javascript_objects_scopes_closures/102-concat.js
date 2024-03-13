#!/usr/bin/node
const files = require('fs');
if (process.argv.length !== 5) {
  process.exit(1);
}
const concated = files.readFileSync(process.argv[2], 'utf-8') + files.readFileSync(process.argv[3], 'utf8');
files.writeFileSync(process.argv[4], concated);
