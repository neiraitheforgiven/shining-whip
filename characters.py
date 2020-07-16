import math
from operator import itemgetter
import random


class monster(object):

    def __init__(
            self, name, moveProfile=None, attackProfile=None, level=None):
        self.stats = {}
        self.hp = 0
        self.fp = 0
        self.mp = 0
        self.movementPoints = 0
        self.name = name
        self.shortName = name[:7]
        self.allowedMovement = []
        self.allowedAttacks = []
        self.allowedEquipment = []
        self.allowedSpells = {}
        self.powers = []
        self.moveProfile = moveProfile
        self.attackProfile = attackProfile
        self.equipment = None
        self.status = None
        if name == "Crazed Dwarf":
            self.level = 3
            stats = {"Strength": 7, "Stamina": 6, "Speed": 4, "Faith": 8}
            self.setStats(5, **stats)
            self.moveProfile = moveProfile or "Defensive"
            self.attackProfile = attackProfile or "Random"
            self.equipment = equipment("Axes", "Rusted Axe", 20, 0, 0, 3, 0, 0)
            self.shortName = "C.Dwarf"
        elif name == "Dark Apprentice":
            self.level = 6
            stats = {
                    "Stamina": 5, "Intelligence": 13, "Strength": 9,
                    "Speed": 9}
            self.setStats(6, **stats)
            self.moveProfile = moveProfile or "Defensive"
            self.attackProfile = attackProfile or "Spellcaster"
            self.equipment = equipment(
                    "Staffs", "Wooden Staff", 80, 0, 0, 1, 3, 3)
            self.powers = ["Blaze II", "Defense: Magic"]
            self.shortName = "D.Apprc"
        elif name == "Giant Bat":
            self.level = 5
            stats = {"Voice": 11, "Stamina": 7, "Speed": 7, "Dexterity": 6}
            self.setStats(7, **stats)
            self.attackProfile = "Singer"
            self.moveProfile = "Aggressive-Singer"
            self.powers.append("Flying Movement")
            self.powers.append("Sonorous Voice")
            self.shortName = "Bat"
        elif name == "Goblin":
            self.level = 1
            stats = {"Dexterity": 6, "Stamina": 5, "Speed": 5}
            self.setStats(5, **stats)
            self.moveProfile = moveProfile or "Aggressive"
            self.attackProfile = attackProfile or "Random"
            self.equipment = equipment(
                    "Swords", "Goblin Sword", 50, 0, 0, 3, 0, 0)
        elif name == "Sniper":
            self.level = 4
            stats = {"Dexterity": 12, "Stamina": 6, "Speed": 7}
            self.setStats(5, **stats)
            self.moveProfile = moveProfile or "Sniper"
            self.attackProfile = attackProfile or "Weakest"
            self.equipment = equipment(
                    "Arrows", "Wooden Arrow", 150, 1, 1, 3, 0, 0)
        elif name == "Traitor Knight":
            self.level = 4
            stats = {"Strength": 11, "Stamina": 6, "Speed": 7, "Charisma": 7}
            self.setStats(6, **stats)
            self.moveProfile = moveProfile or "Retreat-Defensive"
            self.attackProfile = attackProfile or "ChallengeAccepting"
            self.equipment = equipment(
                    "Lances", "Bronze Lance", 300, 0, 0, 6, 0, 0)
            self.powers.append(["Mounted Movement"])
            self.shortName = "Knight"
        else:
            self.level = level
            stats = {}
            self.setStats(5, **stats)
            self.moveProfile = moveProfile or "Defensive"
            self.attackProfile = attackProfile or "Random"

    def maxHP(self):
        return ((self.stats["Stamina"] * 2) + self.level)

    def setStats(self, statLevel, **stats):
        statsToAssign = [
                "Strength", "Dexterity", "Intelligence", "Faith", "Charisma",
                "Luck", "Speed", "Stamina", "Voice", "Fame"]
        advance = True
        for i in range(len(statsToAssign)):
            stat = random.choice(statsToAssign)
            if stat in stats:
                self.stats[stat] = stats[stat]
            else:
                self.stats[stat] = statLevel
                advance = not advance
                if advance:
                    statLevel += 1
            statsToAssign.remove(stat)


