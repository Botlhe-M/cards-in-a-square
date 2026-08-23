# Cards in a Square

# Developer Roadmap

> **Purpose:** This is the living implementation document for Cards in a Square.
>
> It answers: **How are we building it?**
>
> Unlike [01_Game_Design.md](01_Game_Design.md), this document should be updated after every meaningful development session.

---

# 1. Project Status

| Field                 | Current State                               |
| --------------------- | ------------------------------------------- |
| Project               | Cards in a Square                           |
| Category              | Logic Puzzle / Card Puzzle                  |
| Platform              | Web                                         |
| Core grid             | 4 × 4                                       |
| Cards                 | 16 unique playing cards                     |
| Values                | A, J, Q, K                                  |
| Suits                 | ♥, ♠, ♦, ♣                                  |
| Full solution space   | 1,152 valid arrangements                    |
| Fundamental solutions | 144                                         |
| Normal solution space | 6,912                                       |
| Value-only grids      | 576                                         |
| Current phase         | Phase 0, Design Complete / Pre-Development  |
| Mathematical engine   | Not started                                 |
| Validator             | Not started                                 |
| Puzzle generator      | Not started                                 |
| Game UI               | Not started                                 |
| Difficulty system     | Designed                                    |
| Scoring               | Designed                                    |
| Persistence           | Not started                                 |
| Leaderboard           | Not started                                 |
| Deployment            | Not started                                 |
| Overall status        | Design complete, implementation not started |

---

# 2. Development Philosophy

The game should be built from the inside out.

The implementation order is:

```text
Mathematical Model
        ↓
Card Model
        ↓
Board Representation
        ↓
Constraint Validator
        ↓
Solution Library / Generator
        ↓
Difficulty Engine
        ↓
Game State
        ↓
Interaction System
        ↓
UI
        ↓
Scoring
        ↓
Persistence
        ↓
Testing
        ↓
Deployment
```

The mathematical engine must not depend on the UI.

The UI must consume the game engine rather than contain the game rules itself.

---

# 3. Core Architecture Principle

The project should have a clear separation between:

```text
Game Logic
     ↓
Game State
     ↓
UI
```

The following should remain independent of React, Vue, DOM APIs or visual components:

* Card representation
* Board representation
* Constraint validation
* Solution checking
* Puzzle generation
* Difficulty rules
* Move counting
* Hint logic
* Scoring

This makes the puzzle engine testable independently.

---

# 4. Recommended Technology Stack

The initial implementation should use a lightweight Flask architecture with the game engine separated from the presentation layer.

The core puzzle logic should remain independent from the web interface so that it can be tested and reused without running the application.

**## Backend**

* Python
* Flask
* Jinja2
* Flask JSON routes where client-server communication is required

**## Game Engine**

* Pure Python
* Dataclasses for domain models
* Dedicated validation logic
* Dedicated puzzle generation and solving logic
* Dedicated difficulty configuration

The game engine should not depend on Flask.

This separation allows the mathematical puzzle logic to be tested independently from the web application.

**## Frontend**

* HTML5
* CSS
* Vanilla JavaScript

JavaScript should handle interactive game state in the browser, including:

* Card selection
* Card movement
* Board rendering
* Timer
* Move counter
* Conflict highlighting
* Hints
* Difficulty-specific UI behaviour
* Game completion detection

**## State Management**

No dedicated state-management library should be used.

Game state should initially be managed through the browser's JavaScript state.

The server should not be contacted for every player move.

**## Testing**

* pytest for Python game logic
* Flask test client for application routes
* JavaScript tests may be introduced later if the frontend logic becomes sufficiently complex

The puzzle validator, solver and generator should receive the highest testing priority because they define the correctness of the game.

**## Build Tool**

No frontend build tool is required initially.

Flask will serve:

* HTML templates
* CSS
* JavaScript
* Static assets

If frontend complexity eventually justifies a build system, one can be introduced later without changing the underlying game rules.

**## Database**

No database is required for the initial MVP.

A database should only be introduced when persistent functionality requires it, such as:

* Player accounts
* Leaderboards
* Saved games
* Statistics
* Daily puzzle history

If persistence is later required, SQLite should be the initial choice.

**## Deployment**

Potential options:

* Docker
* Render
* Railway
* Fly.io
* A traditional Python hosting environment

The initial application should be deployable as a small Flask application.

**## Architecture Principle**

The project should follow:

```text
Browser
   │
   │ HTTP
   ↓
Flask Application
   │
   ├── Routes
   │
   └── Game Engine
          │
          ├── Card Model
          ├── Board Model
          ├── Rules
          ├── Validator
          ├── Solver
          ├── Generator
          ├── Difficulty
          ├── Scoring
          └── Hints
```

The frontend should communicate with the game engine through clearly defined application interfaces rather than embedding the mathematical rules throughout the UI.

