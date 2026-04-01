class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        base case: path == word
        constraints: len(path) < len(word), cannot use same box twice
        choices: move up, left, down, right (directions matrix?)
        backtracking step: pop back
        notes: need set of chars to ensure not repeating?
        '''
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows, cols = len(board), len(board[0])

        def backtrack(row, col, index, visited):
            if index == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if (row,col) in visited:
                return False
            if board[row][col] != word[index]:
                return False

            visited.add((row, col))
            for dr, dc in directions:
                if backtrack(row + dr, col + dc, index + 1, visited):
                    return True
            visited.remove((row, col))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0, set()):
                    return True
        return False



