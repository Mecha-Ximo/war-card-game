from card import Card
from random import shuffle

class Deck():
    families = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self):
        self.cards = self.create_cards()
    
    def __str__(self):
        stringified_deck = ""
        for card in self.cards:
            stringified_deck += f"{card}\n"

        return stringified_deck

    def shuffle(self):
        shuffle(self.cards)

    def create_cards(self):
        cards = []

        for family in Deck.families:
            family_cards = self.create_cards_family(family)
            for card in family_cards:
                cards.append(card)
        
        return cards

    
    def create_cards_family(self, family):
        cards = []

        cards.append(Card("Ace", 1, family))

        for value in range(2, 11):
            cards.append(Card(str(value), value, family))

        cards.append(Card("J", 11, family))
        cards.append(Card("Q", 12, family))
        cards.append(Card("K", 13, family))

        return cards
