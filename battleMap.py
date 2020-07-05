from characters import equipment
from characters import playerCharacter
from characters import monster
from operator import itemgetter
import math
import random
import sys
import time


class battle(object):

    def __init__(self, game, party, num=None):
        self.game = game
        if input("Type skip to skip this battle: ") == "skip":
            game.battleStatus = 'victory'
            for unit in party:
                unit.levelUp(False)
            return
        if num:
            self.egressing = False
            if num == 1:
                self.battleField = battleField([
                        "Forest", "Grass", "Grass", "Ascending Stairway",
                        "Rubble", "Tiled Floor", "Tiled Floor", "Tiled Floor",
                        "Rubble", "Rubble", "Tiled Floor"],
                        [(monster("Goblin"), 7),
                                (monster("Traitor Knight"), 7),
                                (monster("Goblin"), 8),
                                (monster("Crazed Dwarf"), 9),
                                (monster("Crazed Dwarf"), 9),
                                (monster("Goblin"), 10),
                                (monster("Goblin"), 10)],
                        party)
            elif num == 2:
                self.battleField = battleField([
                        "Loose Rocks", "Loose Rocks", "Loose Rocks",
                        "Loose Rocks", "Loose Rocks", "Grass", "Forest",
                        "Grass", "Loose Rocks", "Grass", "Grass", "Path",
                        "Bridge", "Path", "Path", "Path", "Grass", "Grass"],
                        [(monster(
                                "Goblin", "Retreat-Defensive", "Weakest"),
                                3),
                                (monster(
                                        "Goblin", "Retreat-Defensive",
                                        "Weakest"), 3),
                                (monster(
                                        "Goblin", "Retreat-Defensive",
                                        "Weakest"), 3),
                                (monster(
                                        "Goblin", "Advance-Defensive",
                                        "Weakest"), 9),
                                (monster(
                                        "Goblin", "Advance-Defensive",
                                        "Weakest"), 9),
                                (monster(
                                        "Goblin", "Advance-Defensive",
                                        "Weakest"), 9),
                                (monster(
                                        "Crazed Dwarf", "Retreat-Defensive",
                                        "ChallengeAccepting"), 9),
                                (monster(
                                        "Crazed Dwarf", "Retreat-Defensive",
                                        "ChallengeAccepting"), 10),
                                (monster(
                                        "Crazed Dwarf", None,
                                        "ChallengeAccepting"), 10),
                                (monster(
                                        "Traitor Knight", "Advance-Defensive"),
                                        17),
                                (monster(
                                        "Traitor Knight", "Advance-Defensive"),
                                        17)],
                        party)
            elif num == 3:
                self.battleField = battleField([
                        "Path", "Path", "Path", "Path", "Path", "Path", "Path",
                        "Path", "Path", "Path", "Path", "Path", "Path"],
                        [(monster(
                                "Crazed Dwarf", "Advance-Defensive",
                                "ChallengeAccepting"), 5),
                                (monster(
                                        "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 5),
                                (monster(
                                        "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 5),
                                (monster(
                                        "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 7),
                                (monster(
                                        "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 7),
                                (monster("Giant Bat"), 8),
                                (monster("Giant Bat"), 9),
                                (monster("Giant Bat"), 9),
                                (monster("Giant Bat"), 9),
                                (monster("Giant Bat"), 10),
                                (monster("Traitor Knight"), 11),
                                (monster("Traitor Knight"), 11),
                                (monster("Traitor Knight"), 11),
                                (monster("Traitor Knight"), 11),
                                (monster("Traitor Knight"), 12)],
                        party)
            for unit in self.battleField.units:
                unit.hp = unit.stats["Stamina"] * 2
                unit.fp = unit.stats["Faith"]
                unit.mp = unit.stats["Intelligence"]
                unit.status = None
                if unit.equipment:
                    unit.fp += unit.equipment.fp
                    unit.mp += unit.equipment.mp
                if "Egress I" in unit.powers and unit.mp < self.mpCost(unit, 8):
                    print(f"warning: {unit.name} has insufficient mp to Egress")
            self.game.battleStatus = 'ongoing'
            while self.battleOn():
                self.doRound()

    def attack(self, unit, target):
        bf = self.battleField
        routEnemy = False
        doubleChanceArray = []
        doubleChance = math.floor(
                unit.stats["Dexterity"] + (
                        unit.stats["Dexterity"] * (unit.stats["Luck"] / 10)))
        if "Quick Shot" in unit.powers:
            doubleChance = math.ceil(doubleChance * 1.3)
        doubleChanceArray.extend([1] * (100 - unit.stats["Luck"]))
        doubleChanceArray.extend([2] * doubleChance)
        if "Luck: Enable Triple Attack" in unit.powers:
            doubleChanceArray.extend([3] * doubleChance)
        attackCount = random.choice(doubleChanceArray)
        for i in range(0, attackCount):
            if i == 0:
                print(f"{unit.name} attacks!")
                time.sleep(2./10)
            elif i > 0:
                print(f"{unit.name} attacks again!")
                time.sleep(2./10)
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
            if "Aimed Shot" not in unit.powers:
                dodgeSkill = math.floor(max(
                        target.stats["Intelligence"], target.stats["Luck"],
                        target.stats["Speed"]) * (1 + (
                                (target.stats["Luck"] / 10))))
                attackTypeArray.extend(["dodge"] * dodgeSkill)
            attackType = random.choice(attackTypeArray)
            if attackType == 'dodge':
                print(f"{target.name} dodges the attack!")
                self.giveExperience(unit, target, 1)
            else:
                if attackType == 'critical':
                    print("A Critical Attack!")
                damage = max(
                        unit.stats["Strength"], unit.stats["Dexterity"])
                if (
                        "Unarmed Attack: Increased Damage I"
                        in unit.powers and not unit.equipment):
                    damage *= 1.3
                    damage = math.ceil(damage)
                if "Defense: Melee Attacks I" in target.powers and (
                        bf.getUnitPos(unit) == bf.getUnitPos(target)):
                    damage *= 0.7
                    damage = math.floor(damage)
                if unit.equipment:
                    damage += unit.equipment.damage
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
                    targetPosition = field.getUnitPos(target)
                    field.terrainArray[targetPosition].units.remove(target)
                    if target in self.turnOrder:
                        self.turnOrder.remove(target)
                    del target
                    time.sleep(7./10)
                    return
                elif attackType == "routing":
                    routEnemy = True
                if routEnemy and ((i + 1) == attackCount):
                    if type(target) == playerCharacter:
                        moveTo = self.battleField.getUnitPos(target) - 1
                        if moveTo >= 0:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)
                    elif type(target) == monster:
                        moveTo = self.battleField.getUnitPos(target) + 1
                        if moveTo <= len(self.battleField.terrainArray) - 1:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)

    def battleOn(self):
        if self.egressing:
            self.game.battleStatus = 'egress'
            return False
        if any([
                unit for unit in self.battleField.units
                if type(unit) == playerCharacter and "Egress I"
                in unit.powers and unit.hp > 0]):
            if any([
                    unit for unit in self.battleField.units
                    if type(unit) == monster and unit.hp > 0]):
                return True
            else:
                print("You are victorious!")
                self.game.battleStatus = 'victory'
                return False
        else:
            print("D E F E A T E D")
            print("")
            self.game.battleStatus = 'defeat'
            print("A priest managed to recall your soul from the grave.")
            print("")
            return False

    def castSpell(self, unit, spellName, targetId):
        if spellName == "Blaze I":
            unit.mp -= self.mpCost(unit, 2)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(6, target.hp)
            print(f"{unit.name} deals {damage} damage to {target.name}!")
            target.hp -= damage
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                print(f"{target.name} dies!")
                field = self.battleField
                targetPosition = field.getUnitPos(target)
                field.terrainArray[targetPosition].units.remove(target)
                if target in self.turnOrder:
                    self.turnOrder.remove(target)
                del target
                time.sleep(7./10)
                return
        elif spellName == "Egress I":
            unit.mp -= self.mpCost(unit, 8)
            print(f"{unit.name} casts {spellName}!")
            self.egressing = True
            print(
                    "A whistling fills your ears as the battlefield melts "
                    "into a bright light.")
            print(
                    "The light becomes too bright to bear, and you blink to "
                    "block it out.")
            print(
                    "When you open your eyes, you are somewhere else, with a "
                    "priest, safe.")
            print("")
            print("")
            self.battleOn()
        elif spellName == "Heal I":
            unit.fp -= 3
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
        elif monster.attackProfile == "Singer":
            if monster.allowedAttacks:
                self.doVocalAttack(monster)
        elif monster.attackProfile == "Weakest":
            candidates = [
                    target for target in monster.allowedAttacks
                    if target.hp == min(
                            unit.hp for unit in monster.allowedAttacks)]
            target = random.choice(candidates)
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
        if unit.status == "sleep":
            resistSkill = sum(
                    unit.stats["Faith"], unit.stats["Intelligence"],
                    unit.stats["Stamina"])
            resistChance = math.floor(
                    resistSkill + (resistSkill * (unit.stats["Luck"] / 10)))
            resistArray = []
            resistArray.append(['resist'] * resistChance)
            resistArray.append(['fail'] * (100 - (unit.stats["Luck"])))
            result = random.choice(resistArray)
            if result == 'resist':
                unit.status = None
            elif unit.status == 'sleep':
                print(f"{unit.name} is asleep.")
                return
        position = self.battleField.getUnitPos(unit)
        tile = self.battleField.terrainArray[position]
        otherUnits = ", ".join([
                tileUnit.name for tileUnit in tile.units if tileUnit != unit])
        if type(unit) == playerCharacter:
            allowedCommands = ["W", "w"]
            if not moved:
                print("")
                if type(unit) == playerCharacter:
                    maxHP = unit.stats["Stamina"] * 2
                    maxFP = unit.stats["Faith"]
                    maxMP = unit.stats["Intelligence"]
                    maxMv = unit.stats["Speed"]
                    mvType = ""
                    if "Mounted Movement" in unit.powers:
                        mvType = "M"
                    if unit.equipment:
                        maxFP += unit.equipment.fp
                        maxMP += unit.equipment.mp
                    print(
                            f"It's {unit.name}'s turn! "
                            f"(HP: {unit.hp}/{maxHP} FP: {unit.fp}/{maxFP} "
                            f"MP: {unit.mp}/{maxMP} "
                            f"Move: {unit.movementPoints}/{maxMv}{mvType})")
                    time.sleep(2./10)
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
            vocalEnabled = self.battleField.checkVocal(unit)
            if vocalEnabled:
                print("Type (V) to make a vocal attack.")
                allowedCommands.append("V")
                allowedCommands.append("v")
            print("Type (W) to wait.")
            command = None
            while command not in allowedCommands:
                command = input()
            if command in ("M", "m"):
                moveTo = None
                while moveTo not in unit.allowedMovement:
                    try:
                        moveTo = int(input("Type a number to move to: "))
                    except ValueError:
                        moveTo = None
                self.battleField.move(unit, moveTo)
                self.doTurn(unit, True)
            if command in ("A", "a"):
                attackTarget = None
                while attackTarget not in [
                        unit.allowedAttacks.index(target)
                        for target in unit.allowedAttacks]:
                    try:
                        attackTarget = int(input("Type a number to attack: "))
                    except ValueError:
                        attackTarget = None
                self.doAttack(unit, attackTarget)
            if command in ("S", "s"):
                spellChoice = None
                spellTarget = None
                spellKeys = list(unit.allowedSpells.keys())
                while spellChoice not in [
                        spellKeys.index(spell) for spell in spellKeys]:
                    try:
                        spellChoice = int(input(
                                "Type the number of the spell to cast: "))
                    except ValueError:
                        spellChoice = None
                spellToCast = spellKeys[spellChoice]
                self.battleField.printSpellTargetString(unit, spellToCast)
                targetList = unit.allowedSpells[spellToCast]
                while targetList != 'Self' and spellTarget not in (
                        targetList.index(target) for target in targetList):
                    try:
                        spellTarget = int(input("Type a number to target: "))
                    except ValueError:
                        spellTarget = None
                self.castSpell(unit, spellToCast, spellTarget)
            if command in ("V", "v"):
                self.doVocalAttack(unit)
            if command in ("W", "w"):
                return
        elif type(unit) == monster:
            print("")
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
            position = self.battleField.getUnitPos(unit)
            attackEnabled = self.battleField.checkAttack(unit, position)
            if attackEnabled:
                self.doMonsterAttack(unit)
            else:
                print(f"{unit.name} waited.")
        time.sleep(6./10)
        endBattle = not self.battleOn()
        return endBattle

    def doVocalAttack(self, unit):
        bf = self.battleField
        position = bf.getUnitPos(unit)
        print(f"{unit.name} sings out a note of power!")
        attackTypeArray = []
        attackTypeArray.extend(
                ["normal"] * (100 - (
                        unit.stats["Luck"])))
        criticalChance = math.floor(
                unit.stats["Voice"] + (
                        unit.stats["Voice"] * (
                                unit.stats["Luck"] / 10)))
        attackTypeArray.extend(["critical"] * criticalChance)
        if "Sonorous Voice" in unit.powers:
            sleepChance = math.floor(unit.stats["Luck"])
            attackTypeArray.extend(["sleep"] * sleepChance)
        routSkill = max(unit.stats["Charisma"], unit.stats["Voice"])
        routChance = math.floor(
                routSkill + (routSkill * (unit.stats["Luck"] / 10)))
        attackTypeArray.extend(["routing"] * routChance)
        friendSound = sum([
                tileUnit.stats["Voice"] for tileUnit in
                bf.terrainArray[position].units
                if type(tileUnit) == type(unit)])
        attackType = random.choice(attackTypeArray)
        if attackType == "critical":
            print("A Thunderous Attack!")
            friendSound *= 2
        enemySound = sum([
                tileUnit.stats["Voice"] for tileUnit in
                bf.terrainArray[position].units
                if type(tileUnit) != type(unit)])
        amount = friendSound - enemySound
        if amount <= 0:
            if type(unit) == playerCharacter:
                print(
                        "The sound of the note is drowned out by the sound of the "
                        "enemy!")
            elif type(unit) == monster:
                print(
                        "The sound of the note is drowned out by the holy song of "
                        "the Force.")
            return
        damage = math.ceil(amount / 12)
        damage = max(damage, 1)
        for target in bf.terrainArray[position].units:
            if type(target) != type(unit):
                damage = min(damage, target.hp)
                print(f"The note deals {damage} damage to {target.name}!")
                target.hp -= damage
                self.giveExperience(unit, target, damage)
                if target.hp <= 0:
                    print(f"{target.name} dies!")
                    field = self.battleField
                    targetPosition = field.getUnitPos(target)
                    field.terrainArray[targetPosition].units.remove(target)
                    if target in self.turnOrder:
                        self.turnOrder.remove(target)
                    del target
                    time.sleep(7./10)
                elif attackType == "routing":
                    if type(target) == playerCharacter:
                        moveTo = self.battleField.getUnitPos(target) - 1
                        if moveTo >= 0:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)
                    elif type(target) == monster:
                        moveTo = self.battleField.getUnitPos(target) + 1
                        if moveTo <= len(self.battleField.terrainArray) - 1:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)
                elif attackType == "sleep":
                    target.status = "sleep"

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

    def mpCost(self, unit, amount):
        cost = amount
        if "Magic: Cost Reduction I" in unit.powers:
            cost = math.ceil(cost * 0.75)
        return cost


class battleTile(object):
    """docstring for BattleTile"""

    def __init__(self, terrain):
        self.name = terrain
        self.cost = 5
        # Assign cost
        if self.name in ("Bridge", "Path", "Tiled Floor"):
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
                        candidate = True
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
                # Stealthy Movement prevents blocking for 2 tiles
                if "Stealthy Movement" in unit.powers and (
                        abs(position - self.getUnitPos(unit)) <= 2):
                    blocked = False
                else:
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
        if "Blaze I" in unit.powers and unit.mp >= self.mpCost(unit, 2):
            targets = [
                    target for target in currentTile.units
                    if type(target) == enemy]
            if any(targets):
                unit.allowedSpells["Blaze I"] = targets
        if "Egress I" in unit.powers and unit.mp >= self.mpCost(unit, 8):
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

    def checkVocal(self, unit):
        if unit.movementPoints < 4:
            return False
        position = self.getUnitPos(unit)
        currentTile = self.terrainArray[position]
        if any([
                tileUnit for tileUnit in currentTile.units
                if type(tileUnit) != type(unit)]):
            return sum([tileUnit.level for tileUnit in currentTile.units
                if type(tileUnit) == type(unit)]) >= sum([
                tileUnit.level for tileUnit in currentTile.units
                if type(tileUnit) != type(unit)])
        else:
            return False

    def doMonsterMove(self, monster, position, assignMoveProfile=None):
        if assignMoveProfile:
            monster.moveProfile = assignMoveProfile
        if monster.moveProfile == "Advance-Defensive":
            if monster.hp < monster.stats["Stamina"] * 2:
                monster.moveProfile = "Aggressive"
                self.doMonsterMove(monster, position)
                return
            else:
                moveTo = min(monster.allowedMovement)
                if position == 0 or moveTo > position:
                    monster.moveProfile = "Defensive"
                    self.doMonsterMove(monster, position)
                    return
            self.move(monster, moveTo)
        elif monster.moveProfile == "Aggressive":
            # will not move if in melee range of enemies
            if any([
                    unit for unit in self.terrainArray[position].units
                    if type(unit) == playerCharacter]):
                return
            # move as far forward as possible to tiles with enemies
            candidates = []
            for position in monster.allowedMovement:
                if any([
                        unit for unit in self.terrainArray[position].units
                        if type(unit) == playerCharacter]):
                    candidates.append(position)
            if candidates:
                moveTo = min(candidates)
            else:
                # move as far forward as possible
                moveTo = min(monster.allowedMovement)
            self.move(monster, moveTo)
        elif monster.moveProfile == "Aggressive-Singer":
            # just like aggressive but prefers to move to places with larger
            # concentration of enemies and friends
            candidates = []
            maxPCs = max([len([
                    unit for unit in self.terrainArray[position].units
                    if type(unit) == playerCharacter])
                    for position in monster.allowedMovement])
            if maxPCs > 0:
                for position in monster.allowedMovement:
                    if len([
                            unit for unit in self.terrainArray[position].units
                            if type(unit) == playerCharacter]) == maxPCs:
                        candidates.append(position)
                if any(candidates):
                    candidates2 = []
                    maxMonsters = max([len([
                            unit for unit in self.terrainArray[position].units
                            if type(unit) == monster])
                            for position in candidates])
                    for position in candidates:
                        if len([
                                unit for unit in self.terrainArray[position].units
                                if type(unit) == monster]) == maxMonsters:
                            candidates2.append(position)
                    if any(candidates2):
                        moveTo = random.choice(candidates2)
                    else:
                        moveTo = min(monster.allowedMovement)
                else:
                    moveTo = min(monster.allowedMovement)
            else:
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
                else:
                    return
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

    def getUnitPos(self, unit):
        for tile in self.terrainArray:
            if unit in tile.units:
                return self.terrainArray.index(tile)

    def move(self, unit, moveTo):
        fromPosition = self.getUnitPos(unit)
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

    def mpCost(self, unit, amount):
        cost = amount
        if "Magic: Cost Reduction I" in unit.powers:
            cost = math.ceil(cost * 0.75)
        return cost

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
        for i in unit.allowedSpells:
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
                    f"({count}) {target.name} "
                    f"(HP: {target.hp}/{targetHealth})")
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
        self.battleStatus = None
        self.money = 0

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
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(1, 'king')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'king')
            battle(self, self.party, 1)
        print("")
        print("The party arrives at a small hut overlooking the water.")
        print("There, a lonely priest lives in solitude, a penance.")
        print(
                "A Half-Giant, turned from his life of butchery to that of a "
                "holy monk,")
        print("has come to bring him his supplies.")
        print("The monk, Gong, joins your cause.")
        print("")
        print("You spy a pillar of smoke rising from the direction of home.")
        print("That's not good....")
        print("")
        recruit = playerCharacter("Gong", "Half-Giant", "Monk", chatter, 1)
        recruit.levelUp(chatter)
        self.playerCharacters.append(recruit)
        self.party = self.playerCharacters[:7]
        self.reckoning(3, 'lonely priest')
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(1, 'lonely priest')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'lonely priest')
            battle(self, self.party, 2)
        print("")
        print("The party arrives at the Holy City of . It is burning.")
        print("Too late to intervene, you watch in horror as your mentor ")
        print("and your king are slain by a dark swordsman who looks exactly ")
        print("like you. The swordsman disappears into a black void")
        print("If you weren't in the room when this happened, you're sure ")
        print("that the Knights of  would have posted a bounty on your head.")
        print("")
        print("In the aftermath of the assassination, your mentor's daughter,")
        print(" Mae, joins you. With her is a washed up former city guard, ")
        print("drunk on wine and thirsty for vengence, Gort.")
        print("")
        recruit = playerCharacter("Gong", "Half-Giant", "Monk", chatter, 1)
        recruit.levelUp(chatter)
        recruit = playerCharacter("Mae", "Centaur", "Knight", chatter, 2)
        self.playerCharacters.append(recruit)
        self.equipOnCharacter(
                equipment("Lances", "Bronze Lance", 0, 0, 6, 0, 0), recruit)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit = playerCharacter("Gort", "Dwarf", "Warrior", chatter, 2)
        self.playerCharacters.append(recruit)
        self.equipOnCharacter(
                equipment("Axes", "Short Axe", 0, 0, 5, 0, 0), recruit)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        self.playerCharacters.append(recruit)
        self.party = self.playerCharacters[:9]
        self.reckoning(3, 'widow of your mentor')
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(1, 'widow of your mentor')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'widow of your mentor')
            battle(self, self.party, 3)

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

    def reckoning(self, bounty, patron):
        clergyCost = sum([
                unit.level * 10 for unit in self.playerCharacters
                if unit.hp <= 0])
        trophies = sum([len(unit.trophies) for unit in self.playerCharacters])
        reward = trophies * bounty
        amount = reward - clergyCost
        if amount > 0:
            if clergyCost > 0:
                print(
                        f"The {patron} awards you with {amount} scroulings! "
                        "The priests recalled the souls of your party.")
            else:
                print(f"The {patron} awards you with {amount} scroulings!")
            self.money += amount
        elif amount < 0:
            if -amount >= self.money:
                print(
                        f"The priests take all of your money to cover the "
                        f"cost of the prayers that saved you. Consider them "
                        f"generous.")
            else:
                print(
                        f"The priests request {-amount} scroulings for the "
                        f"prayers that recalled the souls of your party.")


game = game()
