from dataclasses import dataclass
from typing import Optional

from .cards import Card, get_card

BOARD_SIZE = 4

@dataclass(frozen=True)
class Position:
    '''
    Immutable representation of a position on the puzzle board.
    '''
    row: int
    column: int

class Board:
    '''
    Representation of the current state of the puzzle board.
    '''

    def __init__(self, cards: Optional[list[list[Optional[Card]]]] = None):
        if cards is None:
            self._cards = [
                [None for _ in range(BOARD_SIZE)]
                for _ in range(BOARD_SIZE)
            ]
        else:
            self._cards = self._copy_cards(cards)
            self._validate_dimensions()

    def get(self,position: Position) -> Optional[Card]:
        '''
        Returns the card at the given position, or None if the position is empty.
        '''

        self._validate_position(position)
        return self._cards[position.row][position.column]

    def place(self, position: Position, card: Optional[Card]) -> None:
        '''
        Places the given card at a given position. If card is None, the position is cleared.
        '''

        self._validate_position(position)
        self._cards[position.row][position.column] = card

    def swap(self, first: Position, second: Position) -> None:
        '''
        Swaps the cards at the two given positions.
        '''

        self._validate_position(first)
        self._validate_position(second)

        self._cards[first.row][first.column], self._cards[second.row][second.column] = (
            self._cards[second.row][second.column],
            self._cards[first.row][first.column],
        )

    def row(self, index: int) -> list[Optional[Card]]:
        '''
        Returns the cards in a given row.
        '''

        self._validate_index(index)
        return self._cards[index].copy()

    def column(self, index: int) -> list[Optional[Card]]:
        '''
        Returns the cards in a given column.
        '''

        self._validate_index(index)
        return [
            self._cards[row][index] 
            for row in range(BOARD_SIZE)
        ]

    def main_diagonal(self) -> list[Optional[Card]]:
        '''
        Returns the cards in the main diagonal (top-left to bottom-right).
        '''

        return [
            self._cards[index][index]
            for index in range(BOARD_SIZE)
        ]

    def anti_diagonal(self) -> list[Optional[Card]]:
        '''
        Returns the cards in the anti-diagonal (top-right to bottom-left).
        '''

        return [
            self._cards[index][BOARD_SIZE - 1 - index]
            for index in range(BOARD_SIZE)
        ]

    def clone(self) -> 'Board':
        '''
        Returns an independent copy of the board.
        '''

        return Board(self._cards)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Board):
            return NotImplemented

        return self._cards == other._cards

    def serialise(self) -> list[list[Optional[str]]]:
        '''
        Returns a serialisable representation of the board, where each card is represented by its ID.
        '''

        return [
            [
                card.id if card is not None else
                None for card in row
            ]
            for row in self._cards
        ]

    @classmethod
    def deserialise(cls, data: list[list[Optional[str]]]) -> "Board":
        '''
        Reconstructs a Board instance from a serialised representation.
        '''

        cards = [
            [
                get_card(card_id) if card_id is not None else
                None for card_id in row
            ]
            for row in data
        ]

        return cls(cards)

    @staticmethod
    def _copy_cards(cards: list[list[Optional[Card]]]) -> list[list[Optional[Card]]]:

        return [
            row.copy() for row in cards
        ]

    def _validate_dimensions(self) -> None:

        if len(self._cards) != BOARD_SIZE:
            raise ValueError(f"Board must have {BOARD_SIZE} rows")

        if any(len(row) != BOARD_SIZE for row in self._cards):
            raise ValueError(f"Board must have {BOARD_SIZE} columns in each row")

    @staticmethod
    def _validate_index(index: int) -> None:

        if not 0 <= index < BOARD_SIZE:
            raise IndexError(f"Index must be between 0 and {BOARD_SIZE - 1}")

    @staticmethod
    def _validate_position(position: Position) -> None:

        if not(
            0 <= position.row < BOARD_SIZE
            and 0 <= position.column < BOARD_SIZE
        ):
            raise IndexError(f"Position must be within the 4x4 grid.")

        # Board._validate_index(position.row)
        # Board._validate_index(position.column)