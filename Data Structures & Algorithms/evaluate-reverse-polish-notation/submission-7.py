class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def parseInt(t):
            try:
                return int(t)
            except:
                return None
        
        S = []
        for t in tokens:
            i = parseInt(t)
            if i is not None:
                S.append(i)
            else:
                b, a = S.pop(), S.pop()
                if t == '+':
                    S.append(a + b)
                if t == '-':
                    S.append(a - b)
                if t == '*':
                    S.append(a * b)
                if t == '/':
                    S.append(int(float(a) / b))
        return S.pop()