"""Problem 1 of TecnoMate 2014 Paradigm level

To test this program the input and expected output are provided in the `input.txt` and `output.txt` files
"""

class deck(object):
    """A collection of cards which can check whether they are shuffled or
    not."""
    
    def __init__(self):
        """Initialize the deck with the given cards."""
        self.cards = []
        self.shuffled = True
        card_number = int(input())
        self.load_deck(card_number)
    
    def load_deck(self,cards_number):
        """Add as many cards to the deck as the number given"""
        for i in range(cards_number):
            self.add_card()
    
    def add_card(self):
        """ Add a new card to the deck"""
        new_card = card()
        self.cards.append(new_card)
        self.shuffled &= self.is_shuffled()
    
    def is_shuffled(self):
        """Return True if the last two cards correctly shuffled, False otherwise."""
        
        if len(self.cards) < 2:
            return True
        
        return self.cards[-2] != self.cards[-1]
        
        
    
class card(object):
    """A pair of Value-Type where Value can be from 0 to 12 and type can be "p", "c", "o" or "e". """
    
    def __init__(self):
        """Initialize the card with the value and type given."""
        card_raw = input()
        self.value, self.typecard  = card_raw.split()
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            samevalue = self.value == other.value
            sametypecard = self.typecard == other.typecard
            return samevalue or sametypecard
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


def main():
    """Print B if a given deck is correctly shuffled, M otherwise."""
    testsnumber = int(input())
    for i in range(testsnumber):
        new_deck = deck()
        if new_deck.shuffled:
            print("B")
        else:
            print("M")

main()

