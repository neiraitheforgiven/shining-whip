from characters import playerCharacter
from characters import monster
from operator import itemgetter
import random

class battle(object):

    def __init__(self, party, num=None):
        if num:
            if num == 1:
                self.battleField = battleField([
                        "Forest", "Grass", "Grass", "Ascending Stairway",
                        "Rubble", "Tiled Floor", "Tiled Floor", "Tiled Floor",
                        "Rubble", "Rubble", "Tiled Floor"],
                        [("Goblin", 7), ("Traitor Knight", 7), ("Goblin", 8),
                        ("Dark Dwarf", 9), ("Dark Dwarf", 9), ("Goblin", 10),
                        ("Goblin", 10)],
                        party)
            for unit in self.battleField.units:
                unit.hp = unit.stats["Stamina"] * 2
            self.turnOrder = self.determineInitiative()
            while self.battleOn():
                self.doRound()

    def battleOn(self):
        if any([
                unit for unit in self.battleField.units
                if type(unit) == playerCharacter and "Egress I"
                in unit.powers]):
            if any([
                    unit for unit in self.battleField.units
                    if type(unit) == monster]):
                return True
            else:
                print("You are victorious!")
                return False
        else:
            print("D E F E A T E D")
            return False

    def determineInitiative(self):
        initiativeOrder = []
        random.shuffle(self.battleField.units)
        for unit in self.battleField.units:
            initiative = max(
                    unit.stats["Charisma"], unit.stats["Speed"],
                    unit.stats["Dexterity"])
            initiativeOrder.append((unit, initiative, unit.stats["Luck"]))
            while initiative > 15:
                initiative -= 15
                initiativeOrder.append((unit, initiative, unit.stats["Luck"]))
        initiativeOrder = sorted(
                initiativeOrder, key=itemgetter(1, 2), reverse=True)
        print([pair[0].name for pair in initiativeOrder])
        return initiativeOrder

    def doRound(self):
        for unit in self.battleField.units:
            unit.movementPoints = unit.stats["Speed"]
        for unit in self.turnOrder:
            self.doTurn(unit[0])
        print([
                f"{[unit.name for unit in tile.units]} on "
                f"{tile.name}: {tile.cost}"
                for tile in self.battleField.terrainArray])

    def doTurn(self, unit):
        position = self.battleField.getUnitPosition(unit)
        print()
        print(f"It's {unit.name}'s turn!")
        if type(unit) == playerCharacter:
            allowedCommands = ["W", "w"]
            moveEnabled = self.battleField.checkMove(unit, position)
            if moveEnabled:
                self.battleField.printMoveString(unit)
                print("Type (M) to move.")
                allowedCommands.append("M")
                allowedCommands.append("m")
                # print("Type (L) to look at a tile.")
            # attackEnabled = self.battleField.checkAttack(unit, position)
            # if attackEnabled:
            #     print("Type (A) to attack.")
            # spellEnabled = self.battleField.checkSpell(unit, position)
            # if spellEnabled:
            #     print("Type (S) to cast a spell.")
            # equipEnabled = self.battleField.checkEquip(unit, position)
            # if equipEnabled:
            #     print("Type (E) to change equipment.")
            print("Type (W) to wait.")
            command = None
            while command not in allowedCommands:
                command = input()
            if command in ("M", "m"):
                self.battleField.move(unit)
            if command in ("W", "w"):
                return


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
            unitMonster = monster(unit)
            tile = self.terrainArray[position]
            tileUnits = tile.units
            tileUnits.append(unitMonster)
            self.units.append(unitMonster)
        for pc in party:
            self.units.append(pc)
            if len(self.terrainArray[1].units) < 4:
                self.terrainArray[1].units.append(pc)
            elif len((self.terrainArray[0].units)) < 4:
                self.terrainArray[0].units.append(pc)
            else:
                self.terrainArray[2].units.append(pc)
        print([
                f"{[unit.name for unit in tile.units]} on "
                f"{tile.name}: {tile.cost}"
                for tile in self.terrainArray])

    def calculatePossibleMovement(
            self, unit, movementPoints, position, directionIsHigher,
            unstable, bonusSpent=False):
        tile = self.terrainArray[position]
        # calculate if there is space
        if not unstable:
            unstable = tile.unstable
        if movementPoints <= 0 or (
                "Unhindered Movement" in
                unit.powers and movementPoints < 5):
            # mounted units may have bonus movement if they move on solids
            if (
                    "Mounted Movement" in
                    unit.powers and not bonusSpent and not unstable):
                bonusSpent = True
            else:
                return
        candidate = False
        if len([
                tileUnit for tileUnit in tile.units
                if type(tileUnit) == type(unit)]) < 4:
            candidate = True
        # remove movementPoints
        if "Flying Movement" in unit.powers or "Unhindered Movement" \
                in unit.powers:
            movementPoints = movementPoints - 5
        else:
            movementPoints = movementPoints - tile.cost
        if movementPoints <= 0 or (
                "Unhindered Movement" in
                unit.powers and movementPoints < 5):
            # mounted units may have bonus movement if they move on solids
            if ("Mounted Movement" in unit.powers and "Flying Movement"
                    not in unit.powers):
                if unstable:
                    return  # you forfeit your final movement
                else:
                    if not bonusSpent:
                        bonusSpent = True  # You get one more movement
                        movementPoints = 1
            if candidate:
                unit.allowedMovement.append(position)
            if movementPoints <= 0 or (
                    "Unhindered Movement" in
                    unit.powers and movementPoints < 5):
                return
        else:
            if candidate:
                unit.allowedMovement.append(position)
        if "Movement: Ignore Enemies" not in unit.powers:
            # calculate if we are blocked
            if len([
                    tileUnit for tileUnit in tile.units
                    if type(tileUnit) != type(unit)]) >= 2:
                blocked = True
            else:
                blocked = False
        else:
            blocked = False
        if not blocked:
            if directionIsHigher:
                position += 1
                if position <= len(self.terrainArray) - 1:
                    self.calculatePossibleMovement(
                            unit, movementPoints, position, directionIsHigher,
                            unstable, bonusSpent)
            else:
                position -= 1
                if position >= 0:
                    self.calculatePossibleMovement(
                            unit, movementPoints, position, directionIsHigher,
                            unstable, bonusSpent)

    def checkMove(self, unit, position):
        unit.allowedMovement = []
        currentTile = self.terrainArray[position]
        unstable = currentTile.unstable
        if "Movement: Ignore Enemies" in unit.powers:
            retreatBlocked = False
            advancingBlocked = False
        else:
            retreatBlocked = len([
                    tileUnit for tileUnit in currentTile.units
                    if type(tileUnit) != type(unit)]) >= 3
            advancingBlocked = len([
                    tileUnit for tileUnit in currentTile.units
                    if type(tileUnit) != type(unit)]) >= 2
        if retreatBlocked and advancingBlocked:
            return False
        if (type(unit) == playerCharacter and not advancingBlocked) \
                or (type(unit) == monster and not retreatBlocked):
            calcPosition = position + 1
            if calcPosition <= len(self.terrainArray) - 1:
                self.calculatePossibleMovement(
                        unit, unit.movementPoints, calcPosition, True,
                        unstable)
        if (type(unit) == playerCharacter and not retreatBlocked) \
                or (type(unit) == monster and not advancingBlocked):
            calcPosition = position - 1
            if calcPosition >= 0:
                self.calculatePossibleMovement(
                        unit, unit.movementPoints, calcPosition, False,
                        unstable)
        if any(unit.allowedMovement):
            return True
        else:
            return False

    def getUnitPosition(self, unit):
        for tile in self.terrainArray:
            if unit in tile.units:
                return self.terrainArray.index(tile)

    def move(self, unit):
        moveTo = None
        while moveTo not in unit.allowedMovement:
            moveTo = int(input("Type a number to move to: "))
        fromPosition = self.getUnitPosition(unit)
        moveFromTile = self.terrainArray[fromPosition]
        moveToTile = self.terrainArray[moveTo]
        lowest = min(fromPosition, moveTo)
        highest = max(fromPosition, moveTo)
        for i in range(lowest, highest + 1):
            if i != fromPosition:
                costTile = self.terrainArray[i]
                unit.movementPoints -= costTile.cost
        moveFromTile.units.remove(unit)
        moveToTile.units.append(unit)
        print(f"{unit.name} moved to the {moveToTile.name}")

    def printMoveString(self, unit):
        movestring = f"{unit.name} can move to "
        movestringAdds = []
        unit.allowedMovement.sort()
        for position in unit.allowedMovement:
            movestringAdds.append(
                    f"({position}) {self.terrainArray[position].name}")
        movestring += ", ".join(movestringAdds)
        print(movestring + ".")


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
