# 🎮 Obstruction Game in Python

A console-based implementation of the **Obstruction** game written in **Python**.

This project was built using **object-oriented programming** and includes a playable terminal interface, a basic AI opponent, custom exceptions, and unit tests.

---

## 🧠 Overview

**Obstruction** is a two-player strategy game played on a square grid.

In this version, a human player competes against the computer.  
On each turn, a player places a marker on an empty cell. Once a marker is placed, all surrounding empty cells become **blocked**, making them unavailable for future moves.

The game continues until no valid moves remain.

The player who makes the **last possible move wins**.

---

## ✨ Features

- Human vs Computer gameplay
- Grid-based blocking mechanics
- Basic AI opponent that:
  - searches for winning moves
  - blocks the opponent’s winning moves
  - selects a random valid move when no better option exists
- Custom exception handling
- Unit tests with `unittest`
- Console board rendering with `texttable`
- Colored terminal output with `colorama`

---

## 🎯 Game Rules

- The board starts empty
- Players take turns placing a marker
- When a marker is placed, all surrounding empty cells become blocked
- Blocked cells cannot be used
- The player who makes the last valid move wins

