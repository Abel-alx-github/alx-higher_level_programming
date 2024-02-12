#!/usr/bin/node

const c_is = "C is fun";

const argv = process.argv.slice(2);
const intNum = Number(argv[0]);
let i = 0;

if (!isNaN(intNum)) {
  while (i++ < intNum) {
    console.log(c_is);
  }
} else {
  console.log('Missing number of occurrences');
}
