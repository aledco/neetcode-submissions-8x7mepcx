from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        def bruteForce(tasks, n):
            task_counter = Counter(tasks)
            tasks = [
                [x[0], x[1], 0]
                for x in sorted(task_counter.items(), reverse=True, key=lambda x: x[1])
            ]
            cycles = 0
            while len(task_counter) > 0:
                cycles += 1
                cycle_used = False
                for t in tasks:
                    if t[0] not in task_counter: 
                        continue
                    if t[2] == 0:
                        if cycle_used:
                            continue
                        t[1] -= 1
                        if t[1] == 0:
                            del task_counter[t[0]]
                        t[2] = n
                        cycle_used = True
                    elif t[2] > 0:
                        t[2] -= 1
                tasks = list(sorted(tasks, reverse=True, key=lambda x: x[1]))
            return cycles

        def optimized(T, n):
            H = [[c, x] for x, c in Counter(T).items()]
            heapq.heapify_max(H)
            Q = deque()
            cycle = 0
            while len(H) > 0 or len(Q) > 0:
                cycle += 1

                while len(Q) > 0 and Q[0][0] + n < cycle:
                    _, c, t = Q.popleft()
                    heapq.heappush_max(H, [c, t])
                
                if len(H) > 0:
                    c, t = heapq.heappop_max(H)
                    if c-1 > 0:
                        Q.append([cycle, c-1, t])
            return cycle

        return optimized(tasks, n)
        
