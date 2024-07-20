class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0 for _ in range(n)] for _ in range(m)]
        i = j = 0
        while i < m and j < n:
            res[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]
            if not rowSum[i]: i += 1
            else: j += 1
        return res