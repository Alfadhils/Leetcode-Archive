# 997. Find the Town Judge

## Intuition
To find the judge in the town, we can use the following intuition: The judge is the person who is trusted by everyone else in the town but does not trust anyone themselves. We can leverage this insight to solve the problem efficiently.

## Approach
1. We'll maintain an array `trust_counts` to keep track of the number of people who trust each person.
2. We'll also maintain a set `trusting` to keep track of people who trust someone.
3. We'll iterate through the list of trust relationships and update `trust_counts` and `trusting` accordingly.
4. Then, we'll iterate through each person in the town and check if:
   - They are trusted by everyone else (`trust_counts[i] == n - 1`), and
   - They do not trust anyone themselves (`i not in trusting`).
5. If such a person exists, we return their index, which represents the judge.
6. If no such person exists, we return -1, indicating there is no judge in the town.

## Complexity
- Time complexity: O(T + N), where T is the number of trust relationships and N is the number of people in the town.
- Space complexity: O(N), where N is the number of people in the town.

## Code
```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counts = [0] * (n + 1)
        trusting = set()

        # Update trust counts and set of trusting people
        for a, b in trust:
            trust_counts[b] += 1
            trusting.add(a)

        # Iterate through each person to find the judge
        for i in range(1, n + 1):
            if trust_counts[i] == n - 1 and i not in trusting:
                return i

        # If no judge found, return -1
        return -1
```