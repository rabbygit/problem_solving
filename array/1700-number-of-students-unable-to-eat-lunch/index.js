/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
// T.C: O(n) and S.C: O(n)
const countStudents = function (students, sandwiches) {
  const sandwichPref = {};
  let k = 0;

  for (const pref of students) {
    if (sandwichPref[pref] === undefined) {
      sandwichPref[pref] = 0;
    }
    sandwichPref[pref]++;
  }

  while (k < sandwiches.length && sandwichPref[sandwiches[k]]) {
    sandwichPref[sandwiches[k]]--;
    k++;
  }

  return students.length - k;
};
