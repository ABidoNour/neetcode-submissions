class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = nums[:k]
        heapq.heapify(largest)

        for num in nums[k:]:
            if num > largest[0]:
                heapq.heappushpop(largest, num)
        
        return largest[0]