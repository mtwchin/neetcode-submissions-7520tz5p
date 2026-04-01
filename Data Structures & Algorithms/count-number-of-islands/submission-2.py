class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs on items, set to 0 so no need for visited set
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        count = 0

        def dfs(r, c):
            if (r >= rows 
                or r < 0 
                or c >= cols 
                or c < 0
                or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count+=1
        return count
            