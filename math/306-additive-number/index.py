class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        if len(num) < 3:
            return False

        for i in range(1, n):
            # leading 0 at first digit
            if i > 1 and num[0] == '0':
                break
            for j in range(i + 1, n):
                # leading 0 at second digit
                if j > i + 1 and num[i] == '0':
                    break

                x, y, z = 0, i, j
                while z < n:
                    result = str(int(num[x:y]) + int(num[y:z]))
                    if num[z:].startswith(result):
                        # move forward
                        x, y, z = y, z, z + len(result)
                    else:
                        break

                if z == n:
                    return True

        return False