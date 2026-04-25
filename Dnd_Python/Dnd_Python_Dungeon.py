import random
import Character
from zupy_questions import questions

def room_1():
    """Variables"""
    print("Welcome to the Dungeon! A stone door blocks the path. Runes glow with shimmering symbols.")
    print("On the door it says: 'Name the value that holds your destiny. Speak IT!''")
    print("x = 5")
    x = 5
    answer = int(input("What is the value of x?"))
    if answer == 5:
        print("The door opens.....")
        return True
    return False

def room_2():
    """Loops"""
    print("Inside the next room the hallway never seems to end. You count your steps...")
    print("for i in range(3):")
    print("    print('Step', i)")
    answer = int(input("How many times does this loop run? "))
    if answer == 3:
        for i in range(3):
            print("Step", i)
        print("After 3 steps the hallway stops looping...")
        return True
    return False

def room_3():
    """Conditions"""
    print("Through the nect door there stand 3 statues. They all tell riddles but only one tells the truth.")
    print("x = 7")
    print("if x > 10:")
    print("    print('Statue A speaks')")
    print("elif x > 5:")
    print("    print('Statue B speaks')")
    print("else:")
    print("    print('Statue C speaks')")
    answer = input("Which statue speaks? Type it exactly")
    if answer == "Statue B speaks":
        print("Statue B speaks")
        return True
    return False

def room_4():
    """Lists"""
    print("4 doors stand in front of you. Only one is safe..")
    print("doors = ['fire','treasure', 'snake', 'pit']")
    print("print('doors[1]')")
    answer = input("Which door opens?")
    if answer == "treasure":
        print("treasure")
        print("You see a chest")
        return True
    elif answer == "fire":
        print("You caught on fire")
        return False
    elif answer == "snake":
        print("You get bit!")
        return False
    elif answer == "pit":
        print("You fall in a pit")
        return False
    return False

def boss():
    """Debugging"""
    print("A dragon enters the room. You notice a bug on its back. ")
    return True



