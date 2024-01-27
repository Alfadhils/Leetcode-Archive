# 455. Assign Cookies

## Intuition

The goal is to maximize the number of content children by assigning the minimum size of cookies to each child. Sorting the arrays of children's greed factors (`g`) and cookie sizes (`s`) allows us to easily match children with cookies of appropriate sizes.

## Approach

1. Sort the arrays `g` and `s` in ascending order.
2. Initialize two pointers `i` and `c` to iterate through the arrays `s` and `g` respectively.
3. Iterate through the arrays while there are available cookies and unsatisfied children.
4. If the current cookie size `s[i]` is greater than or equal to the current child's greed factor `g[c]`, assign the cookie to the child and move to the next child (`c += 1`).
5. Move to the next available cookie (`i += 1`) regardless of whether it was assigned to a child or not.
6. Continue until either all children are satisfied or there are no more cookies.

## Complexity

- Time complexity: O(n log n) due to the sorting of arrays `g` and `s`.
- Space complexity: O(1) as we are using constant extra space.

## Code

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        c = 0
        while i < len(s) and c < len(g):
            if s[i] >= g[c]:
                c += 1
            i += 1

        return c
```
