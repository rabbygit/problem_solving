/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
const findOrder = function (numCourses, prerequisites) {
  const adj = {};
  const visited = {};
  const currPath = {};
  const result = [];

  for (const [crs, pre] of prerequisites) {
    if (adj[crs] === undefined) adj[crs] = [];
    adj[crs].push(pre);
  }

  function dfs(crs) {
    if (currPath[crs]) return false;
    if (visited[crs]) return true;

    currPath[crs] = true;
    if (adj[crs]) {
      for (const pre of adj[crs]) {
        if (!dfs(pre)) return false;
      }
    }

    currPath[crs] = false;
    visited[crs] = true;
    result.push(crs);
    return true;
  }

  for (let i = 0; i < numCourses; i++) {
    if (!dfs(i)) return [];
  }

  return result;
};
