/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
const merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const result = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const lastResEl = result.length - 1;
    const [start, end] = intervals[i];
    const prevEnd = result[lastResEl][1];
    if (start <= prevEnd) {
      result[lastResEl][1] = Math.max(result[lastResEl][1], end);
    } else {
      result.push([start, end]);
    }
  }

  return result;
};
