import pytest

from app.game.board import Board, Position
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


def test_board_starts_empty():
    board = Board()

    for row in range(4):
        assert board.row(row) == [None, None, None, None]


def test_board_has_four_rows_and_four_columns():
    board = Board()

    assert len(board.row(0)) == 4
    assert len(board.row(1)) == 4
    assert len(board.row(2)) == 4
    assert len(board.row(3)) == 4


def test_place_card():
    board = Board()
    card = get_card("Q-D")
    position = Position(0, 0)

    board.place(position, card)

    assert board.get(position) == card


def test_replace_card():
    board = Board()
    first_card = get_card("Q-D")
    second_card = get_card("A-C")
    position = Position(0, 0)

    board.place(position, first_card)
    board.place(position, second_card)

    assert board.get(position) == second_card


def test_swap_cards():
    board = create_test_board()

    first = Position(0, 0)
    second = Position(3, 3)

    first_card = board.get(first)
    second_card = board.get(second)

    board.swap(first, second)

    assert board.get(first) == second_card
    assert board.get(second) == first_card


def test_row_extraction():
    board = create_test_board()

    assert board.row(0) == [
        get_card("Q-D"),
        get_card("A-C"),
        get_card("J-H"),
        get_card("K-S"),
    ]


def test_column_extraction():
    board = create_test_board()

    assert board.column(0) == [
        get_card("Q-D"),
        get_card("J-S"),
        get_card("K-C"),
        get_card("A-H"),
    ]


def test_main_diagonal_extraction():
    board = create_test_board()

    assert board.main_diagonal() == [
        get_card("Q-D"),
        get_card("K-H"),
        get_card("A-S"),
        get_card("J-C"),
    ]


def test_anti_diagonal_extraction():
    board = create_test_board()

    assert board.anti_diagonal() == [
        get_card("K-S"),
        get_card("Q-C"),
        get_card("J-D"),
        get_card("A-H"),
    ]


def test_clone_creates_equal_board():
    board = create_test_board()

    clone = board.clone()

    assert clone == board
    assert clone is not board


def test_clone_is_independent():
    board = create_test_board()
    clone = board.clone()

    clone.swap(
        Position(0, 0),
        Position(3, 3),
    )

    assert clone != board


def test_board_equality():
    first = create_test_board()
    second = create_test_board()

    assert first == second


def test_different_boards_are_not_equal():
    first = create_test_board()
    second = create_test_board()

    second.swap(
        Position(0, 0),
        Position(3, 3),
    )

    assert first != second


def test_board_serialisation():
    board = create_test_board()

    assert board.serialise() == [
        ["Q-D", "A-C", "J-H", "K-S"],
        ["J-S", "K-H", "Q-C", "A-D"],
        ["K-C", "J-D", "A-S", "Q-H"],
        ["A-H", "Q-S", "K-D", "J-C"],
    ]


def test_board_deserialisation():
    board = create_test_board()

    serialised = board.serialise()
    restored = Board.deserialise(serialised)

    assert restored == board


def test_invalid_board_dimensions():
    with pytest.raises(ValueError):
        Board([[get_card("Q-D")]])


def test_invalid_position():
    board = Board()

    with pytest.raises(IndexError):
        board.get(Position(4, 0))