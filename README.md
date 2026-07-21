# VORREX

A turn-based combat RPG engine built in Python, featuring energy-managed attacks, AI-driven opponents, and JSON-based save persistence.

## Overview

VORREX started as a single-file combat loop prototype and evolved into a modular, multi-file architecture. It's currently being rebuilt with a tkinter GUI (v4.0), moving from a CLI-only experience to a full graphical interface.

## Features

- Turn-based combat system with energy management (power attacks, freeze abilities, etc.)
- AI-controlled opponents
- JSON-based save/load system
- Modular architecture — game logic split across dedicated modules (player, engine, AI, beast/enemy logic)
- **Classic Mode** — original terminal combat logic
- **Arena Mode** *(planned)* — custom enemy selection, unlockable characters via in-game currency

## Tech Stack

- Python 3
- tkinter (GUI, v4.0+)
- JSON (persistence)

## Project Structure