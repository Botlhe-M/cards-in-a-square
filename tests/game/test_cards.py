import pytest

from app.game.cards import (
    CARDS,
    Card,
    Suit,
    Value,
    cards_to_dict,
    create_card,
    create_deck,
    get_card,
)


def test_all_values_are_defined():
    assert {value.value for value in Value} == {"A", "J", "Q", "K"}


def test_all_suits_are_defined():
    assert {suit.value for suit in Suit} == {"H", "S", "D", "C"}


def test_deck_contains_exactly_16_cards():
    assert len(CARDS) == 16


def test_deck_contains_unique_card_ids():
    card_ids = [card.id for card in CARDS]

    assert len(card_ids) == len(set(card_ids))


def test_deck_contains_every_value_suit_combination():
    expected_ids = {
        f"{value.value}-{suit.value}"
        for value in Value
        for suit in Suit
    }

    actual_ids = {card.id for card in CARDS}

    assert actual_ids == expected_ids


def test_create_card():
    card = create_card(Value.QUEEN, Suit.DIAMONDS)

    assert card.id == "Q-D"
    assert card.value == Value.QUEEN
    assert card.suit == Suit.DIAMONDS
    assert card.svg == "/assets/cards/q-d.svg"


def test_card_is_immutable():
    card = create_card(Value.ACE, Suit.CLUBS)

    with pytest.raises(AttributeError):
        card.value = Value.KING


def test_get_card():
    card = get_card("Q-D")

    assert card.id == "Q-D"
    assert card.value == Value.QUEEN
    assert card.suit == Suit.DIAMONDS


def test_get_card_is_case_insensitive():
    card = get_card("q-d")

    assert card.id == "Q-D"


def test_get_card_rejects_unknown_id():
    with pytest.raises(ValueError, match="Unknown card ID"):
        get_card("X-Z")


def test_card_serialization():
    card = create_card(Value.QUEEN, Suit.DIAMONDS)

    assert card.to_dict() == {
        "id": "Q-D",
        "value": "Q",
        "suit": "D",
        "svg": "/assets/cards/q-d.svg",
    }


def test_deck_serialization():
    serialized_cards = cards_to_dict()

    assert len(serialized_cards) == 16
    assert all(
        set(card) == {"id", "value", "suit", "svg"}
        for card in serialized_cards
    )

def test_each_value_occurs_four_times():
    for value in Value:
        matching_cards = [
            card for card in CARDS
            if card.value == value
        ]

        assert len(matching_cards) == 4


def test_each_suit_occurs_four_times():
    for suit in Suit:
        matching_cards = [
            card for card in CARDS
            if card.suit == suit
        ]

        assert len(matching_cards) == 4