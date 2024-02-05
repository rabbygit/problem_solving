/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
const strStr = function (haystack, needle) {
  const needle_len = needle.length;
  if (!needle_len) return 0;

  for (let i = 0; i < haystack.length; i++) {
    const str_part = haystack.slice(i, needle_len + i);
    if (str_part == needle) return i;
  }

  return -1;
};