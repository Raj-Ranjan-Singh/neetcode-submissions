class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        profit=0
        for i in range(1,len(prices)):
            curr_profit=prices[i]-min
            if(curr_profit>profit):
                profit=curr_profit
            min=prices[i] if prices[i]<min else min
        return profit