# 948. Bag of Tokens

## Intuition
The problem asks us to find the maximum number of score while playing a bag of tokens. These tokens can be used to increase our power, therefore allowing us to play more tokens or decrease our power to increase our score. The optimal solution can be solved greedily with a two-pointer approach.

## Approach
We solve the problem using two pointers by traversing through the sorted tokens and selecting the appropriate actions. When our current power is higher than the lowest value token, we use it to increase our score, but when it's lower, we can spend score to get the highest value token. We will exit the loop if the two pointers meet or when there is no score available.

## Complexity
- Time complexity: O(n), the two pointers traverse the tokens list once.
- Space complexity: O(1), we use a constant amount of space for the variables.

## Code
```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score, maxscore = 0, 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                maxscore = max(maxscore, score)
                break

            maxscore = max(maxscore, score)

        return maxscore
```
