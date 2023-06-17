/**
 * @param {string} s
 * @return {string}
 */
const sortString = function (s) {
  const freq = new Array(26).fill(0);
  let res = "";

  for (let idx = 0; idx < s.length; idx++) {
    freq[s.charCodeAt(idx) - 97]++;
  }

  while (res.length < s.length) {
    for (let idx = 0; idx < freq.length; idx++) {
      if (freq[idx]) {
        res += String.fromCharCode(idx + 97);
        freq[idx]--;
      }
    }

    for (let idx = freq.length; idx > -1; idx--) {
      if (freq[idx]) {
        res += String.fromCharCode(idx + 97);
        freq[idx]--;
      }
    }
  }

  return res;
};
