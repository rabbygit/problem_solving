"""
Design a phone directory that initially has maxNumbers empty slots that can store numbers.
The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

Implement the PhoneDirectory class:

1. PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
2. int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
3. bool check(int number) Returns true if the slot number is available and false otherwise.
4. void release(int number) Recycles or releases the slot number.

"""


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.stack = [i for i in range(maxNumbers)]
        self.notAvailable = {}

    def get(self) -> int:
        if self.stack:
            n = self.stack.pop()
            self.notAvailable[n] = True
            return n

        return -1

    def check(self, number: int) -> bool:
        if number in self.notAvailable:
            return False

        return True

    def release(self, number: int) -> None:
        if number in self.notAvailable:
            self.stack.append(number)
            del self.notAvailable[number]
