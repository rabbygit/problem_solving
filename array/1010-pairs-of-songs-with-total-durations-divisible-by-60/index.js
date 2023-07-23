/**
 * @param {number[]} time
 * @return {number}
 */
const numPairsDivisibleBy60 = function (time) {
  const timeMap = new Map();
  let res = 0;

  for (const t of time) {
    const rem = t % 60;

    if (rem == 0) {
      res += timeMap.get(rem) || 0;
    } else {
      res += timeMap.get(60 - rem) || 0;
    }

    timeMap.set(rem, (timeMap.get(rem) || 0) + 1);
  }

  return res;
};
