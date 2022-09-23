# Lucas Miller
# Due:  09-18-2022 (Sunday)
# Software Design
# -----------------------

"""
Instructions:

Implement the methods defined in the BlackjackHand class defined below in a file named BlackjackHand.py and also
write unit test code to fully test the BlackjackHand class in a file named test_BlackjackHand.py. You may change the
instance variables if you prefer a different way of implementing the methods, but the API for each method (name,
parameters and their types, and the return value) must match the API in the provided declaration. • submit your
BlackjackHand.py and test_BlackjackHand.py files on iLearn before the due date

"""


from __future__ import annotations

from Card import Card


class BlackjackHand:
    # name for the hand
    _name: str

    # value at which the hand stops getting cards
    _stayValue: int

    # total value of the hand
    _total: int

    # True if the hand has an ace counted as 11
    _hasAce11: bool

    # ------------------------------------------------------------------

    def __init__(self, name: str = "", stayValue: int = 21):
        """
        :param name: a name for the hand
        :param stayValue: values below stayValue have canGetCard return True
        """
        pass

    def reset(self) -> None:
        """
        resets state to an empty hand
        :return: None
        """
        pass

    def canGetCard(self) -> bool:
        """
        :return: True if total < the stay value, False otherwise
        """
        pass

    def addCard(self, card: Card) -> None:
        """
        adds card to the hand
        :param card: Card to add
        :return: None
        """
        pass

    def score(self) -> int:
        """
        :return: total value of the hand
        """
        pass

    def busted(self) -> bool:
        """
        :return: True if hand total > 21, False otherwise
        """
        pass

    def __str__(self) -> str:
        """
        if the player has a name (_name is not the empty string), the return string contains
        the player's name followed by a colon followed by a space and then the score
        if the player has busted, the string "busted" is used instead of the numeric score
        examples:
        if _name is empty and _total is 12, it just returns "12"
        if _name is empty and the player has busted, it just returns "busted"
        if _name is "Player 1" and _total is 12, it returns "Player 1: 12"
        if _name is "Player 1" and the player has busted, it returns "Player 1: busted"
        :return: string as described above
        """
        pass

    # ------------------------------------------------------------------

    def __lt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if other beats self, otherwise False
        """
        pass

    def __eq__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if both hands the same (a tie), False otherwise
        """
        pass

    def __ne__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if one hand beats the other, False otherwise
        """
        pass

    def __le__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if other beats self or a tie, False otherwise
        """
        pass

    def __gt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other, False otherwise
        """
        pass

    def __ge__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other or a tie, False otherwise
        """
        pass

# ----------------------------------------------------------------------
