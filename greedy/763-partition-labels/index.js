/**
 * @param {string} s
 * @return {number[]}
 */
const partitionLabels = function (s) {
  const result = [];
  const lastOccur = {};
  let partitionSize = 0;
  let partitionEnd = 0;

  for (let idx = 0; idx < s.length; idx++) {
    lastOccur[s[idx]] = idx;
  }

  for (let idx = 0; idx < s.length; idx++) {
    partitionSize++;
    partitionEnd = Math.max(partitionEnd, lastOccur[s[idx]]);
    if (partitionEnd === idx) {
      result.push(partitionSize);
      partitionSize = 0;
    }
  }

  return result;
};