---

# 5. Phase 0: Game Design

## Goal

Define the complete game before implementation.

### Deliverables

* [x] Game concept
* [x] Core rules
* [x] Card set
* [x] 4 × 4 board
* [x] Row constraints
* [x] Column constraints
* [x] Diagonal constraints
* [x] Value constraints
* [x] Suit constraints
* [x] Difficulty system
* [x] Expert mechanics
* [x] Initial scoring system
* [x] Mathematical solution-space information
* [x] Complete valid example solution
* [x] MVP definition

### Status

**Complete**

---

# 6. Phase 1: Project Foundation

## Goal

Create the Flask development environment and establish a clean project structure.

### Deliverables

* [X] Initialize repository
* [X] Create Python virtual environment
* [X] Initialize Flask application
* [X] Configure Flask application factory
* [X] Configure development environment
* [X] Configure testing environment
* [X] Create source directory structure
* [X] Create initial application shell
* [X] Create base Jinja2 template
* [X] Configure static assets
* [X] Create initial CSS
* [X] Create initial JavaScript entry point
* [X] Create README
* [X] Configure Git ignore
* [X] Verify development server
* [X] Verify production-style application startup
* [X] Verify basic Flask test

### Proposed Structure

```text
cards-in-a-square/
│
├── app/
│   │
│   ├── __init__.py
│   ├── routes.py
│   │
│   ├── game/
│   │   ├── __init__.py
│   │   ├── cards.py
│   │   ├── board.py
│   │   ├── rules.py
│   │   ├── validator.py
│   │   ├── solver.py
│   │   ├── generator.py
│   │   ├── difficulty.py
│   │   ├── scoring.py
│   │   └── hints.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── difficulty.html
│   │   ├── game.html
│   │   └── results.html
│   │
│   └── static/
│       ├── css/
│       │   ├── main.css
│       │   ├── cards.css
│       │   └── game.css
│       │
│       ├── js/
│       │   ├── game.js
│       │   ├── board.js
│       │   ├── timer.js
│       │   └── ui.js
│       │
│       └── assets/
│           └── cards/
│
├── tests/
│   ├── game/
│   │   ├── test_cards.py
│   │   ├── test_board.py
│   │   ├── test_rules.py
│   │   ├── test_validator.py
│   │   ├── test_solver.py
│   │   ├── test_generator.py
│   │   ├── test_difficulty.py
│   │   └── test_scoring.py
│   │
│   └── test_routes.py
│
├── instance/
│
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
├── Dockerfile
└── README.md
```

### Architectural Rule

The `app/game/` package must remain independent of Flask wherever practical.

For example:

```text
validator.py
     ↓
receives Board
     ↓
checks puzzle rules
     ↓
returns validation result
```

It should **not** need:

```python
from flask import request
```

The game engine is the core of the project. Flask is the delivery mechanism.

### Exit Criteria

The project:

1. Installs successfully.
2. Starts successfully.
3. Serves the initial page.
4. Loads CSS and JavaScript.
5. Runs the Flask test suite.
6. Has a clean separation between the game engine and web layer.

### Status

**Complete**

---

# 7. Phase 2: Card Domain Model

## Goal

Represent the 16 physical cards in code.

### Card Definition

Each card should contain:

```text
id
value
suit
```

Example:

```text
{
    id: "Q-D",
    value: "Q",
    suit: "D"
}
```

The initial card set consists of exactly one card for every combination of:

```text
Values:
A
J
Q
K

Suits:
Heart
Spade
Diamond
Club
```

Therefore:

```text
4 values × 4 suits = 16 cards
```

### Deliverables

* [X] Define `Value`
* [X] Define `Suit`
* [X] Define `Card`
* [X] Define card ID convention
* [X] Create all 16 cards
* [X] Verify card uniqueness
* [X] Create card lookup utilities
* [X] Create card serialization utilities if required
* [X] Write unit tests

### Example Python Model

The exact implementation can be decided during development, but the domain should conceptually resemble:

```python
@dataclass(frozen=True)
class Card:
    id: str
    value: Value
    suit: Suit
```

The card should be immutable where practical.

### Exit Criteria

The game engine can reliably:

* Represent every card.
* Identify a card's value.
* Identify a card's suit.
* Compare cards.
* Look up cards by ID.
* Verify that the complete deck contains exactly 16 unique cards.

### Status

**Complete**

---
# 8. Phase 3: Board Model

## Goal

Represent a 4 × 4 arrangement independently of the UI.

### Deliverables

* [X] Define board type
* [X] Define board positions
* [X] Define row extraction
* [X] Define column extraction
* [X] Define main diagonal extraction
* [X] Define anti-diagonal extraction
* [X] Define card placement
* [X] Define card swapping
* [X] Define board cloning
* [X] Define board equality
* [X] Write unit tests

