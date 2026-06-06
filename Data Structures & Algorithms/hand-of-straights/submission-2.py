import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand = list(sorted(hand, reverse=True)) # O(nlogn) time
        runs = defaultdict(list) # O(n) space
        while len(hand) > 0: # O(nlogn) time
            c = hand.pop()
            if len(runs[c-1]) > 0 and runs[c-1][0][0] < groupSize:
                s, run = heapq.heappop(runs[c-1])
                run.append(c)
                heapq.heappush(
                    runs[c],
                    (s+1, run)
                )
            else:
                heapq.heappush(
                    runs[c], 
                    (1, [c])
                )
        
        for groups in runs.values():
            if len(groups) > 0 and groups[0][0] < groupSize:
                return False
        return True
                