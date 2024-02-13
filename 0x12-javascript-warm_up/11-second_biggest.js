#!/usr/bin/node

let args = process.argv.slice(2);
args = args.map(arg => parseInt(arg, 10));
args = args.sort();

if (args.length < 2) {
  console.log(0);
} else {
  console.log(args[args.length - 2]);
}
