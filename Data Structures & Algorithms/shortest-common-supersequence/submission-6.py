class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def dfs(s1, s2, i=0, j=0):
            if i >= len(s1):
                return s2[j:]
            elif j >= len(s2):
                return s1[i:]
            
            if s1[i] == s2[j]:
                return s1[i] + dfs(s1, s2, i+1, j+1)
            else:
                scs1 = s1[i] + dfs(s1, s2, i+1, j)
                scs2 = s2[j] + dfs(s1, s2, i, j+1)
                if len(scs1) <= len(scs2):
                    return scs1
                else:
                    return scs2
        
        # return dfs(str1, str2)

        def dynamicProgramming_topDown(s1, s2):
            
            cache = {}

            def dfs(s1, s2, i=0, j=0):
                nonlocal cache

                if (i, j) in cache:
                    return cache[(i, j)]
                
                if i >= len(s1):
                    cache[(i, j)] = list(reversed(s2[j:]))
                    return cache[(i, j)]
                elif j >= len(s2):
                    cache[(i, j)] = list(reversed(s1[i:]))
                    return cache[(i, j)]
                
                if s1[i] == s2[j]:
                    cache[(i, j)] = dfs(s1, s2, i+1, j+1) + [s1[i]]
                else:
                    scs1 =  dfs(s1, s2, i+1, j) + [s1[i]]
                    scs2 = dfs(s1, s2, i, j+1) + [s2[j]]
                    if len(scs1) <= len(scs2):
                        cache[(i, j)] = scs1
                    else:
                        cache[(i, j)] = scs2
                return cache[(i, j)]
            
            return "".join(reversed(dfs(s1, s2)))

        # return dynamicProgramming_topDown(str1, str2)

        def dynamicProgramming_bottomUp(s1, s2):
            
            m, n = len(s1), len(s2)

            def dynamicProgramming(s1, s2):
                dp = [[0] * (n+1) for _ in range(m+1)]
                for i in range(m+1):
                    dp[i][0] = i
                for j in range(n+1):
                    dp[0][j] = j
                
                for i in range(1, m+1):
                    for j in range(1, n+1):
                        if s1[i-1] == s2[j-1]:
                            dp[i][j] = 1 + dp[i-1][j-1]
                        else:
                            dp[i][j] = 1 + min(
                                dp[i-1][j],
                                dp[i][j-1]
                            )
                return dp
            
            def traceBack(s1, s2, dp):
                res = []
                i, j = m, n
                while i > 0 or j > 0:
                    if i > 0 and j > 0:
                        if s1[i-1] == s2[j-1]:
                            res.append(s1[i-1])
                            i -= 1
                            j -= 1
                        elif dp[i-1][j] < dp[i][j-1]:
                            res.append(s1[i-1])
                            i -= 1
                        else:
                            res.append(s2[j-1])
                            j -= 1
                    elif i > 0:
                        res.append(s1[i-1])
                        i -= 1
                    else:
                        res.append(s2[j-1])
                        j -= 1
                return "".join(reversed(res))
            
            dp = dynamicProgramming(s1, s2)
            return traceBack(s1, s2, dp)
        
        return dynamicProgramming_bottomUp(str1, str2)

    #     def greedy(s1, s2):
    #         res = []
    #         i = j = 0
    #         while i < len(s1) or j < len(s2):
    #             if i < len(s1) and j < len(s2):
    #                 if s1[i] == s2[j]:
    #                     res.append(s1[i])
    #                     i += 1
    #                     j += 1
    #                 elif (len(s1) - i) >= (len(s2) - j):
    #                     res.append(s1[i])
    #                     i += 1
    #                 else:
    #                     res.append(s2[j])
    #                     j += 1
    #             elif i < len(s1):
    #                 res.append(s1[i])
    #                 i += 1
    #             else:
    #                 res.append(s2[j])
    #                 j += 1
    #         return "".join(res)
        
    #     # return greedy(str1, str2)
        
    #     # idea: turn the larger string into a suffix array, and find the largest common substring
    #     #       then recurse on the rest of the string that is not in the substring

    #     def divide(s1, s2, i1, j1, i2, j2):
    #         # print(i1, j1, i2, j2)
    #         # TODO base case
    #         if i1 > j1 and i2 > j2:
    #             return ""
    #         elif i1 > j1:
    #             # print('HERE', s2[i2:j2+1])
    #             return s2[i2:j2+1]
    #         elif i2 > j2:
    #             return s1[i1:j1+1]
                        
    #         # print(s1[i1:j1+1], s2[i2:j2+1])
    #         exists, si1, sj1, si2, sj2 = self.longestCommonSubstring(s1, s2, i1, j1, i2, j2)
    #         # print(exists, si1, sj1, si2, sj2)
    #         if not exists:
    #             return s1[i1:j1+1] + s2[i2:j2+1]
            
    #         return (
    #             divide(s1, s2, i1, si1-1, i2, si2-1) + 
    #             s1[si1:sj1+1] +
    #             divide(s1, s2, sj1+1, j1, sj2+1, j2)
    #         )
        
    #     return divide(str1, str2, 0, len(str1)-1, 0, len(str2)-1)

    # def longestCommonSubstring(self, s1, s2, i1, j1, i2, j2):
    #     m, n = j1 - i1 + 1, j2 - i2 + 1
    #     # print("1.", i1, j1, i2, j2, m, n)
    #     dp = [[0] * (n+1) for _ in range(m+1)]

    #     max_length, max_end_i, max_end_j = -1, -1, -1

    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             # print("2.", i-1, j-1, s1[i-1], s2[j-1])
    #             if s1[i1+i-1] == s2[i2+j-1]:
    #                 try:
    #                     dp[i][j] = dp[i-1][j-1] + 1
    #                 except Exception as e:
    #                     print(i, j, m, n)
    #                     raise e
    #                 # print("3.", dp[i][j], max_length)
    #                 if dp[i][j] > max_length:
    #                     max_length = dp[i][j]
    #                     max_end_i = i1+i-1
    #                     max_end_j = i2+j-1
    #                     # print("4.", max_length, max_end_i, max_end_j)

    #     return (
    #         max_length > 0,
    #         (max_end_i + 1) - max_length, 
    #         max_end_i, 
    #         (max_end_j + 1) - max_length, 
    #         max_end_j
    #     )

    