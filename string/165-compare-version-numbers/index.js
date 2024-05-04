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
  while (l1 < v1Array.length || l2 < v2Array.length) {
    const v1Value = l1 < v1Array.length ? v1Array[l1] : 0;
    const v2Value = l2 < v2Array.length ? v2Array[l2] : 0;

    if (v1Value > v2Value) {
      return 1;
    } else if (v2Value > v1Value) {
      return -1;
    }

    l1++;
    l2++;
  }

  return 0;
};
