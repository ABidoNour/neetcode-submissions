class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                past_temp, past_i = stack.pop()
                out[past_i] = (i - past_i)
            stack.append((temp,i))
        return out