#!/usr/bin/node
exports.converter = function (base) {
  function converte (num) {
    return num.toString(base);
  }
  return converte;
};
