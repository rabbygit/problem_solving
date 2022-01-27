package main

func moveZeroes(nums []int) {
	var replace_idx = 0

	for index := 0; index < len(nums); index++ {
		if nums[index] != 0 {
			if replace_idx != index {
				nums[replace_idx] = nums[index]
				nums[index] = 0
			}

			replace_idx++
		}
	}
}
