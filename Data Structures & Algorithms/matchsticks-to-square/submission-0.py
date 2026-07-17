class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        
        side_length = perimeter // 4
        if max(matchsticks) > side_length:
            return False

        def backtrack(matchsticks, side_length, sides=None, i=0):
            if sides is None:
                sides = [0, 0, 0, 0]
            
            if i >= len(matchsticks):
                for j in range(len(sides)):
                    if sides[j] != side_length:
                        return False
                return True
            
            for j in range(len(sides)):
                if sides[j] + matchsticks[i] <= side_length:
                    sides[j] += matchsticks[i]
                    if backtrack(matchsticks, side_length, sides, i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        
        return backtrack(matchsticks, side_length)
