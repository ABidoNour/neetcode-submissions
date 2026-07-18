class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result : list[int] = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        right_prod : int = 1
        for i in range(len(nums) - 1,0,-1):
            right_prod *= nums[i]
            result[i - 1] = result[i - 1] * right_prod
        return(result)