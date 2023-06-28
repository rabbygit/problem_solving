/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
const compareVersion = function (version1, version2) {
  const v1Array = version1.split(".").map((x) => parseInt(x));
  const v2Array = version2.split(".").map((x) => parseInt(x));

  let l1 = 0;
  let l2 = 0;
  while (l1 < v1Array.length && l2 < v2Array.length) {
    if (v1Array[l1] > v2Array[l2]) {
      return 1;
    } else if (v2Array[l2] > v1Array[l1]) {
      return -1;
    }

    l1++;
    l2++;
  }

  if (
    v1Array.length > v2Array.length &&
    v1Array.slice(l1).filter((x) => x).length
  ) {
    return 1;
  }

  if (
    v1Array.length < v2Array.length &&
    v2Array.slice(l2).filter((x) => x).length
  ) {
    return -1;
  }

  return 0;
};
