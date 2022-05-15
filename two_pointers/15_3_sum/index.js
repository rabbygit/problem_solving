/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/3sum/}
 * @description Given an integer array nums, return all the triplets 
 * [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 */


const threeSum = function (nums) {
	const result = []
	const len = nums.length
	nums = nums.sort((a, b) => a - b)

	if (len < 3) {
		return result
	}

	for (let index = 0; index < len - 2; index++) {
		let left = index + 1
		let right = len - 1

		while (left < right) {
			let sum = nums[index] + nums[left] + nums[right]

			if (sum === 0) {
				result.push([nums[index], nums[left], nums[right]])

				// avoid same element
				while (nums[left] === nums[left + 1] && left < right - 1) {
					left++
				}

				// avoid same element
				while (nums[right] === nums[right - 1] && left < right - 1) {
					right--
				}

				left++

			} else if (sum > 0) {
				right--
			} else {
				left++
			}

			// avoid same element
			while (nums[index] === nums[index + 1] && index < len - 3) {
				index++
			}
		}
	}

	return result
};