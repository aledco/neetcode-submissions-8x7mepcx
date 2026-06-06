import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hand = list(sorted(hand, reverse=True))
        runs = defaultdict(list)
        while len(hand) > 0:
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
                