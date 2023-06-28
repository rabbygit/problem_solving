/**
 * @param {string} s
 * @return {string[]}
 */
const restoreIpAddresses = function (s) {
  if (s.length > 12) return [];
  const res = [];

  function backtrack(idx, dots, ip) {
    console.log({ ip });
    if (idx === s.length && dots == 4) {
      res.push(ip.slice(0, ip.length - 1));
      return;
    }

    if (dots > 4) return;

    for (let j = idx; j < Math.min(s.length, idx + 3); j++) {
      if (
        parseInt(s.slice(idx, j + 1)) <= 255 &&
        (idx === j || s[idx] !== "0")
      ) {
        backtrack(j + 1, dots + 1, ip + s.slice(idx, j + 1) + ".");
      }
    }
  }

  backtrack(0, 0, "");
  return res;
};
