/**
 * @param {number[]} nums
 * @return {number}
 */
const findShortestSubArray = function (nums) {
  // count occurence, keep first occurence index, total occurence in hash
  // get degree from the hash, and calculate shortest sub-array length
  let maxDegree = 0;
  let shortestLength = 0;
  const numsMap = new Map();

  for (let idx = 0; idx < nums.length; idx++) {
    const n = nums[idx];
    let prev = numsMap.get(n);

    if (!prev) {
      numsMap.set(n, { firstSeen: idx, total_occured: 1 });
      prev = numsMap.get(n);
    } else {
      prev.total_occured++;
    }

    // update maxDegree and shortestLength
    if (prev.total_occured > maxDegree) {
      maxDegree = prev.total_occured;
      shortestLength = idx - prev.firstSeen + 1;
    } else if (maxDegree === prev.total_occured) {
      shortestLength = Math.min(shortestLength, idx - prev.firstSeen + 1);
    }
  }

  return shortestLength;
};
