# 2073. Time Needed to Buy Tickets
## Intuition
The intuition behind this problem is to simulate the process of buying tickets until all tickets for the desired position are bought.

## Approach
The approach here is to continuously loop through the list of tickets until the desired position, `k`, has no remaining tickets. In each iteration, we decrease the count of available tickets for each position by one, and increment the time taken. We repeat this process until the desired position, `k`, has zero remaining tickets.

## Complexity
- Time complexity:
In the worst case scenario, where all tickets need to be bought, the time complexity would be O(n^2), where n is the number of tickets. This is because for each ticket bought, we may need to loop through the entire list of tickets to check if the desired position has zero remaining tickets.
- Space complexity:
The space complexity of this solution is O(1), as we are not using any extra space that grows with the input size.

## Code
``` python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        time = 0
        while tickets[k] != 0 :
            for i in range(n):
                if tickets[i] :
                    tickets[i] -= 1
                    time += 1
                
                if tickets[k] == 0:
                    break
        
        return time
        
```