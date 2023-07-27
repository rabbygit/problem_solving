/**
 * @param {number} num
 * @return {string}
 */
const intToRoman = function (num) {
  let result = "";
  const romanList = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1],
  ];

  for (const [romanSym, value] of romanList) {
    if (parseInt(num / value)) {
      result += romanSym.repeat(parseInt(num / value));
      num = num % value;
    }
  }

  return result;
};
