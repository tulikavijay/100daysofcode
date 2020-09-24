class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = prices[0]
        sell = 0
        profit = 0
        #local maxima and local minima
        #index of local minima < index of local maxima
        for i in range(1,len(prices)): 
            if buy > prices[i]:
                buy = prices[i]
                sell = 0
            if sell < prices[i]:
                sell = prices[i]
                profit = max(profit,sell-buy)
        return profit
