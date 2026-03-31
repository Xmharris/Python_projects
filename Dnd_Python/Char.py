from dataclasses import dataclass, field
from urllib import response
import json

@dataclass
class Character:
    name : str
    lvl : int
    hp : int
    exp : int
    companion: dict = field(default_factory=dict)
    weapons : dict = field(default_factory=dict)
    invantory: dict = field(default_factory=dict)

    def is_alive(self):
        if self.hp > 0:
            return True
        else: return False


    def level_up(self):
        self.lvl += 1
        self.hp *= self.lvl
        print(f"{self.name} is now level {self.lvl}")
     
    def gain_xp(self,xp):
        self.exp += xp
       
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            print("You died... reincrnating")
            self.hp = self.lvl*5
            print("Welcome Back!")
        else:
            print(f"{self.name} took {dmg} damage. Their hp is now {self.hp}" )
    
    def heal(self, health):
        self.hp += health

    def create_pet(self):
        pet = input("What is your pets name? ")
        abilities = {'hp': self.hp/ 2, 'basic_attack' : 5}
        self.companion[pet] = abilities

        print(
            f"-" * 20,
            f"Pets name: {pet}",
            f"Hp: {abilities['hp']}",
            f"Attack: {abilities['basic_attack']}",
            f"-" * 20,
            sep= "\n"
            )
    
    def print_character(self):
        print(
            "*"*6,
            f"Character Sheet",
            f"Name: {self.name}",
            f"Level: {self.lvl}",
            f"Exp: {self.exp}",
            f"HP: {self.hp}",
            f"Companions: {self.companion}",
            f"Weapons: {self.weapons}",
            "*"*6,
            sep="\n"
            )   
        
    # def save_character(player):
    #     with open("character_save.json", "w") as file:
    #         json.dump(player, file)
    #     print("Your adventure has saved")

