class InvalidRankError(AssertionError):
    """Exception raised when you try to instantiate
    a card with invalid rank"""
    pass


class InvalidSuitError(AssertionError):
    """Exception raised when you try to instantiate
        a card with invalid suit"""
    pass


class NonUniqueCardInHandError(AssertionError):
    """Exception raised when you try to instantiate
        a hand with a invalid card"""
    pass


class InvalidCardStringError(AssertionError):
    """Exception raised when you try instantiate
    a card from a string that could never be resolved
    to a valid card"""
    pass


class InvalidTieBreakError(AssertionError):
    """Exception to be raised when one tries
    a tie for unequally graded hands of cards."""
    pass
