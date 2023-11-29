/**
 * [Problem ref]{@link  https://leetcode.com/problems/reverse-words-in-a-string/}
 * @description Given an input string s, reverse the order of the words.
 * A word is defined as a sequence of non-space characters.
 * The words in s will be separated by at least one space.
 */

/**
 * @param {string} s
 * @return {string}
 */
const reverseWords = function (s) {
  let res = "";
  let i = 0;
  const n = s.length;

  while (i < n) {
    while (i < n && s[i] === " ") i++;
    if (i == n) break;

    let j = i + 1;
    while (j < n && s[j] !== " ") j++;

    const word = s.slice(i, j);
    if (res) res = word + " " + res;
    else res = word;

    i = j + 1;
  }

  return res;
};
