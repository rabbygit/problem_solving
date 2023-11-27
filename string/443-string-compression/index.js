/**
 * @param {character[]} chars
 * @return {number}
 */
const compress = function (chars) {
  const n = chars.length;
  let insertIdx = 0;
  let runnerIdx = 0;

  while (runnerIdx < n) {
    chars[insertIdx] = chars[runnerIdx];
    let count = 1;

    while (runnerIdx + 1 < n && chars[runnerIdx + 1] === chars[insertIdx]) {
      runnerIdx++;
      count++;
    }

    if (count > 1) {
      for (const c of String(count)) {
        chars[++insertIdx] = c;
      }
    }

    insertIdx++;
    runnerIdx++;
  }

  return insertIdx;
};
