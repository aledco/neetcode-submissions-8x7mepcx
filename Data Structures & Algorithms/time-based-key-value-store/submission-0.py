class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))
        print(self.values)

    def get(self, key: str, timestamp: int) -> str:
        
        def bin_search(L, t, i, j):
            if i >= j:
                return ""
            
            m = (i + j) // 2
            if L[m][0] == t:
                return L[m][1]
            elif L[m][0] < t and (m+1 >= len(L) or L[m+1][0] > t):
                return L[m][1]
            elif L[m][0] > t:
                return bin_search(L, t, i, m)
            else:
                return bin_search(L, t, m+1, j)
            
        L = self.values[key]
        return bin_search(L, timestamp, 0, len(L))
