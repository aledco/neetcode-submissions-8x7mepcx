class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #seen = set()
        candidates.sort()

        def dfs(i, cur, total):
            # if tuple(cur) in seen:
            #     return
            if total == target:
                # seen.add(tuple(cur))
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