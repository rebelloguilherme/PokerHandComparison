from Hand import Hand


"""    VALID_SUITS = ("S", "H", "D", "C")
       VALID_RANKS = ("2", "3", "4", "5", "6", "7", "8",
                      "9", "T", "J", "Q", "K", "A")
"""


def compare_hand_strings(string1, string2):
    return Hand.from_string(string1).compare_with(Hand.from_string(string2))

#Testing..
print("the hand winner is ", compare_hand_strings("QD KH 3H 2C TS", "2D 3D 4D 5D 7D"))
