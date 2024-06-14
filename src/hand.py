from src.deck import Deck


class Hand(Deck):

    def init__(self, label=''):
        self.cards = []
        self.label = label
