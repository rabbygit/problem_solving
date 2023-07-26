/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
const divideString = function (s, k, fill) {
  const result = [];
  const total_group = Math.ceil(s.length / k);

  for (let i = 1; i <= total_group; i++) {
    let sub_str = s.slice((i - 1) * k, i * k);
    if (sub_str.length < k) {
      sub_str += fill.repeat(k - sub_str.length);
    }
    result.push(sub_str);
  }

  return result;
};
