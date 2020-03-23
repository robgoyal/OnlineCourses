from itertools import product
from random import shuffle

from card import Card


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value, suit in
                      product(Card.allowed_value, Card.allowed_suit)]

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        deck_size = self.count()

        if not deck_size:
            raise ValueError("All cards have been dealt")

        num = deck_size if num > deck_size else num
        return [self.cards.pop() for _ in range(num)]

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)

    def __repr__(self):
        return f"Deck of {self.count()} cards"
