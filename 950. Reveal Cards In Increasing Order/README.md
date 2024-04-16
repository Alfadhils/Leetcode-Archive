# 950. Reveal Cards In Increasing Order

## Intuition
To reveal the cards in increasing order, we can simulate the process described in the problem statement. Since we need to reveal the cards in increasing order, we can sort the deck initially. Then, we can follow the steps outlined in the problem to reveal the cards one by one.

## Approach
1. Sort the deck in ascending order.
2. Initialize a deque to simulate the deck.
3. Start from the largest card in the sorted deck and construct the revealed deck:
   - Pop the top card from the deque and append it to the revealed deck.
   - If there are still cards in the deque, move the top card to the bottom of the deck.
4. Repeat step 3 until all cards are revealed.

## Complexity
- Time complexity:
  - Sorting the deck takes O(n logn) time.
  - Constructing the revealed deck takes O(n) time.
  - Overall time complexity is O(nlogn).
- Space complexity:
  - We use additional space for the deque and the revealed deck.
  - The space complexity is O(n).

## Code
```python
class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        deck.sort()
        st = deque()
        st.append(deck[n - 1])
        for i in range(n - 2, -1, -1):
            st.appendleft(st.pop())
            st.appendleft(deck[i])
        revealed = []
        while st:
            revealed.append(st.popleft())
        return revealed
```