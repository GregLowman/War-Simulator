"""War simulation: build five-class armies and run random turn-based combat."""
import random
import sqlite3
import tkinter

db = sqlite3.connect("WarSimulation.sqlite")
db.execute('CREATE TABLE IF NOT EXISTS players (id TEXT PRIMARY KEY NOT NULL,'
           ' name TEXT NOT NULL, kills INTEGER NOT NULL, alive BOOL NOT NULL)')

fighter_list = ['ninja', 'knight',
                'ork', 'wizard',
                'werewolf']

numbers = ['0123456789']
names_list = []

ninja_list = []
ninja_names = {}
knight_list = []
knight_names = {}
ork_list = []
ork_names = {}
wizard_list = []
wizard_names = {}
werewolf_list = []
werewolf_names = {}
battle_list = []
kills = {}
army_list = [ninja_names, knight_names,
             ork_names, wizard_names,
             werewolf_names]

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


class Knight(Fighters):
    def __init__(self, name):
        health = random.randint(110, 150)
        super().__init__(name=name, health=health, class_type='Knight')

    def dodge(self):
        if random.randint(1, 10) == 5:
            print(f"{self.name} has dodged an attack")
            return True
        else:
            return False

    def take_damage(self, damage, name):
        if not self.dodge():
            super().take_damage(damage=damage, name=name)
            if self.alive == 0:
                knight_list.remove(name)
                self.alive = False

    def attack(self):
        choice = super().choice()
        bash = 10
        slash = 20
        stab = 35

        if choice == 1:
            return bash
        if choice == 2:
            return slash
        if choice == 3:
            return stab


class Ork(Fighters):
    def __init__(self, name):
        health = random.randint(150, 200)
        super().__init__(name=name, health=health, class_type='Ork')

    def dodge(self):
        if random.randint(1, 25) == 15:
            print(f"{self.name} has dodged an attack")
            return True
        else:
            return False

    def take_damage(self, damage, name):
        if not self.dodge():
            super().take_damage(damage=damage, name=name)
            if self.alive == 0:
                ork_list.remove(name)
                self.alive = False

    def attack(self):
        choice = super().choice()
        slam = 25
        bludgeon = 35
        stomp = 50

        if choice == 1:
            return slam
        elif choice == 2:
            return bludgeon
        else:
            return stomp


class Wizard(Fighters):
    def __init__(self, name):
        health = random.randint(65, 80)
        super().__init__(name=name, health=health, class_type='Wizard')

    def dodge(self):
        if random.randint(1, 8) == 4:
            print(f"{self.name} has dodged an attack")
            return True
        else:
            return False

    def take_damage(self, damage, name):
        if not self.dodge():
            super().take_damage(damage=damage, name=name)
            if self.alive == 0:
                wizard_list.remove(name)
                self.alive = False

    def attack(self):
        choice = super().choice()
        electric = 20
        fire = 35
        ice = 10

        if choice == 1:
            return ice
        elif choice == 2:
            return electric
        else:
            return fire


class WereWolf(Fighters):
    def __init__(self, name):
        health = random.randint(125, 175)
        super().__init__(name=name, health=health, class_type='Werewolf')

    def dodge(self):
        if random.randint(1, 7):
            print(f'{self.name} has dodged an attack')
            return True
        else:
            return False

    def take_damage(self, damage, name):
        if not self.dodge():
            super().take_damage(damage=damage, name=name)
            if self.alive == 0:
                werewolf_list.remove(name)
                self.alive = False

    def attack(self):
        choice = super().choice()
        claw = 25
        bite = 30
        pounce = 40

        if choice == 1:
            return claw
        elif choice == 2:
            return bite
        else:
            return pounce


def name_gen():

    """
    Chooses a random name from 'names list'
    :return: name
    """
    name = random.choice(names_list)
    return name


def list_check():

    """
    Checks to see which fighter class has players.
    If a class has any fighters assigned to it, it will
    return an integer value. If no fighters are assigned
    it will return the class as 'None'

    Also checks to see how many classes are still 'alive'.
    Once 'score' is only 1, the 'war' will end.

    :return: ninja, knight, ork, wizard, werewolf, score
    """

    score = 0

    if (ninja_list == []) is False:
        ninja = 1
        score += 1
    else:
        ninja = None
        if 'ninja' in fighter_list:
            fighter_list.remove('ninja')
    if (knight_list == []) is False:
        knight = 2
        score += 1
    else:
        knight = None
        if 'knight' in fighter_list:
            fighter_list.remove('knight')
    if (ork_list == []) is False:
        ork = 3
        score += 1
    else:
        ork = None
        if 'ork' in fighter_list:
            fighter_list.remove('ork')
    if (wizard_list == []) is False:
        wizard = 4
        score += 1
    else:
        wizard = None
        if 'wizard' in fighter_list:
            fighter_list.remove('wizard')
    if (werewolf_list == []) is False:
        werewolf = 5
        score += 1
    else:
        werewolf = None
        if 'werewolf' in fighter_list:
            fighter_list.remove('werewolf')

    return ninja, knight, ork, wizard, werewolf, score


