import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        def greedy(k, w, P, C):
            # use a max heap to always select the project with max capital gain (profit - capital)
            # if we don't have enough capital to start the highest capital gain project, start the next highest ROI project

            
            gain, expensive = [], []
            for i, (p, c) in enumerate(zip(P, C)):
                if p <= 0: # do not execute projects with no profit
                    continue

                if c <= w:
                    heapq.heappush_max(gain, p)
                else:
                    heapq.heappush(expensive, (c, p))
                
            for i in range(k):
                if len(gain) == 0:
                    break

                w += heapq.heappop_max(gain)
 
                while len(expensive) > 0:
                    c, p = heapq.heappop(expensive)
                    if c > w:
                        heapq.heappush(expensive, (c, p))
                        break

                    heapq.heappush_max(gain, p)
                    
            return w
        
        return greedy(k, w, profits, capital)