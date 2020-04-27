class Solution1:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0

        result = []
        for l, r in intervals:
            result.append(sum(L <= l < R for (L, R) in intervals))
        return max(result)
            

class Solution2:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0
        
        intervals.sort()
        result = []
        for l, _ in intervals:
            nums = 0
            for L, R in intervals:
                if L <= l < R:
                    nums+=1
                elif L > l:
                    break
            result.append(nums)
        return result

import heapq
class Solution3:
    def minMeetingRooms(self, intervals) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

if __name__ == "__main__":
    # Test Case
    intervals = [[13,15],[1,13],[6,9]]

    sol = Solution3()
    print(sol.minMeetingRooms(intervals))