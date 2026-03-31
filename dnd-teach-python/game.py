# game.py
import random
from character import Character

def roll_d(sides=20):
    return random.randint(1, sides)

def modifier(score):
    return (score - 10) // 2

def attack(attacker: Character, defender: Character):
    roll = roll_d(20)
    atk_mod = modifier(attacker.abilities.get("STR", 10))
    total = roll + atk_mod
    print(f"{attacker.name} rolls {roll} + {atk_mod} = {total} vs AC {defender.ac}")
    if total >= defender.ac:
        dmg = random.randint(1, 8) + atk_mod
        dmg = max(1, dmg)
        print(f"Hit! {attacker.name} deals {dmg} damage.")
        defender.take_damage(dmg)
    else:
        print(f"{attacker.name} misses.")

def simple_combat(player, enemy):
    turn = 0
    while player.is_alive() and enemy.is_alive():
        attacker = player if turn % 2 == 0 else enemy
        defender = enemy if attacker is player else player
        attack(attacker, defender)
        print(f"{player.name}: {player.hp}/{player.hp_max} HP  |  {enemy.name}: {enemy.hp}/{enemy.hp_max} HP\n")
        turn += 1
    winner = player if player.is_alive() else enemy
    print(f"Combat over. {winner.name} wins!")

def main():
    random.seed() 
    player = Character("Alden", hp_max=12, hp=12, ac=13,
                       abilities={"STR":14,"DEX":12,"CON":12,"INT":10,"WIS":10,"CHA":11},
                       inventory=["Shortsword","Potion"])
    goblin = Character("Goblin", hp_max=8, hp=8, ac=12,
                       abilities={"STR":10,"DEX":14,"CON":10,"INT":8,"WIS":8,"CHA":6},
                       inventory=["Dagger"])
    simple_combat(player, goblin)

if __name__ == "__main__":
    main()
