# VORREX

A turn-based combat RPG engine built in Python, featuring energy-managed attacks, AI-driven opponents, and JSON-based save persistence.

## Overview

VORREX started as a single-file combat loop prototype and evolved into a modular, multi-file architecture. It has since been rebuilt with a tkinter GUI (v4.0), moving from a CLI-only experience to a full graphical interface with live HP bars and real-time combat feedback.

## Current Version — v4.0

The latest version replaces the terminal interface entirely with a tkinter GUI.

- Classic Mode — Normal Attack and Power Attack, fully wired to the original combat engine
- Live HP bars for both player and enemy, updating in real time
- Floating damage popups on hit
- Win/loss detection with a results screen
- XP and level progress saved automatically to `save.json`

Arena Mode and Beast Battle mode, along with Defense and Freeze Attack, were scoped out of v4.0 to ship a focused, fully working Classic mode first. They're planned for v4.1+.

## Version History

| Version | Interface | Highlights |
|---------|-----------|------------|
| v3.1 | Terminal (CLI) | Full OOP refactor, 5-file modular split (player, beast, engine, ai, main), JSON save system |
| v4.0 | tkinter GUI | Full graphical rebuild, Classic mode, live HP bars, damage popups |

## Features

- Turn-based combat system with energy management (power attacks, freeze abilities, etc.)
- AI-controlled opponents that adapt behavior based on health and energy thresholds
- JSON-based save/load system for level and XP persistence
- Modular architecture — game logic split across dedicated modules (player, engine, AI, beast/enemy logic)
- **Classic Mode** — core combat loop, playable start to finish
- **Arena Mode** *(planned)* — custom enemy selection, unlockable characters via in-game currency
- **Beast Battle Mode** *(planned)*

## Tech Stack

- Python 3
- tkinter (GUI, v4.0+)
- JSON (persistence)

## Project Structure

```
vorrex/
├── v3.1/
│   ├── main.py
│   ├── engine.py
│   ├── beast.py
│   ├── player.py
│   ├── ai.py
│   └── save.json
├── v4.0/
│   ├── main.py
│   ├── main_window.py
│   ├── engine.py
│   ├── beast.py
│   ├── player.py
│   ├── ai.py
│   └── save.json
└── README.md
```

## How to Run

**v4.0 (GUI):**
```
cd v4.0
python main.py
```

**v3.1 (Terminal):**
```
cd v3.1
python main.py
```

## Concepts Practiced

OOP and class design, modular file architecture, JSON persistence, tkinter GUI development (widgets, `.place()` layout, `.after()` for non-blocking timing, Canvas for HP bars), state management across GUI screens, and basic game AI decision trees.

## License

MIT
