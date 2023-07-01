/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
const gcdOfStrings = function (str1, str2) {
  const l1 = str1.length;
  const l2 = str2.length;

  function isDivisor(i) {
    if (l1 % i || l2 % i) {
      return false;
    }

    const f1 = parseInt(l1 / i);
    const f2 = parseInt(l2 / i);
    return (
      str1.slice(0, i).repeat(f1) === str1 &&
      str1.slice(0, i).repeat(f2) === str2
    );
  }

  for (let i = Math.min(l1, l2); i > -1; i--) {
    if (isDivisor(i)) {
      return str1.slice(0, i);
    }
  }

  return "";
};
