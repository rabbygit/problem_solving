package main

func validPath(n int, edges [][]int, source int, destination int) bool {
	stack := []int{source}
	adjacency_list := make(map[int][]int)
	visited := make(map[int]bool)

	// add neighbor nodes in adjacency list
	// like 0:[1,2] , 1:[0,2] , 2:[1,0]
	for _, edge := range edges {
		adjacency_list[edge[0]] = append(adjacency_list[edge[0]], edge[1])
		adjacency_list[edge[1]] = append(adjacency_list[edge[1]], edge[0])
	}

	for len(stack) > 0 {
		length := len(stack)

		node := stack[length-1]  // last element of stack
		stack = stack[:length-1] // remove the last element

		// check if the node is the destination then return
		if node == destination {
			return true
		}

		// check if it's visited or not
		if _, ok := visited[node]; ok {
			continue
		}
		visited[node] = true

		// push all neighbor nodes of the node to stack
		for _, neighbor := range adjacency_list[node] {
			stack = append(stack, neighbor)
		}
	}

	return false
}
