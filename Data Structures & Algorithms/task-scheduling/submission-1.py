from collections import Counter

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
        
        return bruteForce(tasks, n)
        