### Example

```text
Board
[
    [Card, Card, Card, Card],
    [Card, Card, Card, Card],
    [Card, Card, Card, Card],
    [Card, Card, Card, Card]
]
```

### Exit Criteria

The board model is responsible for board structure and state. It must not contain puzzle validation, scoring, difficulty, hint, or UI logic.

### Status

**Complete**
---

# 9. Phase 4: Constraint Engine

## Goal

Implement the actual mathematical rules.

This is the most important technical phase.

### Deliverables

* [ ] Value-line validator
* [ ] Suit-line validator
* [ ] Row validator
* [ ] Column validator
* [ ] Main diagonal validator
* [ ] Anti-diagonal validator
* [ ] Complete-board validator
* [ ] Difficulty-aware validator
* [ ] Structured validation result
* [ ] Unit tests

### Validation Result

The validator should return structured information rather than only:

```text
true / false
```

Example:

```text
{
    solved: false,

    rows: {
        valid: true
    },

    columns: {
        valid: false
    },

    diagonals: {
        valid: true
    },

    values: {
        valid: true
    },

    suits: {
        valid: false
    }
}
```

This allows the UI to provide useful feedback.

### Exit Criteria

The validator correctly accepts the known valid solution and rejects deliberately invalid boards.

---

# 10. Phase 5: Mathematical Verification

## Goal

Verify the known solution space independently of the game UI.

### Deliverables

* [ ] Encode the known valid solution
* [ ] Verify the 10 full constraints
* [ ] Verify rotational symmetry
* [ ] Verify reflection symmetry
* [ ] Verify fundamental solution representation
* [ ] Confirm 144 fundamental solutions
* [ ] Confirm 1,152 full arrangements
* [ ] Verify the 6,912 Normal solution space
* [ ] Verify the 576 value-grid space where applicable
* [ ] Document any assumptions used by the enumeration

### Important Rule

The numerical solution counts should be treated as **verified project data**, not merely copied into the game because they were stated during design.

The implementation should independently reproduce the counts.

### Exit Criteria

The mathematical engine independently confirms the project's solution-space assumptions.

---

# 11. Phase 6: Solution Library

## Goal

Create a reliable source of valid puzzle solutions.

### Deliverables

* [ ] Generate fundamental solutions
* [ ] Store canonical representations
* [ ] Generate symmetry variants
* [ ] Deduplicate equivalent boards
* [ ] Assign solution IDs
* [ ] Create difficulty-specific solution pools
* [ ] Create deterministic selection mechanism
* [ ] Write tests

### Example

```text
Solution ID:
H-0083

Fundamental Solution:
F-021

Transformation:
ROTATE_90
```

### Exit Criteria

The application can request a valid solution by difficulty.

---

# 12. Phase 7: Puzzle Generator

## Goal

Turn valid solutions into playable puzzle instances.

### Deliverables

* [ ] Seed-based generation
* [ ] Solution selection
* [ ] Card permutation
* [ ] Difficulty configuration
* [ ] Expert hidden-card generation
* [ ] Puzzle ID generation
* [ ] Puzzle reproducibility
* [ ] Solvability verification

### Important Constraint

The generator must never produce a puzzle that violates the selected difficulty's intended rules.

### Exit Criteria

The same puzzle seed produces the same puzzle.

---

# 13. Phase 8: Difficulty Engine

## Goal

Implement the four difficulty levels.

### Easy

```text
Rows
Columns
Values
```

### Normal

```text
Rows
Columns
Values
Suits
```

### Hard

```text
Rows
Columns
Main diagonal
Anti-diagonal
Values
Suits
```

### Expert

```text
Rows
Columns
Main diagonal
Anti-diagonal
Values
Suits

+
Face-down cards
Limited moves
Limited hints
Timer
No immediate conflict highlighting
```

### Deliverables

* [ ] Difficulty enum
* [ ] Difficulty configuration
* [ ] Constraint configuration
* [ ] Feedback configuration
* [ ] Move configuration
* [ ] Hint configuration
* [ ] Timer configuration
* [ ] Face-down configuration
* [ ] Unit tests

### Exit Criteria

Changing difficulty changes the actual game rules and not merely the visual label.

---

# 14. Phase 9: Game State Engine

## Goal

Create the state machine governing a game session.

### Game State

Should include concepts such as:

```text
puzzle
difficulty
board
remainingCards
moves
hints
time
status
score
```

### Game Status

Potential states:

```text
READY
PLAYING
PAUSED
SOLVED
FAILED
```

### Deliverables

* [ ] Game initialization
* [ ] Card movement
* [ ] Card swapping
* [ ] Move tracking
* [ ] Timer state
* [ ] Hint tracking
* [ ] Reset
* [ ] Check
* [ ] Solve detection
* [ ] Game completion
* [ ] Unit tests

