from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens)-1
        score, maxscore = 0, 0
        while left <= right :
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else :
                maxscore = max(maxscore,score)
                break

            maxscore = max(maxscore,score)

        return maxscore
        