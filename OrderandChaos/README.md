# 🎮 Order & Chaos

**Order & Chaos** is a terminal-based strategy game written in **Python**.

Two opposing forces battle on a **6×6 board**:

- **Order** tries to create **five identical symbols in a row**
- **Chaos** tries to **prevent this until the board is full**

The game is played entirely in the **terminal**, where the player places pieces while the computer responds with its own moves.

---

## 🎯 Game Objective

The game is played on a **6×6 grid**.

Each turn, a player can place either:

- `X`
- `O`

Unlike games like Tic-Tac-Toe, players are **not restricted to one symbol**.

### Order Wins

Order wins if **five identical symbols appear consecutively**:

- horizontally
- vertically
- diagonally

### Chaos Wins

Chaos wins if the **board becomes full without any five-in-a-row sequence**.

---

## 🕹️ How to Play

When the game starts, an empty board is displayed.

Each turn the player enters:

- piece (`X` or `O`)
- row
- column

The computer will then automatically make its move.

The game continues until either **Order wins** or **Chaos wins**.

---

## 🤖 Computer Strategy

The computer opponent follows a simple decision strategy:

1. Check if there is an **immediate winning move**
2. Choose the symbol (`X` or `O`) that keeps the board balanced
3. Place the piece in a position with the **most neighboring matching symbols**
4. If no strategic position exists, place randomly

---

## 🧩 Board Symbols

| Symbol | Meaning |
|------|--------|
| `X` | X piece |
| `O` | O piece |
| ` ` | Empty space |

---

## 🧠 Concepts Practiced

This project explores several programming concepts:

- Object-Oriented Programming in Python
- Separation of concerns (Board / Controller / UI)
- Grid-based game logic
- Simple AI decision making
- Input validation
- Unit testing with `unittest`
