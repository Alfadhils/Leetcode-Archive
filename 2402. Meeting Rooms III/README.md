# 2402. Meeting Rooms III

## Intuition
The intuition behind this problem is to efficiently allocate meeting rooms to minimize overlaps.

## Approach
- Initialize two heaps: one to keep track of booked rooms and another to keep track of available rooms.
- Sort the meetings based on their start times.
- Iterate through each meeting:
  - Check if there are any booked rooms that have ended before the current meeting's start time. If so, release those rooms back to the available rooms heap.
  - If there are available rooms, assign one to the current meeting. Otherwise, find the room with the earliest release time and allocate that room to the current meeting.
  - Update the frequency of the assigned room.
- Return the room with the highest frequency.

## Complexity
- Time complexity:
  - Sorting the meetings: O(n log n)
  - Iterating through each meeting: O(n)
  - Inside the loop, operations on heaps take O(log n) time.
  - Overall time complexity: O(n log n)
  
- Space complexity:
  - We use two heaps, one for booked rooms and one for available rooms, each potentially storing up to 'n' elements: O(n)
  - Additionally, we use a dictionary to store the frequency of each room: O(n)
  - Overall space complexity: O(n)

## Code
```python
from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        booked, free = [], list(range(n))
        meetings.sort()
        freq = defaultdict(int)

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                _, room = heappop(booked)
                heappush(free, room)
            
            if free:
                room = heappop(free)
                heappush(booked, [end, room])
            else:
                release, room = heappop(booked)
                heappush(booked, [release + end - start, room])
            
            freq[room] += 1

        return max(freq, key=freq.get)
```
