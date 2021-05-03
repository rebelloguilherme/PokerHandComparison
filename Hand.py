from Card import Card
from Exceptions import (NonUniqueCardInHandError, InvalidTieBreakError, )


class Hand:
    # types of hands
    ROYAL_FLUSH = 100
    STRAIGHT_FLUSH = 90
    FLUSH = 80
    STRAIGHT = 70
    FOUR_OF_A_KIND = 60
    FULL_HOUSE = 50
    THREE_OF_A_KIND = 40
    TWO_PAIR = 30
    PAIR = 20
    LOW = 10

    # Results of comparing hands
    WIN = 1
    LOSS = 2
    TIE = 3

    @staticmethod
    def from_string(_string):
        return Hand(*[Card.from_string(substring)
                      for substring in _string.split()])

    def __init__(self, card1, card2, card3, card4, card5):
        """Construct a hand with 5 cards"""
        self.cards = {card1, card2, card3, card4, card5}
        if len(self.cards) < 5:
            raise NonUniqueCardInHandError
        self._cache_expensive_helpers()

    def __iter__(self):
        return (c for c in self.cards)

    def __eq__(self, other_hand):
        self_hashes = {hash(c) for c in self}
        other_hashes = {hash(c) for c in other_hand}
        for h in self_hashes:
            if not h in other_hashes:
                return False
        return True

    def _cache_expensive_helpers(self):
        """Extracts important information based on the cards in this hand and
        caches the information for future use"""

        self._sorted_ranks_string = "".join(
            sorted((card.rank for card in self), key=(lambda r: Card.RANK_WEIGHT_MAP[r]), reverse=True))

        self._rank_histogram = {}
        for rank in self._sorted_ranks_string:
            self._rank_histogram[rank] = self._rank_histogram.get(rank, 0) + 1

        self._sorted_ranks_count_tuple = list(
            sorted(self._rank_histogram.items(), key=lambda t: (-t[1], -Card.RANK_WEIGHT_MAP[t[0]])))
        # self._sorted_rank_count_tuple = list(
        #     reversed(sorted(self._rank_histogram.items(), key=lambda t: (t[1], Card.RANK_WEIGHT_MAP[t[0]]))))
    def is_royal_flush(self):
        """identify the royal flush sequence"""
        return self._sorted_ranks_string == "AKQJT" and self.is_flush

    def is_straight_flush(self):
        """identify the straight flush sequence"""
        return self.is_flush() and self.is_straight()

    def is_flush(self):
        """identify flush sequence"""
        return len({card.suit for card in self}) == 1

    def is_straight(self):
        _string = self._sorted_ranks_string
        # if we have a Ace and 2
        # so Straight cant have a King
        # in this case we allow Ace precede 2
        # so we dont miss a Straight with 2
        if _string[0] == "A" and _string[-1] == "2":
            _string = f"{_string[1:]}A"
            # f.e. "A5432" becomes "5432A"
        return _string in "AKQJT98765432A"

    def is_four_of_a_kind(self):
        """Return if a hands contain 4 cards with same Rank"""
        return (4 in self._rank_histogram.values())

    def is_full_house(self):
        """Return if a hand is a fullhouse"""
        return self.is_three_of_a_kind() and self.is_pair()

    def is_three_of_a_kind(self):
        """Return if a hand contain 3 cards with same Rank(trinca)"""
        return (3 in self._rank_histogram.values())

    def is_two_pair(self):
        """Return if a hand contain 2 cards with same Rank"""
        return list(self._rank_histogram.values()).count(2) == 2

    def is_pair(self):
        """Return if a hand contain a pair"""
        return (2 in self._rank_histogram.values())

    def grade(self):
        """Grade a Hand

            100 represent Royal Flush
            90  represent Straight Flush
            80  represent Flush
            and so on.."""
        if self.is_royal_flush():
            return self.ROYAL_FLUSH
        if self.is_straight_flush():
            return self.STRAIGHT_FLUSH
        if self.is_flush():
            return self.FLUSH
        if self.is_four_of_a_kind():
            return self.FOUR_OF_A_KIND
        if self.is_full_house():
            return self.FULL_HOUSE
        if self.is_three_of_a_kind():
            return self.THREE_OF_A_KIND
        if self.is_two_pair():
            return self.TWO_PAIR
        if self.is_pair():
            return self.PAIR
        return self.LOW

    def compare_with(self, other_hand):
        """returns a constant which represent a winner hand, where:
        1 represent a Winner;
        2 represent a Loser;
        3 let a tie function;"""
        if self.grade() > other_hand.grade():
            return self.WIN
        if self.grade() < other_hand.grade():
            return self.LOSS
        return self.break_tie_with(other_hand)

    def break_tie_with(self, other_hand):
        """returns a constant which indicates a tieBreaker, where:
        1 represent a Winner;
        2 represent a Loser;
        3 Tie;
        """
        if not self.grade() == other_hand.grade():
            raise InvalidTieBreakError

        for ((self_rank, self_freq), (other_rank, other_freq)) in zip(self._sorted_ranks_count_tuple, other_hand._sorted_rank_count_tuple):

            self_weight = Card.RANK_WEIGHT_MAP[self_rank]
            other_weight = Card.RANK_WEIGHT_MAP[other_rank]

            if self_weight > other_weight:
                return self.WIN
            if self_weight < other_weight:
                return self.LOSS
            continue
        return self.TIE
