#!/usr/bin/node

exports.converter = function (base) {
  return function (numToConvert) {
    return numToConvert.toString(base);
  };
};
