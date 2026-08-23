# Cards in a Square

A logic puzzle game where players arrange 16 playing cards into a 4 × 4 square while satisfying a set of increasingly difficult constraints.

The game combines the structure of a Latin square with playing-card values and suits, creating a puzzle that is simple to understand but increasingly difficult to solve.

---

## Overview

Cards in a Square uses the following 16 cards:

- Ace
- Jack
- Queen
- King

Across the four suits:

- ♥ Heart
- ♠ Spade
- ♦ Diamond
- ♣ Club

Each card appears exactly once.

The player's objective is to arrange all 16 cards into a 4 × 4 grid according to the rules of the selected difficulty.

---

## Core Objective

The primary objective is to correctly arrange the cards in the 4 × 4 grid.

Depending on the difficulty, each row, column, and eventually both diagonals must contain:

- One Ace
- One Jack
- One Queen
- One King

The harder modes additionally require:

- One Heart
- One Spade
- One Diamond
- One Club

The suit condition is an additional challenge. The fundamental puzzle is the arrangement of the card values.

---

## Difficulty System

### Easy

**Rules**

- Rows must contain A, J, Q, K
- Columns must contain A, J, Q, K
- Suits are ignored
- Diagonals are ignored

The focus is entirely on arranging the card values.

---

### Normal

**Rules**

- Rows must contain A, J, Q, K
- Columns must contain A, J, Q, K
- Rows must contain all four suits
- Columns must contain all four suits
- Diagonals are ignored

Players must now consider both card value and suit.

---

### Hard

**Rules**

- Rows must contain A, J, Q, K
- Columns must contain A, J, Q, K
- Both diagonals must contain A, J, Q, K
- Rows must contain all four suits
- Columns must contain all four suits
- Both diagonals must contain all four suits

This is the complete core puzzle.

---

### Expert

Expert builds on the Hard rules with additional gameplay restrictions.

Possible mechanics include:

- Some cards begin face down
- Limited moves
- Limited hints
- Timer
- Reduced conflict feedback
- No immediate conflict highlighting

The exact Expert configuration may evolve during development.

---

## Example Valid Hard Solution

One known valid arrangement is:

|  |  |  |  |
|---|---|---|---|
| Q♦ | A♣ | J♥ | K♠ |
| J♠ | K♥ | Q♣ | A♦ |
| K♣ | J♦ | A♠ | Q♥ |
| A♥ | Q♠ | K♦ | J♣ |

### Main diagonal

```text
Q♦ → K♥ → A♠ → J♣
````

Values:

```text
Q, K, A, J
```

Suits:

```text
♦, ♥, ♠, ♣
```

### Anti-diagonal

```text
K♠ → Q♣ → J♦ → A♥
```

Values:

```text
K, Q, J, A
```

Suits:

```text
♠, ♣, ♦, ♥
```

Both diagonals therefore satisfy the complete Hard-mode constraints.

---

## Mathematical Structure

The puzzle has an interesting combinatorial structure.

Under the complete rules, there are multiple valid arrangements rather than a single predetermined solution.

The current design research identifies:

```text
144 structurally distinct fundamental solutions
```

When the eight physical symmetries of the square are considered:

```text
144 × 8 = 1,152
```

This gives:

```text
1,152 valid card arrangements
```

For comparison, removing the diagonal constraints produces a substantially larger solution space:

```text
6,912 valid arrangements
```

When the suit and diagonal constraints are removed, the search space becomes dramatically larger.

The current mathematical analysis identifies:

```text
576 value grids
×
331,776 suit variations
=
191,102,976 arrangements
```

These figures are treated as **implementation hypotheses that must be independently verified by the project's solver and test suite**.

The game should never rely on an unverified mathematical assumption.

---

# Game Design

The game is designed around a simple principle:

> Easy to understand, difficult to master.

The player should immediately understand what the objective is without needing to understand the underlying mathematics.

The difficulty should come from the interaction between:

* Card values
* Card suits
* Board positions
* Diagonal constraints
* Limited information
* Limited resources

The game should remain accessible while allowing increasingly challenging gameplay.

---

# Technology Stack

## Backend

* Python
* Flask
* Jinja2

## Game Engine

* Python
* Dataclasses
* Dedicated puzzle validation
* Dedicated solver
* Dedicated puzzle generator

## Frontend

* HTML5
* CSS
* Vanilla JavaScript

## Testing

* pytest
* Flask test client

## Database

No database is required for the initial MVP.

SQLite may be introduced later if persistent features such as:

* Accounts
* Leaderboards
* Statistics
* Saved games
* Daily puzzles

are implemented.

## Deployment

The application is intended to be deployable as a Flask application.

Docker may be used for reproducible deployment.

---

# Architecture

The project separates the game engine from the web interface.

```text
Browser
   │
   │ HTTP
   ▼
Flask Application
   │
   ├── Routes
   │
   └── Game Engine
          │
          ├── Cards
          ├── Board
          ├── Rules
          ├── Validator
          ├── Solver
          ├── Generator
          ├── Difficulty
          ├── Scoring
          └── Hints
