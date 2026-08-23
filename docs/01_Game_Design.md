# Cards in a Square

## Game Design Document

Version: 1.0

Status: Active

---

# 1. Overview

## Game Name

Cards in a Square

## Category

Logic Puzzle / Card Puzzle

## Genre

Single-player logic puzzle

## Platform

Web

## Core Concept

Cards in a Square is a logic puzzle in which the player must arrange 16 playing cards into a 4 × 4 square.

The 16 cards consist of:

* Four values: A, J, Q, K
* Four suits: ♥, ♠, ♦, ♣
* One card for every value/suit combination

The primary challenge is arranging the card values correctly.

The suits introduce a second layer of constraint and increase the difficulty.

At higher difficulties, both diagonals also become part of the puzzle.

---

# 2. Core Puzzle

The player receives exactly 16 cards:

```text
A♥  A♠  A♦  A♣

J♥  J♠  J♦  J♣

Q♥  Q♠  Q♦  Q♣

K♥  K♠  K♦  K♣
```

The player must place all 16 cards into a 4 × 4 grid.

A card is uniquely identified by:

```text
Value + Suit
```

For example:

```text
Q♦
A♣
J♥
K♠
```

The player cannot use duplicate cards.

---

# 3. Primary Objective

The primary puzzle dimension is **card value**.

The four values are:

```text
A
J
Q
K
```

Depending on difficulty, every required line must contain each value exactly once.

For example:

```text
A  Q  J  K
K  J  A  Q
Q  K  A  J
J  A  K  Q
```

A valid value line must therefore contain:

```text
A + J + Q + K
```

with no duplicate values.

---

# 4. Secondary Objective

The secondary puzzle dimension is **suit**.

The four suits are:

```text
♥
♠
♦
♣
```

At difficulties where suits are enabled, every required line must also contain each suit exactly once.

A valid line therefore satisfies two independent constraints:

```text
Values:
A J Q K

Suits:
♥ ♠ ♦ ♣
```

For example:

```text
A♥  J♠  Q♦  K♣
```

is valid because it contains:

```text
Values: A J Q K
Suits:  ♥ ♠ ♦ ♣
```

---

# 5. Grid

The game board consists of 16 positions arranged as:

```text
┌─────┬─────┬─────┬─────┐
│  1  │  2  │  3  │  4  │
├─────┼─────┼─────┼─────┤
│  5  │  6  │  7  │  8  │
├─────┼─────┼─────┼─────┤
│  9  │ 10  │ 11  │ 12  │
├─────┼─────┼─────┼─────┤
│ 13  │ 14  │ 15  │ 16  │
└─────┴─────┴─────┴─────┘
```

Cards can be moved between positions.

The exact interaction model will be determined during UI development, but the preferred interaction is:

* Drag and drop
* Touch-friendly movement on mobile
* Card swapping when moving onto an occupied position
* Clear visual indication of selected or dragged cards

---

# 6. Required Lines

The puzzle can contain three types of constraints.

## Rows

Four horizontal lines:

```text
──────
──────
──────
──────
```

## Columns

Four vertical lines:

```text
│
│
│
│
```

## Diagonals

Two diagonal lines:

```text
╲╱
╱╲
```

The two diagonals are:

### Main Diagonal

Top-left to bottom-right.

```text
X . . .
. X . .
. . X .
. . . X
```

### Anti-Diagonal

Top-right to bottom-left.

```text
. . . X
. . X .
. X . .
X . . .
```

---

# 7. Complete Solution Example

One confirmed complete solution is:

```text
QD  AC  JH  KS
JS  KH  QC  AD
KC  JD  AS  QH
AH  QS  KD  JC
```

## Rows

Row 1:

```text
QD AC JH KS
```

Values:

```text
Q A J K
```

Suits:

```text
♦ ♣ ♥ ♠
```

Valid.

Row 2:

```text
JS KH QC AD
```

Values:

```text
J K Q A
```

Suits:

```text
♠ ♥ ♣ ♦
```

Valid.

Row 3:

```text
KC JD AS QH
```

Values:

```text
K J A Q
```

Suits:

```text
♣ ♦ ♠ ♥
```

