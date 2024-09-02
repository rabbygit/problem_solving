func chalkReplacer(chalk []int, k int) int {
    // total chalks needed to completed one cycle
	totalChalkNeeded := 0
	for i := 0; i < len(chalk); i++ {
		totalChalkNeeded += chalk[i]
	}

	// remaining chalks after possible cycles completion
	reamins := k % totalChalkNeeded

	// find where the remaining chalks are not sufficient
	for i := 0; i < len(chalk); i++ {
		if chalk[i] > reamins {
			return i
		}

		reamins -= chalk[i]
	}

    return 0
}