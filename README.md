# War Simulation

A turn-based fantasy war simulator built with Python. Players configure armies through a Tkinter GUI, watch randomized combat play out between five fighter classes, and review a post-battle leaderboard backed by a SQLite database.

>Development on this project predated version control — only the final version is included here.

## Features

- **Army builder GUI** — select any combination of five fighter classes and set army size before the battle begins
- **Five fighter classes** — each with unique health ranges, dodge probabilities, and attack moves:

| Class | Health | Dodge Chance | Attacks |
|-------|--------|--------------|---------|
| Ninja | 75–100 | 1 in 3 | Punch, Baton, Ninja Star |
| Knight | 110–150 | 1 in 10 | Bash, Slash, Stab |
| Ork | 150–200 | 1 in 25 | Slam, Bludgeon, Stomp |
| Wizard | 65–80 | 1 in 8 | Ice, Electric, Fire |
| Werewolf | 125–175 | 1 in 7 | Claw, Bite, Pounce |

- **Combat loop** — randomly selects an attacker and defender from opposing classes each round; combat continues until only one class remains
- **Kill tracking** — every fighter's kill count is recorded throughout the battle
- **MVP calculation** — identifies the fighter with the most kills at battle's end
- **SQLite persistence** — every fighter's name, kill count, and alive status is written to `WarSimulation.sqlite` after the battle
- **Leaderboard window** — a second Tkinter window opens post-battle displaying the MVP

## Object-Oriented Design

The project is built around a `Fighters` base class that defines shared attributes (`name`, `health`, `class_type`, `alive`) and shared behavior (`take_damage`, `choice`). Each of the five fighter subclasses overrides `dodge()`, `take_damage()`, and `attack()` to implement class-specific combat behavior, demonstrating inheritance, polymorphism, and encapsulation.

## Files

| File | Description |
|------|-------------|
| `War_Sim_Virtual.py` | Complete simulation: fighter classes, combat loop, Tkinter GUI, and leaderboard |
| `Names.txt` | Pool of names randomly assigned to fighters on army generation |
| `DB_Check.py` | Utility script to print all rows from the WarSimulation SQLite table |

## Requirements

- Python 3.x
- `tkinter` (included with standard Python)
- `sqlite3` (included with standard Python)

## Usage

```bash
python War_Sim_Virtual.py
```

1. Select which armies to include using the checkboxes
2. Enter an army size and click **Set Size**
3. Click **Generate Army** to populate fighters
4. Click **Start War** to run the simulation
5. The leaderboard window opens automatically when the battle ends
