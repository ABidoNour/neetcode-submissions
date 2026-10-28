class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(position[i],speed[i]) for i in range(len(position))]
        times.sort(reverse = True)

        for i, pair in enumerate(times):
            times[i] = (target - pair[0]) / pair[1]
        
        curr_max = 0
        fleets = 0
        for time in times:
            if time > curr_max:
                curr_max = time
                fleets += 1

        return fleets