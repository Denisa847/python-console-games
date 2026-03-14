🎮 Obstruction Game in Python

A simple console-based Obstruction Game built in Python using object-oriented design, custom exceptions, a basic AI opponent, and unit tests.

🧠 Overview

This project is a playable implementation of the Obstruction board game where a human player competes against the computer on a square grid.

Each move places a marker on the board and blocks the surrounding cells, reducing the available space for future moves.

The player who makes the last possible move wins.

✨ Features

Human vs Computer gameplay

Board blocking mechanics

Basic AI opponent that:

searches for winning moves

blocks opponent winning moves

selects a random valid move when no better option exists

Custom exception handling

Unit tests using unittest

Console board rendering using texttable

Colored console output using colorama

🎯 Rules

The board starts empty.

Players take turns placing a marker.

When a marker is placed, all surrounding empty cells become blocked.

Blocked cells cannot be played.

The player who makes the last valid move wins.