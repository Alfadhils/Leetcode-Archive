class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        start, end = '', ''

        for x in word:
            end += x
            if x == ch and not start:
                start = end
                end = ''

        return start[::-1]+end
        