```

The game engine should remain independent from Flask wherever practical.

This allows the mathematical puzzle logic to be:

* Tested independently
* Reused by different interfaces
* Verified without running the web application
* Extended without tightly coupling it to the frontend

---

# Project Structure

The planned structure is:

```text
cards-in-a-square/
│
├── app/
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
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
├── Dockerfile
└── README.md
```

---

# Development Roadmap

Development is divided into stages.

```text
Game Design
     ↓
Flask Foundation
     ↓
Card Model
     ↓
Board Model
     ↓
Rules
     ↓
Validator
     ↓
Solver
     ↓
Puzzle Generator
     ↓
Playable Interface
     ↓
Difficulty System
     ↓
Scoring & Hints
     ↓
Testing
     ↓
Deployment
```

The mathematical game engine should be developed before significant UI work.

This ensures that the interface is built around a verified game rather than the game logic being retrofitted into an existing interface.

---

# Current Development Status

| Component                 | Status                    |
| ------------------------- | ------------------------- |
| Game concept              | Complete                  |
| Core rules                | Complete                  |
| Card set                  | Complete                  |
| Difficulty design         | Complete                  |
| Mathematical analysis     | Initial analysis complete |
| Complete valid example    | Complete                  |
| Technology stack          | Complete                  |
| Project architecture      | Complete                  |
| Flask foundation          | Not started               |
| Card model                | Not started               |
| Board model               | Not started               |
| Validator                 | Not started               |
| Solver                    | Not started               |
| Generator                 | Not started               |
| Game interface            | Not started               |
| Difficulty implementation | Not started               |
| Scoring                   | Not started               |
| Hints                     | Not started               |
| Testing                   | Not started               |
| Deployment                | Not started               |

---

# Contributing

Contributions are welcome.

Cards in a Square is intended to be a collaborative project, and contributions can include:

* Game mechanics
* Puzzle mathematics
* Solver improvements
* Puzzle generation
* Frontend development
* UI/UX improvements
* Accessibility
* Testing
* Performance improvements
* Documentation
* Bug fixes
* New difficulty ideas
* New game modes

## Before Contributing

For significant changes, please open an issue first so the proposed change can be discussed before implementation.

This is especially important for changes involving:

* Core puzzle rules
* Difficulty
* Solver behaviour
* Puzzle generation
* Scoring
* Game architecture

Changes to the fundamental rules should not be introduced casually because they can affect the mathematical properties of the entire puzzle.

## Development Principles

Contributors should aim to:

1. Keep the game logic independent from Flask.
2. Write tests for important game logic.
3. Avoid unnecessary dependencies.
4. Keep the UI accessible and responsive.
5. Document significant architectural decisions.
6. Avoid introducing complexity without a clear benefit.
7. Verify mathematical claims through code.
8. Preserve backward compatibility where practical.

---

# Reporting Bugs

When reporting a bug, include:

* Description of the problem
* Steps to reproduce it
* Expected behaviour
* Actual behaviour
* Browser and operating system where relevant
* Python version
* Relevant error messages or logs

For puzzle-related bugs, include the board state if possible.

---

# Feature Requests

Feature requests are welcome.

Examples include:

* New difficulty modes
* Daily puzzles
* Alternative card designs
* Accessibility improvements
* Leaderboards
* Puzzle statistics
* New hint mechanics
* Additional game modes

Feature requests should explain the problem the feature solves rather than only describing the proposed implementation.

---

# Code of Conduct

Contributors are expected to:

* Be respectful
* Give constructive feedback
* Discuss ideas rather than individuals
* Accept technical disagreement professionally
* Keep discussions focused on improving the project

---

# License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for the full license text.

Copyright (c) 2026 Cards in a Square Contributors

---

# MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# Project Philosophy

Cards in a Square is more than a card-matching game.

The underlying puzzle has a rich mathematical structure, but the player should not need to understand that structure to enjoy the game.

The project therefore aims to combine:

```text
Mathematics
     +
Game Design
     +
Programming
     +
Visual Design
```

into a simple, accessible and replayable puzzle experience.

---

# Roadmap Documentation

The project maintains separate documentation for design and implementation.

> [01_Game_Design.md](/docs/01_Game_Design.md)


Defines:

> What is the game?

> [02_Developer_Roadmap.md](/docs/02_Developer_Roadmap.md)


Defines:

> How are we building it?

The roadmap should be updated as development progresses and should preserve important implementation decisions, problems and lessons learned.

---

# Getting Started

Development setup instructions will be added once the Flask foundation has been created.

The intended setup will be approximately:

```bash
git clone <repository-url>

cd cards-in-a-square

python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
flask --app app run --debug
```

Run tests:

```bash
pytest
```

Exact setup instructions may change as the project develops.

---

# Credits

Cards in a Square is an open collaboration between its contributors.

Contributors will be credited in the project documentation as the project develops.

---

## Status

**Early Development**

The game design is established and implementation is beginning with the Flask project foundation.

````
