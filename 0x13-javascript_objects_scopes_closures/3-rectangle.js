#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const val = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(val.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
