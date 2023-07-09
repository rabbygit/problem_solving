/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
const wordPattern = function (pattern, s) {
  const wordMap = {};
  const patternMap = {};

  const words = s.split(" ");
  if (words.length !== pattern.length) return false;

  for (let i = 0; i < words.length; i++) {
    if (
      !patternMap.hasOwnProperty(pattern[i]) &&
      !wordMap.hasOwnProperty(words[i])
    ) {
      patternMap[pattern[i]] = words[i];
      wordMap[words[i]] = pattern[i];
      continue;
    }

    if (
      patternMap[pattern[i]] !== words[i] ||
      wordMap[words[i]] !== pattern[i]
    ) {
      return false;
    }
  }

  return true;
};
