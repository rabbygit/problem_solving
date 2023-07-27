/**
 * @param {character[][]} box
 * @return {character[][]}
 */
const rotateTheBox = function (box) {
  const r = box.length;
  const c = box[0].length;
  const result = [...Array(c)].map((e) => Array(r).fill(""));

  for (let i = 0; i < r; i++) {
    let empty = c - 1;

    for (let j = c - 1; j >= 0; j--) {
      const cell = box[i][j];
      // obstacle
      if (cell === "*") {
        empty = j - 1;
      } else if (cell === "#") {
        // move stone to last empty cell
        box[i][j] = ".";
        box[i][empty] = "#";
        empty--;
      }
    }
  }

  for (let i = 0; i < r; i++) {
    for (let j = c - 1; j >= 0; j--) {
      result[j][r - i - 1] = box[i][j];
    }
  }

  return result;
};
