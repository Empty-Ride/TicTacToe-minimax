# Unbeatable Tic-Tac-Toe AI

A desktop Tic-Tac-Toe game built with Python and Pygame, featuring an unbeatable AI engine powered by the Minimax algorithm.

## Features
- **Unbeatable AI:** Uses recursive Minimax optimization with depth-penalized scoring to always make the perfect move.
- **Decoupled OOP Architecture:** Strict separation of concerns across Game Logic (Model), Graphics/UI (View), and the AI Decision Engine (Controller).
- **Pygame Graphical Interface:** Smooth rendering of grid systems, visual markers, and game-over conditions.

## How to Play
1. Run `main.py`.
2. Click any empty cell to place your marker.
3. The AI will instantly counter-move.

## Project Structure
- `main.py` - Core execution loop and event controller.
- `board.py` - Encapsulated grid state and win-checking business logic.
- `engine.py` - Minimax optimization engine.
- `graphics.py` - Pygame text rendering and grid visualization.