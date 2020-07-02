from characters import equipment
from characters import playerCharacter
from characters import monster
from operator import itemgetter
import math
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
                        ("Crazed Dwarf", 9), ("Crazed Dwarf", 9),
                        ("Goblin", 10), ("Goblin", 10)],
                        party)
            for unit in self.battleField.units:
                unit.hp = unit.stats["Stamina"] * 2
                unit.fp = unit.stats["Faith"] + unit.equipment.fp
                unit.mp = unit.stats["Intelligence"] + unit.equipment.mp
                if "Egress I" in unit.powers and unit.mp < 8:
                    print(f"warning: {unit.name} has insufficient mp to Egress")
            while self.battleOn():
                self.doRound()

    def attack(self, unit, target):
        routEnemy = False
        doubleChanceArray = []
        doubleChance = math.floor(
                unit.stats["Dexterity"] + (
                        unit.stats["Dexterity"] * (unit.stats["Luck"] / 10)))
        doubleChanceArray.extend([1] * (100 - unit.stats["Luck"]))
        doubleChanceArray.extend([2] * doubleChance)
        if "Luck: Enable Triple Attack" in unit.powers:
            doubleChanceArray.extend([3] * doubleChance)
        attackCount = random.choice(doubleChanceArray)
        for i in range(0, attackCount):
            if i == 0:
                print(f"{unit.name} attacks!")
            elif i > 0:
                print(f"{unit.name} attacks again!")
            attackTypeArray = []
            attackTypeArray.extend(
                    ["normal"] * (100 - (
                            unit.stats["Luck"] - target.stats["Luck"])))
            criticalChance = math.floor(
                    unit.stats["Strength"] + (
                            unit.stats["Strength"] * (
                                    unit.stats["Luck"] / 10)))
            attackTypeArray.extend(["critical"] * criticalChance)
            routSkill = max(unit.stats["Charisma"], unit.stats["Voice"])
            routChance = math.floor(
                    routSkill + (routSkill * (unit.stats["Luck"] / 10)))
            attackTypeArray.extend(["routing"] * routChance)
            attackType = random.choice(attackTypeArray)
            dodgeSkill = math.floor(max(
                    target.stats["Intelligence"], target.stats["Luck"],
                    target.stats["Speed"]) * (1 + (
                            (target.stats["Luck"] / 10) - unit.stats["Luck"])))
            if dodgeSkill > 0:
                attackTypeArray.extend(["dodge"] * dodgeSkill)
            if attackType == 'dodge':
                print(f"{target.name} dodges the attack!")
            else:
                if attackType == 'critical':
                    print("A Critical Attack!")
                damage = (max(
                        unit.stats["Strength"], unit.stats["Dexterity"]) + (
                        unit.equipment.damage))
                if attackType != 'critical':
                    damage -= max(
                            target.stats["Strength"],
                            target.stats["Dexterity"], target.stats["Faith"])
                damage = max(damage, 1)
                damage = min(damage, target.hp)
                print(f"{unit.name} deals {damage} damage to {target.name}!")
                target.hp -= damage
                self.giveExperience(unit, target, damage)
                if target.hp <= 0:
                    print(f"{target.name} dies!")
                    field = self.battleField
                    targetPosition = field.getUnitPosition(target)
                    field.terrainArray[targetPosition].units.remove(target)
                    if target in self.turnOrder:
                        self.turnOrder.remove(target)
                    del target
                    return
                elif attackType == "routing":
                    routEnemy = True
                if routEnemy and ((i + 1) == attackCount):
                    if type(target) == playerCharacter:
                        moveTo = self.battleField.getUnitPosition(target) - 1
                        if moveTo >= 0:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)
                    elif type(target) == monster:
                        moveTo = self.battleField.getUnitPosition(target) + 1
                        if moveTo <= len(self.battleField.terrainArray) - 1:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)

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

    def castSpell(self, unit, spellName, targetId):
        if spellName == "Blaze I":
            unit.mp -= 2
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(6, target.hp)
            print(f"{unit.name} deals {damage} damage to {target.name}!")
            target.hp -= damage
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                print(f"{target.name} dies!")
                field = self.battleField
                targetPosition = field.getUnitPosition(target)
                field.terrainArray[targetPosition].units.remove(target)
                if target in self.turnOrder:
                    self.turnOrder.remove(target)
                del target
                return
        elif spellName == "Egress I":
            unit.mp -= 8
            print(f"{unit.name} casts {spellName}!")
            print(f"Nothing happens... yet.")
            # restart the battle
        elif spellName == "Heal I":
            unit.mp -= 3
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            healing = min(18, (target.stats["Stamina"] * 2) - target.hp)
            print(f"{unit.name} restores {healing} health to {target.name}!")
            target.hp += healing
            self.giveExperience(unit, target, healing)

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
        return initiativeOrder

    def doAttack(self, unit, targetId):
        target = unit.allowedAttacks[targetId]
        self.attack(unit, target)

    def doMonsterAttack(self, monster):
        if monster.attackProfile == "ChallengeAccepting":
            # will attack the highest fame, level, charisma, strength
            candidates = [
                    target for target in monster.allowedAttacks
                    if target.stats["Fame"] == max(
                            unit.stats["Fame"]
                            for unit in monster.allowedAttacks)]
            candidates = [
                    target for target in candidates if target.level == max(
                            unit.level for unit in candidates)]
            candidates = [
                    target for target in candidates
                    if target.stats["Charisma"] == max(
                            unit.stats["Charisma"] for unit in candidates)]
            candidates = [
                    target for target in candidates
                    if target.stats["Strength"] == max(
                            unit.stats["Strength"] for unit in candidates)]
            target = random.choice(candidates)
            self.attack(monster, target)
        elif monster.attackProfile == "Random":
            target = random.choice(monster.allowedAttacks)
            self.attack(monster, target)

    def doRound(self):
        self.turnOrder = self.determineInitiative()
        for unit in self.battleField.units:
            unit.movementPoints = unit.stats["Speed"]
        for unit in self.turnOrder:
            # unit may have died since this loop started.
            if unit[0].hp <= 0:
                continue
            endBattle = self.doTurn(unit[0])
            if endBattle:
                return
        print([
                f"{[unit.name for unit in tile.units]} on "
                f"({self.battleField.terrainArray.index(tile)}) {tile.name}: "
                f"{tile.cost}"
                for tile in self.battleField.terrainArray])

    def doTurn(self, unit, moved=False):
        position = self.battleField.getUnitPosition(unit)
        tile = self.battleField.terrainArray[position]
        otherUnits = ", ".join([
                tileUnit.name for tileUnit in tile.units if tileUnit != unit])
        if type(unit) == playerCharacter:
            allowedCommands = ["W", "w"]
            if not moved:
                print()
                print(f"It's {unit.name}'s turn!")
                if otherUnits:
                    print(
                            f"{unit.name} is standing on ("
                            f"{self.battleField.terrainArray.index(tile)}) "
                            f"{tile.name} with {otherUnits}.")
                else:
                    print(
                            f"{unit.name} is standing on ("
                            f"{self.battleField.terrainArray.index(tile)}) "
                            f"{tile.name}.")
                moveEnabled = self.battleField.checkMove(unit, position)
                if moveEnabled:
                    self.battleField.printMoveString(unit)
                    print("Type (M) to move.")
                    allowedCommands.append("M")
                    allowedCommands.append("m")
                    # print("Type (L) to look at a tile.")
            attackEnabled = self.battleField.checkAttack(unit, position)
            if attackEnabled:
                self.battleField.printAttackString(unit)
                print("Type (A) to attack.")
                allowedCommands.append("A")
                allowedCommands.append("a")
                # spellEnabled = self.battleField.checkSpell(unit, position)
                # if spellEnabled:
                #     print("Type (S) to cast a spell.")
                # equipEnabled = self.battleField.checkEquip(unit, position)
                # if equipEnabled:
                #     print("Type (E) to change equipment.")
            spellEnabled = self.battleField.checkSpells(unit, position)
            if spellEnabled:
                self.battleField.printSpellString(unit)
                print("Type (S) to cast a spell.")
                allowedCommands.append("S")
                allowedCommands.append("s")
            if not any([
                    allowedCommand for allowedCommand in allowedCommands
                    if allowedCommand not in ("W", "w")]):
                print(f"{unit.name} waited.")
                return
            print("Type (W) to wait.")
            command = None
            while command not in allowedCommands:
                command = input()
            if command in ("M", "m"):
                moveTo = None
                while moveTo not in unit.allowedMovement:
                    moveTo = int(input("Type a number to move to: "))
                self.battleField.move(unit, moveTo)
                self.doTurn(unit, True)
            if command in ("A", "a"):
                attackTarget = None
                while attackTarget not in [
                        unit.allowedAttacks.index(target)
                        for target in unit.allowedAttacks]:
                    attackTarget = int(input("Type a number to attack: "))
                self.doAttack(unit, attackTarget)
            if command in ("S", "s"):
                spellChoice = None
                spellTarget = None
                spellKeys = list(unit.allowedSpells.keys())
                while spellChoice not in [
                        spellKeys.index(spell) for spell in spellKeys]:
                    spellChoice = int(input(
                            "Type the number of the spell to cast: "))
                spellToCast = spellKeys[spellChoice]
                self.battleField.printSpellTargetString(unit, spellToCast)
                targetList = unit.allowedSpells[spellToCast]
                while targetList != 'Self' and spellTarget not in (
                        targetList.index(target) for target in targetList):
                    spellTarget = int(input("Type a number to target: "))
                self.castSpell(unit, spellToCast, spellTarget)
            if command in ("W", "w"):
                return
        elif type(unit) == monster:
            print()
            print(f"It's {unit.name}'s turn!")
            if otherUnits:
                print(
                        f"{unit.name} is standing on ("
                        f"{self.battleField.terrainArray.index(tile)}) "
                        f"{tile.name} with {otherUnits}.")
            else:
                print(
                        f"{unit.name} is standing on ("
                        f"{self.battleField.terrainArray.index(tile)}) "
                        f"{tile.name}.")
            moveEnabled = self.battleField.checkMove(unit, position)
            if moveEnabled:
                self.battleField.doMonsterMove(unit, position)
            position = self.battleField.getUnitPosition(unit)
            attackEnabled = self.battleField.checkAttack(unit, position)
            if attackEnabled:
                self.doMonsterAttack(unit)
            else:
                print(f"{unit.name} waited.")
        endBattle = not self.battleOn()
        return endBattle

    def giveExperience(self, unit, target, damage):
        numChunks = math.ceil(damage / (target.stats["Stamina"] * 0.2))
        if type(unit) == playerCharacter:
            unitLevel = unit.level
            targetLevel = target.level + 6
            # elif type(unit) == monster:
            #     unitLevel = unit.level + 6
            #     targetLevel = target.level
        else:
            return
        # check for trophies
        if target.name not in unit.trophies:
            if target.hp <= 0:
                print(f"{unit.name} killed their first {target.name}!")
                numChunks += 4
                unit.trophies.append(target.name)
        amount = max(1, min(((targetLevel - unitLevel) * numChunks), 49))
        unit.xp += amount
        print(f"{unit.name} receives {amount} experience!")
        if unit.xp > 100:
            unit.xp -= 100
            unit.levelUp(True)


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

    def checkAttack(self, unit, position):
        unit.allowedAttacks = []
        currentTile = self.terrainArray[position]
        if unit.equipment:
            minRange = unit.equipment.minRange
            maxRange = unit.equipment.maxRange
        else:
            minRange = 0
            maxRange = 0
        if type(unit) == playerCharacter:
            targetType = monster
        elif type(unit) == monster:
            targetType = playerCharacter
        if minRange == 0 and maxRange == 0:
            unit.allowedAttacks = [
                    unit for unit in currentTile.units
                    if type(unit) == targetType]
            return bool(unit.allowedAttacks)
        else:
            lowRangeBottom = position - maxRange
            lowRangeTop = position - minRange
            highRangeBottom = position + minRange
            highRangeTop = position + maxRange
            tilesInRange = []
            for tile in self.terrainArray[lowRangeBottom:(lowRangeTop + 1)]:
                tilesInRange.append(tile) \
                        if tile not in tilesInRange else tilesInRange
            for tile in self.terrainArray[highRangeBottom:(highRangeTop + 1)]:
                tilesInRange.append(tile) \
                        if tile not in tilesInRange else tilesInRange
            for tile in tilesInRange:
                for tileUnit in tile.units:
                    if type(tileUnit) == targetType:
                        unit.allowedAttacks.append(tileUnit)
            return bool(unit.allowedAttacks)

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

    def checkSpells(self, unit, position):
        unit.allowedSpells = {}
        currentTile = self.terrainArray[position]
        if type(unit) == playerCharacter:
            friend = playerCharacter
            enemy = monster
        elif type(unit) == monster:
            friend = monster
            enemy = playerCharacter
        if "Blaze I" in unit.powers and unit.mp >= 2:
            targets = [
                    target for target in currentTile.units
                    if type(target) == enemy]
            if any(targets):
                unit.allowedSpells["Blaze I"] = targets
        if "Egress I" in unit.powers and unit.mp >= 8:
            unit.allowedSpells["Egress I"] = 'Self'
        if "Heal I" in unit.powers and unit.fp >= 3:
            targets = [
                    target for target in currentTile.units
                    if type(target) == friend and target.hp < (
                            target.stats["Stamina"] * 2)]
            if any(targets):
                unit.allowedSpells["Heal I"] = targets
        if any(unit.allowedSpells):
            return True
        else:
            return False

    def doMonsterMove(self, monster, position, assignMoveProfile=None):
        if assignMoveProfile:
            monster.moveProfile = assignMoveProfile
        if monster.moveProfile == "Aggressive":
            # will not move if in melee range of enemies
            if any([
                    unit for unit in self.terrainArray[position].units
                    if type(unit) == playerCharacter]):
                return
            # move as far forward as possible to tiles with enemies
            candidates = []
            for position in monster.allowedMovement:
                for unit in self.terrainArray[position].units:
                    if type(unit) == playerCharacter:
                        candidates.append(position)
                        break
            if candidates:
                moveTo = min(candidates)
                self.move(monster, moveTo)
            else:
                # move as far forward as possible
                moveTo = min(monster.allowedMovement)
                self.move(monster, moveTo)
        elif monster.moveProfile == "Defensive":
            if monster.hp < monster.stats["Stamina"] * 2:
                monster.moveProfile = "Aggressive"
                self.doMonsterMove(monster, position)
                return
            else:
                candidates = []
                for position in monster.allowedMovement:
                    for unit in self.terrainArray[position].units:
                        if type(unit) == playerCharacter:
                            candidates.append(position)
                            break
                if candidates:
                    moveTo = max(candidates)
                    self.move(monster, moveTo)
        elif monster.moveProfile == "Retreat-Defensive":
            if monster.hp < monster.stats["Stamina"] * 2:
                monster.moveProfile = "Aggressive"
                self.doMonsterMove(monster, position)
                return
            else:
                moveTo = max(monster.allowedMovement)
                if position == len(self.terrainArray) - 1 or moveTo < position:
                    monster.moveProfile = "Defensive"
                    self.doMonsterMove(monster, position)
                    return
                self.move(monster, moveTo)

    def getUnitPosition(self, unit):
        for tile in self.terrainArray:
            if unit in tile.units:
                return self.terrainArray.index(tile)

    def move(self, unit, moveTo):
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
        print(
                f"{unit.name} moved to the ("
                f"{self.terrainArray.index(moveToTile)}) {moveToTile.name}.")

    def printAttackString(self, unit):
        attackString = f"{unit.name} can attack "
        attackStringAdds = []
        for target in unit.allowedAttacks:
            targetHealth = target.stats["Stamina"] * 2
            attackStringAdds.append(
                    f"({unit.allowedAttacks.index(target)}) {target.name} "
                    f"(HP: {target.hp}/{targetHealth})")
        attackString += ", ".join(attackStringAdds)
        print(attackString + ".")

    def printSpellString(self, unit):
        spellString = f"{unit.name} can cast "
        spellStringAdds = []
        count = 0
        print(f"debug: {unit.allowedSpells}")
        for i in unit.allowedSpells:
            print(f"debug: {i}")
            spellStringAdds.append(f"({count}) {i}")
            count += 1
        spellString += ", ".join(spellStringAdds)
        print(spellString + ".")

    def printSpellTargetString(self, unit, spell):
        targetStringAdds = []
        targetString = "This spell can target "
        count = 0
        for target in unit.allowedSpells[spell]:
            if type(target) == str:
                # spell is a placeholder for a spell with no target
                return
            targetHealth = target.stats["Stamina"] * 2
            targetStringAdds.append(
                    f"({count}) {target.name} (HP: {target.hp}/{targetHealth})")
            count += 1
        targetString += ", ".join(targetStringAdds)
        print(targetString + ".")

    def printMoveString(self, unit):
        moveString = f"{unit.name} can move to "
        moveStringAdds = []
        unit.allowedMovement.sort()
        for position in unit.allowedMovement:
            moveStringAdds.append(
                    f"({position}) {self.terrainArray[position].name}")
        moveString += ", ".join(moveStringAdds)
        print(moveString + ".")