Valid.

Row 4:

```text
AH QS KD JC
```

Values:

```text
A Q K J
```

Suits:

```text
♥ ♠ ♦ ♣
```

Valid.

## Columns

Column 1:

```text
QD
JS
KC
AH
```

Values:

```text
Q J K A
```

Suits:

```text
♦ ♠ ♣ ♥
```

Valid.

Column 2:

```text
AC
KH
JD
QS
```

Values:

```text
A K J Q
```

Suits:

```text
♣ ♥ ♦ ♠
```

Valid.

Column 3:

```text
JH
QC
AS
KD
```

Values:

```text
J Q A K
```

Suits:

```text
♥ ♣ ♠ ♦
```

Valid.

Column 4:

```text
KS
AD
QH
JC
```

Values:

```text
K A Q J
```

Suits:

```text
♠ ♦ ♥ ♣
```

Valid.

## Main Diagonal

```text
QD → KH → AS → JC
```

Values:

```text
Q K A J
```

Suits:

```text
♦ ♥ ♠ ♣
```

Valid.

## Anti-Diagonal

```text
KS → QC → JD → AH
```

Values:

```text
K Q J A
```

Suits:

```text
♠ ♣ ♦ ♥
```

Valid.

---

# 8. Mathematical Foundation

The complete puzzle has a finite solution space.

There are:

```text
144
```

structurally distinct fundamental solutions.

Each fundamental solution can be transformed through the eight physical symmetries of a square:

```text
4 rotations
4 reflections/rotational reflections
```

This produces:

```text
144 × 8 = 1,152
```

valid full card arrangements.

These arrangements form the solution space for the full diagonal puzzle.

---

# 9. Reduced Puzzle Spaces

Different constraints produce different solution spaces.

## Rows + Columns + Values + Suits

When diagonals are ignored:

```text
6,912
```

valid arrangements exist.

This forms the mathematical basis of Normal difficulty.

## Values Only

When suit constraints and diagonal constraints are removed, the value layer contains:

```text
576
```

valid value grids.

This forms the mathematical basis of Easy difficulty.

The unrestricted combination space can be represented as:

```text
576 value grids × 331,776 suit variations

= 191,102,976 combinations
```

The important design point is that the game does not need to brute-force the entire unrestricted space.

The known valid solution spaces should be used to generate and validate puzzles efficiently.

---

# 10. Difficulty System

The game has four primary difficulty levels.

---

## 10.1 Easy

### Objective

Arrange the cards so that every row and column contains:

```text
A J Q K
```

exactly once.

### Active constraints

* Rows
* Columns
* Values

### Inactive constraints

* Suits
* Main diagonal
* Anti-diagonal

### Player experience

Easy introduces the fundamental concept of arranging the four card values.

Suits remain visually present but do not affect the result.

---

## 10.2 Normal

### Objective

Arrange the cards so that every row and column contains:

```text
A J Q K
```

and:

```text
♥ ♠ ♦ ♣
```

exactly once.

### Active constraints

* Rows
* Columns
* Values
* Suits

### Inactive constraints

* Main diagonal
* Anti-diagonal

### Player experience

Normal introduces the second dimension of the puzzle.

The player must stop thinking only about values and begin considering the exact identity of each card.

---

## 10.3 Hard

### Objective

Arrange all 16 cards so that every row, column and diagonal contains:

```text
A J Q K
```

and:

```text
♥ ♠ ♦ ♣
```

exactly once.

### Active constraints

* Rows
* Columns
* Main diagonal
* Anti-diagonal
* Values
* Suits

### Player experience

Hard is the complete version of the mathematical puzzle.

The player must reason across ten independent lines:

```text
4 rows
4 columns
2 diagonals
```

with two dimensions of constraints:

```text
Values
Suits
```

---

# 10.4 Expert

Expert uses the same mathematical rules as Hard but introduces information and resource limitations.

### Active constraints

* Rows
* Columns
* Main diagonal
* Anti-diagonal
* Values
* Suits

### Additional restrictions

* Some cards begin face down
* Limited moves
* Limited hints
* Timer
* No immediate conflict highlighting

### Face-Down Cards

