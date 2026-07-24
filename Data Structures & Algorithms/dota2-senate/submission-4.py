class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        senate = list(senate)
        while len(senate) > 1:
            R = deque()
            D = deque()
            rv = dv = 0
            for i, s in enumerate(senate):
                if s == 'R':
                    if dv > 0:
                        dv -= 1
                    else:
                        R.append(i)
                        rv += 1
                elif s == 'D':
                    if rv > 0:
                        rv -= 1
                    else:
                        D.append(i)
                        dv += 1
        
            assert rv == 0 or dv == 0
            assert len(R) > 0 or len(D) > 0

            print(senate)
            print(R, rv)
            print(D, dv)
            print()

            for _ in range(rv):
                if len(D) == 0:
                    break
                D.popleft()
            
            for _ in range(dv):
                if len(R) == 0:
                    break
                R.popleft()
            
            print(R, rv)
            print(D, dv)
            print()

            if len(R) == 0:
                return 'Dire'
            if len(D) == 0:
                return 'Radiant'
            
            senate = []
            while len(R) > 0 and len(D) > 0:
                if R[0] < D[0]:
                    senate.append('R')
                    R.popleft()
                else:
                    senate.append('D')
                    D.popleft()

            senate += ['R'] * len(R)
            senate += ['D'] * len(D)

        if senate[0] == 'D':
            return 'Dire'
        else:
            return 'Radiant'
            