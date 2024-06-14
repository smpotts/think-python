import unittest
from src.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_init(self):
        d = Deck()
        print(d)


if __name__ == '__main__':
    unittest.main()
