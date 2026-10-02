class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        def check(w_ind, b_i, b_j):
            if w_ind >= len(word) or b_i < 0 or b_j < 0 or b_i >= len(board) or b_j >= len(board[b_i]):
                return False
            if (b_i,b_j) in visited:
                return False
            if word[w_ind] == board[b_i][b_j]:
                if w_ind < len(word) - 1:
                    visited.add((b_i,b_j))
                    result = check(w_ind + 1,b_i + 1, b_j) or check(w_ind + 1,b_i, b_j + 1) or check(w_ind + 1, b_i - 1, b_j) or check(w_ind + 1, b_i, b_j - 1)
                    visited.remove((b_i,b_j))
                    return result
                else:
                    return True
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if check(0,i,j):
                    return True
        return False