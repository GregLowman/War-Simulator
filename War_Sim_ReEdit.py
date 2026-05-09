"""War simulation re-edit: fighter classes backed by SQLite, early refactor stage."""
import random, sqlite3, tkinter

db = sqlite3.connect("WarSimulation.sqlite")
db.execute('CREATE TABLE IF NOT EXISTS players (id TEXT PRIMARY KEY NOT NULL,'
           ' name TEXT NOT NULL, kills INTEGER NOT NULL, alive BOOL NOT NULL)')


class Fighters:
    def __init__(self, name: str, health: int, class_type: str):
        self.name = name
        self.health = health
        self.class_type = class_type
        self.alive = True
        print(f"New player: {self.name}, a {class_type} with {self.health} health")

    def take_damage(self, damage, name):
        if self.health > damage:
            self.health -= damage
            if self.health <= 10:
                print(f"{self.name} is about to die")

        else:
            self.health = 0
            print(f"{self.name} has died in the battlefield.")
            self.alive = 0

    @staticmethod
    def choice():
        return random.randint(1, 3)