### Exit Criteria

A complete game can be played entirely through the game-state engine without UI dependencies.

---

# 15. Phase 10: Card UI

## Goal

Create the visual representation of the cards.

### Deliverables

* [ ] Card component
* [ ] Value rendering
* [ ] Suit rendering
* [ ] Red suit styling
* [ ] Black suit styling
* [ ] Selected state
* [ ] Dragged state
* [ ] Face-down state
* [ ] Hover state
* [ ] Mobile interaction
* [ ] Accessibility labels

### Exit Criteria

Cards are readable and usable on desktop and mobile.

---

# 16. Phase 11: Board UI

## Goal

Create the interactive 4 × 4 board.

### Deliverables

* [ ] 4 × 4 grid
* [ ] Card placement
* [ ] Drag and drop
* [ ] Card swapping
* [ ] Touch interaction
* [ ] Empty positions
* [ ] Selected card state
* [ ] Invalid interaction feedback
* [ ] Responsive board

### Exit Criteria

A player can physically arrange all 16 cards through the browser.

---

# 17. Phase 12: Game Interface

## Goal

Build the complete playable game interface.

### Deliverables

* [ ] Game header
* [ ] Difficulty indicator
* [ ] Move counter
* [ ] Timer
* [ ] Card tray
* [ ] Check button
* [ ] Hint button
* [ ] Reset button
* [ ] Pause functionality if required
* [ ] Completion state
* [ ] Results screen

### Exit Criteria

The game can be played from start to finish without developer tools.

---

# 18. Phase 13: Feedback System

## Goal

Make the game's feedback useful without making the puzzle trivial.

### Easy

Show value conflicts.

### Normal

Show value and suit conflicts.

### Hard

Show:

* Row conflicts
* Column conflicts
* Diagonal conflicts
* Value conflicts
* Suit conflicts

### Expert

Remove immediate conflict highlighting.

### Deliverables

* [ ] Constraint indicators
* [ ] Valid state
* [ ] Invalid state
* [ ] Check results
* [ ] Completion feedback
* [ ] Expert feedback restrictions

### Exit Criteria

Feedback corresponds exactly to the mathematical validator.

---

# 19. Phase 14: Hint System

## Goal

Implement controlled assistance.

### Hint Levels

Potential hint types:

1. Identify a contradiction.
2. Reveal a card value.
3. Reveal a card suit.
4. Identify a correct placement.

### Deliverables

* [ ] Hint interface
* [ ] Hint selection logic
* [ ] Hint counter
* [ ] Hint penalties
* [ ] Expert hint restrictions
* [ ] Tests

### Design Constraint

Hints should help the player reason.

They should not simply solve the entire board.

### Exit Criteria

Hints are useful but do not trivialize the puzzle.

---

# 20. Phase 15: Expert Mechanics

## Goal

Implement the additional restrictions unique to Expert.

### Deliverables

* [ ] Face-down cards
* [ ] Card reveal mechanics
* [ ] Move limit
* [ ] Move failure state
* [ ] Hint limit
* [ ] Timer
* [ ] No immediate validation feedback
* [ ] Expert scoring
* [ ] Tests

### Exit Criteria

Expert feels materially more difficult than Hard without changing the underlying mathematical puzzle.

---

# 21. Phase 16: Scoring

## Goal

Implement the scoring system.

### Inputs

* Difficulty
* Completion
* Time
* Moves
* Hints

### Deliverables

* [ ] Base scores
* [ ] Difficulty multipliers
* [ ] Time bonus
* [ ] Move efficiency
* [ ] Hint penalties
* [ ] Final score calculation
* [ ] Score breakdown
* [ ] Unit tests

### Exit Criteria

Scores are deterministic and explainable.

---

# 22. Phase 17: Results Screen

## Goal

Give the player a satisfying conclusion.

### Results

Display:

```text
PUZZLE COMPLETE

Difficulty: Hard

Time: 04:32
Moves: 37
Hints: 0

Score: 8,420
```

### Deliverables

* [ ] Results screen
* [ ] Score breakdown
* [ ] Best score
* [ ] Best time
* [ ] Play again
* [ ] New puzzle
* [ ] Difficulty selection

### Exit Criteria

Players can immediately understand how well they performed.

---

# 23. Phase 18: Local Persistence

## Goal

Persist player progress without requiring an account.

### Possible Storage

```text
localStorage
```

### Store

* Best scores
* Best times
* Best moves
* Completed puzzles
* Difficulty statistics
* Current streak if implemented

### Deliverables

* [ ] Storage abstraction
* [ ] Save results
* [ ] Load results
* [ ] Reset statistics
* [ ] Storage tests

### Exit Criteria

Statistics survive page refreshes.

---

