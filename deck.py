from card import Card
from random import shuffle

class Deck():
    suites = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self):
        self.cards = self.create_cards()
    
    def __str__(self) -> str:
        stringified_deck = ""
        for card in self.cards:
            stringified_deck += f"{card}\n"

        return stringified_deck
    
    def __len__(self) -> int:
        return len(self.cards)
    
    def deal_cards(self) -> tuple[list[Card], list[Card]]:
        first_set: list[Card] = [card for index, card in enumerate(self.cards) if index % 2 == 0]
        second_set: list[Card] = [card for index, card in enumerate(self.cards) if index % 2 != 0]
        self.cards = []

        return (first_set, second_set)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def create_cards(self) -> list[Card]:
        cards = []

        for family in Deck.suites:
            family_cards = self.create_cards_suites(family)
            for card in family_cards:
                cards.append(card)
        
        return cards

    
    def create_cards_suites(self, suit: str) -> list[Card]:
        cards = []

        cards.append(Card("Ace", 1, suit))

        for value in range(2, 11):
            cards.append(Card(str(value), value, suit))

        cards.append(Card("J", 11, suit))
        cards.append(Card("Q", 12, suit))
        cards.append(Card("K", 13, suit))

        return cards
