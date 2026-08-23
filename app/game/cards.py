from dataclasses import dataclass
from enum import Enum

class Value(str, Enum):
    '''
    Values used by the 16-card puzzle.
    '''

    ACE="A"
    JACK="J"
    QUEEN="Q"
    KING="K"

class Suit(str, Enum):
    '''
    Suits used by the 16-card puzzle.
    '''

    HEARTS="H"
    DIAMONDS="D"
    CLUBS="C"
    SPADES="S"

@dataclass(frozen=True)
class Card:
    '''
    Immutable representation of a puzzle card.
    '''
    id: str
    value: Value
    suit: Suit
    svg: str

    def to_dict(self) -> dict[str, str]:
        '''
        Return a JSON-compatible representation of the card.
        '''
        return {
            "id": self.id,
            "value": self.value.value,
            "suit": self.suit.value,
            "svg": self.svg
        }

def create_card(value: Value, suit: Suit) -> Card:
    '''
    Create a card using the project's standard ID and asset format.
    '''

    card_id = f"{value.value}-{suit.value}"
    svg = f"/assets/cards/{card_id.lower()}.svg"

    return Card(
        id=card_id,
        value=value,
        suit=suit,
        svg=svg
    )

def create_deck() -> tuple[Card, ...]:
    '''
    Create a complete set of 16 unique cards for the puzzle.
    '''

    return tuple(
        create_card(value, suit)
        for value in Value
        for suit in Suit
    )

CARDS = create_deck()

def get_card(card_id: str) -> Card:
    '''
    Return a card by its ID, or raise a ValueError if the ID is unknown.
    '''

    card_by_id = {card.id: card for card in CARDS}

    try:
        return card_by_id[card_id.upper()]
    except KeyError as exc:
        raise ValueError(f"Unknown card ID: {card_id}") from exc

def cards_to_dict(cards: tuple[Card, ...] = CARDS) -> list[dict[str,str]]:
    '''
    Serialise the cards for use by the front-end or API.
    '''
    return [card.to_dict() for card in cards]