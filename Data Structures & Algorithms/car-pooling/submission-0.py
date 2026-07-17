class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        import heapq

        trips = list(sorted(trips, key = lambda x: x[1]))
        passengers = []

        i, j = trips[0][1], 0
        while j < len(trips):
            while len(passengers) > 0 and passengers[0][0] <= i:
                _, p = heapq.heappop(passengers)
                capacity += p
            
            while j < len(trips) and trips[j][1] == i:
                capacity -= trips[j][0]
                if capacity < 0:
                    return False
                
                heapq.heappush(passengers, (trips[j][2], trips[j][0]))
                j += 1
            
            if j < len(trips):
                i = trips[j][1]
        return True

