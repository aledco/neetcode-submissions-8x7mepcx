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
        
        return bruteForce(gas, cost)

                

                

