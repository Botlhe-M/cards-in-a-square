from dataclasses import dataclass

from .rules import (
    is_complete_line,
    is_valid_suit_line,
    is_valid_value_line
)

from .board import BOARD_SIZE
from .difficulty import Difficulty, get_difficulty_config

@dataclass(frozen=True)
class LineValidationResult:
    '''
    Represents the result of validating a line (row or column) on the board.
    '''

    valid: bool
    complete: bool
 

@dataclass(frozen=True)
class RowValidationResult:
    '''
    Represents the result of validating a row on the board.
    '''

    index: int
    valid: bool
    complete: bool
    values: LineValidationResult
    suits: LineValidationResult

def validate_value_line(line):
    '''
    Validates the value constraint for a board line (row or column).
    '''


    return LineValidationResult(
        valid=is_valid_value_line(line),
        complete=is_complete_line(line),
    )

def validate_suit_line(line):
    '''
    Validates the suit constraint for a board line (row or column).
    '''

    return LineValidationResult(
        valid=is_valid_suit_line(line),
        complete=is_complete_line(line),
    )

def validate_row(board, row_index):
    '''
    Validates a specific row on the board.
    '''
    row = board.row(row_index)

    values_result = validate_value_line(row)
    suits_result = validate_suit_line(row)

    return RowValidationResult(
        index=row_index,
        valid=values_result.valid and suits_result.valid,
        complete=values_result.complete and suits_result.complete,
        values=values_result,
        suits=suits_result
    )

def validate_rows(board):
    '''
    Validates all rows on the board.
    '''

    return [
        validate_row(board, row_index)
        for row_index in range(BOARD_SIZE)
    ]

@dataclass(frozen=True)
class ColumnValidationResult:
    '''
    Represents the result of validating a column on the board.
    '''

    index: int
    valid: bool
    complete: bool
    values: LineValidationResult
    suits: LineValidationResult

def validate_column(board, column_index):
    '''
    Validates a specific column on the board.
    '''
    column = board.column(column_index)

    values_result = validate_value_line(column)
    suits_result = validate_suit_line(column)

    return ColumnValidationResult(
        index=column_index,
        valid=values_result.valid and suits_result.valid,
        complete=values_result.complete and suits_result.complete,
        values=values_result,
        suits=suits_result
    )

def validate_columns(board):
    '''
    Validates all columns on the board.
    '''

    return [
        validate_column(board, column_index)
        for column_index in range(BOARD_SIZE)
    ]

@dataclass(frozen=True)
class DiagonalValidationResult:
    '''
    Represents the result of validating a diagonal on the board.
    '''

    valid: bool
    complete: bool
    values: LineValidationResult
    suits: LineValidationResult

def validate_main_diagonal(board):
    '''
    Validates the main diagonal on the board.
    '''

    diagonal = board.main_diagonal()

    values_result = validate_value_line(diagonal)
    suits_result = validate_suit_line(diagonal)

    return DiagonalValidationResult(
        valid=values_result.valid and suits_result.valid,
        complete=values_result.complete and suits_result.complete,
        values=values_result,
        suits=suits_result,
    )

def validate_anti_diagonal(board):
    '''
    Validates the anti-diagonal on the board.
    '''

    diagonal = board.anti_diagonal()

    values_result = validate_value_line(diagonal)
    suits_result = validate_suit_line(diagonal)

    return DiagonalValidationResult(
        valid=values_result.valid and suits_result.valid,
        complete=values_result.complete and suits_result.complete,
        values=values_result,
        suits=suits_result,
    )

@dataclass(frozen=True)
class BoardValidationResult:
    '''
    Represents the result of validating the complete board.
    '''

    solved: bool
    valid: bool
    complete: bool
    rows: list[RowValidationResult]
    columns: list[ColumnValidationResult]
    main_diagonal: DiagonalValidationResult
    anti_diagonal: DiagonalValidationResult

def validate_board(board):
    '''
    Validates all applicable constraints on the board.
    '''

    rows = validate_rows(board)
    columns = validate_columns(board)
    main_diagonal = validate_main_diagonal(board)
    anti_diagonal = validate_anti_diagonal(board)

    valid = (
        all(row.valid for row in rows)
        and all(column.valid for column in columns)
        and main_diagonal.valid
        and anti_diagonal.valid
    )

    complete = (
        all(row.complete for row in rows)
        and all(column.complete for column in columns)
        and main_diagonal.complete
        and anti_diagonal.complete
    )

    return BoardValidationResult(
        solved=valid and complete,
        valid=valid,
        complete=complete,
        rows=rows,
        columns=columns,
        main_diagonal=main_diagonal,
        anti_diagonal=anti_diagonal,
    )

'''
Helper functions to validate a board against the constraints active for a specific difficulty.
'''

def is_line_valid_for_config(line_result, config):
    '''
    Determines whether a row or column satisfies the constraints
    required by the selected difficulty.
    '''

    if config.require_values and not line_result.values.valid:
        return False

    if config.require_suits and not line_result.suits.valid:
        return False

    return True
def is_diagonal_valid_for_config(diagonal_result, config):
    '''
    Determines whether a diagonal satisfies the constraints active
    for the selected difficulty.
    '''

    if config.require_values and not diagonal_result.values.valid:
        return False

    if config.require_suits and not diagonal_result.suits.valid:
        return False

    return True

def validate_board_for_difficulty(board, difficulty):
    '''
    Validates a board using the enabled constraints for the selected difficulty
    '''
    config = get_difficulty_config(difficulty)
    result = validate_board(board)

    rows_valid = all(
        is_line_valid_for_config(row, config)
        for row in result.rows
    )

    columns_valid = all(
        is_line_valid_for_config(column, config)
        for column in result.columns
    )

    main_diagonal_valid = (
        not config.require_main_diagonal
        or is_diagonal_valid_for_config(
            result.main_diagonal,
            config
        )
    )

    anti_diagonal_valid = (
        not config.require_anti_diagonal
        or is_diagonal_valid_for_config(
            result.anti_diagonal,
            config
        )
    )

    valid = (
        rows_valid
        and columns_valid
        and main_diagonal_valid
        and anti_diagonal_valid
    )

    solved = valid and result.complete

    return BoardValidationResult(
        solved=solved,
        valid=valid,
        complete=result.complete,
        rows=result.rows,
        columns=result.columns,
        main_diagonal=result.main_diagonal,
        anti_diagonal=result.anti_diagonal,
    )