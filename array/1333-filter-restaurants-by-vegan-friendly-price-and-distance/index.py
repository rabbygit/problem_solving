class Solution:

    def filterRestaurants(self, restaurants: List[List[int]],
                          veganFriendly: int, maxPrice: int,
                          maxDistance: int) -> List[int]:
        res = []

        # [id=1, rating=4, veganFriendly=1, price=40, distance=10]
        for id, r, v, p, d in restaurants:
            if (veganFriendly == 0 or v
                    == veganFriendly) and p <= maxPrice and d <= maxDistance:
                res.append([r, id])

        res.sort(reverse=True)

        return [id for _, id in res]
