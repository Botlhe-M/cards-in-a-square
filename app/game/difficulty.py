from enum import Enum
from dataclasses import dataclass

class Difficulty(str, Enum):
    '''
    Represents the difficulty levels available in the puzzle.
    '''

    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"
    EXPERT = "expert"

@dataclass(frozen=True)
class DifficultyConfig:
    '''
    Represents the puzzle constraints that are active for a specific difficulty level.
    '''

    require_rows: bool
    require_columns: bool
    require_values: bool
    require_suits: bool
    require_main_diagonal: bool
    require_anti_diagonal: bool

    
DIFFICULTY_CONFIGS = {
    Difficulty.EASY: DifficultyConfig(
        require_rows=True,
        require_columns=True,
        require_values=True,
        require_suits=False,
        require_main_diagonal=False,
        require_anti_diagonal=False,
    ),
    Difficulty.NORMAL: DifficultyConfig(
        require_rows=True,
        require_columns=True,
        require_values=True,
        require_suits=True,
        require_main_diagonal=False,
        require_anti_diagonal=False,
    ),
    Difficulty.HARD: DifficultyConfig(
        require_rows=True,
        require_columns=True,
        require_values=True,
        require_suits=True,
        require_main_diagonal=True,
        require_anti_diagonal=True,
    ),
    Difficulty.EXPERT: DifficultyConfig(
        require_rows=True,
        require_columns=True,
        require_values=True,
        require_suits=True,
        require_main_diagonal=True,
        require_anti_diagonal=True,
    ),
}


def get_difficulty_config(difficulty: Difficulty) -> DifficultyConfig:
    '''
    Returns the constraint configuration for a difficulty level.
    '''

    return DIFFICULTY_CONFIGS[difficulty]