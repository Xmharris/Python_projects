# character.py
from dataclasses import dataclass, field

@dataclass
class Character:
    name: str
    hp_max: int
    hp: int
    ac: int
    abilities: dict = field(default_factory=dict)
    inventory: list = field(default_factory=list)

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def heal(self, amount):
        self.hp = min(self.hp_max, self.hp + amount)
