class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direct = [(0,1),(1,0),(0,-1),(-1,0)]
        islands = 0
        visited = set()
        
        def dfs(row,col):
            if (row,col) in visited:
                return
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                return
            if grid[row][col] == '0':
                return
            visited.add((row,col))
            for d in direct:
                dfs(row + d[0],col + d[1])

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if (r,c) in visited or col == '0':
                    continue
                islands += 1
                dfs(r,c)
        
        return islands