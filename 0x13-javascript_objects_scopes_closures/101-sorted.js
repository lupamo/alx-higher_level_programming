#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};
Object.getOwnPropertyNames(dict).forEach(occur => {
  if (newDict[dict[occur]] === undefined) {
    newDict[dict[occur]] = [occur];
  } else {
    newDict[dict[occur]].push(occur);
  }
});
console.log(newDict);
