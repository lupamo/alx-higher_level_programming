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

  rotate () {
    const rotter = this.height;
    this.height = this.width;
    this.width = rotter;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
