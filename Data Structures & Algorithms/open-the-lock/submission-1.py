class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def spin(lock, i, d):
            c = lock[i]
            c = str((int(c) + d) % 10)
            return lock[:i] + c + lock[i+1:]
        
        def distance(lock, target):
            res = 0
            for l, t in zip(lock, target):
                res += abs(int(l) - int(t))
            return res
        
        def bfs(deadends, target):
            from collections import deque
            if "0000" in deadends:
                return -1
            
            queue = deque([("0000", 0)])
            min_spins = sys.maxsize
            while len(queue) > 0:
                lock, spins = queue.popleft()
                if lock == target:
                    return spins
                    #min_spins = min(min_spins, spins)
                    #continue
                
                for i in range(len(lock)):
                    for d in (-1, 1):
                        next_lock = spin(lock, i, d)
                        if next_lock not in deadends:
                            deadends.add(next_lock)
                            queue.append((next_lock, spins+1))
            if min_spins == sys.maxsize:
                return -1
            return min_spins
        
        return bfs(set(deadends), target)
    
        def bfs_withPriorityQueue(deadends, target):
            import heapq

            if "0000" in deadends:
                return -1
            
            queue = [0, (distance("0000", target), "0000")]
            heapq.heapify(queue)

            while len(queue) > 0:
                spins, _, lock = heapq.heappop(queue)
                if lock == target:
                    return spins
                
                for i in range(len(lock)):
                    for d in (-1, 1):
                        next_lock = spin(lock, i, d)
                        if next_lock not in deadends:
                            deadends.add(next_lock)
                            queue.append((next_lock, spins+1))
            if min_spins == sys.maxsize:
                return -1
            return min_spins
    
        # return bfs_withPriorityQueue(set(deadends), target)