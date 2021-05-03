from Hand import Hand
from Player import Player
from Deck import Deck

"""    VALID_SUITS = ("S", "H", "D", "C")
       VALID_RANKS = ("2", "3", "4", "5", "6", "7", "8",
                      "9", "T", "J", "Q", "K", "A")
"""


def compare_hand_strings(string1, string2):
    return Hand.from_string(string1).compare_with(Hand.from_string(string2))


new_deck = Deck

new_deck.show()

jogador1 = Player("Guilherme")
jogador2 = Player("Carlos")

print("the winner is hand ", compare_hand_strings("QD KH 3H 2C TS", "2D 3D 4D 5D 7D"))
