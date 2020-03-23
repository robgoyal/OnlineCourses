class Card:
    allowed_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    allowed_value = ["A", "2", "3", "4", "5", "6", "7", "8",
                     "9", "10", "J", "Q", "K"]

    def __init__(self, value, suit):
        if value not in Card.allowed_value or suit not in Card.allowed_suit:
            raise ValueError("Incorrect value or suit for Card")

        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"
