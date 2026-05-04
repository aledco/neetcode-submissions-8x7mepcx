class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            j = i
            while j < len(candidates):
                n = candidates[j]
                if total + n > target:
                    return
                cur.append(n)
                dfs(j+1, cur, total + n)
                cur.pop()
                j += 1
                while j < len(candidates) and candidates[j] == n:
                    j += 1

        dfs(0, [], 0)
        return res