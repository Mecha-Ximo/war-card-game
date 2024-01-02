import unittest
from deck import Deck
from card import Card

class TestDeck(unittest.TestCase):
    def test_deck_suites(self):
        expected_suites = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.assertEqual(Deck.suites, expected_suites)

    def test_class_instantiation(self):
        deck = Deck()
        self.assertTrue(type(deck.cards) == list)
        self.assertEqual(len(deck.cards), 52)
        for card in deck.cards:
            self.assertTrue(type(card) == Card)