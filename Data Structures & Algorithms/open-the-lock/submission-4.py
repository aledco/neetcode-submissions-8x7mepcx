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
            while len(queue) > 0:
                lock, spins = queue.popleft()
                if lock == target:
                    return spins
                
                for i in range(len(lock)):
                    for d in (-1, 1):
                        next_lock = spin(lock, i, d)
                        if next_lock not in deadends:
                            deadends.add(next_lock)
                            queue.append((next_lock, spins+1))
            return -1
        
        return bfs(set(deadends), target)
    
