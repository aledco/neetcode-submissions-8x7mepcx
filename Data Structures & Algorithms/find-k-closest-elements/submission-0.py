class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # idea: 
        #   first find the position q where x should be in arr
        #   then initialize i to the index of element <= x and j to the index of element > x
        #   if arr[i] is closer to x than arr[j], add arr[i] to the front of the deque
        #   if arr[j] is closer to x than arr[i], add arr[j] to the back of the deque

        from collections import deque

        q = 0
        while q < len(arr) and arr[q] < x:
            q += 1
        
        j = q
        i = q-1
        res = deque()
        while len(res) < k:
            if i < 0:
                res.append(arr[j])
                j += 1
            elif j >= len(arr):
                res.appendleft(arr[i])
                i -= 1
            else:
                if abs(arr[i] - x) <= abs(arr[j] - x):
                    res.appendleft(arr[i])
                    i -= 1
                else:
                    res.append(arr[j])
                    j += 1
        return list(res)