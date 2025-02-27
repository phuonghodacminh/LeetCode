class Solution(object):
    def backtracking(self, rows, check, result, n, cols, dig, anti_dig):
        if rows == n:
            result.append(["".join(r) for r in check])
            return
        else:
            for c in range(n):
                if c in cols:
                    continue
                if rows + c in dig:
                    continue
                if rows - c in anti_dig:
                    continue
                
                check[rows][c] = 'Q'
                cols.add(c)
                dig.add(rows + c)
                anti_dig.add(rows - c)
                self.backtracking(rows + 1, check, result, n, cols, dig, anti_dig)
                check[rows][c] = '.'
                cols.remove(c)
                dig.remove(rows + c)
                anti_dig.remove(rows - c)

            

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        check = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        dig = set()
        anti_dig = set()
        result = []
        self.backtracking(0, check, result, n, cols, dig, anti_dig)
        return result


        
        