class playerCharacter(object):
    """docstring for playerCharacter"""

    def __init__(
            self, name=None, race=None, playerClass=None, chatter=False,
            battleNum=None):
        self.hp = 0
        self.fp = 0
        self.mp = 0
        self.xp = 0
        self.movementPoints = 0
        self.powers = []
        self.equipment = None
        self.allowedMovement = []
        self.allowedAttacks = []
        self.allowedEquipment = []
        self.allowedSpells = {}
        self.status = None
        self.trophies = []
        if playerClass:
            if playerClass == "Assassin":
                self.growth = self.initializeRandomStats(
                        "Strength", "Dexterity")
            elif playerClass == "Archer":
                self.growth = self.initializeRandomStats(
                        "Dexterity", "Stamina")
            elif playerClass == "Baron":
                self.growth = self.initializeRandomStats("Strength", "Fame")
            elif playerClass == "Bolt Mage":
                self.growth = self.initializeRandomStats(
                    "Intelligence", "Luck")
            elif playerClass == "Brass Gunner":
                self.growth = self.initializeRandomStats(
                        "Stamina", "Dexterity")
            elif playerClass == "Fire Mage":
                self.growth = self.initializeRandomStats(
                        "Intelligence", "Charisma")
            elif playerClass == "Frost Mage":
                self.growth = self.initializeRandomStats(
                        "Intelligence", "Stamina")
            elif playerClass == "Harbinger":
                self.growth = self.initializeRandomStats("Speed", "Voice")
            elif playerClass == "Knight":
                self.growth = self.initializeRandomStats("Strength", "Speed")
            elif playerClass == "Monk":
                self.growth = self.initializeRandomStats("Faith", "Strength")
            elif playerClass == "Priest":
                self.growth = self.initializeRandomStats("Faith", "Charisma")
            elif playerClass == "Samurai":
                self.growth = self.initializeRandomStats("Stamina", "Faith")
            elif playerClass == "Sky Battler":
                self.growth = self.initializeRandomStats("Speed", "Strength")
            elif playerClass == "Sky Lord":
                self.growth = self.initializeRandomStats(
                        "Speed", "Intelligence")
            elif playerClass == "Soldier":
                self.growth = self.initializeRandomStats("Luck", "Strength")
            elif playerClass == "Sorceror":
                self.growth = self.initializeRandomStats(
                        "Intelligence", "Faith")
            elif playerClass == "Steam Knight":
                self.growth = self.initializeRandomStats(
                        "Stamina", "Intelligence", "Fame")
            elif playerClass == "Hero":
                self.growth = self.initializeRandomStats(
                        "Strength", "Intelligence")
            elif playerClass == "Survivor":
                self.growth = self.initializeRandomStats("Voice", "Stamina")
            elif playerClass == "Thief":
                self.growth = self.initializeRandomStats(
                        "Dexterity", "Intelligence")
            elif playerClass == "Titan":
                self.growth = self.initializeRandomStats(
                        "Stamina", "Fame", "Speed")
            elif playerClass == "Warrior":
                self.growth = self.initializeRandomStats("Strength", "Stamina")
            elif playerClass == "Werewolf":
                self.growth = self.initializeRandomStats(
                        "Dexterity", "Strength", "Luck")
            else:
                self.growth = self.initializeRandomStats()
        else:
            self.growth = self.initializeRandomStats()
        self.battleNum = battleNum
        self.stats = {}
        for statName, statValue in self.growth.items():
            self.stats[statName] = 13 - statValue
        self.level = 0
        self.statIncreaseCount = 0
        if name:
            self.name = name
            self.shortName = name[:7]
        else:
            num = random.randint(1, 9999)
            self.name = f"Test Subject {num}"
            self.shortName = f"{num}"
        self.title = "newbie"
        self.career = ""
        self.race = self.assignRace(race)
        self.assignTitle(chatter)
        print(f"{self.name} the {self.race} {self.title} created.")
        self.assignPower()
        self.career = f"    Career Path: {self.title}"
        if chatter:
            for statName, statValue in self.stats.items():
                print("    {} of {}".format(statName, statValue))
            print("")

    def assignPower(self):
        if "Mounted" in self.title and "Mounted Movement" not in self.powers:
            self.powers.append("Mounted Movement")
            return
        elif "Sky" in self.title and "Flying Movement" not in self.powers:
            self.powers.append("Flying Movement")
            return
        else:
            listOfPowers = []
            if "Archer" in self.title:
                listOfPowers = [
                        "Equip: Arrows", "Quick Shot", "Aimed Shot",
                        "Arrows: Increased Damage I", "Poison Arrow",
                        "Luck: Enable Triple Attack", "Arrows: Range + 1",
                        "Point-Blank Shot"]
            elif "Assassin" in self.title:
                listOfPowers = [
                        "Stealthy Movement", "Sleep I", "Seal I", "Death I",
                        "Shield I", "Death II", "Equip: Sacred Swords",
                        "Luck: Critical Hit Adds Seal"]
            elif "Bard" in self.title:
                listOfPowers = [
                        "Equip: Dagger", "Heal I", "Equip: Bows",
                        "Counterattack", "Luck: Enable Triple Attack",
                        "Command: Health Regeneration",
                        "Vocal Attack: Increased Damage I",
                        "Luck: Increased Dodge Chance"]
            elif "Baron" in self.title:
                listOfPowers = [
                        "Equip: Long Swords", "Command: Counterattack",
                        "Luck: Reverse Death", "Swords: Increased Damage I",
                        "Luck: Critical Drain I",
                        "Command: Luck: Increased Critical Chance",
                        "Death II", "Luck: Critical Drain II"]
            elif "Berserker" in self.title:
                listOfPowers = [
                        "Equip: Axes", "Unarmed Attack: Increased Damage I",
                        "Unhindered Movement", "Axes: Armor Penetration I",
                        "Unarmed Attack: Add Effect: Slow",
                        "Low Health: Damage Increase I",
                        "Unarmed Attack: Increased Damage II",
                        "Unarmed Attack: Rout Deals Damage"]
            elif "Blood Mage" in self.title:
                listOfPowers = [
                        "Drain I", "Poison I", "Drain II", "Equip: Daggers",
                        "Muddle I", "Death I",
                        "Magic: Critical Chance I", "Poison II"]
            elif "Bolt Mage" in self.title:
                listOfPowers = [
                        "Bolt I", "Blaze I", "Freeze I",
                        "Magic: Increased Area I", "Bolt II", "Bolt III",
                        "Death I", "Bolt IV"]
            elif "Brass Gunner" in self.title:
                listOfPowers = [
                        "Equip: Brass Guns", "Unhindered Movement",
                        "Brass Guns: Critical Damage I",
                        "Defense: Increased Armor I",
                        "Movement: Range Increase I",
                        "Brass Guns: Critical Damage II",
                        "Defense: Increased Armor II",
                        "Brass Guns: Attack Area Increased"]
            elif "Cantor" in self.title:
                listOfPowers = [
                        "Mounted Movement", "Luck: Increased Rout I",
                        "Defense: Vocal Attack I",
                        "Vocal Attack: Increased Damage I",
                        "Luck: Increased Rout II",
                        "Defense: Dark Magic I",
                        "Vocal Attack: Increased Damage II"
                        "Rout: Add Effect: Fear"]
            elif "Chorister" in self.title:
                listOfPowers = [
                        "Vocal Attack: Increased Damage I", "Heal I",
                        "Blast I", "Vocal Attack: Increased Damage II",
                        "Blast II", "Command: Vocal Attack: Increased Damage II",
                        "Vocal Attack: Increased Damage III", "Blast III"]
            elif "Dark Mage" in self.title:
                listOfPowers = [
                        "Blaze I", "Defense: Magic", "Freeze I", "Blaze II",
                        "Death I", "Freeze II", "Death II", "Bolt I"]
            elif "Druid" in self.title:
                listOfPowers = [
                        "Stealthy Movement", "Defense: Increased Resistance I",
                        "Detox I", "Blast I", "Conduit I", "Blast II",
                        "Defense: Increased Resistance II", "Blast III"]
            elif "Duelist" in self.title:
                listOfPowers = [
                        "Equip: Long Swords", "Counterattack",
                        "Defense: Swords I", "Swords: Increased Luck I",
                        "Swords: Increased Luck II", "Luck: Dodge Grants Counterattack",
                        "Swords: Increased Luck III", "First Strike"]
            elif "Fire Mage" in self.title:
                listOfPowers = [
                        "Blaze I", "Magic: Cost Reduction I", "Sleep I",
                        "Blaze II", "Counterspell I", "Blaze III",
                        "Magic: Increased Damage I", "Blaze IV"]
            elif "Frost Mage" in self.title:
                listOfPowers = [
                        "Freeze I", "Blaze I", "Blaze II", "Freeze II",
                        "Freeze III", "Bolt I", "Freeze IV", "Bolt II"]
            elif "Gambler" in self.title:
                listOfPowers = [
                        "Equip: Axes", "Luck: Dodge Chance Increased I",
                        "Improvised Attack",
                        "Luck: Dodge Grants Counterattack",
                        "Luck: Reverse Death", "Axes: Range + 1",
                        "Luck: Dodge Chance Increased I",
                        "Luck: Dodge Chance Increased II"]
            elif "Harbinger" in self.title:
                listOfPowers = [
                        "Unarmed Attack: Damage I",
                        "Vocal Attack: Increased Luck I",
                        "Attack: Use Voice", "Luck: Reverse Death",
                        "Defense: Fire I", "Unarmed Attack: Wind",
                        "Defense: Fire II", "Vocal Attack: Increase Luck II"
                        ]
            elif "Hero" in self.title:
                listOfPowers = [
                        "Egress I", "Equip: Long Swords",
                        "Equip: Sacred Swords", "Counterattack",
                        "Swords: Increased Luck I", "Bolt I", "Bolt II",
                        "Swords: Increased Luck II"]
            elif ("Knight" in self.title and "Mage Knight" not in
                    self.title and "Steam Knight" not in self.title):
                listOfPowers = [
                        "Mounted Movement", "Equip: Polearms", "Charge",
                        "Spears: Increased Damage I", "Defense: Lance I",
                        "Defense: Arrow I", "Equip: Holy Polearms",
                        "Defense: Dark Magic I"]
            elif "Mage Knight" in self.title:
                listOfPowers = [
                        "Equip: Polearms", "Mounted Movement",
                        "Defense: Dark Magic I", "Blaze I", "Freeze I",
                        "Bolt I", "Equip: Holy Polearms",
                        "Defense: Dark Magic II"]
            elif "Monk" in self.title:
                listOfPowers = [
                        "Heal I", "Unarmed Attack: Increased Damage I",
                        "Heal II", "Heal III", "Unarmed Attack: Holy",
                        "Heal IV", "Seal I", "Aura I"]
            elif "Orator" in self.title:
                listOfPowers = [
                        "Aura I", "Vocal Attack: Increased Damage I",
                        "Shield I", "Aura II", "Aura III",
                        "Vocal Attack: Increased Damage II", "Aura IV",
                        "Vocal Attack: Increased Range I"]
            elif "Priest" in self.title:
                listOfPowers = [
                        "Heal I", "Detox I", "Heal II",
                        "Healing Magic: Increased Range I", "Heal III",
                        "Healing Magic: Reduced Cost I", "Heal IV",
                        "Healing Magic: Additional Effect: Haste"]
            elif "Prophet" in self.title:
                listOfPowers = [
                        "Heal I", "Heal II", "Slow I",
                        "Healing Magic: Additional Effect: Cleanse",
                        "Heal III", "Aura I", "Heal IV", "Aura II"]
            elif "Samurai" in self.title:
                listOfPowers = [
                        "Equip: Long Swords", "Increased Damage I",
                        "Swords: Added Effect: Fire", "Defense: Melee I",
                        "Swords: Increased Damage II", "Equip: Katanas"
                        "Swords: Increased Damage III",
                        "Swords: Increased Damage IV"]
            elif "Scholar" in self.title:
                listOfPowers = [
                        "Sleep I", "Magic: Cost Reduction I", "Muddle I",
                        "Seal I", "Magic: All Spells +1 Rank",
                        "Magic: Cost Reduction II",
                        "Magic: Effects Always Hit"]
            elif "Sky Battler" in self.title:
                listOfPowers = [
                        "Flying Movement", "Equip: Long Swords",
                        "Counterattack", "Luck: Increased Dodge I",
                        "Swords: Increased Luck II",
                        "Luck: Increased Dodge II", "Movement: Ignore Enemies",
                        "Swords: Increased Luck III"]
            elif "Sky Lord" in self.title:
                listOfPowers = [
                        "Flying Movement", "Equip: Lances",
                        "Charge", "Lances: Increased Damage I",
                        "Luck: Increased Dodge I", "Lances: Increased Luck I"
                        "Luck: Increased Dodge II",
                        "Dodge: Added Effect: Movement I"]
            elif "Soldier" in self.title:
                listOfPowers = [
                        "Unarmed Attack: Increased Damage I", "Ninja Bolt I",
                        "Unarmed Attack: Increased Damage II",
                        "Increased Defense", "Whirlwind Attack",
                        "Attack: Lightning", "Counterattack",
                        "Unarmed Attack: Increased Damage III"]
            elif "Sorceror" in self.title:
                listOfPowers = [
                        "Dao I", "Apollo I", "Dao II", "Apollo II",
                        "Poseidon I", "Atlas I", "Poseidon II", "Atlas II"]
            elif "Squire" in self.title:
                listOfPowers = ["Equip: Swords"]
            elif "Steam Knight" in self.title:
                listOfPowers = [
                        "Equip: Lances",
                        "Defense: Reduced Critical Damage I",
                        "Defense: Weapons I",
                        "Defense: Reduced Critical Damage II",
                        "Lances: Armor Penetration I", "Unhindered Movement",
                        "Lances: Armor Penetration II", "Defense: Weapons II"]
            elif "Student" in self.title:
                listOfPowers = ["Blaze I"]
            elif "Survivor" in self.title:
                listOfPowers = [
                        "Defense: Magic I",
                        "Unarmed Attack: Increased Damage I",
                        "Luck: Increased Dodge I", "Flying Movement",
                        "Defense: Magic II", "Unarmed Attack: Fire",
                        "Defense: Weapons I",
                        "Critical Attack: Bolt III"]
            elif "Thief" in self.title:
                listOfPowers = [
                        "Equip: Daggers", "Counterattack", "Luck: Steal",
                        "Daggers: Range +1", "Stealthy Movement",
                        "Ninja Fire I", "Ninja Bolt I", "Ninja Fire II"]
            elif "Titan" in self.title:
                listOfPowers = [
                        "Defense: Weapons I", "Defense: Fire I",
                        "Unarmed Attack: Increased Damage I",
                        "Defense: Reduced Critical Damage I",
                        "Stunning Attack",
                        "Unarmed Attack: Increased Damage II",
                        "Defense: Fire II", "Critical: Added Effect: Muddle"]
            elif "Trickster" in self.title:
                listOfPowers = [
                        "Teleport I", "Ninja Fire I", "Teleport II",
                        "Ninja Bolt I", "Initiative: First Strike",
                        "Portal I", "Teleport III", "Teleport: Add Turn"]
            elif "Troubadour" in self.title:
                listOfPowers = [
                        "Equip: Arrows", "Vocal Attack: Increased Damage I",
                        "Vocal Attack: Ignore Movement Cost",
                        "Vocal Attack: Add Effect: Sleep",
                        "Luck: Increased Rout I", "Luck: Increased Rout II",
                        "Arrows: Add Effect: Muddle"]
            elif "Valkyrie" in self.title:
                listOfPowers = [
                        "Equip: Lances", "Defense: Melee Attacks I",
                        "Vocal Attack: Increased Damage I",
                        "Luck: Increased Rout I",
                        "Defense: Melee Attacks II", "Vocal Attack: Heal Self",
                        "Vocal Attack: Lost Health Adds Damage",
                        "Flying Movement"]
            elif "Warrior" in self.title:
                listOfPowers = [
                        "Equip: Axes", "Defense: Melee Attacks I",
                        "Axes: Increased Damage I",
                        "Swords: Increased Luck I", "Whirlwind Attack",
                        "Defense: Melee Attacks II", "Leap",
                        "Axes: Increased Damage I"]
            elif "Werewolf" in self.title:
                listOfPowers = [
                        "Unarmed Attack: Increased Damage I",
                        "Unarmed Attack: Increased Damage II", "Leap",
                        "Unarmed Attack: Increased Damage III",
                        "Unarmed Attack: Ice",
                        "Unarmed Attack: Added Effect: Curse",
                        "Unarmed Attack: Increased Damage IV",
                        "Stealthy Movement"]
            for power in listOfPowers:
                if not any([
                        knownPower for knownPower in self.powers
                        if power in knownPower]):
                    nameOfPower = power
                    if nameOfPower == "Mounted Movement" and any([
                            knownPower for knownPower in self.powers
                            if knownPower == "Flying Movement"]):
                        continue
                    elif nameOfPower == "Equip: Polearms":
                        self.powers.extend("Equip: Lances")
                        self.powers.extend("Equip: Spears")
                    if 'Captain' in self.title and not any([
                            knownPower for knownPower in self.powers
                            if 'Command:' in knownPower]):
                        nameOfPower = 'Command: ' + nameOfPower
                    self.powers.append(nameOfPower)
                    print(f"{self.name} learned {nameOfPower}!")
                    return

    def assignRace(self, race=None):
        if not race:
            race = random.choice([
                    "Armadillo", "Birdman", "Centaur", "Dragon", "Dwarf",
                    "Elf", "Foxling", "Golem", "Half-Giant", "Hobbit", "Human",
                    "Insect", "Kyantol", "Magical Creature", "Phoenix",
                    "Robot", "Tortoise", "Wererat", "Wolfling"])
        if race in ("Armadillo", "Tortoise"):
            self.powers.append("Defense: Weapons I")
        elif race in ("Birdman", "Dragon", "Magical Creature", "Phoenix"):
            self.powers.append("Flying Movement")
        elif race == "Centaur":
            self.powers.append("Mounted Movement")
        elif race == "Dwarf":
            self.powers.append("Equip: Axes")
        elif race == "Elf":
            if self.stats["Intelligence"] >= self.stats["Dexterity"]:
                self.powers.append("Equip: Staffs")
            else:
                self.powers.append("Equip: Bows")
        elif race in ("Foxling", "Hobbit", "Kyantol"):
            self.powers.append("Equip: Staffs")
        elif race == "Human":
            if self.stats["Intelligence"] > max(
                    self.stats["Dexterity"], self.stats["Strength"]):
                self.powers.append("Equip: Staffs")
            elif self.stats["Dexterity"] > self.stats["Strength"]:
                self.powers.append("Equip: Brass Guns")
            else:
                self.powers.append("Equip: Swords")
        elif race == "Insect":
            self.powers.append("Equip: Swords")
        elif race in ("Golem", "Half-Giant", "Robot", "Wolfling"):
            self.powers.append("Unarmed Attack: Increased Damage I")
        elif race == "Wererat":
            self.powers.append("Equip: Daggers")
        return race

    def assignTitle(self, chatter):
        oldTitle = self.title
        listOfStats = {}
        for stat in self.stats:
            if stat != "Fame":
                listOfStats[stat] = self.stats[stat]
        primeStat = max(listOfStats.items(), key=itemgetter(1))[0]
        listOfStats = {}
        for stat in self.stats:
            if stat != primeStat:
                listOfStats[stat] = self.stats[stat]
        secondStat = max(listOfStats.items(), key=itemgetter(1))[0]
        if primeStat == "Charisma":
            if secondStat == "Dexterity":
                self.title = "Troubadour"
            elif secondStat == "Faith":
                self.title = "Prophet"
            elif secondStat == "Fame":
                self.title = "Baron"
            elif secondStat == "Intelligence":
                self.title = "Dark Mage"
            elif secondStat == "Luck":
                self.title = "Troubadour"
            elif secondStat == "Speed":
                self.title = "Orator"
            elif secondStat == "Stamina":
                self.title = "Sorceror"
            elif secondStat == "Strength":
                self.title = "Knight"
            elif secondStat == "Voice":
                self.title = "Troubadour"
        elif primeStat == "Dexterity":
            if secondStat == "Charisma":
                self.title = "Thief"
            elif secondStat == "Faith":
                self.title = "Druid"
            elif secondStat == "Fame":
                if self.stats["Luck"] < (5 + self.level / 4):
                    self.title = "Werewolf"
                else:
                    self.title = "Archer"
            elif secondStat == "Intelligence":
                self.title = "Thief"
            elif secondStat == "Luck":
                self.title = "Bard"
            elif secondStat == "Speed":
                self.title = "Archer"
            elif secondStat == "Stamina":
                self.title = "Archer"
            elif secondStat == "Strength":
                if self.stats["Luck"] < (5 + self.level / 4):
                    self.title = "Werewolf"
                elif "Knight" not in self.title:
                    self.title = "Assassin"
            elif secondStat == "Voice":
                self.title = "Druid"
        elif primeStat == "Faith":
            if secondStat == "Charisma":
                self.title = "Priest"
            elif secondStat == "Dexterity":
                self.title = "Druid"
            elif secondStat == "Fame":
                self.title = "Scholar"
            elif secondStat == "Intelligence":
                self.title = "Priest"
            elif secondStat == "Luck":
                self.title = "Priest"
            elif secondStat == "Speed":
                self.title = "Trickster"
            elif secondStat == "Stamina":
                self.title = "Monk"
            elif secondStat == "Strength":
                self.title = "Monk"
            elif secondStat == "Voice":
                self.title = "Prophet"
        elif primeStat == "Intelligence":
            if secondStat == "Charisma":
                self.title = "Fire Mage"
            elif secondStat == "Dexterity":
                self.title = "Trickster"
            elif secondStat == "Faith":
                self.title = "Sorceror"
            elif secondStat == "Fame":
                self.title = "Scholar"
            elif secondStat == "Luck":
                self.title = "Bolt Mage"
            elif secondStat == "Speed":
                self.title = "Trickster"
            elif secondStat == "Stamina":
                self.title = "Frost Mage"
            elif secondStat == "Strength":
                self.title = "Hero"
            elif secondStat == "Voice":
                self.title = "Sorceror"
        elif primeStat == "Luck":
            if secondStat in ("Charisma", "Dexterity"):
                self.title = "Bard"
            elif secondStat == "Faith":
                self.title = "Soldier"
            elif secondStat in ("Fame, Intelligence, Speed, Stamina"):
                self.title = "Gambler"
            elif secondStat == "Strength":
                self.title = "Soldier"
            elif secondStat == "Voice":
                self.title = "Paladin"
        elif primeStat == "Speed":
            if secondStat == "Charisma":
                if ("Flying Movement" in
                        self.powers or self.stats["Speed"] > 25):
                    self.title = "Sky Battler"
                else:
                    self.title = "Duelist"
            elif secondStat == "Dexterity":
                if ("Flying Movement" in
                        self.powers or self.stats["Speed"] > 25):
                    self.title = "Sky Battler"
                else:
                    self.title = "Brass Gunner"
            elif secondStat == "Faith":
                self.title = "Harbinger"
            elif secondStat == "Fame":
                if ("Flying Movement" in
                        self.powers or self.stats["Speed"] > 25):
                    self.title = "Sky Battler"
                else:
                    self.title = "Duelist"
            elif secondStat == "Intelligence":
                if ("Flying Movement" in
                        self.powers or self.stats["Speed"] > 25):
                    self.title = "Sky Lord"
                else:
                    self.title = "Trickster"
            elif secondStat == "Luck":
                if ("Flying Movement" in
                        self.powers or self.stats["Speed"] > 25):
                    self.title = "Sky Battler"
                else:
                    self.title = "Duelist"
            elif secondStat == "Stamina":
                if ("Flying Movement" in
                        self.powers or self.stats["Speed"] > 25):
                    self.title = "Sky Lord"
                else:
                    self.title = "Knight"
            elif secondStat == "Strength":
                if (self.race in ("Dragon", "Tortoise") or self.level > 20):
                    self.title = "Survivor"
                    if self.race not in ("Dragon", "Phoenix", "Tortoise") or (
                            self.race == "Tortoise" and "Flying Movement"
                            in self.powers):
                        self.race = "Dragon"
                        print(f"{self.name} became a Dragon!")
                else:
                    self.title = "Knight"
            elif secondStat == "Voice":
                self.title = "Harbinger"
        elif primeStat == "Stamina":
            if secondStat == "Charisma":
                self.title = "Samurai"
            elif secondStat == "Dexterity":
                self.title = "Brass Gunner"
            elif secondStat == "Faith":
                self.title = "Samurai"
            elif secondStat == "Fame":
                self.title = "Valkyrie"
            elif secondStat == "Intelligence":
                if self.stats["Fame"] < (5 + self.level / 4):
                    self.title = "Steam Knight"
                else:
                    self.title = "Blood Mage"
            elif secondStat == "Luck":
                if self.stats["Speed"] < (5 + self.level / 4):
                    self.title = "Titan"
                else:
                    self.title = "Duelist"
            elif secondStat == "Speed":
                if self.stats["Luck"] < (5 + self.level / 4):
                    self.title = "Werewolf"
                else:
                    self.title = "Duelist"
            elif secondStat == "Strength":
                if self.stats["Luck"] < (5 + self.level / 4):
                    self.title = "Berserker"
                self.title = "Warrior"
            elif secondStat == "Voice":
                self.title = "Valkyrie"
        elif primeStat == "Strength":
            if secondStat == "Charisma":
                if self.stats["Intelligence"] > max(
                        self.stats["Faith"], self.stats["Dexterity"]) \
                        and self.level > 4:
                    self.title = "Mage Knight"
                else:
                    self.title = "Knight"
            elif secondStat == "Dexterity":
                if "Knight" not in self.title:
                    self.title = "Assassin"
                else:
                    self.title = "Duelist"
            elif secondStat == "Faith":
                self.title = "Monk"
            elif secondStat == "Fame":
                self.title = "Baron"
            elif secondStat == "Intelligence":
                self.title = "Hero"
            elif secondStat == "Luck":
                self.title = "Hero"
            elif secondStat == "Speed":
                if self.stats["Intelligence"] > max(
                        self.stats["Faith"], self.stats["Dexterity"]) \
                        and self.level > 4:
                    self.title = "Mage Knight"
                else:
                    self.title = "Knight"
            elif secondStat == "Stamina":
                if self.stats["Luck"] < (5 + self.level / 4):
                    self.title = "Berserker"
                self.title = "Warrior"
            elif secondStat == "Voice":
                self.title = "Paladin"
        elif primeStat == "Voice":
            if secondStat in ("Stamina", "Strength", "Speed") and (
                    self.race in ("Dragon", "Tortoise") or self.level > 20):
                self.title = "Survivor"
                if self.race not in ("Dragon", "Phoenix", "Tortoise") or (
                        self.race == "Tortoise" and "Flying Movement"
                        in self.powers):
                    self.race = "Dragon"
                    print(f"{self.name} became a Dragon!")
            elif secondStat in ("Charisma", "Dexterity"):
                self.title = "Chorister"
            elif secondStat == "Faith":
                self.title = "Prophet"
            elif secondStat in ("Fame", "Intelligence"):
                self.title = "Orator"
            elif secondStat == "Luck":
                self.title = "Paladin"
            elif secondStat == "Speed":
                self.title = "Chorister"
            elif secondStat == "Stamina":
                self.title = "Valkyrie"
            elif secondStat == "Strength":
                self.title = "Paladin"
        if self.title == "newbie":
            print(
                    f"Newbie found. Let Neirai the Forgiven know."
                    f"Stats are {self.stats}")
            if self.stats["Intelligence"] < self.stats["Strength"]:
                self.title = "Squire"
            else:
                self.title = "Student"
        if self.stats["Fame"] >= 25 and "Captain" not in self.title:
            self.title = self.title + " Captain"
        if self.stats["Speed"] > 25 <= 40 and (
                "Mounted" not in self.title and "Knight" not in
                self.title and "Sky " not in
                self.title and "Flying Movement" not in self.powers):
            self.title = "Mounted " + self.title
        elif (self.stats["Speed"] > 40 or "Flying Movement" in
                self.powers) and "Sky " not in self.title:
            self.title = "Sky " + self.title
        if self.title != oldTitle:
            if chatter:
                print(f"{self.name} became a {self.title}!")
            self.career += f" --> {self.title} ({self.level})"

    def canEquip(self, equipment):
        equipPower = f"Equip: {equipment.type}"
        return equipPower in self.powers

    def initializeRandomStats(
                self, bestStat=None, secondBestStat=None, dumpStat=None):
        statsToAssign = [
                "Strength", "Dexterity", "Intelligence", "Faith", "Charisma",
                "Luck", "Speed", "Stamina", "Voice", "Fame"]
        growth = {}
        advance = True
        growthLevel = 5
        if bestStat:
            growth[bestStat] = 5
            statsToAssign.remove(bestStat)
            advance = False
        if secondBestStat and bestStat:
            growth[secondBestStat] = 5
            statsToAssign.remove(secondBestStat)
            advance = True
            growthLevel = 6
        if dumpStat:
            growth[dumpStat] = 9
            statsToAssign.remove(dumpStat)
        statsCount = len(statsToAssign)
        for i in range(statsCount):
            stat = random.choice(statsToAssign)
            growth[stat] = growthLevel
            statsToAssign.remove(stat)
            advance = not advance
            if advance:
                growthLevel += 1
        return growth

    def levelUp(self, chatter):
        if chatter:
            print('{} hit level {}!'.format(self.name, self.level + 1))
        preLevelStatIncreaseCount = self.statIncreaseCount
        if self.statIncreaseCount != 0:
            bonus = self.level * 4 / self.statIncreaseCount
        else:
            bonus = 1
        if bonus <= 0.5:
            bonus = 0.55
        elif bonus > 2:
            bonus = 2

        for statName, statValue in self.growth.items():
            roll = random.randint(1, 10)
            result = math.floor(bonus * roll)
            if result >= statValue:
                statIncrease = math.ceil(result / 10)
                self.stats[statName] += statIncrease
                if chatter:
                    print("    {} became {}{}".format(
                            statName, self.stats[statName],
                            '!' * statIncrease))
                self.statIncreaseCount += statIncrease
        while preLevelStatIncreaseCount == self.statIncreaseCount:
            for statName, statValue in self.growth.items():
                result = math.floor(bonus * random.randint(1, 10))
                if result >= statValue:
                    statIncrease = math.ceil(result / 10)
                    self.stats[statName] += statIncrease
                    if chatter:
                        print("    {} became {}{}".format(
                                statName, self.stats[statName],
                                '!' * statIncrease))
                    self.statIncreaseCount += statIncrease
                    break
        self.level += 1
        if chatter:
            print("")
        if self.level % 5 == 0:
            if chatter:
                print(f"It's time for {self.name}'s class review.")
            self.assignTitle(chatter)
            self.assignPower()
            self.updateGrowth()
            if chatter:
                for statName, statValue in self.stats.items():
                    print("    {} of {}".format(statName, statValue))
                input()

    def maxHP(self):
        return ((self.stats["Stamina"] * 2) + self.level)

    def updateGrowth(self):
        sortedGrowth = sorted(self.growth.items(), key=itemgetter(1))
        growthLevel = 5
        advance = True
        for statGrowthKey, statGrowthValue in sortedGrowth:
            self.growth[statGrowthKey] = growthLevel
            advance = not advance
            if advance:
                growthLevel += 1


