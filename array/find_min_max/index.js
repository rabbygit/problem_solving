/**
 * Problem Description: Given an array A[] of size n, 
 * you need to find the maximum and minimum element present in the array. 
 * Your algorithm should make the minimum number of comparisons.
 * @param {*} nums 
 * @returns 
 */

function findMinMax(nums) {
  return recurse(nums, 0, nums.length - 1)
}


function recurse(nums, start, end) {
  let min
  let max

  if (start === end) {
    max = nums[start]
    min = nums[start]
  } else if (start + 1 === end) {
    if (nums[start] > nums[end]) {
      max = nums[start]
      min = nums[end]
    } else {
      max = nums[end]
      min = nums[start]
    }
  } else {
    let middle = parseInt((start + end) / 2)
    let left = recurse(nums, start, middle)
    let right = recurse(nums, middle + 1, end)

    if (left[0] > right[0]) {
      max = left[0]
    } else {
      max = right[0]
    }

    if (left[1] < right[1]) {
      min = left[1]
    } else {
      min = right[1]
    }
  }

  let ans = [max, min]
  return ans
}