def choose_fighter():

    """
    Randomly chooses a class, then a fighter from that class.
    Identifies both the fighter and class type

    :return: fighter, fighter type
    """

    [a, b, c, d, e, x] = list_check()
    group = [a, b, c, d, e]
    control = True
    fighter = None
    while control:

        selection = random.choice(group)

        if selection == 1:
            fighter = random.choice(ninja_list)
            control = False
        elif selection == 2:
            fighter = random.choice(knight_list)
            control = False
        elif selection == 3:
            fighter = random.choice(ork_list)
            control = False
        elif selection == 4:
            fighter = random.choice(wizard_list)
            control = False
        elif selection == 5:
            fighter = random.choice(werewolf_list)
            control = False
        elif selection is None:
            pass
        else:
            pass
    return fighter, type(fighter)


def kill_count(fighter, fighter_class):

    """
    When a fighter attacks an enemy and that enemy dies,
    the fighter gains a point. This function is called
    once it is determined that an enemy has died.

    :param fighter: Fighter ID used as a key to log kills
    :param fighter_class: Class of the fighter, used as a key to log kills
    """

    fighter_id = fighter
    class_type = fighter_class
    name = None

    if class_type == 'Ninja':
        name = ninja_names[fighter_id]
    elif class_type == 'Knight':
        name = knight_names[fighter_id]
    elif class_type == 'Ork':
        name = ork_names[fighter_id]
    elif class_type == 'Wizard':
        name = wizard_names[fighter_id]
    elif class_type == 'Werewolf':
        name = werewolf_names[fighter_id]

    x = kills[(name, fighter_id)]
    x += 1
    kills[(name, fighter_id)] = x


def retrieve_damage():

    """
    Chooses a random fighter, and then a random attack from said fighter.

    :return: Int(Damage), Fighter Class, Fighter ID
    """

    fighter, fighter_type = choose_fighter()
    damage = int(fighter.attack())

    return damage, fighter_type, fighter


def score_board():

    """
    Creates a list of everyone in the war. Then uses
    that list to create a scoreboard. This function also
    adds (ID, Name, Kills, Alive Status) of every fighter
    into a database 'War Simulation'
    """

    for group in army_list:
        for key in group:
            battle_list.append(group[key])
    for group in army_list:
        for key in group:
            name = group[key]
            points = kills[(group[key], key)]
            life = key.alive
            fighter_id = key
            print(f"Name: {name} \t|\t 'Kills:'{points}"
                  f" \t|\t 'Alive:'{life}")
            db.execute("INSERT OR REPLACE INTO players (id, name, kills, alive)"
                       " VALUES('{}', '{}', {}, {})"
                       .format(fighter_id, name, points, life))
            db.commit()

    pass


def mvp():

    """
    Identifies the player with the most kills.
    Prints out who the MVP is along with the amount of kills they had.
    * Yet to determine when multiple fighters have the same most kills *
    """

    top = None
    points = 0
    lead = 0
    for group in kills:
        control = kills[group]

        if control >= lead:
            lead = control
            top = group[0]
            points = kills[group]
    print(f"The MVP is {top}, with {points}, kills")


