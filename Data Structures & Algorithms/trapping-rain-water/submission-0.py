class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        l_max,r_max = 0,0
        trapped = 0
        while l < r:
            l_max = max(height[l],l_max)
            r_max = max(height[r],r_max)
            curr_wall = min(l_max,r_max) 
            if l_max <= r_max:
                trapped += curr_wall - height[l]
                l += 1
            else:
                trapped += curr_wall - height[r]
                r -= 1
        return trapped