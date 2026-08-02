class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]

        for price in prices:
            if price <= lowest:
                lowest = price
            new_profit = price - lowest
            if new_profit > profit:
                profit = new_profit
        
        return profit

        