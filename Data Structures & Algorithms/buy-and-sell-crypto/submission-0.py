class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lft,rgt = 0,0
        curr_max_r = -1
        max_profit=0
        while rgt < len(prices):
            if lft == rgt:
                rgt += 1
            while rgt < len(prices) and prices[rgt] >= prices[lft]:
                if curr_max_r == -1 or prices[rgt] > prices[curr_max_r]:
                    curr_max_r = rgt
                rgt += 1
            if rgt < len(prices) and prices[rgt] < prices[lft]:
                max_profit = max(prices[curr_max_r] - prices[lft],max_profit)
                lft = rgt
                curr_max_r = -1
        return max(max_profit,prices[curr_max_r] - prices[lft])