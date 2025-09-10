"""
Iterator protocol:
__iter__(): Returns an iterator, in this case, a reference to itself
__next__(): Returns the next value in the collection or data stream
Both must be defined for a class to be considered an iterator!
"""
import random

class CoinFlip:
    def __init__(self, number_of_flips):
        self.number_of_flips = number_of_flips
        self.counter = 0

    def __iter__(self):
        return self     # Returns a reference of the iterator

    # Flips the next coin, return the output
    def __next__(self):
        if self.counter < self.number_of_flips:
            self.counter += 1
            return random.choice(['H', 'T'])
        else:
            raise StopIteration     # Otherwise, stop execution with StopIteration

three_flips = CoinFlip(3)
# Flip the coin three times
print(next(three_flips))
print(next(three_flips))
print(next(three_flips))
print('------------------')

four_flips = CoinFlip(4)
for flip in four_flips:     # If we don't define StopIteration in __next__, It'll be an infinite loop
    print(flip)
print('------------------')

five_flips = CoinFlip(5)
while True:
    try:
        print(next(five_flips)) # Pulls the next element of the iterator
    except StopIteration:
        print('Completed all coin flips')
        break