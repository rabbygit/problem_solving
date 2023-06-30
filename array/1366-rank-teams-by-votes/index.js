/**
 * @param {string[]} votes
 * @return {string}
 */
const rankTeams = function (votes) {
  const n = votes[0].length;
  const teamPositions = {};

  // create a Map where each key is a team name, and each value is an array of integers.
  // The integers will represent the team's total votes in each position (1st, 2nd, 3rd, etc)
  for (const vote of votes) {
    for (let idx = 0; idx < n; idx++) {
      const team = vote[idx];
      if (teamPositions[team] === undefined) {
        teamPositions[team] = new Array(n).fill(0);
      }
      teamPositions[team][idx]++;
    }
  }

  return Object.keys(teamPositions)
    .sort((a, b) => {
      const teamA = teamPositions[a];
      const teamB = teamPositions[b];
      // sort function compares two teams at a time. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description).
      // compare this team's score in this position with the next team's score in this position.
      // if there's a clear winner, return -1 or 1, breaking the loop.
      for (let idx = 0; idx < n; idx++) {
        if (teamA[idx] !== teamB[idx]) {
          return teamB[idx] - teamA[idx];
        }
      }

      // if the two teams are tied across all positions, compare team names.
      return a > b ? 1 : -1;
    })
    .join("");
};
