class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        res = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while len(stack) > 0:
                    b = stack.pop()
                    if b > -a:
                        stack.append(b)
                        a = 0
                        break
                    elif -a == b:
                        a = 0
                        break
                if a != 0:
                    res.append(a)
        return res + stack
                