def army():

    """
    Presents user with the option to decide how many fighters each
    class should have. Then prompts for input to decide which classes
    will have armies made for them. Once all inputs have been completed
    enemies will be generated for each selected class. Will not continue
    without valid input.
    """

    more = True
    control = True
    amount = None

    while control:
        try:
            print('How many fighters in each army?')
            amount = float(input())
            amount = (amount // 1)

            if amount.is_integer:
                amount = int(amount)
                control = False
            else:
                print("Please enter a valid number")

        except ValueError:
            print("Please enter a valid number.")

    while more:
        print("Select which armies to create: "
              "\n1. Ninja"
              "\n2. Knight"
              "\n3. Ork"
              "\n4. Wizard"
              "\n5. Werewolf"
              "\n6. End")
        selection = input(": ")

        if selection == '1':
            for num in range(0, amount):
                name = name_gen()

                ninja_list.append(name)
                ninja_list[num] = Ninja(name)

                ninja_names.setdefault(ninja_list[num], name)
                kills.setdefault((name, ninja_list[num]), 0)

        elif selection == '2':
            for num in range(0, amount):
                name = name_gen()

                knight_list.append(name)
                knight_list[num] = Knight(name)

                knight_names.setdefault(knight_list[num], name)
                kills.setdefault((name, knight_list[num]), 0)

        elif selection == '3':
            for num in range(0, amount):
                name = name_gen()

                ork_list.append(name)
                ork_list[num] = Ork(name)

                ork_names.setdefault(ork_list[num], name)
                kills.setdefault((name, ork_list[num]), 0)

        elif selection == '4':
            for num in range(0, amount):
                name = name_gen()

                wizard_list.append(name)
                wizard_list[num] = Wizard(name)

                wizard_names.setdefault(wizard_list[num], name)
                kills.setdefault((name, wizard_list[num]), 0)

        elif selection == '5':
            for num in range(0, amount):
                name = name_gen()

                werewolf_list.append(name)
                werewolf_list[num] = WereWolf(name)

                werewolf_names.setdefault(werewolf_list[num], name)
                kills.setdefault((name, werewolf_list[num]), 0)

        elif selection == '6':
            more = False

        else:
            print("Please Enter a Valid Option, 1 - 6")


def war():

    """
    Calls army function to assign players to the war.
    Chooses an attacker and which attack they will use. Assigns the
    damage, fighter ID and the fighter class.
    Then chooses which fighter will be getting attacked, and assigns
    the defender ID and their class.
    Determines if the defender has died, and if so assigns a point
    to the attacker.
    Once only one class of fighters is left, the war will end. Displaying
    a scoreboard and MVP.
    """

    army()
    input("Press Enter to Start War: ")
    battle = True
    winner = None

    while battle:
        attacker, attacker_type, fighter = retrieve_damage()
        defender, defender_type = choose_fighter()

        if attacker_type != defender_type:
            defender.take_damage(attacker, defender)

            if defender.alive == 0:
                kill_count(fighter, fighter.class_type)

        x, x, x, x, x, score = list_check()

        if score == 1:
            battle = False
            for name in fighter_list:
                winner = name
            print("The war is over")
            print(f"The winner is {winner}")
            input("Press Enter to Continue:")
            score_board()
            mvp()

####################################################################
# GUI Build

####################################################################
# Main Window


main_window = tkinter.Tk()
main_window.geometry('500x425+375+15')
main_window.configure(bg='grey69')

####################################################################
# Row / Column Configure

for i in range(0, 9):
    main_window.rowconfigure(i, weight=1)
    if i <= 5:
        main_window.columnconfigure(i, weight=1)

####################################################################
# Title / Title Frame

top_title = tkinter.LabelFrame(main_window)
top_title.grid(row=0, column=0, columnspan=7, sticky='news')

for i in range(0, 3):
    top_title.columnconfigure(i, weight=1)

title = tkinter.Label(top_title, text="War Simulator")
title.grid(column=1)

####################################################################
# Army / Fighters Frame

army_frame = tkinter.Frame(main_window)
army_frame.grid(column=0, row=1, columnspan=2, rowspan=5, sticky='news')

for i in range(0, 6):
    army_frame.rowconfigure(i, weight=1)

# Army Frame title

army_title = tkinter.Label(army_frame, text='Select Which Armies to Build')
army_title.grid(row=0)

# Army Buttons

ninja_button = tkinter.Checkbutton(army_frame, text="Ninja", state='normal')
ninja_button.grid(row=1, sticky='W')

knight_button = tkinter.Checkbutton(army_frame, text="Knight")
knight_button.grid(row=2, sticky='W')

ork_button = tkinter.Checkbutton(army_frame, text="Ork")
ork_button.grid(row=3, sticky='W')

wizard_button = tkinter.Checkbutton(army_frame, text="Wizard")
wizard_button.grid(row=4, sticky='W')

werewolf_button = tkinter.Checkbutton(army_frame, text='Werewolf')
werewolf_button.grid(row=5, sticky='W')

####################################################################
# Number of Fighters

number_frame = tkinter.Frame(main_window)
number_frame.grid(column=0, row=6, columnspan=2, rowspan=2, sticky='nwes')

for i in range(0, 2):
    number_frame.rowconfigure(i, weight=1)

number_label = tkinter.Label(number_frame, text='Army Size')
number_label.grid(row=0, sticky='new')

entry_box = tkinter.Entry(number_frame)
entry_box.grid(row=1, sticky='nsew')

####################################################################
# Generate Button

generate_button = tkinter.Button(main_window, text="Generate Army")
generate_button.grid(row=8, column=0, columnspan=2, sticky='news')

####################################################################
# Players Box

player_canvas = tkinter.Canvas(main_window)
player_canvas.grid(row=1, column=2, rowspan=7, columnspan=4, sticky='news')

player_canvas.rowconfigure(0, weight=1)
player_canvas.rowconfigure(1, weight=35)

player_label = tkinter.Label(player_canvas, text="Players")
player_label.grid(row=0, sticky='ews')

####################################################################
# Player Scroll Bar

player_scroll = tkinter.Scrollbar(main_window)
player_scroll.grid(row=1, column=6, rowspan=7, sticky='nws')

####################################################################
# Start War Button

war_button = tkinter.Button(main_window, text="Start War")
war_button.grid(row=8, column=2, columnspan=5, sticky='news')

if __name__ == '__main__':
    # main_window.mainloop()
    war()
    db.close()
