package main

import "strconv"

func twoSum(nums []int, target int) []int {
	result_map := make(map[string]int)

	for i := 0; i < len(nums); i++ {
		temp := target - nums[i]
		if index, ok := result_map[strconv.Itoa(temp)]; ok {
			return []int{index, i}
		} else {
			result_map[strconv.Itoa(nums[i])] = i
		}
	}

	return []int{}
}
