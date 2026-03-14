# 🚀 Stellar Journey

**Stellar Journey** is a small terminal-based strategy game written in **Python**.

You control a spaceship navigating through a sector of space filled with **stars** and hidden **Blingon enemy ships**. Your goal is to eliminate all enemy ships while avoiding obstacles and dangerous warp destinations.

The game is played entirely in the terminal using simple text commands.

---

## 🎮 How the Game Works

The game takes place on an **8x8 grid** representing a sector of space.

At the start of the game:

- 🚀 1 player ship is placed randomly
- ⭐ 10 stars are placed randomly
- 👾 3 Blingon enemy ships are placed randomly

The player's mission is to **destroy all enemy ships**.

However, the player cannot see the entire board.

### What the Player Can See

The visible board only shows:

- ⭐ Stars
- 🚀 Your ship
- 👾 Enemy ships that are **adjacent to your ship**

Enemy ships that are farther away remain hidden.

---

## 🕹️ Commands

| Command | Description |
|-------|-------------|
| `warp <coordinate>` | Move your ship |
| `fire <coordinate>` | Fire at an adjacent sector |
| `cheat` | Reveal the full board |

Example commands:

```
warp B4
fire C5
cheat
```

---

## 🧭 Movement Rules

Your ship can **warp** to another coordinate only if it is:

- on the same **row**
- on the same **column**
- on the same **diagonal**

Warping is **not allowed** if a **star blocks the path**.

If you warp onto a sector containing an enemy ship, the game ends immediately.

---

## 💥 Combat

You can fire only at sectors **adjacent to your ship**.

If an enemy ship is located there:

- the enemy ship is destroyed
- remaining enemy ships are **randomly repositioned**

Destroy all enemy ships to **win the game**.

---

## 🧩 Board Symbols

| Symbol | Meaning |
|------|--------|
| `E` | Player ship |
| `B` | Blingon enemy ship |
| `*` | Star |
| ` ` | Empty space |

---

## 🧠 Concepts Practiced

This project explores:

- Basic object-oriented programming in Python
- Separating board logic, game logic, and UI
- Grid-based movement systems
- Random object placement
- Command-based terminal interaction
- Simple unit testing with `unittest`

---
