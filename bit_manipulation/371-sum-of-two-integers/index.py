class Solution:

    def getSum(self, a: int, b: int) -> int:
        # python integer is more than 32 bits
        bitShortner = 0xffffffff  # 32 bits 1

        while (b & bitShortner) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return (a & bitShortner) if b > 0 else a