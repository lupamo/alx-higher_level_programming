#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || w <= 0 || !Number.isInteger(w)) {
        w = 0;
    }
    if (typeof h !== 'number' || h <= 0 || !Number.isInteger(h)) {
        h = 0;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