Some cards initially display an unknown state:

```text
┌─────────┐
│         │
│    ?    │
│         │
└─────────┘
```

The player must infer the identity of hidden cards from the available information.

### Limited Moves

The player receives a predefined move allowance.

Example:

```text
Moves: 37 / 50
```

The exact allowance will be tuned through playtesting.

### Limited Hints

Players receive a limited number of hints.

Hints may:

* Identify a contradiction
* Reveal a card's value
* Reveal a card's suit
* Reveal a correct card placement

Hints should provide useful information without simply solving the puzzle.

### Timer

Expert tracks completion time.

The timer primarily affects scoring rather than acting as an automatic failure condition.

### No Immediate Conflict Highlighting

Unlike easier difficulties, Expert does not continuously reveal invalid rows, columns or diagonals.

The player must reason independently.

---

# 11. Validation

The game must have a central validation engine.

The validator receives:

```text
4 × 4 board
+
difficulty
```

and returns the current state of the puzzle.

The validator must be capable of determining:

* Whether every card is unique
* Whether every required value constraint is satisfied
* Whether every required suit constraint is satisfied
* Whether rows are valid
* Whether columns are valid
* Whether the main diagonal is valid
* Whether the anti-diagonal is valid
* Whether the complete puzzle is solved

Validation must be independent of the UI.

---

# 12. Feedback System

Feedback should depend on difficulty.

## Easy

Immediate feedback may identify:

```text
Value conflict
```

## Normal

Feedback may separately identify:

```text
Value conflict
Suit conflict
```

## Hard

Feedback may identify:

```text
Row conflict
Column conflict
Diagonal conflict
Value conflict
Suit conflict
```

## Expert

No immediate conflict highlighting.

The player must use the board and their own reasoning.

---

# 13. Check System

A Check action may be available on Easy, Normal and Hard.

Example:

```text
[ CHECK ]
```

The game evaluates the current board.

The result should communicate useful information without revealing the complete solution.

Example:

```text
Values: ✓
Suits: ✗
Rows: ✓
Columns: ✗
Diagonals: ✓
```

Expert may remove the Check action entirely.

---

# 14. Scoring

Completion and score are separate concepts.

A potential scoring model is:

```text
Base Score
    ↓
Difficulty Multiplier
    ↓
Time Bonus
    ↓
Move Efficiency
    ↓
Hint Penalty
    ↓
Final Score
```

Possible baseline values:

| Achievement     | Base Score |
| --------------- | ---------: |
| Complete Easy   |        100 |
| Complete Normal |        250 |
| Complete Hard   |        400 |
| Complete Expert |        600 |

These values are placeholders and should be tuned during playtesting.

---

# 15. Game Statistics

The game should track:

* Completion status
* Difficulty
* Time
* Moves
* Hints used
* Score
* Puzzle ID
* Best score
* Best time
* Best move count
* Number of attempts

Statistics may be stored locally initially.

Online accounts and global leaderboards can be added later.

---

# 16. Daily Puzzle

A future feature is a Daily Puzzle.

Each day provides a shared puzzle:

```text
Today's Puzzle

August 23, 2026
Hard
Puzzle #047
```

Players compete using:

* Completion time
* Moves
* Hints
* Score

The daily puzzle should be deterministic so that every player receives the same puzzle.

---

# 17. Puzzle Generation

Puzzle generation must not depend on uncontrolled random shuffling.

The system should:

1. Select a valid solution.
2. Apply an appropriate transformation.
3. Generate the starting player state.
4. Apply difficulty-specific restrictions.
5. Verify the resulting puzzle.
6. Assign a puzzle ID and seed.
7. Present it to the player.

The system should never generate an unsolvable puzzle.

---

# 18. Puzzle Identity

Every puzzle should have a deterministic identity.

Example:

```text
Puzzle ID: H-0047
Difficulty: Hard
Seed: 184729
Solution ID: 083
Transformation: Rotation 90°
```

This allows:

* Reproducible puzzles
* Daily puzzles
* Debugging
* Testing
* Leaderboards
* Replay systems

---

# 19. User Experience

The game should feel like manipulating a physical card puzzle rather than completing a spreadsheet.

