/**
 * @param {number[][]} triplets
 * @param {number[]} target
 * @return {boolean}
 */
const mergeTriplets = function (triplets, target) {
  const mergeableIndex = new Set();

  for (const t of triplets) {
    if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2]) {
      continue;
    }

    for (let idx = 0; idx < t.length; idx++) {
      if (t[idx] === target[idx]) {
        mergeableIndex.add(idx);
      }
    }
  }

  return mergeableIndex.size === 3;
};
