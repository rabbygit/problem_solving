/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const backspaceCompare = function (s, t) {
  let i = s.length - 1;
  let j = t.length - 1;

  while (i >= 0 || j >= 0) {
    i = validIdx(s, i);
    j = validIdx(t, j);

    const char_s = i > -1 ? s[i] : "";
    const char_t = j > -1 ? t[j] : "";
    if (char_s !== char_t) return false;

    i--;
    j--;
  }

  return true;
};

function validIdx(s, i) {
  let skip = 0;

  while (i >= 0) {
    if (s[i] == "#") {
      skip++;
    } else if (skip > 0) {
      skip--;
    } else {
      break;
    }

    i--;
  }

  return i;
}
