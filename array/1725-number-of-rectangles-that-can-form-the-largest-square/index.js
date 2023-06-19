/**
 * @param {number[][]} rectangles
 * @return {number}
 */
const countGoodRectangles = function (rectangles) {
  let maxLen = 0;
  let count = 0;

  for (const rec of rectangles) {
    const sideLength = Math.min(rec[0], rec[1]);
    if (sideLength > maxLen) {
      count = 1;
      maxLen = sideLength;
    } else if (sideLength === maxLen) {
      count++;
    }
  }

  return count;
};
