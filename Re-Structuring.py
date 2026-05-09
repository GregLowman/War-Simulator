"""Ninja fighter class prototype: early draft of the war simulation Ninja subclass."""
import random

names_list = []

with open("Names.txt", 'r') as character_names:
    for person in character_names:
        names_list.append(person)


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


class Ninja(Fighters):

    def __init__(self, name):
        health = random.randint(75, 100)
        super().__init__(name=name, health=health, class_type='Ninja')

    def dodge(self):
        if random.randint(1, 3) == 2:
            print(f"{self.name} has dodged an attack")
            return True
        else:
            return False

    def take_damage(self, damage, name):
        if not self.dodge():
            super().take_damage(damage=damage, name=name)
            if self.alive == 0:
                ninja_list.remove(name)
                self.alive = False

    def attack(self):
        choice = super().choice()
        ninja_star = 25
        baton = 10
        punch = 5

        if choice == 1:
            return punch
        elif choice == 2:
            return baton
        else:
            return ninja_star
