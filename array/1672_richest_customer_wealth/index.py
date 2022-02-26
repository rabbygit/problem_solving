class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for account in accounts:
            total_wealth = sum(account)
            maxWealth = max(maxWealth,total_wealth)
        
        return maxWealth