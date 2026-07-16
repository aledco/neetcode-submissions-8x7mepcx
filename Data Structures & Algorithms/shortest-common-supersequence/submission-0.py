class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def greedy(s1, s2):
            res = []
            i = j = 0
            while i < len(s1) or j < len(s2):
                if i < len(s1) and j < len(s2):
                    if s1[i] == s2[j]:
                        res.append(s1[i])
                        i += 1
                        j += 1
                    elif (len(s1) - i) >= (len(s2) - j):
                        res.append(s1[i])
                        i += 1
                    else:
                        res.append(s2[j])
                        j += 1
                elif i < len(s1):
                    res.append(s1[i])
                    i += 1
                else:
                    res.append(s2[j])
                    j += 1
            return "".join(res)
        
        # return greedy(str1, str2)
        
        # idea: turn the larger string into a suffix array, and find the largest common substring
        #       then recurse on the rest of the string that is not in the substring

        def divide(s1, s2, i1, j1, i2, j2):
            # TODO base case
            if i1 > j1 or i2 > j2:
                return ""

            si1, sj1, si2, sj2 = self.longestCommonSubstring(s1, s2, i1, j1, i2, j2)
            # TODO if no substring, need to add both s1 and s2
            return (
                divide(s1, s2, i1, si1-1, i2, si2-1) + 
                s1[si1:sj1+1] +
                divide(s1, s2, sj1+1, j1, si2+1, j2)
            )
        
        return divide(str1, str2, 0, len(str1)-1, 0, len(str2)-1)

    def longestCommonSubstring(self, s1, s2, i1, j1, i2, j2):
        m, n = j1 - i1 + 1, j2 - i2 + 1
        dp = [[0] * (n+1) for _ in range(m+1)]

        max_length, max_end_i, max_end_j = 0, 0, 0

        for i in range(i1+1, j1+1):
            for j in range(i2+1, j2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        max_end_i = i-1
                        max_end_j = j-1

        return (
            max_length - max_end_i + 1, 
            max_end_i, 
            max_length - max_end_j + 1, 
            max_end_j
        )

    