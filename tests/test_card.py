import unittest
from src.card import Card


class TestCard(unittest.TestCase):
    def test_init_card(self):
        init_card = Card()
        self.assertEqual(init_card.suit, 0)
        self.assertEqual(init_card.rank, 2)

    def test_str(self):
        card1 = Card(2, 11)
        print(card1)


if __name__ == '__main__':
    unittest.main()
