class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)

        res, i = 1, 0
        while i < len(arr)-1:
            if arr[i] == arr[i+1]:
                i += 1
                continue
            
            comps = [lambda x, y: x < y, lambda x, y: x > y]
            c = 0 if arr[i] < arr[i+1] else 1
            
            j = i
            while j < len(arr)-1 and comps[c](arr[j], arr[j+1]):
                j += 1
                c = 1 - c
            
            res = max(res, j-i+1)
            i = j
        return res