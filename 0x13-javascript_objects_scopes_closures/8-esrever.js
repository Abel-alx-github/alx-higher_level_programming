#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const relist = [];
  for (let i = len - 1; i >= 0; i--) {
    relist.push(list[i]);
  }
  return relist;
};
