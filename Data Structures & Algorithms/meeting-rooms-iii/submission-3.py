class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq
        
        counts = {i: 0 for i in range(n)}

        meeting_queue = [(s, s, e) for s, e in meetings]
        heapq.heapify(meeting_queue)

        meetings_happening = []

        rooms_available = list(range(n))
        heapq.heapify(rooms_available)

        while len(meeting_queue) > 0:
            s, _, e = heapq.heappop(meeting_queue)

            while len(meetings_happening) > 0:
                he, hr = meetings_happening[0]
                if he > s:
                    break
                heapq.heappop(meetings_happening)
                heapq.heappush(rooms_available, hr)
            
            if len(rooms_available) == 0:
                assert len(meetings_happening) > 0
                he, r = heapq.heappop(meetings_happening)
                s, e = he, he + (e - s)
            else:
                r = heapq.heappop(rooms_available)
            
            counts[r] += 1
            heapq.heappush(meetings_happening, (e, r))

        return max(counts.items(), key=lambda x: (x[1], -x[0]))[0]
