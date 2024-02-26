# 232. Implement Queue using Stacks

## Intuition
The intuition behind this approach is to simulate the behavior of a queue using a single stack. By carefully managing the elements within the stack, we can achieve the required FIFO (first in, first out) behavior.

## Approach
To implement a queue using a single stack, we can use the following approach:
1. For the `push` operation, we simply append the new element to the end of the stack.
2. For the `pop` operation, we need to simulate removing the first element of the queue. To do this, we recursively pop all elements from the stack until we reach the bottom. We then return the last element popped, which effectively removes the first element of the queue. Afterward, we push back all the elements popped except the last one.
3. The `peek` operation returns the top element of the stack, which represents the front of the queue.
4. The `empty` operation checks if the stack is empty.

## Complexity
- Time complexity:
  - `push`: O(1)
  - `pop`: O(n)
  - `peek`: O(1)
  - `empty`: O(1)
- Space complexity:
  - O(n) due to the space used by the stack.

## Code 
``` python 
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
```
