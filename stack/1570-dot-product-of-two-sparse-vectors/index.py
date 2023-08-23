"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
1. dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
2. A sparse vector is a vector that has mostly zero values, 
you should store the sparse vector efficiently and compute the dot product between two SparseVector.

"""


"""
Time complexity: O(n) for creating the <index, value> pair for non-zero values; 
O(L+L2) for calculating the dot product.
Space complexity: O(L) for creating the <index, value> pairs for non-zero values. 
"""


class SparseVector:

    def __init__(self, nums: List[int]):
        self.stack = []
        for i, n in enumerate(nums):
            if n:
                self.stack.append([i, n])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        while self.stack and vec.stack:
            if self.stack[-1][0] == vec.stack[-1][0]:
                res += self.stack[-1][1] * vec.stack[-1][1]
                self.stack.pop()
                vec.stack.pop()
            elif self.stack[-1][0] < vec.stack[-1][0]:
                vec.stack.pop()
            else:
                self.stack.pop()

        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)