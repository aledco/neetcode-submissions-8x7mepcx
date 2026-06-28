class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            match op:
                case '+':
                    res.append(res[-1] + res[-2])
                case 'D':
                    res.append(res[-1] * 2)
                case 'C':
                    res.pop()
                case x:
                    res.append(int(x))
        return sum(res)