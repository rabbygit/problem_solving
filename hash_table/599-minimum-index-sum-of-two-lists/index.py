class Solution:

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2Map = {}

        for idx, s in enumerate(list2):
            if s not in list2Map:
                list2Map[s] = idx

        minSum = -1
        res = []
        for idx, s in enumerate(list1):
            if s in list2Map:
                if (minSum == -1) or minSum == idx + list2Map[s]:
                    minSum = idx + list2Map[s]
                    res.append(s)
                elif minSum > idx + list2Map[s]:
                    res = []
                    res.append(s)

        return res
