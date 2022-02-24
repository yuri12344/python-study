# 1 DATA MODELING
import collections
from random import choice

# Especial methods, is better dont set special methods in class, because builtin python methods are more fast
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('QJKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    # I can print len of the cards
    def __len__(self):
        return len(self._cards)

    # Get item turns class iterable
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
len(deck) # 52

choice(deck) # Get random card - Its is only possible because we have __getitem__ in class

for card in deck: # Because i have __getitem__ in my class, my deck are iterable
    # print(card)
    ...
"""
Card(rank='2', suit='spades')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='clubs')
Card(rank='2', suit='hearts')...
"""

for card in reversed(deck): 
    # print(card)
    ...
"""
Card(rank='A', suit='hearts')
Card(rank='A', suit='clubs')
Card(rank='A', suit='diamonds')
Card(rank='A', suit='spades') ...
"""

# The iteration is implicity, if i dont have method contains, the operator will do a sequencial sweep
# in our case, will work, because deck is iterable
Card('Q', 'hearts') in deck  # True
Card('20', 'beasts') in deck  # False

# Rank and ordenation
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card) -> int:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Ordenate the cards, will show the higher to lower, starting by rank 2 and suits clubs
for card in sorted(deck, key=spades_high):
    # print(card)
    ...

"""
Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
Card(rank='2', suit='spades')...
"""



# 2 EMULATING NUMERIC TYPES
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
    
    # Returns a new Vector, not the same object, first value not change
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # I can define when my class is True or Not
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



# 3 DATA STRUCTURING
""""
- Sequence container
list, tuple and collections.deque 
can store different types of objects

- Simple sequence
str, bytes, bytearray, memoryview and array.array can store only one type

The sequence container store the reference of the objects who have, can be any type
while simple sequence store fisicaly the value of each item in their own space of memory
and not like distinct object.

This way, the simple sequence are more compact, although they are limited to the storage of the
primitive values, like character, bytes and numbers. 

Sample of creating a list and with list compreheension, who can be more fast, and more legible
"""

# ord builting function show's the number of the simbol in Unicode table https://bit.ly/3t5ww7k
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
# [36, 162, 163, 165, 8364, 164] Tip: the break lines in python are ignored betwen the pairs [], {} and (), you dont need to use \

""""
In python 2.x, variable in listcomps can leak

x = 'my precious'
dummy = [x for x in 'ABC']
print(x) 
'C'

Now in python 3.x, the variable x is not leaked
"""

# Comparing list comprehension and with map and filter
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

# timeit.repeat arg setup can receive string and will try compile it
def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

"""
clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')

listcomp        : 0.010 0.010 0.011 0.010 0.011
listcomp + func : 0.017 0.016 0.017 0.017 0.017
filter + lambda : 0.015 0.015 0.014 0.015 0.014
filter + func   : 0.024 0.014 0.014 0.014 0.013
"""

# Cartesian product, the product of all possible combinations of the elements of two sequences
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors # Colors first
                         for size in sizes ] # Sizes second
# List of tshirts ordenated by color, then by size
# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

# Usage of genexp
import array
symbols = '#!@#!@%*'
res = tuple(ord(symbols) for symbols in symbols)
# print(res) 
# (35, 33, 64, 35, 33, 64, 37, 42)

res = array.array('I', (ord(symbols) for symbols in symbols))
# print(res) 
# array('I', [35, 33, 64, 35, 33, 64, 37, 42])

# Print all possible of Tshirts
# [print(color, size) for color in colors for size in sizes] 
"""
black S
black M
black L
white S
white M
white L
"""

travelers_id = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# The %s/%s understand the tuple, and will print the first and second elemente
# [print('%s/%s' % passp) for passp in sorted(travelers_id)] 
"""
BRA/CE342567
ESP/XDA205856
USA/31195855
"""

# Unpacking, the _ variable is most used to ignore the value
# [print(country) for country, _ in sorted(travelers_id)] 
"""
BRA
ESP
USA
"""











