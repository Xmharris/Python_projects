from dataclasses import dataclass, field
@dataclass
class Character:
    name : str
    lvl : int
    hp_max : int
    hp : int
    exp : int
    companion: dict = field(default_factory=dict)
    weapons : dict = field(default_factory=dict)
    invantory: dict = field(default_factory=dict)

    def is_alive(self):
        """Checks HP is above 0. Returns a bool"""
        if self.hp > 0:
            return True
        else: return False
    
    def gain_xp(self,xp):
        """Adds XP to player and checks if level up is needed"""
        print(f"{self.name} gained {xp} exp!")
        self.exp += xp
        self.level_check()
       
    def take_dmg(self, dmg):
        """Subtracts damage from hp and handles death"""
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
        """Creates a companion and sets its stats"""
        pet = input("What is your pets name? ")
        stats = {'hp': self.hp/ 2, 'basic_attack' : 5}
        self.companion[pet] = stats

        print(
            f"-" * 20,
            f"Pets name: {pet}",
            f"Hp: {stats['hp']}",
            f"Attack: {stats['basic_attack']}",
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

    def level_check(self):
        """Checks Current Exp and levels up accourding to the dictionary"""
        lev = {
            0 : 1,
            25 : 2,
            50 : 3,
            100 : 4,
            150 : 5,
            200 : 6,
            250 : 7,
            300 : 8,
            350 : 9,
            400 : 10
            }

        for xpneeded, level in lev.items():
            """Puts the player level at the corresponding EXP and counts how many levels"""
            if self.exp >= xpneeded and self.lvl < level:                
                self.lvl = level
                self.level_up()

    def level_up(self):  
        """Raises the Max hp and refills HP"""
        self.hp_max *= self.lvl
        self.hp = self.hp_max
        print(f"{self.name} is now level {self.lvl}")

    # def save_character(player):
    #     with open("character_save.json", "w") as file:
    #         json.dump(player, file)
    #     print("Your adventure has saved")

