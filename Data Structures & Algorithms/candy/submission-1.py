class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # valleys where rating <= rating -1 and rating + 1 will have 1 candy
        # candies will go up by 1 as ratings increase from the valley


        res = 0
        n = len(ratings)
        candy = [1] * n
        for i in range(n):
            if i-1 >= 0 and ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
            elif i-1 >= 0 and ratings[i-1] > ratings[i]:
                if candy[i-1] == 1: # need to update candy backwards while ratings[i-1] > ratings[i]
                    j = i
                    while j-1 >= 0 and ratings[j-1] > ratings[j] and candy[j-1] <= candy[j]:
                        j -= 1
                        candy[j] += 1
                    
                # otherwise, we can leave candy[i] = 1. If the next rating is smaller, it can update
        print(candy)
        return sum(candy)
            
