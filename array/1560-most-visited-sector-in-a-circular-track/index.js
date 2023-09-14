/**
 * @param {number} n
 * @param {number[]} rounds
 * @return {number[]}
 */
const mostVisited = function (n, rounds) {
  const result = [];
  const tracks = new Array(n).fill(0);

  for (let i = 0; i < rounds.length - 1; i++) {
    let start = rounds[i];
    let end = rounds[i + 1];

    while (start !== end) {
      tracks[start - 1]++;
      start = (start % n) + 1;
    }
  }

  tracks[rounds[rounds.length - 1] - 1]++;
  const maxOccur = Math.max(...tracks);
  for (let i = 0; i < tracks.length; i++) {
    if (tracks[i] === maxOccur) {
      result.push(i + 1);
    }
  }

  return result;
};
