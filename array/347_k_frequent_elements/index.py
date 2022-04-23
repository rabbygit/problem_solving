class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count_map = {}
        count_array = [[] for i in range(n+1)]
        result = []

        # count occurence for each element and keep in hashMap like 1 -> 4
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        # build array for occurence from hashMap. like [ [] , [] , [] , [], [1,2 ..] ]
        for key, value in count_map.items():
            count_array[value].append(key)

        # build the result
        for i in range(n+1 , 0, -1):
            for num in count_array[i]:
                result.append(num)
                # check k element is taken already or not
                if len(result) == k:
                    return result
        

