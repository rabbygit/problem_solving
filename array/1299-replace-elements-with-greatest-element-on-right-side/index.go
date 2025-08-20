func replaceElements(arr []int) []int {
	currMax := arr[len(arr)-1]
	arr[len(arr)-1] = -1

	for i := len(arr) - 2; i >= 0; i-- {
		num := arr[i]
		arr[i] = currMax
		currMax = max(currMax, num)
	}

	return arr
}