# 24. Phase 19: Daily Puzzle

## Goal

Introduce deterministic shared puzzles.

### Deliverables

* [ ] Date-based seed
* [ ] Daily puzzle selection
* [ ] Difficulty
* [ ] Puzzle ID
* [ ] Daily completion tracking
* [ ] Daily statistics

### Exit Criteria

Every player receives the same daily puzzle.

---

# 25. Phase 20: Leaderboard

## Goal

Introduce online competition.

This phase should only happen after the core game is stable.

### Deliverables

* [ ] Backend decision
* [ ] Player identity
* [ ] Score submission
* [ ] Score validation
* [ ] Leaderboard API
* [ ] Leaderboard UI
* [ ] Anti-cheat considerations

### Important

A client-only leaderboard should not be trusted.

If scores become competitive, score validation must happen server-side.

---

# 26. Phase 21: Accessibility

## Goal

Ensure the game is usable by as many players as practical.

### Deliverables

* [ ] Keyboard navigation
* [ ] Focus indicators
* [ ] Screen-reader labels
* [ ] Card descriptions
* [ ] Suit symbols independent of color
* [ ] Contrast testing
* [ ] Reduced-motion support
* [ ] Touch target testing

### Exit Criteria

The game remains understandable without relying exclusively on color or animation.

---

# 27. Phase 22: Responsive Testing

## Goal

Verify the complete game across screen sizes.

### Test Categories

* [ ] Desktop
* [ ] Laptop
* [ ] Tablet
* [ ] Mobile
* [ ] Portrait
* [ ] Landscape
* [ ] Touch
* [ ] Mouse
* [ ] Keyboard

### Exit Criteria

The 4 × 4 board remains usable at all supported breakpoints.

---

# 28. Phase 23: Automated Testing

## Goal

Establish confidence in the mathematical and gameplay systems.

## Unit Tests

* [ ] Card creation
* [ ] Card uniqueness
* [ ] Board creation
* [ ] Row extraction
* [ ] Column extraction
* [ ] Diagonal extraction
* [ ] Value validation
* [ ] Suit validation
* [ ] Full validation
* [ ] Difficulty validation
* [ ] Solution generation
* [ ] Puzzle generation
* [ ] Scoring
* [ ] Hints
* [ ] Move limits

## Integration Tests

* [ ] Start game
* [ ] Select difficulty
* [ ] Move card
* [ ] Swap cards
* [ ] Check board
* [ ] Use hint
* [ ] Complete puzzle
* [ ] Reset game
* [ ] Expert failure conditions

## End-to-End Tests

* [ ] Start Easy
* [ ] Complete Easy
* [ ] Start Normal
* [ ] Complete Normal
* [ ] Start Hard
* [ ] Complete Hard
* [ ] Start Expert
* [ ] Complete Expert

---

# 29. Phase 24: Mathematical Regression Testing

## Goal

Prevent future changes from corrupting the puzzle rules.

### Required Tests

The known complete solution must always remain valid.

```text
QD AC JH KS
JS KH QC AD
KC JD AS QH
AH QS KD JC
```

The test suite must also contain intentionally invalid arrangements.

Examples:

* Duplicate value in a row
* Duplicate suit in a row
* Duplicate value in a column
* Duplicate suit in a column
* Duplicate value on a diagonal
* Duplicate suit on a diagonal
* Duplicate physical card

### Exit Criteria

Any change to the validation engine immediately exposes a regression.

---

# 30. Phase 25: Performance Testing

## Goal

Ensure puzzle generation and validation are fast enough for real-time gameplay.

### Test

* [ ] Validate thousands of boards
* [ ] Generate large puzzle batches
* [ ] Load solution library
* [ ] Measure startup time
* [ ] Measure interaction latency
* [ ] Test low-end mobile performance

### Exit Criteria

Normal card interactions should feel instantaneous.

---

# 31. Phase 26: Security and Anti-Cheat

This is primarily relevant if online leaderboards or multiplayer are introduced.

### Deliverables

* [ ] Never trust client-submitted scores
* [ ] Validate completion server-side
* [ ] Validate puzzle ID
* [ ] Validate timing data
* [ ] Prevent arbitrary score submission
* [ ] Rate-limit score submissions
* [ ] Protect leaderboard endpoints

This is not required for the initial offline MVP.

---

# 32. Phase 27: Deployment

## Goal

Deploy the playable game publicly.

### Deliverables

* [ ] Production build
* [ ] Deployment configuration
* [ ] Environment configuration
* [ ] Production testing
* [ ] Mobile testing
* [ ] Error monitoring
* [ ] Analytics if desired
* [ ] Custom domain if desired

### Exit Criteria

A player can open the public URL and immediately play.

---

# 33. Phase 28: Documentation

### Deliverables

