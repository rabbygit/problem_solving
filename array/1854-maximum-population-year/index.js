/**
 * @param {number[][]} logs
 * @return {number}
 */
// https://leetcode.com/problems/maximum-population-year/solutions/1198978/java-o-n-solution-with-explanation-range-addition/
const maximumPopulation = function (logs) {
  const years = new Array(101).fill(0);

  for (const [birthYear, deathYear] of logs) {
    years[birthYear - 1950]++;
    years[deathYear - 1950]--;
  }

  let year = 1950;
  let maxAlive = years[0];

  for (let idx = 1; idx < years.length; idx++) {
    years[idx] += years[idx - 1];
    if (years[idx] > maxAlive) {
      maxAlive = years[idx];
      year = 1950 + idx;
    }
  }

  return year;
};
