class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_s,min_s = max(piles),1
        if len(piles) == h:
            return max_s
        
        def canEat(speed):
            num_hours = 0
            for i,pile in enumerate(piles):
                num_hours += math.ceil(pile / speed)
                if num_hours > h:
                    return False
            return True
        
        min_answer = max_s
        while min_s <= max_s:
            mid_s = (min_s + max_s) // 2
            if not canEat(mid_s):
                min_s = mid_s + 1
            else:
                min_answer = min(min_answer,mid_s)
                max_s = mid_s - 1
        return min_answer