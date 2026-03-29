class Solution:
    def trap(self, height: List[int]) -> int:
        
        def findBasin(H, i):
            j = i

            # exhaust the decreasing heights
            while j+1 < len(H) and H[j] >= H[j+1]:
                j += 1
            
            print("done decreasing", j)
            if j+1 >= len(H):
                return -1, -1

            # now H[j] < H[j+1], start searching for the basin's right wall
            m, mj = -1, -1
            while j < len(H):
                if H[j] >= H[i]:
                    return min(H[i], H[j]), j
                elif H[j] > m:
                    m, mj = H[j], j
                j += 1
            return min(H[i], m), mj

        def getArea(H, i, j, w):
            A = 0
            for k in range(i+1, j):
                if w - H[k] > 0:
                    A += w - H[k]
            # print("area:", A)
            return A

        def solve(H):
            i, T = 0, 0
            while i < len(H):
                if i+1 < len(H) and H[i+1] < H[i]:
                    print("decreasing", i)
                    w, j = findBasin(H, i)
                    print("basin:", i, j, w)
                    if w == -1:
                        break
                    T += getArea(H, i, j, w)
                    i = j
                else:
                    i += 1
            return T
        
        return solve(height)
