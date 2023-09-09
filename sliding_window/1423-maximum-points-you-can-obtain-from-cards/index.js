/**
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */
const maxScore = function (cardPoints, k) {
  let left = 0;
  let right = cardPoints.length - k;
  let total = cardPoints.slice(right).reduce((a, b) => a + b, 0);
  let result = total;

  while (right < cardPoints.length) {
    total += cardPoints[left] - cardPoints[right];
    result = Math.max(result, total);
    left++;
    right++;
  }

  return result;
};
