# Tic-Tac-Toe — Alpha-Beta Pruning AI

A terminal-based Tic-Tac-Toe game where you play against an **unbeatable AI** powered by the **Alpha-Beta Pruning** search algorithm.

---

## What is Alpha-Beta Pruning?

Alpha-Beta Pruning is an optimization of the **Minimax** algorithm used in two-player zero-sum games. It explores the game tree to find the optimal move, but **skips branches that cannot possibly affect the final decision** — making it significantly faster than plain Minimax.

### Core Idea

```
         [AI's turn — Maximize]
              /       \
         [Move A]   [Move B]
         score=7    α=7, so if Move B's
                    subtree has any node ≤ 7
                    → PRUNE the rest
```

Two values are tracked throughout the search:

| Variable | Meaning |
|----------|---------|
| **α (alpha)** | Best score the AI (maximizer) is guaranteed so far |
| **β (beta)**  | Best score the Human (minimizer) is guaranteed so far |

**Pruning condition:** If `β ≤ α`, the current branch is irrelevant and gets cut off.

### Why it works

- The AI always assumes the **human plays optimally** (minimizes AI's score)
- The human always assumes the **AI plays optimally** (maximizes its score)
- Any branch that can't beat the already-found best option is skipped entirely
- Result: **same optimal move** as Minimax, but explored much faster

---

## Project Structure

```
tictactoe_alpha_beta/
│
├── tictactoe.py     # Main game — all logic here
└── README.md        # This file
```

---

## How to Run

### Requirements
- Python 3.x (no external libraries needed)

### Basic run (you go first)
```bash
python tictactoe.py
```

### Verbose mode (see AI's move evaluations)
```bash
python tictactoe.py --verbose
# or
python tictactoe.py -v
```

---

## Gameplay

```
============================================
   Tic-Tac-Toe  —  Alpha-Beta Pruning AI
============================================
  You are O  |  AI is X

  Board positions:
   0 | 1 | 2
  ---+---+---
   3 | 4 | 5
  ---+---+---
   6 | 7 | 8

   X |   |
  ---+---+---
     | O |
  ---+---+---
     |   |

  Available: [1, 2, 3, 5, 6, 7, 8]
  Your move (0-8): _
```

---

## Code Overview

### Functions

| Function | Description |
|----------|-------------|
| `create_board()` | Returns empty 9-cell board |
| `print_board(board)` | Pretty-prints the board |
| `get_available_moves(board)` | Returns list of empty positions |
| `check_winner(board, player)` | Checks all 8 win conditions |
| `is_terminal(board)` | Returns True if game is over |
| `evaluate(board)` | Returns +10 (AI wins), -10 (Human wins), 0 (draw) |
| `alpha_beta(...)` | Core recursive Alpha-Beta algorithm |
| `best_move(board, verbose)` | Calls alpha_beta for each move, returns best position |
| `play(verbose_ai)` | Main game loop |

### Algorithm Flow

```
best_move()
    └── for each available move:
            place 'X' on board
            call alpha_beta(is_maximizing=False)  ← Human's hypothetical response
                └── for each human move:
                        place 'O' on board
                        call alpha_beta(is_maximizing=True)  ← AI responds
                            └── ... recurse until terminal state
                        if β ≤ α → PRUNE (break)
            undo move
    └── return move with highest score
```

---

## Why the AI Never Loses

Tic-Tac-Toe is a **solved game**. With perfect play:
- If both players play optimally → **always a draw**
- The AI explores the **entire game tree** and always picks the move with the best guaranteed outcome
- Best case for you: **draw** (if you also play perfectly)

---

## Example: Verbose Output

```
  AI is thinking...
  [AI evaluating moves...]
  Position 0 → score: 0
  Position 2 → score: 0
  Position 4 → score: 10
  Position 6 → score: 0
  → AI picks position 4
```

The AI correctly prioritizes the **center (position 4)** as the strongest opening move.

---

## Concepts Demonstrated

- **Game tree search**
- **Minimax algorithm** (base concept)
- **Alpha-Beta pruning** (optimization)
- **Terminal state detection**
- **Heuristic evaluation function**

---
