class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        num_min = prices[0]
        profit = 0

        for i in range(1,len(prices)):

            if prices[i] < num_min:
                num_min = prices[i]
            elif prices[i] > num_min:
                profit = prices[i] - num_min

            max_profit = max(max_profit,profit)
        
        return max_profit            