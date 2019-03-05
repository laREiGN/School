### COMPOSITION / AGGREGATION
#   Part 3
#

print("PART 3")

# Let's make a Hero class
class Hero:
    def __init__(self,name,maxhealth):
        self.__name = name
        self.__hp = maxhealth
        self.__baseatt = 1
        self.__dead = False
        self.__inventory = Inventory()
        self.active_item = None

    # perhaps we want to change name later
    def set_name(self, new_name):
        self.__name = new_name

    # since name is private, we need method to get it from outside
    def get_name(self):
        return self.__name

    # hero takes DAMAGE provided as argument; also updates DEAD state if HP below 0
    def take_damage(self, damage):
        self.__hp -= damage
        if (self.__hp <= 0):
            self.__dead = True

    # check if hero is dead and return value
    def is_dead(self):
        return self.__dead

    # overloaded __str__ for easier printing
    def __str__(self):
        temp_str = "alive" if not self.is_dead() else "dead"
        at = self.__baseatt if self.active_item == None else self.active_item.damage
        return "%s: AT(%2d) HP(%3d) - %s" % (self.__name, at, self.__hp,temp_str)

    # access inventory, add item
    def add_item(self, item):
        self.__inventory.add(item)

    # access inventory, equip selected item
    def equip(self, item):
        if self.__inventory.has(item):
            self.active_item = item

    # perform attack; apply damage from active item to the target
    # or use base attack if no item present
    def attack(self, target):
        if self.active_item:
            self.active_item.use(target)
        else:
            print("%s hit using fists for %d damage" % (target.get_name(), self.__baseatt))
            target.take_damage(self.__baseatt)

# Inventory class to ilustrate composition
# Basic list manipulation; add and check if exists
class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def has(self, item):
        return item in self.items

# Weapon class; nothing special
class Weapon:
    def __init__(self, damage):
        self.damage = damage

    def use(self, target):
        print("%s hit for %d damage" % (target.get_name(), self.damage))
        target.take_damage(self.damage)


# For experiment let's create two weapons ...
short_sword = Weapon(5)
long_sword = Weapon(10)
staff = Weapon(12)

# ... and two heroes
wizard = Hero("Gandalf", 100)
demon = Hero("Balrog", 150)

# ... we test if everything is working by printing the stats
# (note the use of overloaded __str__ to print directly
print(wizard)
print(demon)

# Next, let's try to give both weapons to wizard and none to demon
wizard.add_item(long_sword)
wizard.add_item(short_sword)
#demon.add_item(staff) ## Added by me
# ... and equip long_sword
wizard.equip(long_sword)

# To test the robustness of our design we will try to equip short_sword to demon
# ... and see if his stats would change (it shouldn't)
demon.equip(short_sword)
#demon.equip(staff) ## Added by me

# Test stats again by printing (wizard should have greater attack)
print("\n\nWeapons equipped\n")
print(wizard)
print(demon)

round = 1
while((not wizard.is_dead())   and   (not demon.is_dead())):
    print("\nRound:", round)
    wizard.attack(demon)
    demon.attack(wizard)
    print("\nStats after round", round)
    print(wizard)
    print(demon)
    round += 1
    print('\n' + "-"*15)


print("\nEOF part 3\n")
print("-"*20)
