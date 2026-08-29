import pytest

from app.game.cards import get_card
from app.game.rules import (
    LINE_SIZE,
    is_complete_line,
    is_valid_suit_line,
    is_valid_value_line,
    validate_line,
)

def test_incomplete_value_line_without_duplicates_is_valid():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        None,
        get_card("K-D"),
    ]

    assert is_valid_value_line(cards) is True

def test_complete_value_line_is_valid():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        get_card("K-D"),
        get_card("Q-C"),
    ]

    assert is_valid_value_line(cards) is True

def test_incomplete_suit_line_without_duplicates_is_valid():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        None,
        get_card("K-D"),
    ]

    assert is_valid_suit_line(cards) is True

def test_suit_line_with_duplicates_is_invalid():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        get_card("K-D"),
        get_card("Q-H"),
    ]

    assert is_valid_suit_line(cards) is False

def test_complete_suit_line_is_valid():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        get_card("K-D"),
        get_card("Q-C"),
    ]

    assert is_valid_suit_line(cards) is True

def test_incomplete_line_is_not_complete():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        None,
        get_card("K-D"),
    ]

    assert is_complete_line(cards) is False

def test_complete_line_is_complete():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        get_card("K-D"),
        get_card("Q-C"),
    ]

    assert is_complete_line(cards) is True

def test_valid_incomplete_line_is_valid():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        None,
        get_card("K-D"),
    ]

    result = validate_line(cards)

    assert result.valid is True
    assert result.complete is False
    assert result.values_valid is True
    assert result.suits_valid is True

def  test_line_with_duplicate_value():
    cards = [
        get_card("A-H"),
        get_card("A-S"),
        None,
        None,
    ]

    result = validate_line(cards)

    assert result.valid is False
    assert result.complete is False
    assert result.values_valid is False
    assert result.suits_valid is True

def test_line_with_duplicate_suit():
    cards = [
        get_card("A-H"),
        get_card("J-H"),
        None,
        None,
    ]

    result = validate_line(cards)

    assert result.valid is False
    assert result.complete is False
    assert result.values_valid is True
    assert result.suits_valid is False

def test_complete_valid_line():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        get_card("K-D"),
        get_card("Q-C"),
    ]

    result = validate_line(cards)

    assert result.valid is True
    assert result.complete is True
    assert result.values_valid is True
    assert result.suits_valid is True

def test_line_can_ignore_suit_constraints():
    cards = [
        get_card("A-H"),
        get_card("J-H"),
        None,
        None,
    ]

    result = validate_line(cards,check_values=True, check_suits=False)

    assert result.valid is True
    assert result.complete is False
    assert result.values_valid is True
    assert result.suits_valid is True

def test_line_can_ignore_value_constraints():
    cards = [
        get_card("A-H"),
        get_card("A-S"),
        None,
        None,
    ]

    result = validate_line(cards, check_values=False, check_suits=True)

    assert result.valid is True
    assert result.complete is False
    assert result.values_valid is True
    assert result.suits_valid is True

def test_line_must_contain_exactly_four_cards():
    cards = [
        get_card("A-H"),
        get_card("J-S"),
        None,
    ]

    with pytest.raises(ValueError):
        validate_line(cards)