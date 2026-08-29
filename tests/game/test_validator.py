import pytest

from app.game.validator import (
    validate_column,
    validate_columns,
    validate_row,
    validate_rows,
    validate_main_diagonal,
    validate_anti_diagonal,
    validate_board
    )
from app.game.board import Board,Position
from app.game.cards import get_card

def create_test_board():
    return Board(
        [
            [
                get_card("Q-D"),
                get_card("A-C"),
                get_card("J-H"),
                get_card("K-S"),
            ],
            [
                get_card("J-S"),
                get_card("K-H"),
                get_card("Q-C"),
                get_card("A-D"),
            ],
            [
                get_card("K-C"),
                get_card("J-D"),
                get_card("A-S"),
                get_card("Q-H"),
            ],
            [
                get_card("A-H"),
                get_card("Q-S"),
                get_card("K-D"),
                get_card("J-C"),
            ],
        ]
    )


def test_validate_row():
    row_index = 0
    board = create_test_board()
    result = validate_row(board, row_index)

    assert result.index == row_index
    assert result.valid is True

def test_validate_row_with_duplicate_value():
    board = create_test_board()

    board.place(Position(0, 1), get_card("Q-C"))  # Duplicate value "Q"

    result = validate_row(board, 0)

    assert result.valid is False
    assert result.values.valid is False
    assert result.suits.valid is True

def test_validate_row_with_duplicate_suit():
    board = create_test_board()

    board.place(Position(0, 1), get_card("A-D"))  # Duplicate suit "D"

    result = validate_row(board, 0)

    assert result.valid is False
    assert result.values.valid is True
    assert result.suits.valid is False

def test_validate_incomplete_valid_row():
    board = create_test_board()

    board.place(Position(0, 1), None)

    result = validate_row(board, 0)

    assert result.valid is True
    assert result.complete is False
    assert result.values.valid is True
    assert result.suits.valid is True

def test_validate_incomplete_invalid_row():
    board = create_test_board()

    board.place(Position(0, 1), get_card("Q-C"))  # Duplicate value "Q"
    board.place(Position(0, 2), None)

    result = validate_row(board, 0)

    assert result.valid is False
    assert result.complete is False
    assert result.values.valid is False
    assert result.suits.valid is True

def test_validate_complete_valid_row_with_valid_suits_and_values():
    board = create_test_board()

    result = validate_row(board, 0)

    assert result.valid is True
    assert result.complete is True
    assert result.values.valid is True
    assert result.suits.valid is True

def test_validate_all_rows_on_Board():
    board = create_test_board()

    results = validate_rows(board)

    for result in results:
        assert result.valid is True
        assert result.complete is True
        assert result.values.valid is True
        assert result.suits.valid is True


def test_validate_columns():
    column_index = 0
    board = create_test_board()

    result = validate_column(board, column_index)

    assert result.index == column_index
    assert result.valid is True

def test_validate_column_with_duplicate_value():
    board = create_test_board()

    board.place(Position(2, 0), get_card("Q-C")) # Duplicate value "Q"

    result = validate_column(board, 0)

    assert result.valid is False
    assert result.values.valid is False
    assert result.suits.valid is True

def test_validate_column_with_duplicate_suit():
    board = create_test_board()

    board.place(Position(2, 0), get_card("K-D")) # Duplicate suit "D"

    result = validate_column(board, 0)

    assert result.valid is False
    assert result.values.valid is True
    assert result.suits.valid is False

def test_validate_incomplete_valid_column():
    board = create_test_board()

    board.place(Position(0,1), None)

    result = validate_column(board, 1)

    assert result.valid is True
    assert result.values.valid is True
    assert result.suits.valid is True
    assert result.complete is False

def test_validate_invalid_column_with_duplicate_value():
    board = create_test_board()

    board.place(Position(1, 0), get_card("Q-S")) # Duplicate value "Q"
    board.place(Position(2, 0), None)

    result = validate_column(board, 0)

    assert result.valid is False
    assert result.values.valid is False
    assert result.suits.valid is True
    assert result.complete is False

    
def test_validate_invalid_column_with_duplicate_suit():
    board = create_test_board()

    board.place(Position(0,3), get_card("K-H")) # Duplicate suit "H"
    board.place(Position(1,3), None)

    result = validate_column(board, 3)

    assert result.valid is False
    assert result.values.valid is True
    assert result.suits.valid is False
    assert result.complete is False

def test_validate_all_columns():
    board = create_test_board()

    results = validate_columns(board)

    for result in results:
        assert result.valid is True
        assert result.complete is True
        assert result.values.valid is True
        assert result.suits.valid is True


def test_validate_main_diagonal():
    board = create_test_board()

    result = validate_main_diagonal(board)

    assert result.valid is True
    assert result.complete is True

def test_validate_main_diagonal_with_duplicate_value():
    board = create_test_board()

    board.place(Position(1, 1), get_card("Q-H"))  # Duplicate value "Q"

    result = validate_main_diagonal(board)

    assert result.valid is False
    assert result.complete is True
    assert result.values.valid is False
    assert result.suits.valid is True

def test_validate_main_diagonal_with_duplicate_suit():
    board = create_test_board()

    board.place(Position(0, 0), get_card("Q-H"))  # Duplicate suit "H"

    result = validate_main_diagonal(board)

    assert result.valid is False
    assert result.complete is True
    assert result.values.valid is True
    assert result.suits.valid is False

