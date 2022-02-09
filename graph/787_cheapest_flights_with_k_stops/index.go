package main

import (
	"math"
)

func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
	previous := make([]int, n) // keep shortest path using at most (k-1)th edges
	current := make([]int, n)  // keep shortest path using at most k th edges
	infinity := math.MaxInt16

	// Fill the previous state to max int
	for i := 0; i < n; i++ {
		previous[i] = infinity
	}

	// Fill the current state to max int
	for i := 0; i < n; i++ {
		current[i] = infinity
	}

	previous[src] = 0
	for i := 1; i < k+2; i++ {
		current[src] = 0
		for _, edge := range flights {
			previous_flight, current_flight, cost := edge[0], edge[1], edge[2]
			// path relaxation for every edge if needed
			if previous[previous_flight]+cost < current[current_flight] {
				current[current_flight] = previous[previous_flight] + cost
			}
		}

		// after every iteration update the previous state
		copy(previous, current)
	}

	if current[dst] == infinity {
		return -1
	}

	return current[dst]
}
