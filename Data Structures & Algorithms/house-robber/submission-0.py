class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        for i, num in enumerate(nums):
            if i == 0:
                dp.append(num)
                continue
            if i == 1:
                dp.append(max(num,dp[0]))
                continue
            dp.append(max(dp[-1],num + dp[-2]))

        return dp[-1]