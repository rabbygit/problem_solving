/**
 * [Problem ref]{@link https://leetcode.com/problems/all-paths-from-source-to-target/}
 * @description Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
 * find all possible paths from node 0 to node n - 1 and return them in any order.
 * The graph is given as follows: graph[i] is a list of all nodes you can visit
 * from node i (i.e., there is a directed edge from node i to node graph[i][j]).
 */

/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
const allPathsSourceTarget = function (graph) {
    const destination = graph.length - 1
    const result = []

    function dfs(node, sub_result) {
        // append the node
        sub_result.push(node) 

        // check if this node is the destination
        if (node === destination) {
            result.push([...sub_result])
            return
        }

        // get all adjacent nodes of the node
        let next_nodes = graph[node]

        // call recursively for each adjacent node
        for (let index = 0; index < next_nodes.length; index++) {
            dfs(next_nodes[index],sub_result)
            sub_result.pop()
        }
    }

    dfs(0,[])
    return result
};