#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }

    for (let i = this.height; i > 0; i--) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
