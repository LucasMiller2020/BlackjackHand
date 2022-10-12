# Lucas Miller
# 10-10-2022
# Software Design
# -----------------------

from CardDeck import CardDeck
from graphics import *
#

class BlackjackHand:
    _handFiles: list

    def __init__(self, name: str = "", stayValue: int = 21):
        """
        This initializes the HandUI with the data needed for self. It may be used to initialize the BlackjackHand as
        well.
        :param name: Used for the hand
        :param stayValue: States the highest value for the hand
        """

        super().__init__(name, stayValue)
        pass
    # hello

    def CardHandData(self) -> GraphWin:
        """
        returns the string from the Card hand that's in the BlackjackHand.py that has the card name and number
        :return:
        """
        pass

    def drawCardHand(self) -> list:
        """
        iterates over the self._handFiles and creates a GraphWin object for each card hand
        :return: None
        """
        pass

    def addCard(self, deck: CardDeck):
        """
        Gets the filename from CardDeck. The name is added to the self._handFiles and the score is updated

        :param deck: a deck of Card objects
        :return: None
        """
        pass

    def test(self):
        pass

    # there we go






