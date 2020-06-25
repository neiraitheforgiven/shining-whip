from characters import playerCharacter
from operator import itemgetter

class battle(object):

    def __init__(self, party, num=None):
        if num:
            if num == 1:
                self.battleField = battleField([
                        "Grass", "Grass", "Grass", "Ascending Stairway",
                        "Rubble", "Tiled Floor", "Tiled Floor", "Tiled Floor",
                        "Rubble", "Rubble"],
                        [("Goblin", 5), ("Goblin", 8), ("Dark Dwarf", 8)],
                        party)
            self.turnOrder = self.determineInitiative(self.battleField)

    def determineInitiative(self, battleField):
        print("Welcome to determineInitiative")
        initiativeOrder = []
        print(battleField.units)
        for unit in battleField.units:
            if type(unit) == playerCharacter:
                initiative = max(
                        unit.stats["Charisma"], unit.stats["Speed"],
                        unit.stats["Dexterity"])
                initiativeOrder.append((unit, initiative, unit.stats["Luck"]))
                while initiative > 15:
                    initiative -= 15
                    initiativeOrder.append((unit, initiative))
        initiativeOrder = sorted(
                initiativeOrder, key=itemgetter(1, 2), reverse=True)
        print(initiativeOrder)
        return initiativeOrder


class battleTile(object):
    """docstring for BattleTile"""

    def __init__(self, terrain):
        self.name = terrain
        self.cost = 5
        # Assign cost
        if self.name == "Tiled Floor":
            self.cost = 5
        elif self.name == "Grass":
            self.cost = 6
        elif self.name in ("Sand", "Overgrowth"):
            self.cost = 7
        elif self.name in (
                "Ascending Stairway", "Descending Stairway", "Loose Rocks"):
            self.cost = 8
        elif self.name == "Forest":
            self.cost = 10

        # is it unstable?
        if self.name in ("Sand", "Loose Rocks"):
            self.unstable = True
        else:
            self.unstable = False
        self.units = []

class battleField(object):

    def __init__(self, listOfTiles, listOfUnits, party):
        self.terrainArray = []
        self.units = []
        for tile in listOfTiles:
            self.terrainArray.append(battleTile(tile))
        for unit, position in listOfUnits:
            tile = self.terrainArray[position]
            tileUnits = tile.units
            tileUnits.append(unit)
            self.units.append(unit)
        for pc in party:
            self.units.append(pc)
            if len(self.terrainArray[1].units) < 4:
                self.terrainArray[1].units.append(pc)
            elif len((self.terrainArray[0].units)) < 4:
                self.terrainArray[0].units.append(pc)
            else:
                self.terrainArray[2].units.append(pc)
        print([
                f"{[unit.name if type(unit) == playerCharacter else unit for unit in tile.units]} on {tile.name}: {tile.cost}"
                for tile in self.terrainArray])


class game(object):

    def __init__(self):
        self.playerCharacters = []

        chatter = False
        recruit = playerCharacter(
                "Max", "Human", "Swordsman", chatter, 0)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Lowe", "Hobbit", "Priest", chatter, 0)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Tao", "Elf", "Fire Mage", chatter, 0)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Luke", "Dwarf", "Warrior", chatter, 0)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Ken", "Centaur", "Knight", chatter, 0)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Hans", "Elf", "Archer", chatter, 0)
        self.playerCharacters.append(recruit)
        self.party = self.playerCharacters[:5]
        battle(self.party, 1)


print("Let's do a test!")
game = game()
