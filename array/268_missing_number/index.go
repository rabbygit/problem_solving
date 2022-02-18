package main

func missingNumber(nums []int) int {
	n := len(nums)
	total_sum := (n * (n + 1)) / 2
	total := 0

	for i := 0; i < n; i++ {
		total += nums[i]
	}

	return total_sum - total
}
