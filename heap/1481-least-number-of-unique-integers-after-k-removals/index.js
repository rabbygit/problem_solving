/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
const findLeastNumOfUniqueInts = function (arr, k) {
  const counts = {};
  for (const n of arr) {
    counts[n] = counts[n] ? counts[n] + 1 : 1;
  }

  // sort the count array in descending order
  const countArray = Array.from(Object.values(counts)).sort((a, b) => b - a);

  // pop the least occured elements from the end
  while (k > 0) k -= countArray.pop();

  return k < 0 ? countArray.length + 1 : countArray.length;
};
