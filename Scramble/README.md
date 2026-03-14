# 🔤 Sentence Scramble Game

A small **terminal-based word puzzle game written in Python**.

The game selects a random sentence from a file and **scrambles the middle letters of the words**.
Your goal is to restore the original sentence by swapping letters.

Each swap costs **one point**, so try to solve the puzzle before your score reaches **zero**.

---

# 🎮 How the Game Works

1. The game loads a **random sentence** from a file.
2. The sentence is **scrambled**:

   * The **first and last letter of each word stay the same**
   * The **middle letters are shuffled**
3. The player restores the sentence using **letter swaps**.
4. Every swap **reduces the score by 1**.
5. The game ends when:

   * ✅ The sentence is solved
   * ❌ The score reaches **0**

---

# 🧠 Example

Original sentence:

```text
hello world
```

Scrambled sentence:

```text
hlleo wrold
```

Player command:

```text
swap 0 1 - 1 2
```

Meaning:

```
swap letter 1 of word 0
with letter 2 of word 1
```

---

# 🕹️ Commands

| Command              | Description      |
| -------------------- | ---------------- |
| `swap w1 l1 - w2 l2` | Swap two letters |
| `exit`               | Quit the game    |

Example:

```text
swap 0 1 - 2 3
```

Notes:

* **Word indexing starts at 0**
* **Letter indexing starts at 0**
* **First and last letters cannot be swapped**

---

# 🧩 Concepts Practiced

This small project explores:

* Basic object-oriented programming in Python
* Separating logic into multiple components
* Simple string manipulation
* File input for loading data
* Command-based terminal interaction
* Unit testing with unittest

---
