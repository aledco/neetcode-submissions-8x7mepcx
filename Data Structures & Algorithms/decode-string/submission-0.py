class Solution:
    def decodeString(self, s: str) -> str:
        tokens = self.tokenize(s)
        stack = [["", 1]]
        for t, v in tokens:
            if t == "str":
                stack[-1][0] += v
            elif t == "open":
                stack.append(["", v])
            elif t == "close":
                r, p = stack.pop()
                stack[-1][0] += (r * p)
            else:
                print(f"unexpected token: ({t}, {v})")
        return stack[-1][0]

    def tokenize(self, s: str) -> List:
        tokens = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                r = ""
                while i < len(s) and s[i].isdigit():
                    r += s[i]
                    i += 1
                if i+1 < len(s) and s[i] == "[":
                    i += 1
                    tokens.append(("open", int(r)))
                else:
                    tokens.append(("str", r))
            elif s[i].isalpha():
                r = ""
                while i < len(s) and s[i].isalpha():
                    r += s[i]
                    i += 1
                tokens.append(("str", r))
            elif s[i] == "]":
                i += 1
                tokens.append(("close", "]"))
            else:
                print(f"unexpected char: {s[i]}")
        return tokens
            