* [ ] README
* [ ] Setup instructions
* [ ] Development instructions
* [ ] Architecture documentation
* [ ] Game rules
* [ ] Testing instructions
* [ ] Deployment instructions
* [ ] Puzzle-generation documentation

---

# 34. MVP Scope

The first release should contain only what is necessary for a complete, polished game.

### Required

* [ ] Home screen
* [ ] Difficulty selection
* [ ] 16 cards
* [ ] 4 × 4 board
* [ ] Card movement
* [ ] Easy
* [ ] Normal
* [ ] Hard
* [ ] Expert
* [ ] Validator
* [ ] Puzzle library/generator
* [ ] Timer
* [ ] Move counter
* [ ] Hints
* [ ] Check system
* [ ] Scoring
* [ ] Results screen
* [ ] Responsive design
* [ ] Local statistics

### Not Required for MVP

* [ ] Accounts
* [ ] Global leaderboard
* [ ] Multiplayer
* [ ] Daily puzzle
* [ ] Social sharing
* [ ] Cloud synchronization
* [ ] Custom puzzle creator

---

# 35. Progress Tracker

| Phase                                     | Status        |
| ----------------------------------------- | ------------- |
| Phase 0: Game Design                      | ✅ Complete    |
| Phase 1: Project Foundation               | ✅ Complete    |
| Phase 2: Card Domain Model                | 🔃 In-Progress |
| Phase 3: Board Model                      | ⬜ Not Started |
| Phase 4: Constraint Engine                | ⬜ Not Started |
| Phase 5: Mathematical Verification        | ⬜ Not Started |
| Phase 6: Solution Library                 | ⬜ Not Started |
| Phase 7: Puzzle Generator                 | ⬜ Not Started |
| Phase 8: Difficulty Engine                | ⬜ Not Started |
| Phase 9: Game State Engine                | ⬜ Not Started |
| Phase 10: Card UI                         | ⬜ Not Started |
| Phase 11: Board UI                        | ⬜ Not Started |
| Phase 12: Game Interface                  | ⬜ Not Started |
| Phase 13: Feedback System                 | ⬜ Not Started |
| Phase 14: Hint System                     | ⬜ Not Started |
| Phase 15: Expert Mechanics                | ⬜ Not Started |
| Phase 16: Scoring                         | ⬜ Not Started |
| Phase 17: Results Screen                  | ⬜ Not Started |
| Phase 18: Local Persistence               | ⬜ Not Started |
| Phase 19: Daily Puzzle                    | ⬜ Not Started |
| Phase 20: Leaderboard                     | ⬜ Not Started |
| Phase 21: Accessibility                   | ⬜ Not Started |
| Phase 22: Responsive Testing              | ⬜ Not Started |
| Phase 23: Automated Testing               | ⬜ Not Started |
| Phase 24: Mathematical Regression Testing | ⬜ Not Started |
| Phase 25: Performance Testing             | ⬜ Not Started |
| Phase 26: Security / Anti-Cheat           | ⬜ Not Started |
| Phase 27: Deployment                      | ⬜ Not Started |
| Phase 28: Documentation                   | ⬜ Not Started |

---

# 36. Development Sessions

This section should be updated after each meaningful development session.

## Session Template

### Date

YYYY-MM-DD

### Phase

Phase X

### Completed

* [ ]

### Decisions

*

### Problems

*

### Resolutions

*

### Tests

*

### Next Step

*

---

# 37. Important Implementation Decisions

## Decision 1: Logic Must Be UI Independent

The mathematical puzzle engine must not know that cards are being rendered in React.

Reason:

The same validator should be usable by:

* Unit tests
* Puzzle generation
* UI feedback
* Hint system
* Future backend validation

---

## Decision 2: Do Not Randomly Shuffle and Hope

A random permutation of 16 cards is not automatically a valid puzzle.

Puzzle instances must originate from known valid arrangements or a verified constraint-solving/generation process.

---

## Decision 3: Validate the Mathematics

The project's known solution counts should be independently verified by the implementation.

Do not build critical generation logic around unverified assumptions.

---

## Decision 4: Expert Uses the Same Core Rules

Expert should not introduce an entirely different puzzle.

It uses the Hard mathematical rules and changes:

* Information
* Feedback
* Moves
* Hints
* Time

---

## Decision 5: Keep the MVP Client-Side

The core game does not require a backend.

A backend should only be introduced when features such as:

* Global leaderboards
* Accounts
* Multiplayer
* Cloud saves

actually require one.

---

## Decision 6: Avoid Premature Dependencies

Do not introduce:

* Global state libraries
* Backend services
* Databases
* Authentication
* Analytics

until a real feature requires them.

The initial puzzle should remain technically simple.

---

# 38. Known Technical Risks

## Risk 1: Incorrect Validator

The validator is the foundation of the entire game.

### Mitigation

