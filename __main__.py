from deck import Deck
from game import Game
from time import sleep


game = Game(Deck(), 5)
player1, player2 = game.init_game()

while True:
    winner = game.play_turn(player1, player2)
    if winner:
        print("*" * 20)
        print(f"{winner.name} is the WINNER!")
        print("*" * 20)
        break
    sleep(0.25)