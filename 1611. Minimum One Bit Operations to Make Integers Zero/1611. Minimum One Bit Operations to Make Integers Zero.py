class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        binary = bin(n)[2:]
        length = len(binary)
        res = 0
        state = 0

        for i, bit in enumerate(binary):
            if bit == '1':
                state ^= 1

            res += (1 << (length - 1 - i)) * state

        return res
