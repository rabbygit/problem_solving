/**
 * [Problem ref]{@link  https://leetcode.com/problems/koko-eating-bananas/description/}
 */

/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
const minEatingSpeed = function (piles, h) {
  let left = 1;
  let right = Math.max(...piles);
  let result = right;

  while (left <= right) {
    let middle = parseInt((left + right) / 2);
    let total_hours = 0;
    for (const pile of piles) {
      total_hours += Math.ceil(pile / middle);
    }

    if (total_hours <= h) {
      result = Math.min(result, middle);
      right = middle - 1;
    } else {
      left = middle + 1;
    }
  }

  return result;
};
