class Solution:

    def twoCitySchedCost(self, costs):
        costForA = [i for i, j in costs]
        diff = [j - i for i, j in costs]
        return sum(costForA) + sum(sorted(diff)[:len(costs) // 2])
