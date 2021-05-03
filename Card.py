from Exceptions import (InvalidRankError, InvalidSuitError, InvalidCardStringError, )


class Card:
    VALID_SUITS = ("S", "H", "D", "C")
    VALID_RANKS = ("2", "3", "4", "5", "6", "7", "8",
                   "9", "T", "J", "Q", "K", "A")

    RANK_WEIGHT_MAP = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    @staticmethod
    def from_string(_string):
        if len(_string) != 2:
            raise InvalidCardStringError
        return Card(rank=_string[0], suit=_string[1])

    def __init__(self, rank, suit):
        """Card Constructor"""
        if not rank.upper() in self.VALID_RANKS:
            raise InvalidRankError
        if not suit.upper() in self.VALID_SUITS:
            raise InvalidSuitError
        self.rank = rank.upper()
        self.suit = suit.upper()


    def get_rank_weight(self):
        """Translate the card rank to respective weight, f.e. K-->13"""
        return self.RANK_WEIGHT_MAP[self.rank]

    def __eq__(self, other_card):
        """Two cards with same rank are equal,
        regardless of their suits"""
        return self.rank == other_card.rank

    def __gt__(self, other_card):
        """A card with higher rank is greater"""
        return self.get_rank_weight() > other_card.get_rank_weight()

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __hash__(self):
        return hash(str(self))
