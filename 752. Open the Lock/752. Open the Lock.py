from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0

        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        visited = set()
        queue = {'0000'}

        steps = 0

        while queue:
            next_queue = set()
            steps += 1

            for node in queue:
                for i in range(4):
                    for diff in [-1, 1]:
                        new_digit = (int(node[i]) + diff) % 10
                        new_node = node[:i] + str(new_digit) + node[i+1:]

                        if new_node in deadends or new_node in visited:
                            continue

                        if new_node == target:
                            return steps

                        visited.add(new_node)
                        next_queue.add(new_node)

            queue = next_queue

        return -1