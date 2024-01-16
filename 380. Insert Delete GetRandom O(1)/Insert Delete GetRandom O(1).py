import random

class RandomizedSet:
    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        else:
            self.set.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.set))