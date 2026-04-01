class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # keep running max
        # bfs recursion
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        res = 0

        def bfs(r, c):
            area = 1
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            while q: 
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    area+=1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r,c))
        return res