from dataclasses import dataclass
from typing import Optional

from .cards import Card

LINE_SIZE = 4

@dataclass(frozen=True)
class LineValidationResult:
    '''
    Represents the result of validating a line (row or column) on the board.
    '''

    valid: bool
    complete: bool
    values_valid: bool
    suits_valid: bool

def is_valid_value_line(cards: list[Optional[Card]]) -> bool:
    '''
    Checks if the given line of cards has unique values (ignoring None).
    '''

    values = [
        card.value
        for card in cards 
        if card is not None
    ]
    return len(values) == len(set(values))

def is_valid_suit_line(cards: list[Optional[Card]]) -> bool:
    '''
    Checks if the given line of cards has unique suits (ignoring None).
    '''

    suits = [
        card.suit
        for card in cards 
        if card is not None
    ]
    return len(suits) == len(set(suits))

def is_complete_line(cards: list[Optional[Card]]) -> bool:
    '''
    Checks if the given line of cards is complete (no None values).
    '''

    return all(card is not None for card in cards)

def validate_line(
        cards: list[Optional[Card]],
        *,
        check_values: bool = True,
        check_suits: bool = True
) -> LineValidationResult:
    '''
    Validates a line of cards based on the specified constraints.
    '''

    if len(cards) != LINE_SIZE:
        raise ValueError(f"A puzzle line must contain exactly {LINE_SIZE} cards.")
    
    complete = is_complete_line(cards)
    
    values_valid = (
        is_valid_value_line(cards) 
        if check_values
        else True
    )
    suits_valid = (
        is_valid_suit_line(cards) 
        if check_suits
        else True
    )

    return LineValidationResult(
        valid=values_valid and suits_valid,
        complete=complete,
        values_valid=values_valid,
        suits_valid=suits_valid
    )