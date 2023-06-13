/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
const fractionToDecimal = function (numerator, denominator) {
  if (numerator === 0) return "0";

  let res = "";
  if (Math.sign(numerator) !== Math.sign(denominator)) {
    res = "-";
  }

  let num = Math.abs(numerator);
  let den = Math.abs(denominator);

  let remainder = num % den;
  res += Math.floor(num / den);
  if (remainder === 0) return res;

  res += ".";
  const remainderMap = new Map(); // remainder -> it's starting index in result
  while (remainder > 0) {
    remainderMap.set(remainder, res.length);

    remainder *= 10;
    res += Math.floor(remainder / den);
    remainder %= den;

    if (remainderMap.has(remainder)) {
      const idx = remainderMap.get(remainder);
      return `${res.slice(0, idx)}(${res.slice(idx)})`;
    }
  }

  return res;
};
