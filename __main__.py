from deck import Deck
from game import Game
from time import sleep
from utils import log_winner


game = Game(Deck(), 5)
player1, player2 = game.init_game()

while True:
    winner = game.play_turn(player1, player2)
    if winner:
        game.log_game_state(player1, player2)
        log_winner(winner)
        break