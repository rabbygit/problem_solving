/**
 * [Problem ref]{@link https://leetcode.com/problems/find-if-path-exists-in-graph}
 * @description There is a bi-directional graph with n vertices, 
 * where each vertex is labeled from 0 to n - 1 (inclusive). 
 * The edges in the graph are represented as a 2D integer array edges, 
 * where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
 * Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
 */

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
const validPath = function(n, edges, source, destination) {
    const adjacency_list = {}
    const stack = [source]
    const visited = {}
    
    // add neighbor nodes in adjacency list
    // like '0':[1,2] , '1':[0,2] , '2':[1,0]
    edges.forEach(([a,b]) => {
        adjacency_list[a] ? adjacency_list[a].push(b) : adjacency_list[a] = [b]
        adjacency_list[b] ? adjacency_list[b].push(a) : adjacency_list[b] = [a]
    });

    while (stack.length) {
        // pop the last node
        let node = stack.pop()

        // check if this node is the destinantion node
        if (node === destination) return true

        // check if this node is already visited or not
        if(visited[node]) continue
        visited[node] = true

        // add all neighbor nodes of the node to stack
        for (let index = 0; index < adjacency_list[node].length; index++) {
            const neighbor = adjacency_list[node][index];
            stack.push(neighbor)
        }
    }

    return false
};