class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
        
        res = candy[n-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
            res += candy[i]
        
        return res

        # n = len(ratings)
        # candy = [1] * n
        # for i in range(1, n):
        #     if ratings[i-1] < ratings[i]:
        #         candy[i] = candy[i-1] + 1
        #     elif ratings[i-1] > ratings[i]:
        #         # TODO should be able to optimize this by keeping track of m, c where m is the index of the last mountain, and c is the amount of candy at the peak
        #         if candy[i-1] == 1: # need to update candy backwards while ratings[i-1] > ratings[i]
        #             j = i
        #             while j-1 >= 0 and ratings[j-1] > ratings[j] and candy[j-1] <= candy[j]:
        #                 j -= 1
        #                 candy[j] += 1
        #         # otherwise, we can leave candy[i] = 1. If the next rating is smaller, it can update
        # return sum(candy)
            
