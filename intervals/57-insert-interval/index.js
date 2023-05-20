/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
const insert = function (intervals, newInterval) {
  const res = [];

  for (let i = 0; i < intervals.length; i++) {
    const interval = intervals[i];
    if (newInterval[1] < interval[0]) {
      res.push(newInterval);
      return res.concat(intervals.slice(i));
    } else if (newInterval[0] > interval[1]) {
      res.push(interval);
    } else {
      newInterval = [
        Math.min(newInterval[0], interval[0]),
        Math.max(newInterval[1], interval[1]),
      ];
    }
  }

  res.push(newInterval);
  return res;
};
