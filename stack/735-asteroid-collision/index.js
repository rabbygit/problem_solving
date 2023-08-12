/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
const asteroidCollision = function (asteroids) {
  const stack = [];

  for (let a of asteroids) {
    while (stack.length && stack[stack.length - 1] > 0 && a < 0) {
      const diff = a + stack[stack.length - 1];
      if (diff < 0) stack.pop();
      else if (diff > 0) a = 0;
      else {
        stack.pop();
        a = 0;
      }
    }

    if (a) stack.push(a);
  }

  return stack;
};