def test_validate_incomplete_valid_main_diagonal():
    board = create_test_board()

    board.place(Position(0, 0), None) 

    result = validate_main_diagonal(board)

    assert result.valid is True
    assert result.complete is False
    assert result.values.valid is True
    assert result.suits.valid is True

def test_validate_incomplete_invalid_main_diagonal_with_duplicate_value():
    board = create_test_board()

    board.place(Position(0, 0), None) 
    board.place(Position(3,3), get_card("K-C")) # Duplicate value "K"

    result = validate_main_diagonal(board)

    assert result.valid is False
    assert result.complete is False
    assert result.values.valid is False
    assert result.suits.valid is True

def test_validate_incomplete_invalid_main_diagonal_with_duplicate_suit():
    board = create_test_board()

    board.place(Position(0, 0), None) 
    board.place(Position(3,3), get_card("J-H")) # Duplicate suit "H"

    result = validate_main_diagonal(board)

    assert result.valid is False
    assert result.complete is False
    assert result.values.valid is True
    assert result.suits.valid is False


def test_validate_anti_diagonal():
    board = create_test_board()

    result = validate_anti_diagonal(board)

    assert result.valid is True
    assert result.complete is True

def test_validate_anti_diagonal_with_duplicate_value():
    board = create_test_board()

    board.place(Position(0, 3), get_card("Q-S"))  # Duplicate value "Q"

    result = validate_anti_diagonal(board)

    assert result.valid is False
    assert result.complete is True
    assert result.values.valid is False
    assert result.suits.valid is True

def test_validate_anti_diagonal_with_duplicate_suit():
    board = create_test_board()

    board.place(Position(0, 3), get_card("K-H"))  # Duplicate suit "H"

    result = validate_anti_diagonal(board)

    assert result.valid is False
    assert result.complete is True
    assert result.values.valid is True
    assert result.suits.valid is False

def test_validate_incomplete_valid_anti_diagonal():
    board = create_test_board()

    board.place(Position(0, 3), None) 

    result = validate_anti_diagonal(board)

    assert result.valid is True
    assert result.complete is False
    assert result.values.valid is True
    assert result.suits.valid is True

def test_validate_incomplete_invalid_anti_diagonal_with_duplicate_value():
    board = create_test_board()

    board.place(Position(1, 2), None) 
    board.place(Position(3,0), get_card("K-H"))

    result = validate_anti_diagonal(board)

    assert result.valid is False
    assert result.complete is False
    assert result.values.valid is False
    assert result.suits.valid is True

def test_validate_incomplete_invalid_anti_diagonal_with_duplicate_suit():
    board = create_test_board()

    board.place(Position(0, 3), None) 
    board.place(Position(3,0), get_card("A-D")) # Duplicate suit "D"

    result = validate_anti_diagonal(board)

    assert result.valid is False
    assert result.complete is False
    assert result.values.valid is True
    assert result.suits.valid is False

def test_validate_board():
    board = create_test_board();

    result = validate_board(board)

    assert result.solved is True
    assert result.valid is True
    assert result.complete is True

    for row in result.rows:
        assert row.valid is True
        assert row.complete is True
        assert row.values.valid is True
        assert row.suits.valid is True

    for column in result.columns:
        assert column.valid is True
        assert column.complete is True
        assert column.values.valid is True
        assert column.suits.valid is True

    assert result.main_diagonal.valid is True
    assert result.main_diagonal.valid is True
    assert result.main_diagonal.complete is True
    assert result.main_diagonal.complete is True

    assert result.anti_diagonal.suits.valid is True
    assert result.anti_diagonal.suits.valid is True
    assert result.anti_diagonal.values.valid is True
    assert result.anti_diagonal.values.valid is True

def test_validate_board_with_invalid_row():
    board = create_test_board()

    board.place(Position(0,0), get_card("A-D")) # Duplicate value A

    result = validate_board(board)

    assert result.solved is False
    assert result.valid is False
    assert result.complete is True

    for row in result.rows:
        assert row.suits.valid is True

    assert result.rows[0].valid is False
    assert result.rows[0].values.valid is False
    

def test_validate_board_with_invalid_column():
    board = create_test_board()

    board.place(Position(2,0), get_card("K-D")) # Duplicate suit D

    result = validate_board(board)

    assert result.solved is False
    assert result.complete is True
    assert result.valid is False

    for column in result.columns:
        assert column.values.valid is True

    assert result.columns[0].values.valid is True
    assert result.columns[0].valid is False
    assert result.columns[0].suits.valid is False


def test_validate_board_with_invalid_main_diagonal():
    board = create_test_board()

    board.place(Position(1,1), get_card("Q-H")) # Duplicate value Q

    result = validate_board(board)

    assert result.valid is False
    assert result.complete is True
    assert result.solved is False

    assert result.main_diagonal.valid is False
    assert result.main_diagonal.values.valid is False
    assert result.main_diagonal.suits.valid is True

def test_validate_board_with_invalid_anti_diagonal():
    board = create_test_board()

    board.place(Position(3,0), get_card("A-D")) # Duplicate suit D

    result = validate_board(board)

    assert result.valid is False
    assert result.complete is True
    assert result.solved is False

    assert result.anti_diagonal.valid is False
    assert result.anti_diagonal.values.valid is True
    assert result.anti_diagonal.suits.valid is False

def test_validate_board_with_incomplete_line():
    board = create_test_board()

    board.place(Position(3,0), None)

    result = validate_board(board)

    assert result.valid is True
    assert result.complete is False
    assert result.solved is False

    for column in result.columns:
        assert column.valid is True
        assert column.values.valid is True
        assert column.suits.valid is True
