/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
const numWaterBottles = function (numBottles, numExchange) {
  let result = numBottles;
  let emptyBottles = numBottles;
  numBottles = 0;

  while (emptyBottles >= numExchange || numBottles) {
    result += numBottles;
    emptyBottles += numBottles;
    numBottles = parseInt(emptyBottles / numExchange);
    emptyBottles = emptyBottles - numBottles * numExchange;
  }

  return result;
};
