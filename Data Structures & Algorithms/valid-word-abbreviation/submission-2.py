class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # parse abbr
        parsed = []
        i = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                n = ""
                while i < len(abbr) and abbr[i].isdigit():
                    n += abbr[i]
                    i += 1
                if n[0] == '0': # need to handle leading zeroes as special case
                    return False
                parsed.append(('int', int(n)))
            else:
                parsed.append(('char', abbr[i]))
                i += 1

        stack = list(reversed(word))
        for t, a in parsed:
            if len(stack) == 0:
                return False
            if t == 'char':
                if stack[-1] == a:
                    stack.pop()
                else:
                    return False
            else:
                if a == 0 or a > len(stack):
                    return False
                for _ in range(a):
                    stack.pop()
        return len(stack) == 0