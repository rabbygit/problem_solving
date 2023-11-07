class Solution:

    def minOperations(self, s: str) -> int:
        answ0 = answ1 = 0
        """
        Answer is either "01010101010101010....." or "101010101010101010...."
        To compare this "01010101010101010.....", we have to mod the index by 2.
        index: [0,1,2,3..] mod by 2 ->  [0,1,0,1,0..]
        """
        for i, c in enumerate(s):
            z = str(i % 2)
            if c == z:
                answ0 += 1
            else:
                answ1 += 1

        return min(answ0, answ1)
