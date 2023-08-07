class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengersAtstations = [0] * 1001  # 1000 stations
        totalPassengers = 0

        # record how many passengers at a given station
        for trip in trips:
            passengersAtstations[trip[1]] += trip[0]  # on-board
            passengersAtstations[trip[2]] -= trip[0]  # drop-off

        for passengers in passengersAtstations:
            # calculate total passengers so far
            totalPassengers += passengers
            if totalPassengers > capacity:
                return False

        return True