Build comprehensive unit tests before implementing the visual game.

---

## Risk 2: Incorrect Solution Enumeration

The stated solution counts may depend on precise definitions of structural equivalence and symmetry.

### Mitigation

Document the exact mathematical definition and independently verify enumeration.

---

## Risk 3: Expert Becoming Frustrating

Too many restrictions could make Expert feel unfair.

### Mitigation

Playtest:

* Move limits
* Hint limits
* Number of hidden cards
* Timer
* Feedback restrictions

---

## Risk 4: Mobile Interaction

A 4 × 4 card grid can become cramped on mobile.

### Mitigation

Design mobile interaction early rather than treating it as a final CSS adjustment.

---

## Risk 5: Drag and Drop Reliability

Traditional desktop drag-and-drop can behave poorly on touch devices.

### Mitigation

Consider a hybrid interaction model:

```text
Tap card
    ↓
Select card
    ↓
Tap destination
    ↓
Swap
```

while supporting drag-and-drop where appropriate.

---

## Risk 6: Puzzle Repetition

Because the complete solution space is finite, players may eventually encounter repeated structures.

### Mitigation

Use:

* Deterministic puzzle IDs
* Solution transformations
* Difficulty-specific pools
* Daily selection
* Puzzle history
* Future generated puzzle variants

---

# 39. Definition of Done

The project is complete when:

1. A fresh developer can install and run the project.
2. The application can generate or select valid puzzles.
3. The validator correctly evaluates all required constraints.
4. Easy correctly enforces values across rows and columns.
5. Normal correctly enforces values and suits across rows and columns.
6. Hard correctly enforces values and suits across rows, columns and diagonals.
7. Expert correctly applies its additional restrictions.
8. Players can manipulate cards naturally.
9. Players can complete a puzzle without technical errors.
10. Scores are calculated deterministically.
11. The game works on desktop and mobile.
12. The known mathematical solution passes regression tests.
13. Invalid arrangements are correctly rejected.
14. The production build works.
15. The game can be deployed publicly.

---

# 40. Immediate Next Steps

## Priority 1: Repository and Flask Project Setup

Create the project repository and establish the development environment:

```text
Python

Flask

Virtual Environment

pytest

HTML5

CSS

Vanilla JavaScript

Git
```

### Deliverables

* [X] Create GitHub repository
* [X] Create Python virtual environment
* [X] Create Flask application factory
* [X] Create initial project structure
* [X] Configure Flask development environment
* [X] Configure pytest
* [X] Create `.gitignore`
* [X] Create `requirements.txt`
* [X] Create `.env.example`
* [X] Create initial README
* [X] Create base Jinja2 template
* [X] Configure static CSS and JavaScript
* [X] Create initial home page
* [X] Verify Flask development server
* [X] Verify test suite
* [X] Create initial Git commit

### Expected Structure

```text
cards-in-a-square/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   │
│   ├── game/
│   │   ├── cards.py
│   │   ├── board.py
│   │   ├── rules.py
│   │   ├── validator.py
│   │   ├── solver.py
│   │   ├── generator.py
│   │   ├── difficulty.py
│   │   ├── scoring.py
│   │   └── hints.py
│   │
│   ├── templates/
│   │   └── base.html
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       └── assets/
│
├── tests/
│   └── game/
│
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
└── README.md
```

### Exit Criteria

The repository should be able to:

1. Create and activate the development environment.
2. Start the Flask application.
3. Render the initial page.
4. Load CSS and JavaScript assets.
5. Run the test suite successfully.
6. Provide a clean foundation for implementing the game engine.

---

## Priority 2: Implement the Card Domain Model

Before building the playable interface, implement the fundamental card system.

### Deliverables

* [X] Define card values
* [X] Define card suits
* [X] Define `Card`
* [X] Generate the complete 16-card set
* [X] Verify card uniqueness
* [X] Implement card lookup
* [X] Write unit tests

### Exit Criteria

The application can reliably represent the complete:

```text
4 Values × 4 Suits = 16 Cards
```

---

## Priority 3: Implement the Board Model

Create the representation of the 4 × 4 puzzle board.

### Deliverables

* [X] Define board structure
* [X] Define board positions
* [X] Implement card placement
* [X] Implement card movement/swapping
* [X] Implement board cloning
* [X] Implement board serialization
* [X] Write board tests

### Exit Criteria

The game engine can create, modify, copy and inspect a 4 × 4 board without involving Flask or the browser.

---

## Priority 4: Implement the Puzzle Rules and Validator

Build the mathematical rules independently from the UI.

The validator must eventually support:

```text
Rows
Columns
Main diagonal
Anti-diagonal
Values
Suits
```

The validator should be able to determine independently whether:

```text
Value constraints → valid/invalid

Suit constraints → valid/invalid

Diagonal constraints → valid/invalid

Complete board → solved/unsolved
```

