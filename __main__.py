from deck import Deck
from player import Player
from card import Card
from utils import choose_name
from time import sleep


def init_game() -> tuple[Player, Player]:
    my_deck = Deck()
    for _ in range(0, 10):
        my_deck.shuffle()
        
    player1_cards, player2_cards = my_deck.deal_cards()

    player_1 = Player(choose_name(), player1_cards)
    player_2 = Player(choose_name(), player2_cards)

    return (player_1, player_2)

def play_turn(player_1: Player, player_2: Player):
    p1_card = player_1.draw_card()
    p2_card = player_2.draw_card()

    if not p1_card:
        return player_2
    if not p2_card:
        return player_1

    print(f"\n{player_1.name} -> {p1_card} V.S. {p2_card} <- {player_2.name}")

    if p1_card.value > p2_card.value:
        print(f"{player_1.name} wins")
        player1.take_cards([p1_card, p2_card])
    elif p1_card.value < p2_card.value:
        print(f"{player_2.name} wins")
        player2.take_cards([p1_card, p2_card])
    else:
        play_war_turn(player_1, player_2, [])
    
    print(f"{player_1.name}: {len(player_1)}")
    print(f"{player_2.name}: {len(player_2)}")

def play_war_turn(player_1: Player, player_2: Player, bounty: list[Card]) -> None | Player:
    print("\nW.A.R\n")

    war_bounty = bounty + player_1.draw_cards(3) + player_2.draw_cards(3)
    p1_card = player_1.draw_card()
    p2_card = player_2.draw_card()

    if not p1_card:
        return player_2
    if not p2_card:
        return player_1

    print(f"\n{player_1.name} -> {p1_card} V.S. {p2_card} <- {player_2.name}")

    if p1_card.value > p2_card.value:
        print(f"{player_1.name} wins")
        player1.take_cards(war_bounty + [p1_card, p2_card])
    elif p1_card.value < p2_card.value:
        print(f"{player_2.name} wins")
        player1.take_cards(war_bounty + [p1_card, p2_card])
    else:
        play_war_turn(player_1, player_2, war_bounty)


player1, player2 = init_game()
while True:
    winner = play_turn(player1, player2)
    if winner:
        print("*" * 20)
        print(f"{winner.name} is the WINNER!")
        print("*" * 20)
        break
    sleep(0.5)