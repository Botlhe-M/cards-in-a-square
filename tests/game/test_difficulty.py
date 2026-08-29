import pytest

from app.game.board import Board, Position
from app.game.cards import get_card
from app.game.difficulty import Difficulty
from app.game.validator import validate_board_for_difficulty


def create_easy_test_board_configuration():
    return Board(
        [
            [
                get_card("A-H"),
                get_card("J-S"),
                get_card("Q-D"),
                get_card("K-C"),
            ],
            [
                get_card("J-D"),
                get_card("Q-C"),
                get_card("K-H"),
                get_card("A-S"),
            ],
            [
                get_card("Q-H"),
                get_card("K-S"),
                get_card("A-D"),
                get_card("J-C"),
            ],
            [
                get_card("K-D"),
                get_card("A-C"),
                get_card("J-H"),
                get_card("Q-S"),
            ],
        ]
    )

def create_normal_test_board_configuration():
        return Board(
        [
            [
                get_card("A-H"),
                get_card("J-S"),
                get_card("Q-D"),
                get_card("K-C"),
            ],
            [
                get_card("J-D"),
                get_card("A-C"),
                get_card("K-H"),
                get_card("Q-S"),
            ],
            [
                get_card("Q-C"),
                get_card("K-D"),
                get_card("A-S"),
                get_card("J-H"),
            ],
            [
                get_card("K-S"),
                get_card("Q-H"),
                get_card("J-C"),
                get_card("A-D"),
            ],
        ]
    )

def create_hard_test_board_configuration():
    return Board(
        [
            [
                get_card("A-H"),
                get_card("J-S"),
                get_card("Q-D"),
                get_card("K-C"),
            ],
            [
                get_card("K-D"),
                get_card("Q-C"),
                get_card("J-H"),
                get_card("A-S"),
            ],
            [
                get_card("J-C"),
                get_card("A-D"),
                get_card("K-S"),
                get_card("Q-H"),
            ],
            [
                get_card("Q-S"),
                get_card("K-H"),
                get_card("A-C"),
                get_card("J-D"),
            ],
        ]
    )
def test_easy_configuration():
    board = create_easy_test_board_configuration()

    result = validate_board_for_difficulty(board, Difficulty.EASY)

    assert result.valid is True
    assert result.complete is True
    assert result.solved is True

def test_valid_incomplete_easy_configuration():
    board = create_easy_test_board_configuration()

    board.place(Position(0, 0), None)

    result = validate_board_for_difficulty(board, Difficulty.EASY)

    assert result.valid is True
    assert result.complete is False
    assert result.solved is False

def test_invalid_easy_configuration_with_duplicate_value():
    board = create_easy_test_board_configuration()

    board.place(Position(0, 1), get_card("A-D")) # Duplicate value A

    result = validate_board_for_difficulty(board, Difficulty.EASY)

    assert result.valid is False
    assert result.complete is True
    assert result.solved is False

def test_normal_configuration():
    board = create_normal_test_board_configuration()

    result = validate_board_for_difficulty(board, Difficulty.NORMAL)

    assert result.valid is True
    assert result.complete is True
    assert result.solved is True

def test_valid_incomplete_normal_configuration():
    board = create_normal_test_board_configuration()

    board.place(Position(0, 0), None)

    result = validate_board_for_difficulty(board, Difficulty.NORMAL)

    assert result.valid is True
    assert result.complete is False
    assert result.solved is False

def test_invalid_normal_configuration_with_duplicate_value():
    board = create_normal_test_board_configuration()

    board.place(Position(1, 0), get_card("A-D")) # Duplicate value A

    result = validate_board_for_difficulty(board, Difficulty.NORMAL)

    assert result.valid is False
    assert result.complete is True
    assert result.solved is False

def test_invalid_normal_configuration_with_duplicate_suit():
    board = create_normal_test_board_configuration()

    board.place(Position(1, 0), get_card("K-H")) # Duplicate suit H

    result = validate_board_for_difficulty(board, Difficulty.NORMAL)

    assert result.valid is False
    assert result.complete is True
    assert result.solved is False

def test_hard_configuration():
    board = create_hard_test_board_configuration()

    result = validate_board_for_difficulty(board, Difficulty.HARD)

    assert result.valid is True
    assert result.complete is True
    assert result.solved is True

def test_valid_incomplete_hard_configuration():
    board = create_hard_test_board_configuration()

    board.place(Position(0, 0), None)

    result = validate_board_for_difficulty(board, Difficulty.HARD)

    assert result.valid is True
    assert result.complete is False
    assert result.solved is False

def test_invalid_main_diagonal_hard_configuration_with_duplicate_value():
    board = create_hard_test_board_configuration()

    board.place(Position(1, 1), get_card("Q-H")) # Duplicate value Q

    result = validate_board_for_difficulty(board, Difficulty.HARD)

    assert result.valid is False
    assert result.complete is True
    assert result.solved is False

def test_invalid_anti_diagonal_hard_configuration_with_duplicate_suit():
    board = create_hard_test_board_configuration()

    board.place(Position(3, 0), get_card("A-D")) # Duplicate suit D

    result = validate_board_for_difficulty(board, Difficulty.HARD)

    assert result.valid is False
    assert result.complete is True
    assert result.solved is False

def test_expert_configuration():
    board = create_hard_test_board_configuration()

    result = validate_board_for_difficulty(board, Difficulty.EXPERT)

    assert result.valid is True
    assert result.complete is True
    assert result.solved is True

def test_valid_incomplete_expert_configuration():
    board = create_hard_test_board_configuration()

    board.place(Position(0, 0), None)

    result = validate_board_for_difficulty(board, Difficulty.EXPERT)

    assert result.valid is True
    assert result.complete is False
    assert result.solved is False