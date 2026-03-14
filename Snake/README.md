# 🐍 Snake Console Game

A simple **console-based Snake game written in Python**.
The game runs in the terminal and allows the player to control the snake using text commands.

This project focuses on **clean structure and object-oriented design**, separating the game into multiple components such as the board, game logic, and user interface.

---

## 🎮 Game Features

* Terminal-based Snake game
* Customizable board size and number of apples
* Apples spawn randomly on the board
* Apples cannot spawn next to each other
* Snake grows when eating an apple
* Collision detection:

  * ❌ hitting the wall
  * ❌ hitting itself
* Prevents **180° direction changes**
* Move multiple steps with one command

---

## 🕹️ Commands

| Command  | Description                |
| -------- | -------------------------- |
| `move`   | Move the snake one step    |
| `move n` | Move the snake **n steps** |
| `left`   | Change direction to left   |
| `right`  | Change direction to right  |
| `up`     | Change direction upward    |
| `down`   | Change direction downward  |

Example:

```
move
move 3
left
```

---

## ⚙️ Configuration

Game settings are stored in **`settings.txt`**.

Example:

```
10
5
```

Where:

* `10` = board size (10x10)
* `5` = number of apples placed initially

---

## 🧩 Symbols on the Board

| Symbol | Meaning     |
| ------ | ----------- |
| `*`    | Snake head  |
| `+`    | Snake body  |
| `a`    | Apple       |
| ` `    | Empty space |

---

## 📚 Things practiced in this project

* Object-Oriented Programming in Python
* Separation of concerns
* Basic game logic implementation
* Terminal UI design
* File-based configuration

---
