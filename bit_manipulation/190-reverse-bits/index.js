/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
const reverseBits = function (n) {
  let result = 0;

  for (let i = 0; i < 32; i++) {
    // find the last bit of n
    const bit = n & 1; // this bit is 0 or 1

    // the last bit of n is already taken care of, so we need to drop it
    n >>>= 1;

    // shift the last bit of n to the left
    const reversedLastBit = bit << (31 - i);

    // insert the reversed last bit of n into the result
    result = result | reversedLastBit;
  }

  // convert the result to an unsigned 32-bit integer
  return result >>> 0;
};
