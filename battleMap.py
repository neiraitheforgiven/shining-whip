from characters import equipment
from characters import playerCharacter
from characters import monster
from operator import itemgetter
from shopping import shop
import math
import random
import time


class battle(object):

    def __init__(self, game, party, num=None):
        self.game = game
        self.party = party
        if input("Type skip to skip this battle: ") == "skip":
            game.battleStatus = 'victory'
            for unit in party:
                unit.levelUp(False)
            return
        if num:
            self.egressing = False
            if num == 1:
                self.battleField = battleField([
                        "Forest", "Grass", "Grass", "Upward Stair",
                        "Rubble", "Tiled Floor", "Tiled Floor", "Tiled Floor",
                        "Rubble", "Rubble", "Tiled Floor"],
                        [(monster("Goblin"), 7),
                                (monster("Traitor Knight"), 7),
                                (monster("Goblin"), 8),
                                (monster("Crazed Dwarf"), 9),
                                (monster("Crazed Dwarf"), 9),
                                (monster("Goblin"), 10),
                                (monster("Goblin"), 10)],
                        party, game)
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
                        party, game)
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
                        party, game)
            elif num == 4:
                self.battleField = battleField([
                        "Path", "Path", "Path", "Bridge", "Bridge", "Path",
                        "Path", "Bridge", "Path", "Path", "Path", "Bridge",
                        "Bridge", "Path", "Path", "Path", "Path", "Bridge",
                        "Bridge", "Path"],
                        [(monster(
                                "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 11),
                                (monster(
                                        "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 11),
                                (monster(
                                        "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 11),
                                (monster(
                                        "Crazed Dwarf", "Advance-Defensive",
                                        "ChallengeAccepting"), 11),
                                (monster("Giant Bat"), 10),
                                (monster("Giant Bat"), 13),
                                (monster("Giant Bat"), 13),
                                (monster("Giant Bat"), 14),
                                (monster("Traitor Knight", "SlowAdvance"), 18),
                                (monster("Traitor Knight", "SlowAdvance"), 18),
                                (monster("Traitor Knight", "SlowAdvance"), 18),
                                (monster("Traitor Knight", "SlowAdvance"), 18),
                                (monster("Sniper"), 19),
                                (monster("Sniper"), 19),
                                (monster("Dark Apprentice"), 19)],
                        party, game)
            for unit in self.battleField.units:
                unit.hp = unit.maxHP()
                unit.fp = unit.stats["Faith"]
                unit.mp = unit.stats["Intelligence"]
                unit.status = None
                if unit.equipment:
                    unit.fp += unit.equipment.fp
                    unit.mp += unit.equipment.mp
                if self.getPower(unit, "Egress I") and unit.mp < self.mpCost(
                        unit, 8):
                    print(f"warning: {unit.name} has too few mp to Egress")
            self.game.battleStatus = 'ongoing'
            while self.battleOn():
                self.doRound()

    def attack(self, unit, target):
        bf = self.battleField
        routEnemy = False
        doubleChanceArray = []
        dex = self.getStat(unit, "Dexterity")
        luck = self.getStat(unit, "Luck")
        doubleChance = math.floor(dex + (dex * (luck / 10)))
        if self.getPower(unit, "Quick Shot"):
            doubleChance = math.ceil(doubleChance * 1.3)
        doubleChanceArray.extend([1] * (100 - luck))
        doubleChanceArray.extend([2] * doubleChance)
        if self.getPower(unit, "Luck: Enable Triple Attack"):
            doubleChanceArray.extend([3] * doubleChance)
        attackCount = random.choice(doubleChanceArray)
        for i in range(0, attackCount):
            if i == 0:
                print(f"{unit.name} attacks!")
                time.sleep(2. / 10)
            elif i > 0:
                print(f"{unit.name} attacks again!")
                time.sleep(2. / 10)
            attackTypeArray = []
            targetLuck = self.getStat(target, "Luck")
            attackTypeArray.extend(["normal"] * (100 - (luck - targetLuck)))
            strength = self.getStat(unit, "Strength")
            criticalChance = math.floor(strength + (strength * (luck / 10)))
            attackTypeArray.extend(["critical"] * criticalChance)
            routSkill = max(
                    self.getStat(unit, "Charisma"),
                    self.getStat(unit, "Voice"))
            routChance = math.floor(routSkill + (routSkill * (luck / 10)))
            attackTypeArray.extend(["routing"] * routChance)
            if not self.getPower(unit, "Aimed Shot"):
                dodgeSkill = math.floor(max(
                        self.getStat(target, "Intelligence"), targetLuck,
                        self.getStat(target, "Speed")) * (1 + (
                                (targetLuck / 10))))
                attackTypeArray.extend(["dodge"] * dodgeSkill)
            attackType = random.choice(attackTypeArray)
            if attackType == 'dodge':
                print(f"{target.name} dodges the attack!")
                self.giveExperience(unit, target, 1)
            else:
                if attackType == 'critical':
                    print("A Critical Attack!")
                damage = max(strength, dex)
                if unit.equipment:
                    damageString = f"{unit.equipment.type}: Increased Damage "
                else:
                    damageString = "Unarmed Attack: Increased Damage "
                if self.getPower(unit, damageString + "I"):
                    damage *= 1.3
                if self.getPower(unit, damageString + "II"):
                    damage *= 1.3
                if self.getPower(unit, damageString + "III"):
                    damage *= 1.3
                if self.getPower(unit, damageString + "IV"):
                    damage *= 1.3
                damage = math.ceil(damage)
                if self.getPower(target, "Defense: Melee Attacks I") and (
                        bf.getUnitPos(unit) == bf.getUnitPos(target)):
                    damage *= 0.7
                    damage = math.floor(damage)
                if unit.equipment:
                    damage += unit.equipment.damage
                if attackType != 'critical':
                    damage -= max(
                            self.getStat(target, "Strength"),
                            self.getStat(target, "Dexterity"),
                            self.getStat(target, "Faith"))
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
                    time.sleep(7. / 10)
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
                if type(unit) == playerCharacter and self.getPower(
                        unit, "Egress I") and unit.hp > 0]):
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
            if self.getPower(target, "Defense: Magic"):
                damage = min(4, target.hp)
            print(f"{unit.name} deals {damage} damage to {target.name}!")
            target.hp -= damage
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                self.kill(target)
        elif spellName == "Blaze II":
            unit.mp -= self.mpCost(unit, 6)
            position = unit.allowedSpells[spellName][targetId]
            # target will be a position
            print(f"{unit.name} casts {spellName}!")
            field = self.battleField
            for target in field.terrainArray[position].units:
                if type(target) != type(unit):
                    damage = min(9, target.hp)
                    if self.getPower(target, "Defense: Magic"):
                        damage = min(7, target.hp)
                    print(
                            f"{unit.name} deals {damage} damage to "
                            f"{target.name}!")
                    target.hp -= damage
                    self.giveExperience(unit, target, damage)
                    if target.hp <= 0:
                        self.kill(target)
        elif spellName == "Detox I":
            unit.mp -= self.mpCost(unit, 3)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            target.status = None
            print(f"{target.name} recovers!")
            self.giveExperience(unit, target, 10)
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
        elif spellName == "Freeze I":
            unit.mp -= self.mpCost(unit, 3)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(9, target.hp)
            if self.getPower(target, "Defense: Magic"):
                damage = min(7, target.hp)
            print(f"{unit.name} deals {damage} damage to {target.name}!")
            target.hp -= damage
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                self.kill(target)
        elif spellName == "Freeze II":
            unit.mp -= self.mpCost(unit, 7)
            targetTile = self.battleField.getUnitPos(unit)
            for target in targetTile.units:
                if type(unit) != type(target):
                    print(f"{unit.name} casts {spellName} on {target.name}!")
                    damage = min(14, target.hp)
                    if self.getPower(target, "Defense: Magic"):
                        damage = min(10, target.hp)
                    print(
                            f"{unit.name} deals {damage} damage to "
                            f"{target.name}!")
                    target.hp -= damage
                    self.giveExperience(unit, target, damage)
                    if target.hp <= 0:
                        self.kill(target)
        elif spellName == "Frezze III":
            unit.mp -= self.mpCost(unit, 10)
            targetTile = unit.allowedSpells[spellName][targetId]
            for target in targetTile.units:
                if type(unit) != type(target):
                    print(f"{unit.name} casts {spellName} on {target.name}!")
                    damage = min(20, target.hp)
                    if self.getPower(target, "Defense: Magic"):
                        damage = min(17, target.hp)
                    print(
                            f"{unit.name} deals {damage} damage to "
                            f"{target.name}!")
                    target.hp -= damage
                    self.giveExperience(unit, target, damage)
                    if target.hp <= 0:
                        self.kill(target)
        elif spellName == "Freeze IV":
            unit.mp -= self.mpCost(unit, 12)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(52, target.hp)
            if self.getPower(target, "Defense: Magic"):
                damage = min(45, target.hp)
            print(f"{unit.name} deals {damage} damage to {target.name}!")
            target.hp -= damage
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                self.kill(target)
        elif spellName == "Heal I":
            unit.fp -= 3
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            healing = min(15, (target.maxHP() - target.hp))
            print(f"{unit.name} restores {healing} health to {target.name}!")
            target.hp += healing
            self.giveExperience(unit, target, healing)
        elif spellName == "Heal II":
            unit.fp -= 6
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            healing = min(15, (target.maxHP - target.hp))
            print(f"{unit.name} restores {healing} health to {target.name}!")
            target.hp += healing
            self.giveExperience(unit, target, healing)

    def determineInitiative(self):
        initiativeOrder = []
        random.shuffle(self.battleField.units)
        for unit in self.battleField.units:
            luck = self.getStat(unit, "Luck")
            initiative = max(
                    self.getStat(unit, "Charisma"),
                    self.getStat(unit, "Speed"),
                    self.getStat(unit, "Dexterity"))
            initiativeOrder.append((unit, initiative, luck))
            while initiative > 15:
                initiative -= 15
                initiativeOrder.append((unit, initiative, luck))
        initiativeOrder = sorted(
                initiativeOrder, key=itemgetter(1, 2), reverse=True)
        return initiativeOrder

    def doAttack(self, unit, targetId):
        target = unit.allowedAttacks[targetId]
        self.attack(unit, target)

    def doMonsterAttack(self, monster):
        field = self.battleField
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
                    if self.getStat(target, "Charisma") == max(
                            self.getStat(unit, "Charisma")
                            for unit in candidates)]
            candidates = [
                    target for target in candidates
                    if self.getStat(target, "Strength") == max(
                            self.getStat(unit, "Strength")
                            for unit in candidates)]
            target = random.choice(candidates)
            self.attack(monster, target)
        elif monster.attackProfile == "Random":
            target = random.choice(monster.allowedAttacks)
            self.attack(monster, target)
        elif monster.attackProfile == "Singer":
            if monster.allowedAttacks:
                self.doVocalAttack(monster)
        elif monster.attackProfile == "Spellcaster":
            canCast = False
            field = self.battleField
            if self.getPower(monster, "Blaze II"):
                if monster.mp >= self.mpCost(monster, 6):
                    canCast = True
                    position = field.getUnitPos(monster)
                    minRange = max(0, position - 1)
                    maxRange = min(position + 1, len(field.terrainArray) - 1)
                targets = []
                targetHP = max([
                        sum(unit.hp) for unit in [
                                tile.units for tile in
                                field.terrainArray[minRange:maxRange + 1]]])
                targets = [
                        tile for tile in
                        field.terrainArray[minRange:maxRange + 1]
                        if [sum([unit.hp for unit in tile.units]) == targetHP]]
                target = random.choice(targets)
                if any(target):
                    self.castSpell(monster, "Blaze II", target)
            if not canCast:
                monster.attackProfile = "Random"
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
            unit.movementPoints = self.getStat(unit, "Speed")
        for unit in self.turnOrder:
            # unit may have died since this loop started.
            if unit[0].hp <= 0:
                continue
            endBattle = self.doTurn(unit[0])
            if endBattle:
                return

    def doTurn(self, unit, moved=False):
        if unit.status == "sleep":
            luck = self.getStat(unit, "Luck")
            resistSkill = sum([
                    self.getStat(unit, "Faith"),
                    self.getStat(unit, "Intelligence"),
                    self.getStat(unit, "Stamina")])
            resistChance = math.floor(
                    resistSkill + (resistSkill * (luck / 10)))
            resistArray = []
            resistArray.append(['resist'] * resistChance)
            resistArray.append(['fail'] * (min(10, 50 - (resistChance))))
            result = random.choice(resistArray)
            if result == 'resist':
                if unit.status == 'sleep':
                    print(f"{unit.name} woke up!")
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
                self.battleField.viewMapFromUnit(unit)
                print("")
                if type(unit) == playerCharacter:
                    maxHP = unit.maxHP()
                    maxFP = unit.stats["Faith"]
                    maxMP = unit.stats["Intelligence"]
                    maxMv = unit.stats["Speed"]
                    fame = self.getFameBonus(unit)
                    mvType = ""
                    if self.getPower(unit, "Mounted Movement"):
                        mvType = "M"
                    if unit.equipment:
                        maxFP += unit.equipment.fp
                        maxMP += unit.equipment.mp
                    print(
                            f"It's {unit.name}'s turn! "
                            f"(HP: {unit.hp}/{maxHP} FP: {unit.fp}/{maxFP} "
                            f"MP: {unit.mp}/{maxMP} "
                            f"Move: {unit.movementPoints}/{maxMv}{mvType} "
                            f"Fame Bonus: {fame}%)")
                    time.sleep(2. / 10)
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
        time.sleep(6. / 10)
        endBattle = not self.battleOn()
        return endBattle

    def doVocalAttack(self, unit):
        bf = self.battleField
        position = bf.getUnitPos(unit)
        print(f"{unit.name} sings out a note of power!")
        cha = self.getStat(unit, "Charisma")
        luck = self.getStat(unit, "Luck")
        voice = self.getStat(unit, "Voice")
        attackTypeArray = []
        attackTypeArray.extend(["normal"] * (100 - (luck)))
        criticalChance = math.floor(voice + (voice * (luck / 10)))
        attackTypeArray.extend(["critical"] * criticalChance)
        friendSound = sum([
                self.getStat(tileUnit, "Voice") for tileUnit in
                bf.terrainArray[position].units
                if type(tileUnit) == type(unit)])
        attackType = random.choice(attackTypeArray)
        if attackType == "critical":
            print("A Thunderous Attack!")
            friendSound *= 2
        enemySound = sum([
                self.getStat(tileUnit, "Voice") for tileUnit in
                bf.terrainArray[position].units
                if type(tileUnit) != type(unit)])
        amount = max(1, friendSound - enemySound)
        damage = math.ceil(amount / 12)
        damage = max(damage, 1)
        for target in bf.terrainArray[position].units:
            if type(target) != type(unit):
                attackTypeArray = []
                attackTypeArray.extend(["normal"] * (100 - (luck)))
                if self.getPower(unit, "Sonorous Voice"):
                    sleepChance = luck
                    attackTypeArray.extend(["sleep"] * sleepChance)
                routSkill = max(cha, voice)
                routChance = math.floor(routSkill + (routSkill * (luck / 10)))
                attackTypeArray.extend(["routing"] * routChance)
                attackType = random.choice(attackTypeArray)
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
                    time.sleep(7. / 10)
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
                    print(f"{target.name} fell asleep!")

    def getFameBonus(self, unit):
        return self.battleField.getFameBonus(unit)

    def getPower(self, unit, name):
        return self.battleField.getPower(unit, name)

    def getStat(self, unit, statName):
        return self.battleField.getStat(unit, statName)

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

    def kill(self, target):
        print(f"{target.name} dies!")
        field = self.battleField
        targetPosition = field.getUnitPos(target)
        field.terrainArray[targetPosition].units.remove(target)
        if target in self.turnOrder:
            self.turnOrder.remove(target)
        del target
        time.sleep(7. / 10)
        return

    def mpCost(self, unit, amount):
        cost = amount
        if self.getPower(unit, "Magic: Cost Reduction I"):
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
                "Upward Stair", "Downward Stair", "Loose Rocks"):
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

    def __init__(self, listOfTiles, listOfUnits, party, game):
        self.game = game
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

    def calculatePossibleMovement(
            self, unit, movementPoints, position, directionIsHigher,
            unstable, bonusSpent=False):
        tile = self.terrainArray[position]
        # calculate if there is space
        if not unstable:
            unstable = tile.unstable
        if movementPoints <= 0 or (
                self.getPower(unit, "Unhindered Movement") and (
                        movementPoints < 5)):
            # mounted units may have bonus movement if they move on solids
            if (
                    self.getPower(unit, "Mounted Movement") and not (
                            bonusSpent) and not unstable):
                bonusSpent = True
            else:
                return
        candidate = False
        if len([
                tileUnit for tileUnit in tile.units
                if type(tileUnit) == type(unit)]) < 4:
            candidate = True
        # remove movementPoints
        if self.getPower(unit, "Flying Movement") or (
                self.getPower(unit, "Unhindered Movement")):
            movementPoints = movementPoints - 5
        else:
            movementPoints = movementPoints - tile.cost
        if movementPoints <= 0 or (
                self.getPower(unit, "Unhindered Movement") and (
                        movementPoints < 5)):
            # mounted units may have bonus movement if they move on solids
            if (self.getPower(unit, "Mounted Movement") and not (
                    self.getPower(unit, "Flying Movement"))):
                if unstable:
                    if directionIsHigher:
                        if position == self.getUnitPos(unit) + 1:
                            bonusSpent = True
                            candidate = True
                        else:
                            return  # you forfeit your final movement
                    else:
                        if position == self.getUnitPos(unit) - 1:
                            bonusSpent = True
                            candidate = True
                        else:
                            return  # you forfeit your final movement
                else:
                    if not bonusSpent:
                        bonusSpent = True  # You get one more movement
                        candidate = True
                        movementPoints = 1
            if candidate:
                unit.allowedMovement.append(position)
            if movementPoints <= 0 or (
                        self.getPower(unit, "Unhindered Movement") and (
                                movementPoints < 5)):
                return
        else:
            if candidate:
                unit.allowedMovement.append(position)
        if not self.getPower(unit, "Movement: Ignore Enemies"):
            # calculate if we are blocked
            if len([
                    tileUnit for tileUnit in tile.units
                    if type(tileUnit) != type(unit)]) >= 2:
                # Stealthy Movement prevents blocking for 2 tiles
                if self.getPower(unit, "Stealthy Movement") and (
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
        if minRange == 0 and maxRange == 0:
            unit.allowedAttacks = [
                    target for target in currentTile.units
                    if type(unit) != type(target)]
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
                    if type(tileUnit) != type(unit):
                        unit.allowedAttacks.append(tileUnit)
            return bool(unit.allowedAttacks)

    def checkMove(self, unit, position):
        unit.allowedMovement = []
        currentTile = self.terrainArray[position]
        unstable = currentTile.unstable
        if self.getPower(unit, "Movement: Ignore Enemies"):
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
        if self.getPower(unit, "Blaze I") and unit.mp >= self.mpCost(unit, 2):
            targets = [
                    target for target in currentTile.units
                    if type(target) != type(unit)]
            if any(targets):
                unit.allowedSpells["Blaze I"] = targets
        if self.getPower(unit, "Detox I") and unit.mp >= self.mpCost(unit, 3):
            targets = [
                    target for target in currentTile.units
                    if type(target) == type(unit) and target.status]
            if any(targets):
                unit.allowedSpells["Detox I"] = targets
        if self.getPower(unit, "Egress I") and unit.mp >= self.mpCost(unit, 8):
            unit.allowedSpells["Egress I"] = 'Self'
        if self.getPower(unit, "Freeze I") and unit.mp >= self.mpCost(unit, 3):
            targets = [
                    target for target in currentTile.units
                    if type(target) != type(unit)]
            if any(targets):
                unit.allowedSpells["Freeze I"] = targets
        if (
                self.getPower(unit, "Freeze II") and (
                unit.mp >= self.mpCost(unit, 7))):
            targets = [
                    target for target in currentTile.units
                    if type(target) != type(unit)]
            if any(targets):
                unit.allowedSpells["Freeze II"] = currentTile
        if (
                self.getPower(unit, "Freeze III") and (
                unit.mp >= self.mpCost(unit, 10))):
            targetTiles = []
            minRange = max(0, (position - 1))
            maxRange = min((position + 1), len(self.terrainArray) - 1)
            for tile in self.terrainArray[minRange:(maxRange + 1)]:
                tileTargets = [
                    target for target in tile.units
                    if type(target) != type(unit)]
                if any(tileTargets):
                    targetTiles.append(tile)
                    continue
            if any(targetTiles):
                unit.allowedSpells["Freeze III"] = targetTiles
        if (
                self.getPower(unit, "Freeze IV") and (
                unit.mp >= self.mpCost(unit, 12))):
            targets = []
            minRange = max(0, position - 2)
            maxRange = min((position + 2), len(self.terrainArray) - 1)
            for tile in self.terrainArray[minRange:(maxRange + 1)]:
                tileTargets = [
                    target for target in tile.units
                    if type(target) != type(unit)]
                if any(tileTargets):
                    targets.extend(target for target in tileTargets)
            if any(targets):
                unit.allowedSpells["Freeze IV"] = targets
        if self.getPower(unit, "Heal I") and unit.fp >= 3:
            targets = [
                    target for target in currentTile.units
                    if type(target) == type(unit) and target.hp < (
                            target.maxHP())]
            if any(targets):
                unit.allowedSpells["Heal I"] = targets
        if self.getPower(unit, "Heal II") and unit.fp >= 6:
            targets = []
            minRange = max(0, (position - 1))
            maxRange = min((position + 1), len(self.terrainArray) - 1)
            for tile in self.terrainArray[minRange:(maxRange + 1)]:
                tileTargets = [
                    target for target in tile.units
                    if type(target) == type(unit) and target.hp < (
                            target.maxHP())]
                if any(tileTargets):
                    targets.extend(target for target in tileTargets)
            if any(targets):
                unit.allowedSpells["Heal II"] = targets

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
            return sum([
                    tileUnit.level for tileUnit in currentTile.units
                    if type(tileUnit) == type(unit)]) >= sum([
                            tileUnit.level for tileUnit in
                            currentTile.units
                            if type(tileUnit) != type(unit)])
        else:
            return False

    def doMonsterMove(self, monster, position):
        if monster.moveProfile == "Advance-Defensive":
            if monster.hp < monster.maxHP():
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
                                unit for unit in
                                self.terrainArray[position].units
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
            if monster.hp < monster.maxHP():
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
            if monster.hp < monster.maxHP():
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
        elif monster.moveProfile == "SlowAdvance":
            # will not move if in melee range of enemies
            if any([
                    unit for unit in self.terrainArray[position].units
                    if type(unit) == playerCharacter]):
                monster.moveProfile == "Aggressive"
                return
            # move as far forward as possible to tiles with enemies
            candidates = []
            for position in monster.allowedMovement:
                if any([
                        unit for unit in self.terrainArray[position].units
                        if type(unit) == playerCharacter]):
                    candidates.append(position)
                    monster.moveProfile == "Aggressive"
            if candidates:
                moveTo = min(candidates)
            else:
                # move as far forward as possible
                moveTo = min(monster.allowedMovement)
            self.move(monster, moveTo)
        elif monster.moveProfile == "Sniper":
            candidates = [
                    target for target in self.game.party if target.hp > 0]
            candidates = [
                    target for target in candidates
                    if target.stats["Fame"] == max(
                            unit.stats["Fame"] for unit in candidates)]
            candidates = [
                    target for target in candidates
                    if target.hp == min(
                            unit.hp for unit in candidates)]
            targetPos = max([
                    self.getUnitPos(target) for target in candidates]) + 1
            if targetPos in monster.allowedMovement:
                moveTo = targetPos
            else:
                if targetPos < min(monster.allowedMovement):
                    moveTo = min(monster.allowedMovement)
                elif targetPos > max(monster.allowedMovement):
                    moveTo = max(monster.allowedMovement)
                else:
                    return
            self.move(monster, moveTo)

    def getFameBonus(self, unit):
        position = self.getUnitPos(unit)
        if not position:
            return 0
        currentTile = self.terrainArray[position]
        allyFame = [
                ally.stats["Fame"] for ally in currentTile.units
                if type(ally) == type(unit) and ally != unit]
        if any(allyFame):
            return max(allyFame)
        else:
            return 0

    def getPower(self, unit, name):
        if name in unit.powers:
            return True
        elif unit.equipment:
            if name in unit.equipment.powers:
                return True
        else:
            commandName = "Command: " + name
            position = self.getUnitPos(unit)
            if not position:
                return False
            currentTile = self.terrainArray[position]
            for ally in currentTile.units:
                if type(ally) == type(unit):
                    if commandName in unit.powers:
                        return True
        return False

    def getStat(self, unit, statName):
        if statName == "Fame":
            print("warning: you called getStat for fame.")
        self.getFameBonus(unit)
        stat = unit.stats[statName]
        stat = math.floor(stat + (stat * (self.getFameBonus(unit) / 100)))
        return stat

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
        if self.getPower(unit, "Magic: Cost Reduction I"):
            cost = math.ceil(cost * 0.75)
        return cost

    def printAttackString(self, unit):
        attackString = f"{unit.name} can attack "
        attackStringAdds = []
        for target in unit.allowedAttacks:
            targetHealth = target.maxHP()
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
            targetHealth = target.maxHP()
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

    def viewMap(self, position):
        minRange = max(0, position - 3)
        maxRange = minRange + 6
        if maxRange > len(self.terrainArray) - 1:
            maxRange = len(self.terrainArray) - 1
            minRange = maxRange - 5
        tilesInRange = self.terrainArray[minRange:maxRange + 1]
        mapRow = ""
        for tile in tilesInRange:
            mapAdd = f"({self.terrainArray.index(tile)})"
            mapRow += f"{mapAdd:18}"
        print(mapRow)
        for i in range(3, -1, -1):
            mapRow = ""
            for tile in tilesInRange:
                try:
                    goodUnits = [
                            unit for unit in tile.units
                            if type(unit) == playerCharacter]
                    goodUnits.sort(key=lambda x: x.shortName, reverse=True)
                    mapRow += f"{goodUnits[i].shortName:7}  "
                except IndexError:
                    mapRow += (" " * 9)
                try:
                    badUnits = [
                            unit for unit in tile.units
                            if type(unit) == monster]
                    badUnits.sort(key=lambda x: x.shortName, reverse=True)
                    mapRow += f"{badUnits[i].shortName:7}  "
                except IndexError:
                    mapRow += (" " * 9)
            if [letter for letter in mapRow if letter != " "]:
                print(mapRow)
        print("-" * 18 * len(tilesInRange))
        mapRow = ""
        for tile in tilesInRange:
            mapRow += f"{tile.name:18}"
        print(mapRow)

    def viewMapFromUnit(self, unit):
        # center the map on the unit
        position = self.getUnitPos(unit)
        self.viewMap(position)

class game(object):

    def __init__(self):
        self.playerCharacters = []
        self.battleStatus = None
        self.money = 0
        self.inventory = []

        chatter = False
        recruit = playerCharacter(
                "Max", "Human", "Hero", chatter, 0)
        self.equipOnCharacter(
                equipment("Swords", "Middle Sword", 250, 0, 0, 5, 0, 0),
                recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Lowe", "Hobbit", "Priest", chatter, 0)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 80, 0, 0, 1, 3, 3),
                recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Tao", "Elf", "Fire Mage", chatter, 0)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 80, 0, 0, 1, 3, 3),
                recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Luke", "Dwarf", "Warrior", chatter, 0)
        self.equipOnCharacter(
                equipment("Axes", "Short Axe", 120, 0, 0, 3, 0, 0), recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Ken", "Centaur", "Knight", chatter, 0)
        self.equipOnCharacter(
                equipment("Spears", "Wooden Spear", 100, 0, 1, 3, 0, 0),
                recruit)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Hans", "Elf", "Archer", chatter, 0)
        self.equipOnCharacter(
                equipment("Arrows", "Wooden Arrow", 150, 1, 1, 3, 0, 0),
                recruit)
        self.playerCharacters.append(recruit)

        self.party = self.playerCharacters
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(10, 'king')
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
        self.party = self.playerCharacters
        self.reckoning(30, 'lonely priest')
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(10, 'lonely priest')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'lonely priest')
            battle(self, self.party, 2)
        print("")
        print("The party arrives at the Holy City of Yatahal. It is burning.")
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
        recruit = playerCharacter("Mae", "Centaur", "Knight", chatter, 2)
        self.playerCharacters.append(recruit)
        self.equipOnCharacter(
                equipment("Lances", "Bronze Lance", 300, 0, 0, 6, 0, 0),
                recruit)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit = playerCharacter("Gort", "Dwarf", "Warrior", chatter, 2)
        self.playerCharacters.append(recruit)
        self.equipOnCharacter(
                equipment("Axes", "Hand Axe", 200, 0, 0, 4, 0, 0), recruit)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        self.party = self.playerCharacters
        self.reckoning(30, 'widow of your mentor')
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(10, 'widow of your mentor')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'widow of your mentor')
            battle(self, self.party, 3)
        print("")
        print("You arrive in Ulmara, a small merchant city bordering Yatahal.")
        print("The King of Ulmara greets you warmly, bestowing lavish gifts.")
        self.reckoning(50, "King of Ulmara")
        print(
                "The King gestures to the shopping district: \"Go visit a "
                "smith!\"")
        print(
                "On your way to the shops, you notice a young Kyantol woman "
                "following you.")
        shop(self, 350, [
                "Wooden Arrow", "Hand Axe", "Short Knife", "Spear",
                "Wooden Staff", "Middle Sword"])
        print("")
        print(
                "As you leave the shop, the young Kyantol woman appears at "
                "your side.")
        print("\"Don't trust the king!\", she hisses, then spirits away.")
        print("She looked a bit wild, like a prophet.")
        print(
            "Before you can decide what to do, the king summons you to the "
            "castle.")
        print("There, the king reveals that he has made a deal with Darksol,")
        print("the dark wizard behind the army that destroyed Yatahal.")
        print(
                "In exchange for keeping Ulmara safe, he is now supplying "
                "Darksol.")
        print("You are now to be sent to Darksol as more recruits.")
        print("")
        print("You refuse, so the king throws you into prison.")
        print("")
        print("")
        print("")
        print(
                "That night, a door opens in the wall of your cell and the "
                "Kyantol woman enters.")
        print("\"My people built this palace and the prison.\" She smirks.")
        print("\"Come with me -- we'll have to fight our way out of town.\"")
        print(
                "\"We have to go north to inform Her Majesty of her father's "
                "death.\"")
        print("\"I'm Khris. The priesthood is still loyal to Yatahal.\"")
        recruit = playerCharacter("Khris", "Kyantol", "Prophet", chatter, 4)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 80, 0, 0, 1, 3, 3),
                recruit)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        self.playerCharacters.append(recruit)
        self.party = self.playerCharacters
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(20, 'the priests')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'the priests')
            battle(self, self.party, 4)

    def equipItem(self, equipment):
        allowedUnits = [
                unit for unit in self.playerCharacters
                if unit.canEquip(equipment)]
        if allowedUnits:
            for unit in allowedUnits:
                equipString = f"({allowedUnits.index(unit)}) {unit.name} "
                if unit.equipment:
                    currentDamage = unit.equipment.damage
                    currentFaith = unit.equipment.fp
                    currentMagic = unit.equipment.mp
                else:
                    currentDamage = 0
                    currentFaith = 0
                    currentMagic = 0
                if equipment.damage != currentDamage:
                    equipString += (
                            f"Damage: {currentDamage}-->{equipment.damage} ")
                if equipment.fp != currentFaith:
                    equipString += f"Faith: {currentFaith}-->{equipment.fp} "
                if equipment.mp != currentMagic:
                    equipString += f"Magic: {currentMagic}-->{equipment.mp}"
                print(equipString)
            print(f"({len(allowedUnits)}) Just throw it in my bag.")
            command = None
            while command not in [
                    allowedUnits.index(unit) for unit in allowedUnits]:
                try:
                    command = int(input(
                            "Type a number to equip the weapon."))
                except ValueError:
                    command = None
                if command == len(allowedUnits):
                    break
            if command in [allowedUnits.index(unit) for unit in allowedUnits]:
                self.equipOnCharacter(equipment, allowedUnits[command])

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

    def getSellPrice(self, item):
        equipString = f"Equip: {item.type}"
        fame = max([
                pc.stat["Fame"] for pc in self.playerCharacters
                if equipString in pc.powers])
        amount = math.floor(item.price * (0.1 + (fame / 100)))
        return amount

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
