class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for d in path.split("/"):
            if d == "" or d == ".":
                continue
            elif d == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(d)
        return "/" + "/".join(stack)