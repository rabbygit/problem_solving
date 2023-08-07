/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
const minReorder = function (n, connections) {
  const neighbors = {};
  const edges = {};
  const visited = {};
  let changes = 0;

  for (const i = 0; i < n; i++) neighbors[i] = [];

  for (const [a, b] of connections) {
    neighbors[a].push(b);
    neighbors[b].push(a);
    edges[`${a}#${b}`] = true;
  }

  function dfs(city) {
    for (let i = 0; i < neighbors[city].length; i++) {
      const neighbor = neighbors[city][i];
      if (visited[neighbor]) continue;

      if (!edges[`${neighbor}#${city}`]) changes++;
      visited[neighbor] = true;
      dfs(neighbor);
    }
  }

  visited[0] = true;
  dfs(0);

  return changes;
};
