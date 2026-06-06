class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def bruteForce(gas, cost):
            
            def canCircuit(gas, cost, s):
                
                if gas[s] < cost[s]:
                    return False
                
                n = len(gas)
                g = gas[s] - cost[s]
                i = (s + 1) % n
                while i != s:
                    g += gas[i] - cost[i]
                    if g < 0:
                        return False
                    i = (i + 1) % n
                return True
            
            for i in range(len(gas)):
                if canCircuit(gas, cost, i):
                    return i
            return -1
        
        # return bruteForce(gas, cost)

        def bfs(gas, cost):
            from collections import deque

            n = len(gas)
            Q = deque()
            for i in range(n):
                if gas[i] >= cost[i]:
                    Q.append((i, (i+1) % n, gas[i] - cost[i]))
            
            while len(Q) > 0:
                s, i, g = Q.popleft()
                if s == i:
                    return s

                if g + gas[i] >= cost[i]:
                    Q.append((s, (i+1) % n, g + gas[i] - cost[i]))
            
            return -1
        
        # return bfs(gas, cost)

        def greedy(gas, cost):
            
            if sum(gas) < sum(cost):
                return -1
            
            n = len(gas)
            s, total = 0, 0
            for i in range(n):
                total += gas[i] - cost[i]
                if total < 0:
                    s, total = i+1, 0
            return s
        
        return greedy(gas, cost)
