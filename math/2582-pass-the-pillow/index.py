class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time // (n - 1)
        visited = time % (n - 1)
        return visited + 1 if cycle % 2 == 0 else n - visited
