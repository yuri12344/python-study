import collections
from random import choice

# Especial methods, is better dont set special methods in class, because builtin python methods are more fast

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('QJKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
len(deck) # 52


choice(deck) # Get random card - Its is only possible because we have __getitem__ in class


for card in deck: # Because i have __getitem__ in my class, my deck are iterable
    # print(card)
    ...

for card in reversed(deck): # or reversed
    # print(card)
    ...


# The iteration is implicity, if i dont have method contains, the operator will do a sequencial sweep
# in our case, will work, because deck is iterable
Card('Q', 'hearts') in deck  # True
Card('20', 'beasts') in deck  # False


# And ordenation, by the suits, and ranks
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card) -> int:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    # print(card)
    # Will show the higher to lower, starting by rank 2 and suits clubs
    ...


# EMULATING NUMERIC TYPES

from math import hypot
import ipdb

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Shows Vector(int, int), instead will show <Vector object at 0x10e10070>
    # Not ambiguous, for understeand the obj creation. Take care with infinit looping with reference yourself
    # Reference: https://bit.ly/36zWl87 Stack Overflow
    def __repr__(self) -> str:
        return f'Vector{self.x, self.y}' 
        # return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)

  
    
    # add and mul returns new object
    # we can operate numbers, but not Vectors for numbers
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Any obj in python is accept in bool context, Python applyes bool(x) which aways returns True or False
    # by default, Python will call x.__len__() if __bool__ is not implemented
    def __bool__(self):
        # return False - Aways will return False
        # return True - Aways will return True
        return bool(abs(self))



v1 = Vector(2, 4)
v2 = Vector(2, 1)
res = v1 + v2 # 4, 5

v = Vector(3, 4)
abs(v) # 5

ipdb.set_trace()