class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        basically a graph problem
        dfs/bfs?
            recurse on each direction, 
            if cell 0 (or r < rows or c < cols ...) return 0
            elif cell 1, set cell to 0 and iterate through
        '''

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        fresh = 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
        while fresh > 0:
            flag = False
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            row, col = r + dr, c + dc
                            if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                                grid[row][col] = 3
                                fresh -= 1
                                flag = True
            if not flag:
                return -1
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
            res += 1
        return res
