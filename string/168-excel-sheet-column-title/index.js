/**
 * @param {number} columnNumber
 * @return {string}
 */
const convertToTitle = function (columnNumber) {
  let title = "";
  const startingPoint = "A".charCodeAt(0);

  while (columnNumber) {
    columnNumber--;
    title = String.fromCharCode(startingPoint + (columnNumber % 26)) + title;
    columnNumber = parseInt(columnNumber / 26);
  }

  return title;
};
