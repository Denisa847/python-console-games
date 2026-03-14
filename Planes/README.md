# ✈️ Planes Battle Game

A console-based strategy game written in **Python** where the player battles a computer opponent by locating and destroying hidden planes on a grid.

This project demonstrates **object-oriented programming**, a **modular project structure**, a **basic AI opponent**, and **unit testing**.

---

## 🎮 Game Overview

The game takes place on a **10×10 grid** where both the player and the computer have **three hidden planes** placed randomly.

Each turn follows this sequence:

1. The player enters a coordinate to attack.
2. The system determines whether the attack is a **hit**, **miss**, or **destroys a plane**.
3. The computer takes its turn using a simple AI strategy.

The game continues until **all planes from one side are destroyed**.

---

## ✨ Features

- Human vs Computer gameplay
- Hidden plane placement on a grid
- Basic AI opponent
- Console interface for user interaction
- Input validation and error handling
- Unit tests using `unittest`
- Modular and maintainable project structure

---

## 🧩 Game Rules

- The board size is **10 × 10**.
- Each side has **3 planes**.
- A plane occupies **3 connected cells** (horizontal or vertical).
- Players attack by entering coordinates:
