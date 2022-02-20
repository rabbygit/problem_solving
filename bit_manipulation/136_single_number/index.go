package main

func singleNumber(nums []int) int {
	result := 0

	for i := 0; i < len(nums); i++ {
		// xor operation returns 0 if both bits are same and 1 for different bits
		// so, if we xor two same number it will return 0 and after that xor with unique number
		// it will give the unique number
		// Ex: [2,2,1] 010 ^ 010 = 000 ^ 001 = 001
		result = result ^ nums[i]
	}

	return result
}
