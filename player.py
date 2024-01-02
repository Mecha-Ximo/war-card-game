from card import Card

class Player():
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.cards = cards
    
    def __str__(self):
        stringified_player = self.name
        for card in self.cards:
            stringified_player += f"\n{card.title}"
        
        return stringified_player

    def __len__(self) -> int:
        return len(self.cards)
    
    def draw_card(self) -> Card | None:
        if len(self) > 0:
            return self.cards.pop()
    
    def draw_cards(self, amount: int) -> list[Card]:
        if len(self) < amount:
            return self.cards
        
        cards = []
        for _ in range(0, amount):
            cards.append(self.cards.pop())
        
        return cards
    
    def take_cards(self, new_cards: list[Card]) -> None:
        for card in new_cards:
            self.cards.insert(0, card)
    