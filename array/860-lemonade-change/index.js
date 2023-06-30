/**
 * @param {number[]} bills
 * @return {boolean}
 */
const lemonadeChange = function (bills) {
  let fiveDollar = 0;
  let tenDollar = 0;

  for (const bill of bills) {
    if (bill === 5) {
      fiveDollar++;
    } else if (bill === 10) {
      if (!fiveDollar) return false;

      fiveDollar--;
      tenDollar++;
    } else if (bill === 20) {
      if (!fiveDollar || (fiveDollar < 3 && !tenDollar)) {
        return false;
      }

      if (tenDollar) {
        fiveDollar--;
        tenDollar--;
      } else {
        fiveDollar -= 3;
      }
    }
  }

  return true;
};