Core interface:

```text
Cards in a Square

┌───────────────────────────────┐
│                               │
│       4 × 4 CARD BOARD        │
│                               │
│       [ CARD GRID ]           │
│                               │
└───────────────────────────────┘

Cards Remaining: 16

Moves: 24
Time: 04:21

[ CHECK ]   [ HINT ]   [ RESET ]
```

The interface should prioritize:

* Card readability
* Board clarity
* Minimal distractions
* Fast interaction
* Mobile usability
* Clear game state

---

# 20. Visual Design

The game should use recognizable playing-card conventions.

### Card values

```text
A
J
Q
K
```

### Suits

```text
♥
♦
♠
♣
```

Hearts and Diamonds should use the conventional red treatment.

Spades and Clubs should use the conventional black treatment.

Cards should remain visually recognizable at desktop and mobile sizes.

---

# 21. Responsive Design

The game must work on:

* Desktop
* Laptop
* Tablet
* Mobile

The 4 × 4 board must remain the dominant visual element.

On smaller screens:

* Card dimensions may shrink
* Controls may move below the board
* The card tray may become horizontally scrollable
* Touch interactions must remain reliable

---

# 22. Accessibility

The game should not depend exclusively on color.

Suit identity should be represented through:

* Suit symbol
* Textual/card representation
* Conventional color

Interactive elements should have:

* Keyboard focus states
* Accessible labels
* Sufficient contrast
* Touch-friendly targets

---

# 23. Design Principles

* The puzzle should be easy to understand but difficult to master.
* Values are the primary conceptual layer.
* Suits provide the secondary challenge.
* Diagonals provide the advanced mathematical constraint.
* Expert difficulty should increase cognitive pressure rather than merely increasing numerical complexity.
* The game should never generate an invalid puzzle.
* The validator must remain independent of the UI.
* The game should feel like a card puzzle, not a Sudoku clone.
* Feedback should teach without solving.
* Randomness should never compromise solvability.
* Difficulty should change the player experience in meaningful ways.
* Every completed puzzle should be reproducible through its puzzle ID/seed.

---

# 24. Long-Term Features

Potential future features include:

* Daily puzzle
* Global leaderboard
* Player accounts
* Achievement system
* Puzzle streaks
* Statistics dashboard
* Multiplayer race mode
* Custom puzzle generation
* Puzzle sharing
* Replay system
* Time attack mode
* Practice mode
* Accessibility mode
* Custom card themes

These features are not part of the initial MVP unless development scope changes.

---

# 25. MVP Definition

The MVP is complete when a player can:

1. Open the game.
2. Select a difficulty.
3. Receive 16 cards.
4. Arrange the cards on a 4 × 4 board.
5. Move or swap cards.
6. Receive difficulty-appropriate feedback.
7. Complete a valid puzzle.
8. Receive a score.
9. See completion statistics.
10. Restart or play another puzzle.

The MVP does not require:

* Accounts
* Online leaderboards
* Multiplayer
* Daily puzzles
* Social sharing

Those are post-MVP features.

---

# 26. Success Criteria

The game is successful when:

* The core rules are immediately understandable.
* Easy teaches the value constraint.
* Normal introduces the suit constraint.
* Hard introduces diagonal reasoning.
* Expert introduces information and resource management.
* Players can complete puzzles without technical confusion.
* Every generated puzzle is valid.
* The UI works on mobile and desktop.
* The game feels like a coherent puzzle rather than a collection of mechanics.
* Players have a reason to replay completed puzzles.

---

# 27. Current Design Status

Core puzzle concept:

**Defined**

Mathematical constraint system:

**Defined**

Complete valid solution:

**Verified**

Difficulty progression:

**Defined**

Expert mechanics:

**Defined**

Scoring:

**Initial design**

Puzzle generation:

**To be implemented**

UI:

**Not started**

Backend:

**Not started**

Online persistence:

**Not started**

---

# 28. Document Status

Version: 1.0

Status: Active

This document defines the intended player experience and game rules.

Implementation-specific decisions belong in:

> [02_Developer_Roadmap.md](02_Developer_Roadmap.md)


The design document should only change when the actual game design changes.