### Exit Criteria

A known valid arrangement, including the previously verified solution, passes every applicable rule.

Invalid arrangements fail for the correct reason.

---

## Priority 5: Implement the Solver and Solution Verification

Use the known valid solution:

```text
QD AC JH KS
JS KH QC AD
KC JD AS QH
AH QS KD JC
```

and independently verify:

* All rows
* All columns
* Main diagonal
* Anti-diagonal
* Values
* Suits

Only after these five phases are stable should substantial UI development begin.


Before generating playable puzzles, build a reliable solver.

The solver should allow us to verify:

* [ ] A board has a solution
* [ ] A board has multiple solutions
* [ ] A board has a unique solution
* [ ] The number of solutions for a defined rule set
* [ ] The known 1,152 full arrangements
* [ ] The reduced rule-space counts where applicable

This is particularly important because **the game should never generate an unsolvable puzzle accidentally**.

### Exit Criteria

The solver can independently verify the mathematical claims made in the Game Design Document.

**---

## Priority 6: Implement Puzzle Generation

Once the solver and validator are trustworthy, build the puzzle generator.

The generator should support:

```text
Generate valid solution
        ↓
Transform / scramble solution
        ↓
Create playable starting position
        ↓
Verify solvability
        ↓
Verify intended difficulty
```

### Exit Criteria

The system can reliably produce playable boards for the initial difficulty levels.

---

## Priority 7: Build the Playable Game Interface

Only after the underlying game engine is reliable should we build the main interactive UI.

Implement:

* [ ] 4 × 4 board
* [ ] Card rendering
* [ ] Card selection
* [ ] Card swapping/movement
* [ ] Reset
* [ ] Move counter
* [ ] Timer
* [ ] Completion detection
* [ ] Basic conflict feedback

### Exit Criteria

A player can open the website and actually play a complete puzzle from start to finish.

---

## Priority 8: Implement Difficulty Modes

Implement the defined progression:

```text
Easy
↓
Rows + Columns
Values only

Normal
↓
Rows + Columns
Values + Suits

Hard
↓
Rows + Columns + Diagonals
Values + Suits

Expert
↓
Face-down cards
Limited moves
Limited hints
Timer
Reduced feedback
```

Each difficulty should be represented as configuration rather than duplicated game logic.

For example:

```text
Difficulty
├── constraints
├── diagonal rules
├── suit rules
├── hidden cards
├── move limit
├── hint limit
├── time limit
└── feedback level
```

---

## Priority 9: Scoring, Hints and Game Feedback

Implement the systems that make the puzzle feel like a game rather than simply a validator.

### Deliverables

* [ ] Scoring
* [ ] Move penalties
* [ ] Time scoring
* [ ] Hint system
* [ ] Hint penalties
* [ ] Victory screen
* [ ] Failure state
* [ ] Difficulty summary
* [ ] Performance statistics

---

## Priority 10: Testing and Mathematical Verification

Before deployment, independently verify:

```text
Card model
       ↓
Board model
       ↓
Rules
       ↓
Validator
       ↓
Solver
       ↓
Generator
       ↓
Difficulty
       ↓
Scoring
       ↓
Playable game
```

Particular attention should be given to the mathematical claims about the solution space.

We should **not treat the previously stated 1,152, 6,912, or 191,102,976 figures as axioms simply because they were calculated previously**. The implementation should independently reproduce and verify those counts.

That gives us a much stronger foundation for the game.

---

### Recommended immediate action

So the very next development session should **not** be "build the card UI."

It should be:

```text
Repository
   ↓
Flask foundation
   ↓
Card model
   ↓
Board model
   ↓
Rules
   ↓
Validator
```

Once those are correct, we can build the solver and generator with confidence.

---

# 41. Document Maintenance Rules

Update this document whenever:

* A phase is completed.
* A milestone is completed.
* A technical decision changes.
* The architecture changes.
* A game mechanic changes.
* A bug reveals an important implementation lesson.
* A dependency is introduced.
* A testing strategy changes.
* The next recommended action changes.

Do not rewrite completed development history merely to make the roadmap appear cleaner.

This document is intended to preserve the actual development process.

---

# 42. Current Project State

The game design is complete.

The mathematical rules are defined.

A complete valid solution has been verified.

The difficulty system has been defined:

```text
Easy
    ↓
Normal
    ↓
Hard
    ↓
Expert
```

The implementation has not yet begun.

The next development milestone is:

```text
Phase 1: Project Foundation
```

followed immediately by:

```text
Phase 2: Card Domain Model
Phase 3: Board Model
Phase 4: Constraint Engine
```

The first major technical milestone is therefore:

> **Build a UI-independent puzzle engine that can prove whether any 4 × 4 arrangement is valid.**
