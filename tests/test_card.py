import unittest
from card import Card

class TestCard(unittest.TestCase):

    def test_card_initialization(self):
        card = Card("Ace", 1, "Spades")
        self.assertEqual(card.name, "Ace")
        self.assertEqual(card.value, 1)
        self.assertEqual(card.family, "Spades")

    def test_card_title(self):
        card = Card("King", 13, "Hearts")
        self.assertEqual(card.title, "King of Hearts")

    def test_card_string_representation(self):
        card = Card("Queen", 12, "Diamonds")
        self.assertEqual(str(card), "Queen of Diamonds")

if __name__ == '__main__':
    unittest.main()
