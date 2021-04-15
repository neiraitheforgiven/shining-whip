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
        self.party = self.assembleParty(party, game.maxPartySize)
        self.currentInitiative = 0
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
                                self.party, game)
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
                                self.party, game)
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
                                self.party, game)
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
                                self.party, game)
            elif num == 5:
                self.battleField = battleField([
                        "Grass", "Grass", "Grass", "Grass", "Grass", "Bridge",
                        "Grass", "Grass", "Sand", "Sand", "Sand", "Sand",
                        "Sand", "Sand", "Sand", "Sand", "Sand"],
                        [(monster(
                                "Crazed Dwarf", "Defensive",
                                "ChallengeAccepting"), 6),
                                (monster(
                                        "Crazed Dwarf", "Defensive",
                                        "ChallengeAccepting"), 6),
                                (monster(
                                        "Crazed Dwarf", "Defensive",
                                        "ChallengeAccepting"), 6),
                                (monster("Giant Bat"), 10),
                                (monster("Sniper"), 11),
                                (monster("Sniper"), 11),
                                (monster(
                                        "Dark Apprentice", "SlowAdvance"), 12),
                                (monster("Giant Bat"), 14),
                                (monster("Giant Bat"), 15),
                                (monster("Zombie"), 14),
                                (monster("Zombie"), 14),
                                (monster("Zombie"), 16),
                                (monster("Zombie"), 16),
                                (monster("Dark Apprentice"), 16),
                                (monster("Dark Apprentice"), 16)], self.party,
                                game)
            elif num == 6:
                self.battleField = battleField([
                        "Cavern", "Cavern", "Cavern", "Cavern", "Cavern",
                        "Bridge", "Cavern", "Cavern", "Cavern", "Loose Rocks",
                        "Cavern", "Loose Rocks", "Cavern"],
                        [(monster(
                                "Zombie"), 3),
                                (monster("Zombie"), 3),
                                (monster("Zombie"), 6),
                                (monster("Sniper"), 6),
                                (monster("Sniper"), 6),
                                (monster("Dark Apprentice"), 6),
                                (monster("Giant Bat", "SlowAdvance"), 10),
                                (monster("Giant Bat", "SlowAdvance"), 10),
                                (monster("Giant Bat", "SlowAdvance"), 10),
                                (monster("Giant Bat", "SlowAdvance"), 10),
                                (monster("Giant Bat", "SlowAdvance"), 11),
                                (monster("Dark Apprentice"), 12),
                                (monster("Dark Apprentice"), 12),
                                (monster("Dark Apprentice"), 12),
                                (monster("Skeleton Warrior"), 12)],
                                party, game)
            elif num == 7:
                self.battleField = battleField([
                        "Sand", "Sand", "Sand", "Upward Stair", "Upward Stair",
                        "Tiled Floor", "Tiled Floor", "Tiled Floor",
                        "Tiled Floor", "Tiled Floor", "Tiled Floor"],
                        [(monster(
                                "Body Puppet"), 3),
                                (monster("Body Puppet"), 4),
                                (monster("Mannequin"), 4),
                                (monster("Body Puppet"), 7),
                                (monster("Mannequin"), 7),
                                (monster("Mannequin"), 7),
                                (monster("Giant Bat", "SlowAdvance"), 8),
                                (monster("Giant Bat", "SlowAdvance"), 9),
                                (monster("Giant Bat", "SlowAdvance"), 10),
                                (monster("Deranged Clown"), 8),
                                (monster("Deranged Clown"), 8),
                                (monster("Marionette"), 10)],
                                party, game, -10)
            elif num == 8:
                self.battleField = battleField([
                        "Tiled Floor", "Tiled Floor", "Tiled Floor",
                        "Downward Stair", "Tiled Floor", "Tiled Floor",
                        "Tiled Floor", "Tiled Floor"],
                        [(
                                monster(
                                        "Skeleton Warrior",
                                        "Advance-Defensive",
                                        "ChallengeAccepting"), 3),
                                (monster("Zombie"), 4),
                                (monster("Zombie"), 4),
                                (monster(
                                        "Skeleton Warrior",
                                        "Advance-Defensive",
                                        "ChallengeAccepting"), 4),
                                (monster("Zombie"), 5),
                                (monster("Zombie"), 5),
                                (monster(
                                        "Skeleton Warrior",
                                        "Advance-Defensive",
                                        "ChallengeAccepting"), 5),
                                (monster("Ghoul"), 5),
                                (monster("Zombie"), 7),
                                (monster("Zombie"), 7)],
                                party, game, 10)
            for unit in self.battleField.units:
                unit.hp = unit.maxHP()
                unit.fp = unit.stats["Faith"]
                unit.mp = unit.stats["Intelligence"]
                unit.actedThisRound = False
                unit.status = []
                if unit.equipment:
                    unit.fp += unit.equipment.fp
                    unit.mp += unit.equipment.mp
                if self.getPower(unit, "Egress I") and unit.mp < self.mpCost(
                        unit, 8):
                    print(f"warning: {unit.name} has too few mp to Egress")
            self.determineStartingInitiative()
            self.game.battleStatus = 'ongoing'
            while self.battleOn():
                self.doRound()

    def addVocalPower(self, tile, amount):
        tileId = self.battleField.terrainArray.index(tile)
        tile.voicePower += amount
        if tileId + 1 < len(self.battleField.terrainArray):
            tile2 = self.battleField.terrainArray[tileId + 1]
            # set proposed voice power for each side = 1/2 current
            # voice power
            if (
                    tile.voicePower / 2) > (
                    tile2.proposedGoodVoicePower) and (
                    tile.voicePower > tile2.voicePower):
                tile2.proposedGoodVoicePower = tile.voicePower / 2
            if (
                    tile.voicePower / 2) < (
                    tile2.proposedEvilVoicePower) and (
                    tile.voicePower < tile2.voicePower):
                tile2.proposedEvilVoicePower = tile.voicePower / 2
        if tileId - 1 >= 0:
            tile2 = self.battleField.terrainArray[tileId - 1]
            if (
                    tile.voicePower / 2) > (
                    tile2.proposedGoodVoicePower) and (
                    tile.voicePower > tile2.voicePower):
                tile2.proposedGoodVoicePower = tile.voicePower / 2
            if (
                    tile.voicePower / 2) < (
                    tile2.proposedEvilVoicePower) and (
                    tile.voicePower < tile2.voicePower):
                tile2.proposedEvilVoicePower = tile.voicePower / 2

    def assembleParty(self, party, maxPartySize):
        if len(party) <= maxPartySize:
            return party
        else:
            currentParty = []
            leaders = [
                    unit for unit in party if "Egress I" in unit.powers]
            if len(leaders) == 1:
                currentParty.append(leaders[0])
                print(f"{leaders[0].name} leads the Force into battle!")
            else:
                leaderChoice = None
                while leaderChoice not in ([
                        leaders.index(leader) for leader in leaders], 'L',
                        'l'):
                    leaderString = ''
                    leaderStringAdds = []
                    count = 0
                    for leader in leaders:
                        leaderStringAdds.append(f"({count}) {leader.name}")
                        count += 1
                    leaderString += ", ".join(leaderStringAdds)
                    print(leaderString)
                    leaderChoice = input((
                            "Type a number to choose a leader for the party. "
                            "Press (L) to look more closely at a leader. "))
                    if leaderChoice in ('L', 'l'):
                        leaderChoice = None
                        while leaderChoice not in ([
                                leaders.index(leader) for leader in leaders]):
                            try:
                                leaderChoice = int(input((
                                    "Type a number to choose which leader to "
                                    "look at: ")))
                            except ValueError:
                                leaderChoice = None
                            leaders(leaderChoice).printCharacterSheet()
                            leaderChoice = None
                    else:
                        try:
                            leaderChoice = int(leaderChoice)
                            party.append(leaders[leaderChoice])
                            print(
                                    f"{leaders[leaderChoice].name} leads the "
                                    "Force into battle!")
                        except ValueError:
                            leaderChoice = None
            while len(currentParty) < maxPartySize:
                unitChoice = None
                partyOptions = [
                        unit for unit in party if unit not in currentParty]
                while unitChoice not in ([
                        partyOptions.index(option)
                        for option in partyOptions], 'L', 'l'):

                    optionString = ''
                    optionStringAdds = []
                    count = 0
                    for unit in partyOptions:
                        optionStringAdds.append(f"({count}) {unit.name}")
                        count += 1
                    optionString += ", ".join(optionStringAdds)
                    print(optionString)
                    unitChoice = input((
                            "Type a number to choose a character to join "
                            "the party. Press (L) to look more closely at a "
                            "character. Press (S) to start the battle without "
                            "adding any new characters. "))
                    if unitChoice in ('L', 'l'):
                        unitChoice = None
                        while unitChoice not in ([
                                partyOptions.index(option)
                                for option in partyOptions]):
                            try:
                                unitChoice = int(input(
                                    "Type a number to choose a character to "
                                    "look at: "))
                            except ValueError:
                                unitChoice = None
                            partyOptions[unitChoice].printCharacterSheet()
                    elif unitChoice in ('S', 's'):
                        return currentParty
                    else:
                        try:
                            unitChoice = int(unitChoice)
                        except ValueError:
                            unitChoice = None
                        if unitChoice is not None and (
                                unitChoice <= len(partyOptions) - 1):
                            currentParty.append(partyOptions[unitChoice])
                            print((
                                    f"{partyOptions[unitChoice].name} joins "
                                    "the party!"))
                            partyOptions = [
                                unit for unit in party
                                if unit not in currentParty]
                            break
            return currentParty

    def attack(self, unit, target):
        bf = self.battleField
        counterattack = False
        poisonEnemy = False
        routEnemy = False
        doubleChanceArray = []
        dex = self.getStat(unit, "Dexterity")
        luck = self.getStat(unit, "Luck")
        if self.getPower(unit, "Swords: Increased Luck I"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck II"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck III"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
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
                time.sleep(4. / 10)
            elif i > 0:
                print(f"{unit.name} attacks again!")
                time.sleep(4. / 10)
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
            if self.getPower(unit, "Luck: Increased Rout I"):
                routChance = math.ceil(routChance * 1.3)
            if self.getPower(unit, "Luck: Increased Rout II"):
                routChance = math.ceil(routChance * 1.3)
            attackTypeArray.extend(["routing"] * routChance)
            if i + 1 == attackCount:
                stamina = self.getStat(unit, "Stamina")
                heavyChance = math.floor(stamina + (stamina * (luck / 10)))
                attackTypeArray.extend(["heavy"] * heavyChance)
            if not self.getPower(unit, "Aimed Shot"):
                if not self.battleField.canMove(target):
                    dodgeSkill = math.floor(max(
                            self.getStat(target, "Intelligence"), targetLuck,
                            self.getStat(target, "Speed")) * (1 + (
                                    (targetLuck / 10))))
                    attackTypeArray.extend(["dodge"] * dodgeSkill)
            if self.getPower(target, "Luck: Counterattack"):
                counterSkill = math.floor(
                        self.getStat(target, "Dexterity") * (
                                1 + targetLuck / 10))
                attackTypeArray.extend(["counter"] * counterSkill)
            attackType = random.choice(attackTypeArray)
            if self.getPower(unit, "Poisonous Attack"):
                stamina = self.getStat(unit, "Stamina")
                vsStamina = self.getStat(target, "Stamina")
                poisonChance = luck + stamina - vsStamina
                if poisonChance > 0:
                    attackTypeArray.extend(["poison"] * poisonChance)
            if attackType == 'dodge':
                time.sleep(1. / 10)
                print(f"{target.name} dodges the attack!")
                self.giveExperience(unit, target, 1)
            else:
                if attackType == 'critical':
                    time.sleep(2. / 10)
                    print("")
                    print("A Critical Attack!")
                    print("")
                    time.sleep(4. / 10)
                elif attackType == 'normal':
                    if self.getPower(
                            unit,
                            "Heavy Attack Instead of Normal For Ranged Tile"):
                        unitPos = self.battleField.getUnitPos(unit)
                        targetPos = self.battleField.getUnitPos(target)
                        if unitPos != targetPos:
                            attackType = 'heavy'
                damage = max(strength, dex)
                if attackType == 'heavy':
                    time.sleep(2. / 10)
                    print("")
                    print("A heavy attack!")
                    print("")
                    damage *= 1.15
                    time.sleep(1. / 10)
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
                strengthForDamage = strength
                if self.getPower(unit, "Lances: Movement Increases Damage I"):
                    if unit.equipment and unit.equipment.type == "Lances":
                        strengthForDamage += math.ceil((
                                self.getStat(unit, "Speed"
                                ) - unit.movementPoints) / 5)
                damage = max(strengthForDamage, damage)
                if i == 0:
                    if self.getPower(unit, "Charge"):
                        speed = self.getStat(unit, "Speed")
                        damage += speed - unit.movementPoints
                if self.getPower(target, "Defense: Melee Attacks I") and (
                        bf.getUnitPos(unit) == bf.getUnitPos(target)):
                    damage *= 0.7
                    damage = math.floor(damage)
                if unit.equipment:
                    damage += unit.equipment.damage
                # elevation damage
                unitHeight = bf.terrainArray[bf.getUnitPos(unit)].elevation
                targetHeight = bf.terrainArray[bf.getUnitPos(target)].elevation
                heightBonus = 1 + ((unitHeight - targetHeight) / 20)
                damage = math.floor(damage * heightBonus)
                if attackType != 'critical':
                    damage -= max(
                            self.getStat(target, "Strength"),
                            self.getStat(target, "Dexterity"),
                            self.getStat(target, "Faith"))
                damage = max(damage, 1)
                damage = min(damage, target.hp)
                print(f"{unit.name} deals {damage} damage to {target.name}!")
                if attackType == 'critical':
                    if self.getPower(
                            unit, "Luck: Critical Drain I") or (
                            self.getPower(unit, "Luck: Critical Drain II")):
                        if self.getPower(unit, "Luck: Critical Drain II"):
                            heal = min(math.ceil(damage * 0.6), unit.maxHP())
                        else:
                            heal = min(math.ceil(damage * 0.3), unit.maxHP())
                        print(
                                f"{unit.name} drained {heal} health during "
                                "the attack!")
                        unit.hp += heal
                target.hp -= damage
                self.giveExperience(unit, target, damage)
                if target.hp <= 0:
                    self.kill(target, unit)
                    return
                elif attackType == "counter":
                    counterattack = True
                elif attackType == "poison":
                    poisonEnemy = True
                elif attackType == "routing":
                    routEnemy = True
                if poisonEnemy and ((i + 1) == attackCount):
                    print(f"{target.name} is poisoned!.")
                    target.status.append['Poisoned']
                if routEnemy and ((i + 1) == attackCount):
                    if type(target) == playerCharacter:
                        moveTo = self.battleField.getUnitPos(target) - 1
                    elif type(target) == monster:
                        moveTo = self.battleField.getUnitPos(target) + 1
                    if 0 <= moveTo <= len(self.battleField.terrainArray) - 1:
                        if len([
                                tileUnit for tileUnit
                                in bf.terrainArray[moveTo].units
                                if type(tileUnit) == type(target)]) < 4:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)
                        else:
                            print(f"{target.name} was stunned!")
                            time.sleep(4. / 10)
                            setback = min(15, math.ceil(
                                    225 / self.determineInitiative(target)))
                            if target.initiativePoints < (
                                    self.currentInitiative - setback):
                                setback = math.ceil(setback / 2)
                            if target.initiativePoints < (
                                    self.currentInitiative - 3 * setback):
                                setback = math.floor(setback / 2)
                            target.initiativePoints -= setback
                            if target in self.turnOrder:
                                self.turnOrder.remove(target)
                    else:
                        print(f"{target.name} was stunned!")
                        time.sleep(4. / 10)
                        setback = min(15, math.ceil(
                                225 / self.determineInitiative(target)))
                        target.initiativePoints -= setback
                        if target in self.turnOrder:
                            self.turnOrder.remove(target)
                if attackType == 'heavy':
                    setback = math.ceil(stamina / 2)
                    if target.initiativePoints < (
                            self.currentInitiative - setback):
                        setback = math.ceil(setback / 2)
                    if target.initiativePoints < (
                            self.currentInitiative - 3 * setback):
                        setback = math.floor(setback / 2)
                    target.initiativePoints -= setback
                    if target in self.turnOrder:
                        self.turnOrder.remove(target)
                if counterattack and ((i + 1) == attackCount):
                    bf.checkAttack(target, bf.getUnitPos(target))
                    if unit in target.allowedAttacks:
                        self.attack(target, unit)

    def battleOn(self):
        if self.egressing:
            self.game.battleStatus = 'egress'
            return False
        if any([
                unit for unit in self.battleField.units
                if type(unit) == playerCharacter and self.getPower(
                        unit, "Egress I") and unit.hp > 0 and not (
                        unit.status and "Petrified" in unit.status)]):
            if any([
                    unit for unit in self.battleField.units
                    if type(unit) == monster and unit.hp > 0 and not (
                    unit.status and "Petrified" in unit.status)]):
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

    def castAreaSpell(
            self, unit, targetId, spellName, cost, damage, area=0,
            element=None, spread=False, faith=False):
        bf = self.battleField
        if element:
            elementWithSpace = element + " "
        else:
            elementWithSpace = None
        if faith:
            unit.fp -= self.mpCost(unit, cost)
        else:
            unit.mp -= self.mpCost(unit, cost)
        targetTile = unit.allowedSpells[spellName][targetId]
        print(f"{unit.name} casts {spellName}!")
        position = bf.terrainArray.index(targetTile)
        minRange = max(0, position - area)
        maxRange = min(position + area, len(bf.terrainArray) - 1)
        if spread and damage > 0:
            count = len(
                    target for target
                    in [
                            tile for tile in
                            bf.terrainArray[minRange:maxRange + 1]]
                    if type(target) != type(unit))
        for i in range(minRange, maxRange + 1):
            tile = bf.terrainArray[i]
            for target in tile.units:
                if not self.battleField.canBeTarget(unit):
                    continue
                if damage < 0:
                    # spell is a healing spell
                    if type(target) == type(unit):
                        healing = min(
                                abs(damage), (target.maxHP() - target.hp))
                        print(
                                f"{unit.name} restores {healing} health "
                                f"to {target.name}!")
                        target.hp += healing
                        self.giveExperience(unit, target, healing)
                elif damage > 0:
                    # spell is a damage spell
                    targetDamage = damage
                    if type(target) != type(unit):
                        if spread:
                            targetDamage = math.ceil(targetDamage / count)
                        if self.getPower(target, "Defense: Magic"):
                            targetDamage = math.floor(targetDamage / 1.3)
                        if self.getPower(
                                target, f"Defense: {element} Resistance"):
                            targetDamage = math.floor(targetDamage / 1.3)
                        if self.getPower(
                                target,
                                f"Defense: {element} Vulnerability"):
                            targetDamage = math.ceil(targetDamage * 1.3)
                        targetDamage = min(targetDamage, target.hp)
                        print(
                                f"{unit.name} deals {targetDamage} "
                                f"{elementWithSpace}damage to "
                                f"{target.name}!")
                        target.hp -= targetDamage
                        self.giveExperience(unit, target, targetDamage)
                        if target.hp <= 0:
                            self.kill(target)

    def castSingleSpell(
            self, unit, targetId, spellName, cost, damage, element=None,
            faith=False):
        if faith:
            unit.fp -= self.mpCost(unit, cost)
        else:
            unit.mp -= self.mpCost(unit, cost)
        target = unit.allowedSpells[spellName][targetId]
        print(f"{unit.name} casts {spellName} on {target.name}!")
        if damage < 0:
            # spell is a healing spell
            healing = min(abs(damage), (target.maxHP() - target.hp))
            print(f"{unit.name} restores {healing} health to {target.name}!")
            target.hp += healing
            self.giveExperience(unit, target, healing)
        elif damage > 0:
            if self.getPower(target, "Defense: Magic"):
                damage = math.floor(damage / 1.3)
            if self.getPower(
                    target, f"Defense: {element} Resistance"):
                damage = math.floor(damage / 1.3)
            if self.getPower(
                    target, f"Defense: {element} Vulnerability"):
                damage = math.ceil(damage * 1.3)
            damage = min(damage, target.hp)
            if element:
                element += " "
            print(
                    f"{unit.name} deals {damage} {element}damage to "
                    f"{target.name}!")
            target.hp -= damage
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                self.kill(target)

    def castStatusSpell(
            self, unit, targetId, spellName, cost, statusName, faith=False,
            gold=False, stats=[],
            counterStats=["Stamina", "Faith"]):
        if faith:
            unit.fp -= self.mpCost(unit, cost)
        else:
            unit.mp -= self.mpCOst(unit, cost)
        target = unit.allowedSpells[spellName][targetId]
        print(f"{unit.name} casts {spellName} on {target.name}!")
        # assemble chance array
        chanceArray = []
        chanceArray.extend(['fail'] * (50 - self.getStat(unit, "Luck")))
        successChance = sum(self.getStat(unit, stat) for stat in stats)
        chanceArray.extend(['success'] * successChance)
        resistChance = 0
        if "Life" in counterStats:
            resistChance += target.hp
            counterStats.remove("Life")
        resistChance += math.floor(sum((
                self.getStat(target, stat) * (
                        self.getStat(target, "Luck") * 0.1))
                        for stat in counterStats))
        chanceArray.extend(['fail'] * resistChance)
        result = random.choice(chanceArray)
        if result == "success":
            print(f"{target.name} is {statusName}!")
            target.status.append(statusName)
            if gold and type(unit) == playerCharacter:
                print(
                        f"{unit.name} discovered a statue worth {target.hp} "
                        "scroulings!")
                self.game.money += target.hp
            self.giveExperience(unit, target, math.ceil(target.hp / 3))
        else:
            print(f"By sheer will, {target.name} was not {statusName}!")
            self.giveExperience(unit, target, math.ceil(target.hp / 10))

    def castSpell(self, unit, spellName, targetId):
        if spellName == "Afflict I":
            unit.mp -= self.mpCost(unit, 13)
            print(f"{unit.name} casts Afflict I!")
            self.castStatusSpell(
                    unit, targetId, "Sleep", 0, "Lulled to Sleep",
                    stats=["Luck", "Intelligence"],
                    counterStats=["Stamina", "Faith"])
            self.castStatusSpell(
                    unit, targetId, "Poison", 0, "Poisoned",
                    stats=["Luck", "Intelligence"],
                    counterStats=["Stamina", "Faith"])
            self.castStatusSpell(
                    unit, targetId, "Petrify", 0, "Petrified",
                    stats=["Luck", "Intelligence"],
                    counterStats=["Stamina", "Faith"])
        elif spellName == "Aura I":
            self.castAreaSpell(unit, targetId, "Aura I", 7, -15, faith=True)
        elif spellName == "Aura II":
            self.castAreaSpell(unit, targetId, "Aura II", 11, -15, faith=True)
        elif spellName == "Aura III":
            self.castAreaSpell(
                    unit, targetId, "Aura III", 15, -30, 1, faith=True)
        elif spellName == "Aura IV":
            unit.fp -= self.mpCost(unit, 20)
            print(f"{unit.name} casts {spellName}!")
            for target in self.party:
                healing = min(25, (target.maxHP() - target.hp))
                print(
                        f"{unit.name} restores {healing} health to "
                        f"{target.name}!")
                target.hp += healing
                self.giveExperience(unit, target, healing)
        elif spellName == "Blaze I":
            self.castSingleSpell(unit, targetId, "Blaze I", 2, 6, "Fire")
        elif spellName == "Blaze II":
            self.castAreaSpell(unit, targetId, "Blaze II", 6, 9, 0, "Fire")
        elif spellName == "Blaze III":
            self.castAreaSpell(unit, targetId, "Blaze III", 8, 17, 0, "Fire")
        elif spellName == "Blaze IV":
            self.castSingleSpell(unit, targetId, "Blaze IV", 8, 40, "Fire")
        elif spellName == "Bolt I":
            self.castAreaSpell(unit, targetId, "Bolt I", 8, 13, 0, "Lightning")
        elif spellName == "Bolt II":
            self.castAreaSpell(
                    unit, targetId, "Bolt II", 15, 16, 1, "Lightning")
        elif spellName == "Bolt III":
            self.castAreaSpell(
                    unit, targetId, "Bolt III", 20, 25, 1, "Lightning")
        elif spellName == "Bolt IV":
            self.castSingleSpell(
                    unit, targetId, "Bolt IV", 20, 72, "Lightning")
        elif spellName == "Dao I":
            self.castAreaSpell(
                    unit, targetId, "Dao I", 8, 18, 0, "Earth", spread=True)
        elif spellName == "Dao II":
            self.castAreaSpell(
                    unit, targetId, "Dao II", 15, 40, 0, "Earth", spread=True)
        elif spellName == "Detox I":
            unit.fp -= self.mpCost(unit, 3)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            if "Petrified" in target.status:
                target.initiativePoints = unit.initiativePoints - 15
            target.status = []
            print(f"{target.name} recovers!")
            self.giveExperience(unit, target, 10)
        elif spellName == "Drain I":
            unit.mp -= self.mpCost(unit, 5)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(10, target.hp)
            print(f"{unit.name} drains {damage} health from {target.name}!")
            target.hp -= damage
            unit.hp = min(unit.hp + damage, unit.maxHP())
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                self.kill(target, unit)
        elif spellName == "Drain II":
            unit.mp -= self.mpCost(unit, 12)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(18, target.hp)
            print(f"{unit.name} drains {damage} health from {target.name}!")
            mdamage = min(6, target.mp)
            if mdamage > 0:
                print(f"{unit.name} drains {damage} magic from {target.name}!")
                target.mp -= mdamage
                maxMP = unit.stats["Intelligence"]
                if unit.equipment:
                    maxMP += unit.equipment.mp
                unit.mp = min(unit.mp + mdamage, maxMP)
            target.hp -= damage
            unit.hp = min(unit.hp + damage, unit.maxHP())
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                self.kill(target, unit)
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
            self.castSingleSpell(unit, targetId, "Freeze I", 3, 9, "Ice")
        elif spellName == "Freeze II":
            self.castAreaSpell(unit, targetId, "Freeze II", 7, 14, 0, "Ice")
        elif spellName == "Freeze III":
            self.castAreaSpell(unit, targetId, "Freeze III", 10, 20, 0, "Ice")
        elif spellName == "Freeze IV":
            self.castSingleSpell(unit, targetId, "Freeze IV", 12, 45, "Ice")
        elif spellName == "Heal I":
            self.castSingleSpell(unit, targetId, "Heal I", 3, -15, faith=True)
        elif spellName == "Heal II":
            self.castSingleSpell(unit, targetId, "Heal II", 6, -15, faith=True)
        elif spellName == "Heal III":
            self.castAreaSpell(unit, targetId, "Heal III", 10, -30, faith=True)
        elif spellName == "Heal IV":
            self.castAreaSpell(unit, targetId, "Heal IV", 20, -60, faith=True)
        elif spellName == "Midas I":
            self.castStatusSpell(
                    unit, targetId, "Midas I", 8, "Petrified", gold=True,
                    stats=["Intelligence", "Dexterity", "Luck"],
                    counterStats=["Stamina", "Dexterity"])
        elif spellName == "Portal I":
            unit.mp -= self.mpCost(unit, 21)
            field = self.battleField
            moveFromTile = field.terrainArray[field.getUnitPos(unit)]
            position = unit.allowedSpells[spellName][targetId]
            # target is a position
            moveToTile = field.terrainArray[position]
            for tileUnit in moveFromTile.units:
                if type(tileUnit) == type(unit):
                    moveFromTile.units.remove(tileUnit)
                    moveToTile.units.append(tileUnit)
                    self.giveExperience(unit, tileUnit, 5)
        elif spellName == "Teleport I":
            unit.mp -= self.mpCost(unit, 5)
            field = self.battleField
            moveFromTile = field.terrainArray[field.getUnitPos(unit)]
            moveToTile = unit.allowedSpells[spellName][targetId]
            moveFromTile.units.remove(unit)
            moveToTile.units.append(unit)
            self.giveExperience(unit, unit, 5)
        elif spellName == "Teleport II":
            unit.mp -= self.mpCost(unit, 10)
            field = self.battleField
            moveFromTile = field.terrainArray[field.getUnitPos(unit)]
            moveToTile = unit.allowedSpells[spellName][targetId]
            moveFromTile.units.remove(unit)
            moveToTile.units.append(unit)
            self.giveExperience(unit, unit, 10)
        elif spellName == "Teleport III":
            unit.mp -= self.mpCost(unit, 6)
            field = self.battleField
            moveFromTile = field.terrainArray[field.getUnitPos(unit)]
            moveToTile = unit.allowedSpells[spellName][targetId]
            moveFromTile.units.remove(unit)
            moveToTile.units.append(unit)
            self.giveExperience(unit, unit, 10)

    def determineInitiative(self, unit):
        luck = self.getStat(unit, "Luck")
        if self.getPower(unit, "Swords: Increased Luck I"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck II"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck III"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        initiative = max(
                self.getStat(unit, "Charisma"),
                self.getStat(unit, "Speed"),
                self.getStat(unit, "Dexterity"))
        return initiative

    def determineStartingInitiative(self):
        random.shuffle(self.battleField.units)
        # increment each unit's initiative points by their initiative
        for unit in self.battleField.units:
            unit.initiativePoints = self.determineInitiative(unit)

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
                if field.checkVocal(monster):
                    self.doVocalAttack(monster)
                else:
                    target = random.choice(monster.allowedAttacks)
                    self.attack(monster, target)
        elif monster.attackProfile == "Spellcaster":
            canCast = False
            field = self.battleField
            if self.getPower(monster, "Freeze III"):
                if monster.mp >= self.mpCost(monster, 10):
                    canCast = True
                    position = field.getUnitPos(monster)
                    minRange = max(0, position - 1)
                    maxRange = min(position + 1, len(field.terrainArray) - 1)
                    targetTile = None
                    numTargets = 0
                    for tile in field.terrainArray[minRange:(maxRange + 1)]:
                        targets = [
                                unit for unit in tile.units
                                if type(unit) != type(monster)]
                        if len(targets) > numTargets:
                            targetTile = tile
                            numTargets = len(targets)
                    if targetTile:
                        targetPosition = field.terrainArray.index(targetTile)
                        monster.allowedSpells["Freeze III"] = [targetPosition]
                        self.castSpell(monster, "Freeze III", 0)
            elif self.getPower(monster, "Freeze II"):
                if monster.mp >= self.mpCost(monster, 7):
                    canCast = True
                    position = field.getUnitPos(monster)
                    tile = field.terrainArray[position]
                    numTargets = 0
                    if any([unit for unit in tile.units
                            if type(unit) != type(monster)]):
                        monster.allowedSpells["Freeze II"] = [position]
                        self.castSpell(monster, "Freeze II", 0)
            elif self.getPower(monster, "Freeze I"):
                if monster.mp >= self.mpCost(monster, 3):
                    canCast = True
                    position = field.getUnitPos(monster)
                    tile = field.terrainArray[position]
                    targets = [
                            target for target in tile.units
                            if type(target) != type(monster)]
                    candidates = [
                            target for target in targets
                            if target.hp == min(unit.hp for unit in targets)]
                    target = random.choice(candidates)
                    monster.allowedSpells["Freeze I"] = [target]
                    self.castSpell(monster, "Freeze I", 0)
            elif self.getPower(monster, "Blaze II"):
                if monster.mp >= self.mpCost(monster, 6):
                    canCast = True
                    position = field.getUnitPos(monster)
                    minRange = max(0, position - 1)
                    maxRange = min(position + 1, len(field.terrainArray) - 1)
                    targetTile = None
                    numTargets = 0
                    for tile in field.terrainArray[minRange:(maxRange + 1)]:
                        targets = [
                                unit for unit in tile.units
                                if type(unit) != type(monster)]
                        if len(targets) > numTargets:
                            targetTile = tile
                            numTargets = len(targets)
                    if targetTile:
                        targetPosition = field.terrainArray.index(targetTile)
                        monster.allowedSpells["Blaze II"] = [targetPosition]
                        self.castSpell(monster, "Blaze II", 0)
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
        idleUnits = [
                unit for unit in self.battleField.units
                if unit.hp > 0 and not unit.actedThisRound]
        while idleUnits:
            self.turnOrder = []
            nextInitiative = max([
                    unit.initiativePoints for unit in self.battleField.units
                    if (unit.hp > 0 and not (
                            unit.status and "Petrified" in unit.status))])
            nextUnits = [
                    unit for unit in self.battleField.units
                    if unit.initiativePoints == nextInitiative and unit.hp > 0]
            for unit in nextUnits:
                self.turnOrder.append((
                        unit, unit.initiativePoints,
                        self.getStat(unit, "Luck")))
            self.turnOrder = sorted(
                    self.turnOrder, key=itemgetter(1, 2), reverse=True)
            for entry in self.turnOrder:
                unit = entry[0]
                # unit may have died since this loop started.
                if unit.hp <= 0:
                    continue
                if not unit.actedThisRound:
                    if type(unit) == playerCharacter:
                        unit.hasEquipped = False
                    unit.movementPoints = 3 + math.ceil(
                            self.getStat(unit, "Speed") / 2)
                else:
                    if unit.movementPoints <= 0:
                        unit.actedThisRound = True
                        # push back the unit's initiative
                        setback = min(
                                15, math.ceil(
                                        225 / self.determineInitiative(unit)))
                        unit.initiativePoints -= setback
                        continue
                if type(unit) == playerCharacter:
                    pc = unit
                    print("")
                    self.battleField.viewMapFromUnit(pc)
                    print("")
                    maxHP = pc.maxHP()
                    maxFP = pc.stats["Faith"]
                    maxMP = pc.stats["Intelligence"]
                    fame = self.getFameBonus(pc)
                    mvType = ""
                    if self.getPower(pc, "Mounted Movement"):
                        mvType = "M"
                    if pc.equipment:
                        maxFP += pc.equipment.fp
                        maxMP += pc.equipment.mp
                    print(
                            f"It's {pc.name}'s turn! (Level {pc.level} "
                            f"{pc.title})")
                    print(
                            f"  (HP: {pc.hp}/{maxHP} FP: {pc.fp}/{maxFP} "
                            f"MP: {pc.mp}/{maxMP} "
                            f"Move: {pc.movementPoints}{mvType} "
                            f"Fame Bonus: {fame}%)")
                    time.sleep(2. / 10)
                    position = self.battleField.getUnitPos(pc)
                    tile = self.battleField.terrainArray[position]
                    print(
                            f"{pc.name} is standing on ("
                            f"{self.battleField.terrainArray.index(tile)}) "
                            f"{tile.name}.")
                unit.actedThisRound = True
                # push back the unit's initiative
                setback = min(
                        15, math.ceil(225 / self.determineInitiative(unit)))
                unit.initiativePoints -= setback
                endBattle = self.doTurn(unit)
                if endBattle:
                    return
            idleUnits = [
                    unit for unit in self.battleField.units
                    if unit.hp > 0 and not unit.actedThisRound]
            #  degrade the tiles now
            timePassed = abs(self.currentInitiative - nextInitiative)
            """New model design:
            Potential Spread should be added whenever resonance is added to a
            tile. Whenever time passes, 4xTime% points (rounded up) should be
            degraded from each tile, and then 2xTime% points (rounded up)
            should bleed from potential into the real resonance."""
            self.currentInitiative = nextInitiative
            for tile in self.battleField.terrainArray:
                voicePowerLost = round(float((
                        tile.voicePower + tile.resonance) * float(
                                timePassed * 4 / 100)))
                tile.voicePower = math.floor(float(
                        tile.voicePower - voicePowerLost))
                if tile.voicePower > 0:
                    if not tile.goodRinging:
                        voicePowerLost = float(
                                (tile.voicePower + tile.resonance) * (
                                        timePassed * 4 / 100))
                        tile.voicePower = float(
                                tile.voicePower - voicePowerLost)
                elif tile.voicePower < 0:
                    if not tile.evilRinging:
                        voicePowerLost = float(
                                (tile.voicePower + tile.resonance) * (
                                        timePassed * 4 / 100))
                        tile.voicePower = float(
                                tile.voicePower - voicePowerLost)
            for tile in self.battleField.terrainArray:
                goodPowerSoaked = float((
                        tile.proposedGoodVoicePower + tile.resonance) * (
                                timePassed * 4 / 100))
                if not tile.goodRinging:
                    tile.proposedGoodVoicePower = max(
                            0, tile.proposedGoodVoicePower - goodPowerSoaked)
                evilPowerSoaked = abs(float(
                        tile.proposedEvilVoicePower + tile.resonance) * (
                                timePassed * 4 / 100))
                if not tile.evilRinging:
                    tile.proposedEvilVoicePower = min(
                            0, tile.proposedEvilVoicePower + evilPowerSoaked)
                proposedVoiceChange = goodPowerSoaked - evilPowerSoaked
                if tile.voicePower + proposedVoiceChange != tile.resonance:
                    self.addVocalPower(tile, proposedVoiceChange)
                tile.goodRinging = max(0, tile.goodRinging - timePassed)
                tile.evilRinging = max(0, tile.evilRinging - timePassed)
        for unit in self.battleField.units:
            unit.actedThisRound = False

    def doTurn(self, unit, moved=False, statusChecked=False):
        if unit.status and "Petrified" in unit.status:
            return
        for state in unit.status:
            if statusChecked:
                continue
            luck = self.getStat(unit, "Luck")
            if self.getPower(unit, "Swords: Increased Luck I"):
                if unit.equipment and unit.equipment.type == "Swords":
                    luck = math.ceil(luck * 1.3)
            if self.getPower(unit, "Swords: Increased Luck II"):
                if unit.equipment and unit.equipment.type == "Swords":
                    luck = math.ceil(luck * 1.3)
            if self.getPower(unit, "Swords: Increased Luck III"):
                if unit.equipment and unit.equipment.type == "Swords":
                    luck = math.ceil(luck * 1.3)
            resistSkill = sum([
                    self.getStat(unit, "Faith"),
                    self.getStat(unit, "Intelligence"),
                    self.getStat(unit, "Stamina")])
            resistChance = math.floor(
                    resistSkill + (resistSkill * (luck / 10)))
            if self.getPower(unit, "Defense: Increased Resistance I"):
                resistChance = math.ceil(resistChance * 1.3)
            if self.getPower(unit, "Defense: Increased Resistance II"):
                resistChance = math.ceil(resistChance * 1.3)
            resistArray = []
            resistArray.extend(['resist'] * resistChance)
            resistArray.extend(['fail'] * (50 - (luck)))
            result = random.choice(resistArray)
            if result == 'resist':
                if state == "Lulled to Sleep":
                    print(f"{unit.name} woke up!")
                else:
                    print(f"{unit.name} recovered from being {state}!")
                unit.status.remove(state)
            elif state == 'Lulled to Sleep':
                print(f"{unit.name} is asleep.")
                return
            elif state == 'Poisoned':
                print(f"{unit.name} is Poisoned!")
                damage = math.floor(self.getStat(unit, "Stamina") * 1.5)
                unit.hp -= damage
                print(f"{unit.name} takes {damage} damage from the poison.")
                if unit.hp <= 0:
                    self.kill(unit)
            statusChecked = True
        position = self.battleField.getUnitPos(unit)
        tile = self.battleField.terrainArray[position]
        otherUnits = ", ".join([
                tileUnit.name for tileUnit in tile.units if tileUnit != unit])
        if type(unit) == playerCharacter:
            if self.getPower(unit, 'Random Additional Spell I') and not (
                    unit.extraPowerSlot):
                unit.extraPowerSlot = self.getExtraSpell(unit, 1)
            if self.getPower(unit, 'Random Additional Spell II') and not (
                    unit.extraPowerSlot2):
                unit.extraPowerSlot2 = self.getExtraSpell(unit, 2)
            allowedCommands = ["C", "c", "L", "l", "W", "w"]
            if not moved:
                if type(unit) == playerCharacter:
                    moveEnabled = self.battleField.checkMove(unit, position)
                if moveEnabled:
                    self.battleField.printMoveString(unit)
                    print("Type (M) to move.")
                    allowedCommands.append("M")
                    allowedCommands.append("m")
            print(f"Type (C) to look at {unit.name}'s character sheet.")
            print("Type (L) to look at the battlefield,")
            attackEnabled = self.battleField.checkAttack(unit, position)
            if attackEnabled:
                self.battleField.printAttackString(unit)
                print("Type (A) to attack.")
                allowedCommands.append("A")
                allowedCommands.append("a")
            if not unit.hasEquipped and not moved and self.getPower(
                    unit, "Equip"):
                print("Type (E) to equip or unequip weapons.")
                allowedCommands.append("E")
                allowedCommands.append("e")
            spellEnabled = self.battleField.checkSpells(unit, position)
            if spellEnabled:
                self.battleField.printSpellString(unit)
                print("Type (S) to cast a spell.")
                allowedCommands.append("S")
                allowedCommands.append("s")
            if not moved or self.getPower(
                    unit, "Vocal Attack: Ignore Movement"):
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
                self.doTurn(unit, True, statusChecked)
            elif command in ("A", "a"):
                attackTarget = None
                while attackTarget not in [
                        unit.allowedAttacks.index(target)
                        for target in unit.allowedAttacks]:
                    try:
                        attackTarget = int(input("Type a number to attack: "))
                    except ValueError:
                        attackTarget = None
                self.doAttack(unit, attackTarget)
                if not moved or self.getPower(
                        unit, "Vocal Attack: Ignore Movement"):
                    vp = self.getStat(unit, "Voice")
                    darkTile = tile.voicePower < -1
                    if darkTile:
                        print(
                                f'{unit.name} shouts a few lines from the '
                                'holy song, hoping to be heard over the '
                                'unholy din.')
                    elif tile.voicePower > 1:
                        print(
                                f'{unit.name} sings along with the holy song '
                                'of the Force.')
                    else:
                        print(
                                f'{unit.name} sings out a stanza from the '
                                'holy song.')
                    if self.getPower(
                            unit, "Vocal Attack: Increased Resonance I"):
                        vp = math.ceil(vp * 1.3)
                    if self.getPower(
                            unit, "Vocal Attack: Increased Resonance II"):
                        vp = math.ceil(vp * 1.3)
                    self.addVocalPower(tile, vp)
                    if self.getPower(unit, "Vocal Attack: Sustain Effect"):
                        if type(unit) == playerCharacter:
                            tile.goodRinging = max(
                                    15, tile.goodRinging + self.getStat(
                                            unit, "Voice"))
                        else:
                            tile.evilRinging = max(
                                    15, tile.evilRinging + self.getStat(
                                            unit, "Voice"))
                    if darkTile and tile.voicePower > -1:
                        print(f"{unit.name}'s voice overcame the darkness!")
            elif command in ("C", "c"):
                print()
                unit.printCharacterSheet()
                print(f"Scroulings: {self.game.money}")
                print()
                self.doTurn(unit, moved, statusChecked)
            elif command in ("E", "e"):
                allowedEquipment = [
                        item for item in self.game.inventory
                        if unit.canEquip(item) and not item.equippedBy]
                itemToEquip = None
                while itemToEquip not in [
                        allowedEquipment.index(item)
                        for item in allowedEquipment] and (itemToEquip not in (
                        len(allowedEquipment), len(allowedEquipment) + 1)):
                    for item in allowedEquipment:
                        print(
                                f"({allowedEquipment.index(item)}) "
                                f"{item.name}")
                        self.printEstimatedValue(unit, item)
                    print(f"({len(allowedEquipment)}) Go barehanded.")
                    self.printEstimatedValue(unit)
                    print(f"({len(allowedEquipment) + 1}) Never mind.")
                    try:
                        itemToEquip = int(input("Type a number to equip: "))
                    except ValueError:
                        itemToEquip = None
                if itemToEquip == len(allowedEquipment):
                    if unit.equipment:
                        incumbent = unit.equipment
                        incumbent.equippedBy = None
                    unit.equipment = None
                    unit.hasEquipped = True
                    print(f"{unit.name} put away their weapon.")
                    itemToEquip = None
                    if unit.fp > self.getStat(unit, "Faith"):
                        unit.fp = self.getStat(unit, "Faith")
                    if unit.mp > self.getStat(unit, "Intelligence"):
                        unit.mp = self.getStat(unit, "Intelligence")
                elif itemToEquip == len(allowedEquipment) + 1:
                    pass
                elif itemToEquip is not None:
                    self.game.equipOnCharacter(
                            allowedEquipment[itemToEquip], unit)
                    itemToEquip = None
                    unit.hasEquipped = True
                    if unit.fp > self.getStat(
                            unit, "Faith") + unit.equipment.fp:
                        unit.fp = self.getStat(
                                unit, "Faith") + unit.equipment.fp
                    if unit.mp > (self.getStat(
                            unit, "Intelligence") + unit.equipment.mp):
                        unit.mp = (self.getStat(
                                unit, "Intelligence") + unit.equipment.mp)
                    print()
                self.doTurn(unit, True, statusChecked)
            elif command in ("L", "l"):
                tileChoice = None
                while tileChoice not in ([
                        self.battleField.terrainArray.index(lookTile)
                        for lookTile in self.battleField.terrainArray]):
                    try:
                        tileChoice = int(input(
                                "Type the number of a tile to look from: "))
                    except ValueError:
                        tileChoice = None
                self.battleField.viewMap(tileChoice)
                self.doTurn(unit, moved, statusChecked)
            elif command in ("S", "s"):
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
            elif command in ("V", "v"):
                self.doVocalAttack(unit)
            elif command in ("W", "w"):
                if not moved or self.getPower(
                        unit, "Vocal Attack: Ignore Movement"):
                    vp = self.getStat(unit, "Voice")
                    darkTile = tile.voicePower < -1
                    if darkTile:
                        print(
                                f'{unit.name} shouts a few lines from the '
                                'holy song, hoping to be heard over the '
                                'unholy din.')
                    elif tile.voicePower > 1:
                        print(
                                f'{unit.name} sings along with the holy song '
                                'of the Force.')
                    else:
                        print(
                                f'{unit.name} sings out a stanza from the '
                                'holy song.')
                    if self.getPower(
                            unit, "Vocal Attack: Increased Resonance I"):
                        vp = math.ceil(vp * 1.3)
                    if self.getPower(
                            unit, "Vocal Attack: Increased Resonance II"):
                        vp = math.ceil(vp * 1.3)
                    self.addVocalPower(tile, vp)
                    if self.getPower(unit, "Vocal Attack: Sustain Effect"):
                        if type(unit) == playerCharacter:
                            tile.goodRinging = max(
                                    15, tile.goodRinging + self.getStat(
                                            unit, "Voice"))
                        else:
                            tile.evilRinging = max(
                                    15, tile.evilRinging + self.getStat(
                                            unit, "Voice"))
                    if darkTile and tile.voicePower > -1:
                        print(f"{unit.name}'s voice overcame the darkness!")
                else:
                    print(f'{unit.name} waited.')
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
                moved = self.battleField.doMonsterMove(unit, position)
            position = self.battleField.getUnitPos(unit)
            attackEnabled = self.battleField.checkAttack(unit, position)
            if attackEnabled:
                self.doMonsterAttack(unit)
            else:
                print(f"{unit.name} waited.")
            if not moved or self.getPower(
                    unit, "Vocal Attack: Ignore Movement"):
                vp = self.getStat(unit, "Voice")
                if self.getPower(
                        unit, "Vocal Attack: Increased Resonance I"):
                    vp = math.ceil(vp * 1.3)
                if self.getPower(
                        unit, "Vocal Attack: Increased Resonance II"):
                    vp = math.ceil(vp * 1.3)
                self.addVocalPower(tile, -vp)
                if self.getPower(unit, "Vocal Attack: Sustain Effect"):
                    if type(unit) == playerCharacter:
                        tile.goodRinging = max(
                                15, tile.goodRinging + self.getStat(
                                        unit, "Voice"))
                    else:
                        tile.evilRinging = max(
                                15, tile.evilRinging + self.getStat(
                                        unit, "Voice"))
        time.sleep(6. / 10)
        endBattle = not self.battleOn()
        return endBattle

    def doVocalAttack(self, unit):
        bf = self.battleField
        position = bf.getUnitPos(unit)
        tile = bf.terrainArray[position]
        print(f"{unit.name} sings out a note of power!")
        cha = self.getStat(unit, "Charisma")
        luck = self.getStat(unit, "Luck")
        if self.getPower(unit, "Swords: Increased Luck I"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck II"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck III"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        voice = self.getStat(unit, "Voice")
        attackTypeArray = []
        attackTypeArray.extend(["normal"] * (100 - (luck)))
        criticalChance = math.floor(voice + (voice * (luck / 10)))
        attackTypeArray.extend(["critical"] * criticalChance)
        friendSound = sum([
                max(self.getStat(tileUnit, "Faith"), self.getStat(
                        tileUnit, "Voice"))
                for tileUnit in
                bf.terrainArray[position].units
                if type(tileUnit) == type(unit)])
        attackType = random.choice(attackTypeArray)
        if attackType == "critical":
            print("")
            time.sleep(4. / 10)
            print("A Thunderous Attack!")
            print("")
            friendSound *= 2
        enemySound = sum([
                max(self.getStat(tileUnit, "Faith"), self.getStat(
                        tileUnit, "Voice"))
                for tileUnit in
                bf.terrainArray[position].units
                if type(tileUnit) != type(unit)])
        amount = max(1, friendSound - enemySound)
        amount = amount + abs(tile.voicePower)
        damage = math.ceil(amount / 16)
        damage = max(damage, 1)
        for target in list(tile.units):
            if not self.battleField.canBeTarget(target):
                continue
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
                targetDamage = damage
                targetDamage = min(targetDamage, target.hp)
                print(
                        f"The note deals {targetDamage} damage to "
                        f"{target.name}!")
                target.hp -= targetDamage
                self.giveExperience(unit, target, targetDamage)
                if target.hp <= 0:
                    self.kill(target, unit)
                elif attackType == "routing":
                    if type(target) == playerCharacter:
                        moveTo = self.battleField.getUnitPos(target) - 1
                    elif type(target) == monster:
                        moveTo = self.battleField.getUnitPos(target) + 1
                    if 0 <= moveTo <= len(self.battleField.terrainArray) - 1:
                        if len([
                                tileUnit for tileUnit
                                in bf.terrainArray[moveTo].units
                                if type(tileUnit) == type(target)]) < 4:
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)
                        else:
                            print(f"{target.name} was stunned!")
                            setback = min(15, math.ceil(
                                    225 / self.determineInitiative(target)))
                            if target.initiativePoints < (
                                    self.currentInitiative - setback):
                                setback = math.ceil(setback / 2)
                            if target.initiativePoints < (
                                    self.currentInitiative - 3 * setback):
                                setback = math.floor(setback / 2)
                            target.initiativePoints -= setback
                    else:
                        print(f"{target.name} was stunned!")
                        setback = min(15, math.ceil(
                                225 / self.determineInitiative(target)))
                        if target.initiativePoints < (
                                    self.currentInitiative - setback):
                            setback = math.ceil(setback / 2)
                        if target.initiativePoints < (
                                self.currentInitiative - 3 * setback):
                            setback = math.floor(setback / 2)
                        target.initiativePoints -= setback
                elif attackType == "sleep":
                    target.status.append("Lulled to Sleep")
                    print(f"{target.name} fell asleep!")

    def getExtraSpell(self, unit, slot):
        possibleSpells = []
        #  Faith Spells
        if unit.fp >= self.mpCost(unit, 3):
            possibleSpells.append("Detox I")
            possibleSpells.append("Heal I")
        if unit.fp >= self.mpCost(unit, 6):
            possibleSpells.append("Heal II")
        if unit.fp >= self.mpCost(unit, 7):
            possibleSpells.append("Aura I")
        if unit.fp >= self.mpCost(unit, 10):
            possibleSpells.append("Heal III")
        if unit.fp >= self.mpCost(unit, 11):
            possibleSpells.append("Aura II")
        if unit.fp >= self.mpCost(unit, 13):
            possibleSpells.append("Afflict I")
        if unit.fp >= self.mpCost(unit, 15):
            possibleSpells.append("Aura III")
        if unit.fp >= self.mpCost(unit, 20):
            possibleSpells.append("Aura IV")
            possibleSpells.append("Heal IV")
        #  MP spells
        if unit.mp >= self.mpCost(unit, 2):
            possibleSpells.append("Blaze I")
        if unit.mp >= self.mpCost(unit, 3):
            possibleSpells.append("Freeze I")
        if unit.mp >= self.mpCost(unit, 5):
            possibleSpells.append("Drain I")
            possibleSpells.append("Teleport I")
        if unit.mp >= self.mpCost(unit, 6):
            possibleSpells.append("Blaze II")
            possibleSpells.append("Teleport III")
        if unit.mp >= self.mpCost(unit, 7):
            possibleSpells.append("Freeze II")
        if unit.mp >= self.mpCost(unit, 8):
            possibleSpells.append("Blaze III")
            possibleSpells.append("Blaze IV")
            possibleSpells.append("Bolt I")
            possibleSpells.append("Dao I")
            possibleSpells.append("Egress I")
            possibleSpells.append("Midas I")
        if unit.mp >= self.mpCost(unit, 10):
            possibleSpells.append("Freeze III")
            possibleSpells.append("Teleport II")
        if unit.mp >= self.mpCost(unit, 12):
            possibleSpells.append("Drain II")
            possibleSpells.append("Freeze IV")
        if unit.mp >= self.mpCost(unit, 15):
            possibleSpells.append("Bolt II")
            possibleSpells.append("Dao II")
        if unit.mp >= self.mpCost(unit, 20):
            possibleSpells.append("Bolt III")
            possibleSpells.append("Bolt IV")
        if unit.mp >= self.mpCost(unit, 21):
            possibleSpells.append("Portal I")

        possibleSpells = [
                spell for spell in possibleSpells if spell not in unit.powers]
        if slot == 1:
            possibleSpells = [
                spell for spell in possibleSpells
                if spell not in unit.extraPowerSlot2]
        elif slot == 2:
            possibleSpells = [
                spell for spell in possibleSpells
                if spell not in unit.extraPowerSlot]
        return random.choice(possibleSpells)

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
            targetLevel = target.level + 4
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

    def kill(self, target, killer=None):
        print(f"{target.name} dies!")
        field = self.battleField
        targetPosition = field.getUnitPos(target)
        field.terrainArray[targetPosition].units.remove(target)
        if target in self.turnOrder:
            self.turnOrder.remove(target)
        if type(target) == monster and target.boss:
            if killer:
                killer.stats["Fame"] += 1
                print(
                        f"The wicked {target.name} finally falls, slain "
                        f"by {killer.name}. {killer.name}'s name quickly "
                        "becomes a favorite tale of skalds and minstrels. ")
                print("You are victorious!")
                self.gameStatus = 'victory'
            else:
                self.party[0].stats["Fame"] += 1
                print(
                        f"The monstrous {target.name} finally falls. You are "
                        "victorious!")
                self.gameStatus = 'victory'
        del target
        time.sleep(7. / 10)
        return

    def mpCost(self, unit, amount):
        cost = amount
        if self.getPower(unit, "Magic: Cost Reduction I"):
            cost = math.ceil(cost * 0.75)
        return cost

    def printEstimatedValue(self, unit, equipment=None):
        bf = self.battleField
        bf.printEstimatedValue(unit, equipment)


class battleTile(object):
    """docstring for BattleTile"""

    def __init__(self, terrain, battleField):
        self.name = terrain
        self.cost = 5
        self.goodRinging = 0
        self.evilRinging = 0
        self.proposedGoodVoicePower = 0
        self.proposedEvilVoicePower = 0
        self.voicePower = 0
        self.resonance = self.voicePower

        # Assign cost
        if self.name in ("Bridge", "Path", "Tiled Floor"):
            self.cost = 5
        elif self.name in ("Cavern", "Grass"):
            self.cost = 6
        elif self.name in ("Sand", "Overgrowth"):
            self.cost = 7
        elif self.name in (
                "Upward Stair", "Downward Stair", "Loose Rocks"):
            self.cost = 8
        elif self.name == "Forest":
            self.cost = 10
        # Assign elevation
        if self.name in ("Bridge", "Loose Rocks"):
            self.elevation = battleField.elevation + 1
        elif self.name == "Cavern":
            self.elevation = battleField.elevation - 1
        elif self.name == "Downward Stair":
            self.elevation = battleField.elevation - 1
            battleField.elevation -= 2
        elif self.name == "Upward Stair":
            self.elevation = battleField.elevation + 1
            battleField.elevation += 2
        else:
            self.elevation = battleField.elevation

        # is it unstable?
        if self.name in ("Sand", "Loose Rocks"):
            self.unstable = True
        else:
            self.unstable = False
        self.units = []

class battleField(object):

    def __init__(self, listOfTiles, listOfUnits, party, game, resonance=0):
        self.game = game
        self.elevation = 20
        self.terrainArray = []
        self.units = []
        for tile in listOfTiles:
            self.terrainArray.append(battleTile(tile, self))
        for tile in self.terrainArray:
            tile.voicePower = resonance
        for unit, position in listOfUnits:
            tile = self.terrainArray[position]
            tileUnits = tile.units
            tileUnits.append(unit)
            self.units.append(unit)

        initiativeOrder = []
        for pc in party:
            luck = self.getStat(pc, "Luck")
            initiative = max(
                    self.getStat(pc, "Charisma"),
                    self.getStat(pc, "Speed"),
                    self.getStat(pc, "Dexterity"))
            initiativeOrder.append((pc, initiative, luck))
            initiativeOrder = sorted(initiativeOrder, key=itemgetter(1, 2))
            self.units.append(pc)

        characterBuffer = len(initiativeOrder)
        if characterBuffer < 5:
            for pc, _, _ in initiativeOrder:
                self.terrainArray[1].units.append(pc)
        elif characterBuffer < 9:
            for pc, _, _ in initiativeOrder[:characterBuffer - 4]:
                self.terrainArray[0].units.append(pc)
            for pc, _, _ in initiativeOrder[characterBuffer - 4:]:
                self.terrainArray[1].units.append(pc)
        else:
            for pc, _, _ in initiativeOrder[:characterBuffer - 8]:
                self.terrainArray[0].units.append(pc)
            for pc, _, _ in initiativeOrder[
                    characterBuffer - 8:characterBuffer - 4]:
                self.terrainArray[1].units.append(pc)
            for pc, _, _ in initiativeOrder[characterBuffer - 4:]:
                self.terrainArray[2].units.append(pc)

    def alliesAtPosition(self, me, position):
        return [
                unit for unit in self.terrainArray[position].units
                if type(unit) != type(me) and self.canBeTarget(unit) and (
                        unit != me)]

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
        if len(self.friendsAtPosition(unit, position, False)) < 4:
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
                        else:
                            return  # you forfeit your final movement
                    else:
                        if position == self.getUnitPos(unit) - 1:
                            bonusSpent = True
                        else:
                            return  # you forfeit your final movement
                else:
                    if not bonusSpent:
                        bonusSpent = True  # You get one more movement
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
            # flying units are easier to block but blocked by flying units only
            if self.getPower(unit, "Flying Movment"):
                if len([
                    tileUnit for tileUnit in tile.units
                    if type(tileUnit) != type(unit) and self.getPower(
                            tileUnit, "Flying Movement") and (
                            self.canBlock(tileUnit))]) >= 1:
                    blocked = True
            elif len([
                    tileUnit for tileUnit in tile.units
                    if type(tileUnit) != type(unit) and (
                    self.canBlock(tileUnit))]) >= 2:
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

    def canBlock(self, unit):
        if unit.status:
            if "Petrified" in unit.status:
                return False
            if "Lulled to Sleep" in unit.status:
                return False
        return True

    def canBeTarget(self, unit):
        if unit.status and "Petrified" in unit.status:
            return False
        return True

    def canMove(self, unit):
        if unit.status:
            if "Petrified" in unit.status:
                return False
            if "Lulled to Sleep" in unit.status:
                return False
        return True

    def checkAttack(self, unit, position):
        unit.allowedAttacks = []
        if unit.equipment:
            minRange = unit.equipment.minRange
            maxRange = unit.equipment.maxRange
        else:
            minRange = 0
            maxRange = 0
        # we need to check for spells if the caster is a monster
        if type(unit) == monster:
            if self.getPower(unit, "Blaze II") or (
                    self.getPower(unit, "Freeze III")):
                minRange = 0
                maxRange = 1
        if minRange == 0 and maxRange == 0:
            unit.allowedAttacks = self.enemiesAtPosition(unit, position)
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
                tilePos = self.terrainArray.index(tile)
                for tileUnit in self.enemiesAtPosition(unit, tilePos):
                    unit.allowedAttacks.append(tileUnit)
            return bool(unit.allowedAttacks)

    def checkMove(self, unit, position):
        unit.allowedMovement = []
        currentTile = self.terrainArray[position]
        unstable = currentTile.unstable
        if (self.getPower(unit, "Movement: Ignore Enemies") or self.getPower(
                unit, "Stealthy Movement")):
            retreatBlocked = False
            advancingBlocked = False
        else:
            # flyers are only blocked by other fliers but easier to block
            if self.getPower(unit, "Flying Movement"):
                retreatBlocked = len([
                        tileUnit for tileUnit in currentTile.units
                        if type(tileUnit) != type(unit) and self.getPower(
                                tileUnit, "FlyingMovement") and (
                                self.canBlock(tileUnit))]) >= 2
                advancingBlocked = len([
                        tileUnit for tileUnit in currentTile.units
                        if type(tileUnit) != type(unit) and self.getPower(
                                tileUnit, "FlyingMovement") and (
                                self.canBlock(tileUnit))]) >= 1
            else:
                retreatBlocked = len([
                        tileUnit for tileUnit in currentTile.units
                        if type(tileUnit) != type(unit) and (
                                self.canBlock(tileUnit))]) >= 3
                advancingBlocked = len([
                        tileUnit for tileUnit in currentTile.units
                        if type(tileUnit) != type(unit) and (
                                self.canBlock(tileUnit))]) >= 2
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

    def checkSpell(self, unit, position, name, healing=False, range=0, area=0):
        minRange = max(0, (position - range))
        maxRange = min((position + range), len(self.terrainArray) - 1)
        if area == 0:
            targets = []
            for tile in self.terrainArray[minRange:(maxRange + 1)]:
                tileTargets = self.checkSpellTargets(unit, tile, healing)
                if any(tileTargets):
                    targets.extend(target for target in tileTargets)
            if any(targets):
                unit.allowedSpells[name] = targets
        elif area == 1:
            # area spells target tiles -- should they?
            targetTiles = []
            for tile in self.terrainArray[minRange:(maxRange + 1)]:
                tileTargets = self.checkSpellTargets(unit, tile, healing)
                if any(tileTargets):
                    targetTiles.append(tile)
            if any(targetTiles):
                unit.allowedSpells[name] = targetTiles
        elif area > 1:
            targets = []
            for i in range(minRange, (maxRange + 1)):
                minFocusedRange = max(0, i - (area - 1))
                maxFocusedRange = min(
                        i + (area - 1), len(self.terrainArray - 1))
                tileTargets = []
                for tile in [
                        self.terrainArray[minFocusedRange:(
                        maxFocusedRange + 1)]]:
                    tileTargets = self.checkSpellTargets(unit, tile, healing)
                    if any(tileTargets):
                        targets.extend(self.terrainArray[i])
                        tileTargets = []
                        continue
            if any(targets):
                unit.allowedSpells[name] = targets
        if any(unit.allowedSpells):
            return True
        else:
            return False

    def checkSpellTargets(self, unit, tile, healing):
        position = self.terrainArray.index(tile)
        if healing:
            friends = self.friendsAtPosition(unit, position)
            return [friend for friend in friends if friend.hp < friend.maxHP()]
        else:
            return self.enemiesAtPosition(unit, position)

    def checkSpells(self, unit, position):
        unit.allowedSpells = {}
        currentTile = self.terrainArray[position]
        if (
                self.getPower(unit, "Afflict I") and (
                        unit.mp >= self.mpCost(unit, 13))):
            self.checkSpell(unit, position, "Afflict I", False, 0, 0)
        if self.getPower(unit, "Aura I") and unit.fp >= self.mpCost(unit, 7):
            self.checkSpell(unit, position, "Aura I", True, 1, 1)
        if self.getPower(unit, "Aura II") and unit.fp >= self.mpCost(unit, 11):
            self.checkSpell(unit, position, "Aura II", True, 2, 2)
        if (
                self.getPower(unit, "Aura III") and (
                        unit.mp >= self.fpCost(unit, 15))):
            self.checkSpell(unit, position, "Aura III", True, 2, 2)
        if self.getPower(unit, "Aura IV") and unit.fp >= self.mpCost(unit, 20):
            targets = [
                    target for target in self.party
                    if target.hp > 0 and target.hp < target.maxHP() and (
                            self.canBeTarget(target))]
            if any(targets):
                unit.allowedSpells["Aura IV"] = "Self"
        if self.getPower(unit, "Blaze I") and unit.mp >= self.mpCost(unit, 2):
            self.checkSpell(unit, position, "Blaze I", False, 0, 0)
        if self.getPower(unit, "Blaze II") and unit.mp >= self.mpCost(unit, 6):
            self.checkSpell(unit, position, "Blaze II", False, 1, 1)
        if self.getPower(
                unit, "Blaze III") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Blaze III", False, 1, 1)
        if self.getPower(unit, "Blaze IV") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Blaze IV", False, 1, 0)
        if self.getPower(unit, "Bolt I") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Bolt I", False, 0, 1)
        if self.getPower(unit, "Bolt II") and unit.mp >= self.mpCost(unit, 15):
            self.checkSpell(unit, position, "Bolt II", False, 2, 2)
        if self.getPower(
                unit, "Bolt III") and unit.mp >= self.mpCost(unit, 20):
            self.checkSpell(unit, position, "Bolt III", False, 2, 2)
        if self.getPower(unit, "Bolt IV") and unit.mp >= self.mpCost(unit, 20):
            self.checkSpell(unit, position, "Bolt IV", False, 2, 0)
        if self.getPower(unit, "Dao I") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Dao I", False, 1, 1)
        if self.getPower(unit, "Dao II") and unit.mp >= self.mpCost(unit, 15):
            self.checkSpell(unit, position, "Dao II", False, 1, 1)
        if self.getPower(unit, "Detox I") and unit.fp >= self.mpCost(unit, 3):
            targets = [
                    target for target in currentTile.units
                    if type(target) == type(unit) and target.status]
            if any(targets):
                unit.allowedSpells["Detox I"] = targets
        if self.getPower(unit, "Drain I") and unit.mp >= self.mpCost(unit, 5):
            self.checkSpell(unit, position, "Drain I", False, 0, 0)
        if self.getPower(
                unit, "Drain II") and unit.mp >= self.mpCost(unit, 12):
            self.checkSpell(unit, position, "Drain II", False, 0, 0)
        if self.getPower(unit, "Egress I") and unit.mp >= self.mpCost(unit, 8):
            unit.allowedSpells["Egress I"] = 'Self'
        if self.getPower(unit, "Freeze I") and unit.mp >= self.mpCost(unit, 3):
            self.checkSpell(unit, position, "Freeze I", False, 0, 0)
        if (
                self.getPower(unit, "Freeze II") and (
                unit.mp >= self.mpCost(unit, 7))):
            self.checkSpell(unit, position, "Freeze II", False, 0, 0)
        if (
                self.getPower(unit, "Freeze III") and (
                unit.mp >= self.mpCost(unit, 10))):
            self.checkSpell(unit, position, "Freeze III", False, 1, 1)
        if (
                self.getPower(unit, "Freeze IV") and (
                unit.mp >= self.mpCost(unit, 12))):
            self.checkSpell(unit, position, "Freeze IV", False, 2, 1)
        if self.getPower(unit, "Heal I") and unit.fp >= self.mpCost(unit, 3):
            self.checkSpell(unit, position, "Heal I", True, 0, 0)
        if self.getPower(unit, "Heal II") and unit.fp >= self.mpCost(unit, 6):
            self.checkSpell(unit, position, "Heal II", True, 1, 0)
        if (
                self.getPower(unit, "Heal III") and (
                unit.fp >= self.mpCost(unit, 10))):
            self.checkSpell(unit, position, "Heal III", True, 2, 1)
        if self.getPower(unit, "Heal IV") and unit.fp >= self.mpCost(unit, 20):
            self.checkSpell(unit, position, "Heal IV", True, 0, 0)
        if self.getPower(unit, "Midas I") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Midas I", False, 0, 0)
        if (
                self.getPower(unit, "Portal I") and (
                unit.mp >= self.mpCost(unit, 21))):
            targets = []
            minRange = max(0, (position - 2))
            maxRange = min((position + 2), len(self.terrainArray) - 1)
            currentTile = self.terrainArray[self.getUnitPos(unit)]
            passengers = self.friendsAtPosition(position)
            for tilePos in range(minRange, (maxRange + 1)):
                if tilePos != position:
                    if len(self.friendsAtPosition(tilePos, False)) <= (
                            4 - len(passengers)):
                        targets.extend(self.terrainArray[tilePos])
            if any(targets):
                unit.allowedSpells["Portal I"] = targets
        if (
                self.getPower(unit, "Teleport I") and (
                unit.mp >= self.mpCost(unit, 5))):
            targets = []
            minRange = max(0, (position - 1))
            maxRange = min((position + 1), len(self.terrainArray) - 1)
            for tilePos in range(minRange, (maxRange + 1)):
                if tilePos != position:
                    if len(self.friendsAtPosition(tilePos, False)) < 4:
                        targets.append(self.terrainArray[tilePos])
            if any(targets):
                unit.allowedSpells["Teleport I"] = targets
        if (
                self.getPower(unit, "Teleport II") and (
                unit.mp >= self.mpCost(unit, 10))):
            targets = []
            minRange = max(0, (position - 2))
            maxRange = min((position + 2), len(self.terrainArray) - 1)
            for tilePos in range(minRange, (maxRange + 1)):
                if tilePos != position:
                    if len(self.friendsAtPosition(position, False)) < 4:
                        targets.append(self.terrainArray[tilePos])
            if any(targets):
                unit.allowedSpells["Teleport II"] = targets
        if (
                self.getPower(unit, "Teleport III") and (
                unit.mp >= self.mpCost(unit, 6))):
            targets = []
            minRange = max(0, (position - 3))
            maxRange = min((position + 3), len(self.terrainArray) - 1)
            for tilePos in range(minRange, (maxRange + 1)):
                if tilePos != position:
                    if len(self.friendsAtPosition(position, False)) < 4:
                        targets.append(self.terrainArray[tilePos])
            if any(targets):
                unit.allowedSpells["Teleport III"] = targets
        if any(unit.allowedSpells):
            return True
        else:
            return False

    def checkVocal(self, unit):
        position = self.getUnitPos(unit)
        currentTile = self.terrainArray[position]
        vp = currentTile.voicePower
        if ((
                type(unit) == playerCharacter and (vp > 1)) or (
                type(unit) == monster and (vp < -1))):
            return any(self.enemiesAtPosition(unit, position))
        else:
            return False

    def doMonsterMove(self, monster, position):
        moveTo = None
        if monster.moveProfile == "Advance-Defensive":
            if monster.hp < monster.maxHP():
                monster.moveProfile = "Aggressive"
                moved = self.doMonsterMove(monster, position)
                return moved
            else:
                moveTo = min(monster.allowedMovement)
                if position == 0 or moveTo > position:
                    monster.moveProfile = "Defensive"
                    moved = self.doMonsterMove(monster, position)
                    return moved
            self.move(monster, moveTo)
            return True
        elif monster.moveProfile == "Aggressive":
            # will not move if in melee range of enemies
            if any(self.playersAtPosition(position)):
                return False
            # move as far forward as possible to tiles with enemies
            candidates = []
            for position in monster.allowedMovement:
                if any(self.playersAtPosition(position)):
                    candidates.append(position)
            if candidates:
                moveTo = min(candidates)
            else:
                # move as far forward as possible
                moveTo = min(monster.allowedMovement)
            self.move(monster, moveTo)
            return True
        elif monster.moveProfile == "Aggressive-Singer":
            # just like aggressive but prefers to move to places with larger
            # concentration of enemies and friends
            candidates = []
            maxPCs = max([
                    len(self.playersAtPosition(position))
                    for position in monster.allowedMovement])
            if maxPCs > 0:
                for position in monster.allowedMovement:
                    if len(self.playersAtPosition(position)) == maxPCs:
                        candidates.append(position)
                if any(candidates):
                    candidates2 = []
                    maxMonsters = max([
                            len(self.monstersAtPosition(position))
                            for position in candidates])
                    for position in candidates:
                        if len(
                                self.monstersAtPosition(position)) == (
                                maxMonsters):
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
            return True
        elif monster.moveProfile == "Defensive":
            if monster.hp < monster.maxHP():
                monster.moveProfile = "Aggressive"
                moved = self.doMonsterMove(monster, position)
                return moved
            else:
                candidates = []
                for position in monster.allowedMovement:
                    if self.playersAtPosition(position):
                        candidates.append(position)
                if candidates:
                    moveTo = max(candidates)
                else:
                    return False
            self.move(monster, moveTo)
            return True
        elif monster.moveProfile == "Random":
            if monster.hp < monster.maxHP():
                monster.moveProfile = "Aggressive"
                moved = self.doMonsterMove(monster, position)
                return moved
            else:
                moveTo = random.choice(monster.allowedMovement)
                self.move(monster, moveTo)
                return True
        elif monster.moveProfile == "Retreat-Defensive":
            if monster.hp < monster.maxHP():
                monster.moveProfile = "Aggressive"
                moved = self.doMonsterMove(monster, position)
                return moved
            else:
                moveTo = max(monster.allowedMovement)
                if position == len(self.terrainArray) - 1 or moveTo < position:
                    monster.moveProfile = "Defensive"
                    moved = self.doMonsterMove(monster, position)
                    return moved
            self.move(monster, moveTo)
            return True
        elif monster.moveProfile == "SlowAdvance":
            # will not move if in melee range of enemies
            if any([self.playersAtPosition(position)]):
                monster.moveProfile == "Aggressive"
                return False
            # move as far forward as possible to tiles with enemies
            candidates = []
            for candidate in monster.allowedMovement:
                if any([self.playersAtPosition(position)]):
                    candidates.append(candidate)
            if candidates:
                moveTo = min(candidates)
                monster.moveProfile == "Aggressive"
            else:
                # move as little forward as possible
                candidates = [
                        candidate for candidate in monster.allowedMovement
                        if candidate < position]
                if candidates:
                    moveTo = max(candidates)
            if moveTo:
                self.move(monster, moveTo)
                return True
            else:
                return False
        elif monster.moveProfile == "Sniper":
            candidates = [
                    target for target in self.game.party if target.hp > 0 and (
                            self.canBeTarget(target))]
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
                    return False
            self.move(monster, moveTo)
            return True

    def enemiesAtPosition(self, me, position):
        return [
                unit for unit in self.terrainArray[position].units
                if type(unit) != type(me) and self.canBeTarget(unit)]

    def friendsAtPosition(self, me, position, filterTargets=True):
        if filterTargets:
            return [
                    unit for unit in self.terrainArray[position].units
                    if type(unit) == type(me) and self.canBeTarget(unit)]
        else:
            return [
                    unit for unit in self.terrainArray[position].units
                    if type(unit) == type(me)]

    def getFameBonus(self, unit):
        position = self.getUnitPos(unit)
        if not position:
            return 0
        allyFame = [
                ally.stats["Fame"]
                for ally in self.alliesAtPosition(unit, position)]
        if any(allyFame):
            return max(allyFame)
        else:
            return 0

    def getName(self, unit, target):
        if type(unit) == playerCharacter:
            if type(target) == monster and target.name not in unit.trophies:
                return f'{target.name}*'
        return target.name

    def getPower(self, unit, name):
        if any([name in power for power in unit.powers]):
            return True
        if unit.equipment:
            if any([name in power for power in unit.equipment.powers]):
                return True
        if name not in (
                'Random Additional Spell I', 'Random Additional Spell II'):
            if self.getPower(unit, 'Random Additional Spell I'):
                if any([name in power for power in unit.extraPowerSlot]):
                    return True
            if self.getPower(unit, 'Random Additional Spell II'):
                if any([name in power for power in unit.extraPowerSlot2]):
                    return True
        commandName = "Command: " + name
        position = self.getUnitPos(unit)
        if not position:
            return False
        for ally in self.alliesAtPosition(unit, position):
            if any([commandName in power for power in unit.powers]):
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

    def monstersAtPosition(self, position):
        return [
                unit for unit in self.terrainArray[position].units
                if type(unit) == monster and self.canBeTarget(unit)]

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

    def playersAtPosition(self, position):
        return [
                unit for unit in self.terrainArray[position].units
                if type(unit) == playerCharacter and self.canBeTarget(unit)]

    def printAttackString(self, unit):
        attackString = f"{unit.name} can attack "
        attackStringAdds = []
        for target in unit.allowedAttacks:
            targetHealth = target.maxHP()
            attackStringAdds.append(
                    f"({unit.allowedAttacks.index(target)}) "
                    f"{self.getName(unit, target)} "
                    f"(HP: {target.hp}/{targetHealth})")
        attackString += ", ".join(attackStringAdds)
        print(attackString + ".")

    def printEstimatedValue(self, unit, equipment=None):
        valueString = "  "
        incumbent = unit.equipment
        unitDamage = max(
                self.getStat(unit, "Strength"),
                self.getStat(unit, "Dexterity"))
        if incumbent:
            fromDamage = incumbent.damage + unitDamage
            fromFaith = incumbent.fp + self.getStat(unit, "Faith")
            fromMagic = incumbent.mp + self.getStat(unit, "Intelligence")
            fromType = incumbent.type
        else:
            fromDamage = unitDamage
            fromFaith = self.getStat(unit, "Faith")
            fromMagic = self.getStat(unit, "Intelligence")
            fromType = "Unarmed Attack"
        if self.getPower(unit, f"{fromType}: Increased Damage I"):
            fromDamage *= 1.3
        if self.getPower(unit, f"{fromType}: Increased Damage II"):
            fromDamage *= 1.3
        if self.getPower(unit, f"{fromType}: Increased Damage III"):
            fromDamage *= 1.3
        if self.getPower(unit, f"{fromType}: Increased Damage IV"):
            fromDamage *= 1.3
        if equipment:
            toDamage = equipment.damage + unitDamage
            toFaith = equipment.fp + self.getStat(unit, "Faith")
            toMagic = equipment.mp + self.getStat(unit, "Intelligence")
            toType = equipment.type
        else:
            toDamage = unitDamage
            toFaith = self.getStat(unit, "Faith")
            toMagic = self.getStat(unit, "Intelligence")
            toType = "Unarmed Attack"
        if self.getPower(unit, f"{toType}: Increased Damage I"):
            toDamage *= 1.3
        if self.getPower(unit, f"{toType}: Increased Damage II"):
            toDamage *= 1.3
        if self.getPower(unit, f"{toType}: Increased Damage III"):
            toDamage *= 1.3
        if self.getPower(unit, f"{toType}: Increased Damage IV"):
            toDamage *= 1.3
        if fromDamage != toDamage:
            valueString += (
                    f"Damage: {round(fromDamage)}-->"
                    f"{round(toDamage)}  ")
        if fromFaith != toFaith:
            valueString += f"FP: {fromFaith}-->{toFaith}  "
        if fromMagic != toMagic:
            valueString += f"MP: {fromMagic}-->{toMagic}  "
        print(valueString)

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
            elif type(target) in (monster, playerCharacter):
                targetHealth = target.maxHP()
                targetStringAdds.append(
                        f"({count}) {self.getName(unit, target)} "
                        f"(HP: {target.hp}/{targetHealth})")
                count += 1
            elif type(target) == battleTile:
                targetStringAdds.append(
                        f"({count}) {target.name} "
                        f"({self.terrainArray.index(target)})")
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
        maxRange = minRange + 7
        if maxRange > len(self.terrainArray) - 1:
            maxRange = len(self.terrainArray) - 1
            minRange = maxRange - 7
        tilesInRange = self.terrainArray[minRange:maxRange + 1]
        mapRow = ""
        for tile in tilesInRange:
            mapAdd = f"({self.terrainArray.index(tile)})"
            tileHeight = tile.elevation - 20
            if tileHeight > 0:
                mapAdd += f" +{tileHeight} "
            elif tileHeight < 0:
                mapAdd += f" {tileHeight} "
            if round(tile.voicePower) > 0:
                mapAdd += "(Shining)"
            elif round(tile.voicePower) < 0:
                mapAdd += "(Unholy)"
            mapRow += f"{mapAdd:24}"
        print(mapRow)
        for i in range(11, -1, -1):
            mapRow = ""
            for tile in tilesInRange:
                try:
                    goodUnits = [
                            unit for unit in tile.units
                            if type(unit) == playerCharacter]
                    goodUnits.sort(key=lambda x: x.shortName, reverse=True)
                    mapRow += f"{goodUnits[i].shortName:9}   "
                except IndexError:
                    mapRow += (" " * 12)
                try:
                    badUnits = [
                            unit for unit in tile.units
                            if type(unit) == monster]
                    badUnits.sort(key=lambda x: x.shortName, reverse=True)
                    mapRow += f"{badUnits[i].shortName:9}   "
                except IndexError:
                    mapRow += (" " * 12)
            if [letter for letter in mapRow if letter != " "]:
                print(mapRow)
        print("-" * 24 * len(tilesInRange))
        mapRow = ""
        for tile in tilesInRange:
            mapRow += f"{tile.name:24}"
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
        self.maxPartySize = 12

        chatter = False
        print("You are the leader of a small part of misfits.")
        print("You are from Yatahal, the Holy City.")
        print(
                "Yatahal is a bastion of goodness, but the centaur Knights of "
                "Yatahal")
        print(
                "look down on all other people as unfit to participate in "
                "combat.")
        print(
                "Despite this, your mentor has assembled a small force of "
                "untrained fighters that he believes have potential.")
        print("Elves and Dwarves and the occaisional drummed-out Knight.")
        print(
                "You are the laughingstock of Yatahal's knights, but you "
                "believe that you are destined for greatness.")
        print("")
        print(
                "One day, you go out to bring supplies to the knight that "
                "guards the Ancient Sealed Door.")
        print(
                "When you arrive, you find that he is consorting with Goblins "
                "and plotting the downfall of Yatahal.")
        print("")
        print("Swallowing your fear, you draw arms and challenge them!")
        recruit = playerCharacter(
                "Max", "Human", "Hero", chatter, 0)
        self.equipOnCharacter(
                equipment("Swords", "Middle Sword", 250, 0, 0, 5, 0, 0),
                recruit, False)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Lowe", "Hobbit", "Priest", chatter, 0)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 80, 0, 0, 1, 3, 3),
                recruit, False)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Tao", "Elf", "Fire Mage", chatter, 0)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 80, 0, 0, 1, 3, 3),
                recruit, False)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Luke", "Dwarf", "Warrior", chatter, 0)
        self.equipOnCharacter(
                equipment("Axes", "Short Axe", 120, 0, 0, 3, 0, 0), recruit,
                False)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Ken", "Centaur", "Knight", chatter, 0)
        self.equipOnCharacter(
                equipment("Spears", "Wooden Spear", 100, 0, 1, 3, 0, 0),
                recruit, False)
        self.playerCharacters.append(recruit)
        recruit = playerCharacter(
                "Hans", "Elf", "Archer", chatter, 0)
        self.equipOnCharacter(
                equipment("Arrows", "Wooden Arrow", 150, 1, 1, 3, 0, 0),
                recruit, False)
        self.playerCharacters.append(recruit)

        self.party = self.playerCharacters
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(8, 'king')
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
        print("The monk, Gong, joins your cause!")
        print("")
        print("You spy a pillar of smoke rising from the direction of home.")
        print("That's not good....")
        print("")
        recruit = playerCharacter("Gong", "Half-Giant", "Monk", chatter, 1)
        recruit.levelUp(chatter)
        self.playerCharacters.append(recruit)
        self.party = self.playerCharacters
        self.reckoning(25, 'lonely priest')
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(8, 'lonely priest')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'lonely priest')
            battle(self, self.party, 2)
        print("")
        print("The party arrives at the Holy City of Yatahal. It is burning.")
        print("Too late to intervene, you watch in horror as your mentor ")
        print("and your king are slain by a dark swordsman who looks exactly ")
        print("like you. The swordsman disappears into a black void")
        print(
                "If you weren't in the room with them when this happened, "
                "you're sure ")
        print(
                "that the Knights of Yatahal would have posted a bounty on "
                "your head.")
        print("")
        print("In the aftermath of the assassination, your mentor's daughter,")
        print("Mae, joins you! With her is a washed up former city guard, ")
        print("drunk on wine and thirsty for vengence, Gort!")
        print("")
        recruit = playerCharacter("Mae", "Centaur", "Knight", chatter, 2)
        self.playerCharacters.append(recruit)
        self.equipOnCharacter(
                equipment("Lances", "Bronze Lance", 300, 0, 0, 6, 0, 0),
                recruit, False)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit = playerCharacter("Gort", "Dwarf", "Warrior", chatter, 2)
        self.playerCharacters.append(recruit)
        self.equipOnCharacter(equipment(
                "Axes", "Hand Axe", 200, 0, 0, 4, 0, 0), recruit, False)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        self.party = self.playerCharacters
        self.reckoning(25, 'widow of your mentor')
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(8, 'widow of your mentor')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'widow of your mentor')
            battle(self, self.party, 3)
        print("")
        print("You arrive in Ulmara, a small merchant city bordering Yatahal.")
        print("The King of Ulmara greets you warmly, bestowing lavish gifts.")
        self.reckoning(40, "King of Ulmara")
        print(
                "The King gestures to the shopping district: \"Go visit a "
                "smith!\"")
        print(
                "On your way to the shops, you notice a young Kyantol woman "
                "following you.")
        shop(self, [
                "Wooden Arrow", "Hand Axe", "Short Knife", "Spear",
                "Wooden Staff", "Middle Sword"], [
                "Wooden Arrow", "Hand Axe", "Short Knife", "Spear",
                "Wooden Staff", "Middle Sword", "Middle Axe", "Iron Shot",
                "Bronze Lance"])
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
        print("Khris joins your force!")
        recruit = playerCharacter("Khris", "Kyantol", "Priest", chatter, 4)
        self.equipOnCharacter(
                equipment("Staffs", "Wooden Staff", 80, 0, 0, 1, 3, 3),
                recruit, False)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        self.playerCharacters.append(recruit)
        self.party = self.playerCharacters
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(15, 'priests')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'priests')
            battle(self, self.party, 4)
        print("")
        print("You arrive at Malanar, the Cathedral of magic.")
        print(
                "Malanar is the heart of magical and divine research and "
                "training in Yatahal, and ")
        print("still stands against the enemy forces.")
        print(
                "You ask to see the Princess, now the queen of Malanar and "
                "Yatahal.")
        print(
                "You are ushered into the court of the Ice Rose, retainers "
                "for the princess.")
        self.reckoning(30, 'the courtiers')
        print(
                "A worried courtier directs you north, across the desert of "
                "Penance.")
        print(
                "She says that the princess is at the Chapel of Penance "
                "learning the secrets of the Songs of the Creator.")
        print(
                "Before you venture north, you establish a base of operations "
                "in Malanar and go shopping.")
        shop2 = shop(self, [
                "Middle Sword", "Spear", "Bronze Lance", "Wooden Staff",
                "Power Staff", "Iron Shot"], [
                "Steel Arrow", "Middle Axe", "Knife", "Power Staff",
                "Power Spear"])
        self.party = self.playerCharacters
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(15, 'the courtiers')
                shop2.goShopping(self)
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'the courtiers')
                shop2.goShopping(self)
            battle(self, self.party, 5)
        print("")
        print("You enter the chapel and immediately find the princess.")
        print(
                "You inform her that her father is dead and that she is now "
                "the Queen.")
        print(
                "She turns white and orders you to take her back to Malanar "
                "at once.")
        print(
                "Once in Malanar, Anri mourns for half a day before gathering "
                "her resolve and summoning you.")
        self.reckoning(35, "new Queen")
        print(
                "Anri he informs you of her intent to join you "
                "and take the battle back to Darksol.")
        print("To do that, you will need to brave a dark cave under Malanar ")
        print("-- the very thing that Malanar was created to seal.")
        print("Within, she claims you will find a sacred sword.")
        print("Anri joins your force!")
        recruit = playerCharacter("Anri", "Human", "Frost Mage", chatter, 6)
        self.equipOnCharacter(
                equipment("Staffs", "Power Staff", 500, 0, 0, 4, 6, 6),
                recruit, False)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        recruit.levelUp(chatter)
        print(
                "You head to the shopping district before descending into the "
                "cavern.")
        shop2.goShopping(self)
        print("With that out of the way, you descend into the dark cavern.")
        self.party = self.playerCharacters
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(15, 'the royal coffers')
                shop2.goShopping(self)
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'the royal coffers')
                shop2.goShopping(self)
            battle(self, self.party, 6)
        print("")
        print(
                "After slaying the evil Skeleton, you find the sword buried "
                "in a sacred stone altar.")
        print('"It\'s the Sword of Truth." says Anri.')
        print(
                '"It\'s sacred because it give the wielder the power to see '
                'through falsehoods and illusions."')
        print("You nod, gripping the Sword as you head up to the surface.")
        print(
                "You'd better remember to equip the Sword for battle, if you "
                "can.")
        swordOfTruth = equipment(
                "Sacred Swords", "Sword of Truth", 7200, 0, 0, 10, 0, 8,
                ["Bolt I"])
        self.inventory.append(swordOfTruth)
        print(
                "When you leave the cave, blinking in the sunlight over "
                "you notice a sinister sight on the outskirts of Malanar.")
        print(
                "Where once stood a pavilion for a traveling circus, instead "
                "stands a dark altar. Evil emanates from it, and lifeless "
                "bodies shuffle around it.")
        print(
                'Anri gasps. "The power of the Sword! It has dispelled an '
                "illusion! This must be Darksol\'s handiwork -- and here in "
                'the Holy City!"')
        print("You steel yourself for a grueling battle. By going shopping.")
        shop2.goShopping(self)
        print(
                "Gritting your teeth, you rally the Force and head to the "
                "altar. What dark trials await?")
        self.party = self.playerCharacters
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(15, 'the royal coffers')
                shop2.goShopping(self)
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'the royal coffers')
                shop2.goShopping(self)
            battle(self, self.party, 7)
        print("")
        print(
                "Anri lets out a shuttering sigh, wiping the blood from her "
                "face.")
        print(
                "Once she catches her breath, she turns to you with a "
                "startling look.")
        print(
                '"That thing -- it was a dark creation." She says, "They '
                'should be held at bay by the words of the Holy Songs."')
        print(
                '"But people have stopped singing the songs or teaching them '
                'to their children."')
        print(
                '"The words of the Holy Songs are kept in a chapel to the '
                'North." She turns and points North.')
        print(
                '"We need to retrieve them, now! If evil has come this '
                'close, the Holy Songs will be threatened!"')
        print(
                "With that, she gathers herself and heads North.")
        print(
                "Unsure of what she is talking about, you follow.")
        print("")
        print(
                "When you arrive at the chapel, you are met by a group of "
                "priests, led by a tall Vicar.")
        print(
                'The vicar welcomes you, "The Words are kept in a warded '
                'room, that can only be opened by the Keepers, Angelic '
                'bird-men who are devoted to Heaven."')
        print(
                "You watch as the Keepers remove the wards. But as soon as "
                "they do, the Vicar removes his hood and reveals himself to "
                "be Darksol!")
        print(
                "He casts a dark spell, turning the Keepers to stone, then "
                "grabs the scrolls containing the words. They burst into "
                "dark blue flames as he laughs. As they burn, he disappears.")
        print(
                "What remains of his delegation lurches forward. The priests "
                "are dead, transformed to Zombies and Skeletons!")
        self.party = self.playerCharacters
        self.battleStatus = None
        while self.battleStatus != 'victory':
            if self.battleStatus == 'egress':
                self.reckoning(15, 'Anri')
            elif self.battleStatus == 'defeat':
                self.reckoning(0, 'Anri')
            battle(self, self.party, 8)

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

    def equipOnCharacter(self, equipment, character, chatter=True):
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
            if equipment.equippedBy:
                incumbent = equipment.equippedBy
                incumbent.equipment = None
            equipment.equippedBy = pc
            pc.equipment = equipment
            if equipment not in self.inventory:
                self.inventory.append(equipment)
            if chatter:
                print(f"{pc.name} equipped the {equipment.name}.")

    def getSellPrice(self, item):
        equipString = f"Equip: {item.type}"
        blame = None
        equipable = [
                pc for pc in self.playerCharacters if equipString in pc.powers]
        if equipable:
            fame = max([pc.stats["Fame"] for pc in equipable])
            if fame > 15:
                blame = [
                        pc.name for pc in self.playerCharacters
                        if equipString in
                        pc.powers and pc.stats["Fame"] == fame][0]
        else:
            fame = 0
        amount = math.floor(item.price * (0.1 + (fame / 100)))
        return amount, blame

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
            if abs(amount) >= self.money:
                print(
                        f"The priests take all of your money to cover the "
                        f"cost of the prayers that saved you. Consider them "
                        f"generous.")
            else:
                print(
                        f"The priests request {-amount} scroulings for the "
                        f"prayers that recalled the souls of your party.")


game = game()
