import random
import json
print("Welcome, brave adventurer, to the realm of Pythonia!")
name = input("What is your character's name? ")
character_class = input("What class will you be? ")
strength = random.randint(8, 18)
hit_points = random.randint(10, 20)
gold = random.randint(0, 25)

character = {

    "name": name,
    "class" : character_class,
    "level" : 1,
    "strength" : strength,
    "hit_points" : hit_points,
    "gold" : gold
}

def character_sheet(character):
    print("\n--- Your Character Sheet ---")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Hit Points: {character['hit_points']}")
    print(f"Gold: {character['gold']}")
    print("----------------------------")

def save_character(character):
    with open("character_save.json", "w") as file:
        json.dump(character, file)
    print("Your adventure has saved")

def level_up(character):
    character["hit_points"] +=5
    character["level"] += 1
    print(f"{character['name']} just leveled up to level {character['level']}!")
    return character
    
# level_up(character)
# character_sheet(character)
# save_character(character)