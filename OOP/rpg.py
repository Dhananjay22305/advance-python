from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Warrior(Character):
    def __init__(self, name, health, weapon_obj):
        self.name = name
        self._health = health    # "Protected" variable for internal logic
      
        # We store the entire weapon object inside the warrior
        self.weapon = weapon_obj 

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, amount):
        if amount < 0:
            self._health = 0
            print(f"{self.name} has died!")
        else:
            self._health = amount

    # Implementing the abstract method
    def attack(self):
        # Accessing data from the composed 'weapon' object
        print(f"⚔️ {self.name} attacks with {self.weapon.name}!")
        print(f"   -> Dealt {self.weapon.damage} damage.")

    def __str__(self):
        return f"Warrior: {self.name} | HP: {self.health} | Weapon: {self.weapon.name}"

# 1. Create the Component (The Weapon) FIRST
sword = Weapon("Excalibur", 50)
axe = Weapon("Battle Axe", 65)

# 2. Create the Warrior and PASS the weapon object to him
# "arthur" now contains the "sword" object inside him.
arthur = Warrior("King Arthur", 100, sword)


print(arthur)          # Uses __str__
arthur.attack()        # Uses the composed Weapon object to get damage info
 (Swap the weapon!)
print("\n...Arthur swaps weapons...")
arthur.weapon = axe    # We just swapped the object inside the attribute!
arthur.attack()        # Now he does 65 damage
