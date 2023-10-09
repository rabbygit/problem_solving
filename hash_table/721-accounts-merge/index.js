// Input: accounts = [
//   ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
//   ["John", "johnsmith@mail.com", "john00@mail.com"],
//   ["Mary", "mary@mail.com"],
//   ["John", "johnnybravo@mail.com"],
// ];
// Output: [
//   ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
//   ["Mary", "mary@mail.com"],
//   ["John", "johnnybravo@mail.com"],
// ];

// https://leetcode.com/problems/accounts-merge/solutions/1335073/js-using-dfs-with-approach-explained/
/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
const accountsMerge = function (accounts) {
  const em_to_em = new Map();
  const em_to_name = new Map();

  accounts.forEach((account) => {
    const name = account[0];
    em_to_name.set(account[1], name);

    if (!em_to_em.has(account[1])) {
      em_to_em.set(account[1], new Set());
    }
    em_to_em.set(account[1], em_to_em.get(account[1]).add(account[1]));

    for (let i = 2; i < account.length; ++i) {
      if (!em_to_em.has(account[i])) {
        em_to_em.set(account[i], new Set());
      }
      em_to_em.set(account[i], em_to_em.get(account[i]).add(account[1]));
      em_to_name.set(account[i], name);
      em_to_em.set(account[1], em_to_em.get(account[1]).add(account[i]));
    }
  });

  const result = [];
  const stack = [];
  const visited = new Set();

  em_to_em.forEach((neighbors, email) => {
    if (!visited.has(email)) {
      visited.add(email);
      stack.push(email);
      let email_list = [];

      while (stack.length) {
        let em = stack.pop();
        email_list.push(em);
        em_to_em.get(em).forEach((nei) => {
          if (!visited.has(nei)) {
            visited.add(nei);
            stack.push(nei);
          }
        });
      }
      email_list = sortEmails(email_list);
      const part = [em_to_name.get(email)].concat(email_list);
      result.push(part);
    }
  });

  return result;
};

const sortEmails = (emails) => {
  return emails.sort((a, b) => {
    a = a.split("");
    b = b.split("");
    let i = 0,
      j = 0;
    while (i < a.length && j < b.length) {
      if (a[i].charCodeAt(0) !== b[j].charCodeAt(0)) {
        return a[i].charCodeAt(0) - b[j].charCodeAt(0);
      }
      ++i;
      ++j;
    }
    if (i < a.length) {
      return 1;
    }
    if (j < b.length) {
      return -1;
    }
    return 0;
  });
};