class equipment(object):

    def __init__(
            self, equipType, name, price, minRange=0, maxRange=0, damage=3,
            fp=0, mp=0, powers=[]):
        self.type = equipType
        self.name = name
        self.price = price
        self.minRange = minRange
        self.maxRange = maxRange
        self.damage = damage
        self.equippedBy = None
        self.fp = fp
        self.mp = mp
        self.powers = powers

    def canEquip(self, unit):
        equipPower = f"Equip: {self.type}"
        return equipPower in unit.powers


party = []
stop = input("Type stop if you want to skip this.")
if not stop == "stop":
    module = input("Type SF if you want me to run the SF module.")
    chatty = input(
            "Type chatty if you want to be barraged with leveling info.")
    if chatty == 'chatty':
        chatter = True
        stopEveryLevel = input(
                "Type slow if you want to stop for every level.")
    else:
        chatter = False
        stopEveryLevel = "fast"
    if module == 'SF':
        recruit = playerCharacter("Max", "Human", "Hero", chatter, 0)
        party.append(recruit)
        recruit = playerCharacter("Lowe", "Hobbit", "Priest", chatter, 0)
        party.append(recruit)
        recruit = playerCharacter("Tao", "Elf", "Fire Mage", chatter, 0)
        party.append(recruit)
        recruit = playerCharacter("Luke", "Dwarf", "Warrior", chatter, 0)
        party.append(recruit)
        recruit = playerCharacter("Ken", "Centaur", "Knight", chatter, 0)
        party.append(recruit)
        recruit = playerCharacter("Hans", "Elf", "Archer", chatter, 0)
        party.append(recruit)
        recruit = playerCharacter("Gong", "Half-Giant", "Monk", chatter, 1)
        party.append(recruit)
        recruit = playerCharacter("Mae", "Centaur", "Knight", chatter, 2)
        party.append(recruit)
        recruit = playerCharacter("Gort", "Dwarf", "Warrior", chatter, 2)
        party.append(recruit)
        recruit = playerCharacter("Khris", "Kyantol", "Priest", chatter, 3)
        party.append(recruit)
        recruit = playerCharacter("Anri", "Human", "Frost Mage", chatter, 5)
        party.append(recruit)
        recruit = playerCharacter("Arthur", "Centaur", "Knight", chatter, 6)
        party.append(recruit)
        recruit = playerCharacter(
                "Balbaroy", "Birdman", "Sky Battler", chatter, 8)
        party.append(recruit)
        recruit = playerCharacter("Amon", "Birdman", "Sky Battler", chatter, 8)
        party.append(recruit)
        recruit = playerCharacter("Diane", "Elf", "Archer", chatter, 8)
        party.append(recruit)
        recruit = playerCharacter("Zylo", "Wolfling", "Werewolf", chatter, 9)
        party.append(recruit)
        recruit = playerCharacter("Pelle", "Centaur", "Knight", chatter, 11)
        party.append(recruit)
        recruit = playerCharacter("Kokichi", "Human", "Sky Lord", chatter, 11)
        party.append(recruit)
        recruit = playerCharacter("Vankar", "Centaur", "Knight", chatter, 11)
        party.append(recruit)
        recruit = playerCharacter(
                "Domingo", "Magical Creature", "Frost Mage", chatter, 12)
        party.append(recruit)
        recruit = playerCharacter(
                "Guntz", "Armadillo", "Steam Knight", chatter, 12)
        party.append(recruit)
        recruit = playerCharacter("Earnest", "Centaur", "Knight", chatter, 13)
        party.append(recruit)
        recruit = playerCharacter("Lyle", "Centaur", "Archer", chatter, 17)
        party.append(recruit)
        recruit = playerCharacter("Bleu", "Dragon", "Survivor", chatter, 18)
        party.append(recruit)
        recruit = playerCharacter("Musashi", "Human", "Samurai", chatter, 21)
        party.append(recruit)
        recruit = playerCharacter("Alef", "Foxling", "Bolt Mage", chatter, 23)
        party.append(recruit)
        recruit = playerCharacter("Torasu", "Hobbit", "Priest", chatter, 23)
        party.append(recruit)
        recruit = playerCharacter("Adam", "Robot", "Soldier", chatter, 23)
        party.append(recruit)
        recruit = playerCharacter("Hanzou", "Human", "Assassin", chatter, 25)
        party.append(recruit)
    elif module == 'SF2':
        recruit = playerCharacter("Bowie", "Human", "Hero", chatter)
        party.append(recruit)
        recruit = playerCharacter("Sarah", "Elf", "Priest", chatter)
        party.append(recruit)
        recruit = playerCharacter("Chester", "Centaur", "Knight", chatter)
        party.append(recruit)
        recruit = playerCharacter("Jaha", "Dwarf", "Warrior", chatter)
        party.append(recruit)
        recruit = playerCharacter("Kazin", "Elf", "Bolt Mage", chatter)
        party.append(recruit)
        recruit = playerCharacter("Slade", "Wererat", "Thief", chatter)
        party.append(recruit)
        recruit = playerCharacter("Kiwi", "Tortoise", "Survivor", chatter)
        party.append(recruit)
        recruit = playerCharacter("Peter", "Phoenix", "Harbinger", chatter)
        party.append(recruit)
        recruit = playerCharacter("May", "Centaur", "Archer", chatter)
        party.append(recruit)
        recruit = playerCharacter("Gerhalt", "Wolfling", "Werewolf", chatter)
        party.append(recruit)
        recruit = playerCharacter("Luke", "Birdman", "Sky Battler", chatter)
        party.append(recruit)
        recruit = playerCharacter("Rohde", "Human", "Brass Gunner", chatter)
        party.append(recruit)
        recruit = playerCharacter("Rick", "Centaur", "Knight", chatter)
        party.append(recruit)
        recruit = playerCharacter("Elric", "Elf", "Archer", chatter)
        party.append(recruit)
        recruit = playerCharacter("Eric", "Centaur", "Knight", chatter)
        party.append(recruit)
        recruit = playerCharacter("Karna", "Elf", "Priest", chatter)
        party.append(recruit)
        recruit = playerCharacter("Randolf", "Dwarf", "Warrior", chatter)
        party.append(recruit)
        recruit = playerCharacter("Tyrin", "Elf", "Frost Mage", chatter)
        party.append(recruit)
        recruit = playerCharacter("Janet", "Elf", "Archer", chatter)
        party.append(recruit)
        recruit = playerCharacter("Higins", "Centaur", "Knight", chatter)
        party.append(recruit)
        recruit = playerCharacter("Taya", "Elf", "Sorceror", chatter)
        party.append(recruit)
        recruit = playerCharacter("Skreech", "Birdman", "Sky Battler", chatter)
        party.append(recruit)
        recruit = playerCharacter("Frayja", "Human", "Priest", chatter)
        party.append(recruit)
        recruit = playerCharacter("Jaro", "Centaur", "Knight", chatter)
        party.append(recruit)
        recruit = playerCharacter("Gyan", "Dwarf", "Warrior", chatter)
        party.append(recruit)
        recruit = playerCharacter("Sheela", "Human", "Monk", chatter)
        party.append(recruit)
        recruit = playerCharacter("Zynk", "Robot", "Soldier", chatter)
        party.append(recruit)
        recruit = playerCharacter("Chaz", "Human", "Bolt Mage", chatter)
        party.append(recruit)
        recruit = playerCharacter("Claude", "Golem", "Titan", chatter)
        party.append(recruit)
        recruit = playerCharacter("Lemon", "Human", "Baron", chatter)
        party.append(recruit)
    else:
        partySize = int(input("How many characters should I create? "))
        for i in range(partySize):
            recruit = playerCharacter(None, None, chatter)
            party.append(recruit)
    print("")
    sim = False
    if module:
        mode = input("Type Yes if you want to simulate a game.")
        if mode == "Yes":
            sim = True
    if sim:
        if module == "SF":
            gameLevel = 0
            modifier = 40 / 30
            for i in range(30):
                gameLevel = math.floor((i + 1) * modifier)
                print(f"The party faces Battle {i + 1}")
                for pc in party:
                    if pc.battleNum < i + 1:
                        while pc.level < gameLevel:
                            pc.levelUp(chatter)
                        if i == pc.battleNum:
                            print(
                                    f"{pc.name} is a level {pc.level} "
                                    f"{pc.race} {pc.title} with {pc.powers}.")
                        else:
                            print(
                                    f"{pc.name} is a level {pc.level} "
                                    f"{pc.race} {pc.title} with "
                                    f"{pc.powers[len(pc.powers) - 1:]}.")
                stop = input()
        # elif module == "SF2":
    else:
        levelUpNum = int(input("How many levels should they get? "))
        for i in range(levelUpNum):
            for pc in party:
                pc.levelUp(chatter)
                if stopEveryLevel == "slow":
                    stop = input()
    for pc in party:
        print(f"{pc.name} is a level {pc.level} {pc.race} {pc.title}.")
        print(pc.career)
        if pc.powers:
            print("    Powers: " + " -> ".join(pc.powers))
else:
    chatter = False
