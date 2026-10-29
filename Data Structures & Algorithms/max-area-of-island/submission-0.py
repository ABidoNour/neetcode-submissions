class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        maxi = 0
        for r, row in enumerate(grid):
            for c, land in enumerate(row):
                if land == 0 or (r,c) in visited:
                    continue

                queue = collections.deque([(r,c)])
                visited.add((r,c))
                area = 0
                while queue:
                    cr,cc = queue.popleft()
                    area += 1

                    for dr,dc in directs:
                        nr, nc = cr + dr, cc + dc
                        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(row):
                            continue
                        if grid[nr][nc] == 0 or (nr,nc) in visited:
                            continue

                        visited.add((nr,nc))
                        queue.append((nr,nc))

                maxi = max(area,maxi)
        return maxi