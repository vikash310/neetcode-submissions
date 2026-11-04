class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        max_p = 0

        for sell in prices:
            max_p = max(max_p,sell - minbuy)
            minbuy = min(minbuy, sell)

        return max_p


        