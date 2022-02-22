import collections
from random import choice

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
print(len(deck)) # 52


random_card = choice(deck) # Get random card - Its is only possible because we have __getitem__ in class


for card in deck: # Because i have __getitem__ in my class, my deck are iterable
    # print(card)
    ...

for card in reversed(deck): # or reversed
    # print(card)
    ...


# The iteration is implicity, if i dont have method contains, the operator will do a sequencial sweep
# in our case, will work, because deck is iterable
print(Card('Q', 'hearts') in deck)  # True
print(Card('20', 'beasts') in deck)  # False


# And ordenation, by the suits, and ranks
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card) -> int:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
    # Will show the higher to lower, starting by rank 2 and suits clubs








