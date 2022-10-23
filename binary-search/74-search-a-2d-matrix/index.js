/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
const searchMatrix = function (matrix, target) {
  let n = matrix[0].length - 1;
  let foundRow;

  for (let row = 0; row < matrix.length; row++) {
    if (target <= matrix[row][n]) {
      foundRow = row;
      break;
    }
  }

  if (foundRow === undefined) return false;

  return binarySearch(matrix, foundRow, target);
};

const binarySearch = (matrix, foundRow, target) => {
  let start = 0;
  let end = matrix[0].length - 1;

  while (start <= end) {
    mid = parseInt((start + end) / 2);

    if (target === matrix[foundRow][mid]) {
      return true;
    } else if (target > matrix[foundRow][mid]) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return false;
};
