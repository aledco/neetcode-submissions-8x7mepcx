class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        C = list(sorted(zip(position, speed), reverse=True))
        S = []
        for p, s in C:
            t = (target - p) / s
            if len(S) == 0 or t > S[-1]:
                S.append(t)
        return len(S)


