from deck import Deck
from card import Card
from player import Player
from utils import choose_name

class Game():
    def __init__(self, deck: Deck, amount_of_bounty: int):
        self.deck = deck
        self.amount_of_bounty = amount_of_bounty
    
    def init_game(self) -> tuple[Player, Player]:
        for _ in range(0, 10):
            self.deck.shuffle()
            
        player1_cards, player2_cards = self.deck.deal_cards()

        player_1 = Player(choose_name(), player1_cards)
        player_2 = Player(choose_name(), player2_cards)

        return (player_1, player_2)

    def log_game_state(self, player_1: Player, player_2: Player) -> None:
        print(f"{player_1.name}: {len(player_1)}")
        print(f"{player_2.name}: {len(player_2)}")
    
    def play_turn(self, player_1: Player, player_2: Player, bounty: list[Card] = []) -> None | Player:
        if len(bounty):
            print("\nW.A.R\n")
            war_bounty = bounty + player_1.draw_cards(self.amount_of_bounty) + player_2.draw_cards(self.amount_of_bounty)
        else:
            war_bounty = []

        p1_card = player_1.draw_card()
        p2_card = player_2.draw_card()

        if not p1_card:
            war_bounty.append(p2_card)
            player_2.take_cards(war_bounty)
            return player_2
        if not p2_card:
            war_bounty.append(p1_card)
            player_1.take_cards(war_bounty)
            return player_1
        
        war_bounty += [p1_card, p2_card]

        print(f"\n{player_1.name} -> {p1_card} V.S. {p2_card} <- {player_2.name}")

        if p1_card.value > p2_card.value:
            print(f"{player_1.name} wins")
            player_1.take_cards(war_bounty)
        elif p1_card.value < p2_card.value:
            print(f"{player_2.name} wins")
            player_2.take_cards(war_bounty)
        else:
            self.log_game_state(player_1, player_2)
            winner = self.play_turn(player_1, player_2, war_bounty)
            if winner:
                return winner
        
        self.log_game_state(player_1, player_2)