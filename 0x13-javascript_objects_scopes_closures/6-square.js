#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }

    while (this.height > 0) {
      console.log(c.repeat(this.width));
      this.height--;
    }
  }
}

module.exports = Square;
