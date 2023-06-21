/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
const suggestedProducts = function (products, searchWord) {
  let l = 0;
  let r = products.length - 1;
  const result = [];

  products.sort();

  for (let idx = 0; idx < searchWord.length; idx++) {
    const char = searchWord[idx];

    while (l <= r && (products[l].length <= idx || products[l][idx] !== char)) {
      l++;
    }
    while (l <= r && (products[r].length <= idx || products[r][idx] !== char)) {
      r--;
    }

    validProducts = r - l + 1;
    result.push(products.slice(l, l + Math.min(3, validProducts)));
  }

  return result;
};
