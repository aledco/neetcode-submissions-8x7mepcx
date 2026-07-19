class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def spin(lock, i, d):
            c = lock[i]
            c = str((int(c) + d) % 10)
            return lock[:i] + c + lock[i+1:]
        
        def bfs(deadends, target):
            from collections import deque
            if "0000" in deadends:
                return -1
            
            queue = deque([("0000", 0)]) # TODO use priority queue with distance to target as priority
            min_spins = sys.maxsize
            while len(queue) > 0:
                lock, spins = queue.popleft()
                if lock == target:
                    min_spins = min(min_spins, spins)
                    continue
                
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
                    
                


        # def dfs(deadends, target, lock):
        #     print(lock)
        #     if lock == target:
        #         return 0
        #     elif lock in deadends:
        #         return -1
            
        #     deadends.add(lock)

        #     res = sys.maxsize
        #     for i in range(len(lock)):
        #         for d in (-1, 1):
        #             lock = spin(lock, i, d)
        #             if lock in deadends:
        #                 continue
        #             steps = dfs(deadends, target, lock)
        #             if steps != -1:
        #                 res = 1 + min(res, steps)
        #     if res == sys.maxsize:
        #         return -1
        #     return res
                
        # return dfs(
        #     set(deadends),
        #     target,
        #     "0" * len(target)
        # )