class game(object):

    def __init__(self):
        self.playerCharacters = []

        chatter = False
        recruit = playerCharacter(
                "Max", "Human", "Swordsman", chatter, 0)
        self.equipOnCharacter(
                equipment("Swords", "Middle Sword", 0, 0, 5, 0, 0), recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Lowe", "Hobbit", "Priest", chatter, 0)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 0, 0, 1, 3, 3), recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Tao", "Elf", "Fire Mage", chatter, 0)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 0, 0, 1, 3, 3), recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Luke", "Dwarf", "Warrior", chatter, 0)
        self.equipOnCharacter(
                equipment("Axes", "Short Axe", 0, 0, 5, 0, 0), recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Ken", "Centaur", "Knight", chatter, 0)
        self.equipOnCharacter(
                equipment("Spears", "Wooden Spear", 0, 1, 4, 0, 0), recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Hans", "Elf", "Archer", chatter, 0)
        self.equipOnCharacter(
                equipment("Arrows", "Wooden Arrow", 1, 1, 3, 0, 0), recruit)
        self.playerCharacters.append(recruit)
        self.party = self.playerCharacters[:6]
        battle(self.party, 1)

    def equipOnCharacter(self, equipment, character):
        if type(character) == str:
            pc = [
                    player for player in self.party
                    if player.name == character][0]
        elif type(character) == playerCharacter:
            pc = character
        if pc:
            if pc.equipment:
                incumbent = pc.equipment
                incumbent.equippedBy = None
            equipment.equippedBy = pc
            pc.equipment = equipment
            print(f"{pc.name} equipped the {equipment.name}.")


game = game()
