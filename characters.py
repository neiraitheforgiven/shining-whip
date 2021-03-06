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
        self.shortName = name[:9]
        self.allowedMovement = []
        self.allowedAttacks = []
        self.allowedEquipment = []
        self.allowedSpells = {}
        self.initiativePoints = 0
        self.actedThisRound = False
        self.powers = []
        self.moveProfile = moveProfile
        self.attackProfile = attackProfile
        self.equipment = None
        self.status = []
        self.boss = False
        self.extraPowerSlot = []
        self.extraPowerSlot2 = []
        if name == "Body Puppet":
            self.level = 7
            stats = {
                    "Strength": 10, "Stamina": 7, "Dexterity": 7, "Speed": 5,
                    "Intelligence": 15}
            self.setStats(8, **stats)
            self.shortName = "Puppet"
            self.moveProfile = moveProfile or "Random"
            self.attackProfile = attackProfile or "Spellcaster"
            self.powers.append("Poisonous Attack")
            self.powers.append("Freeze I")
            self.powers.append("Unarmed Attack: Increased Damage I")
            self.powers.append("Unarmed Attack: Increased Damage II")
            self.powers.append("Luck: Critical Drain I")
            self.powers.append("Luck: Counterattack")
        elif name == "Crazed Dwarf":
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
        elif name == "Deranged Clown":
            self.level = 7
            stats = {"Stamina": 8, "Strength": 11, "Dexterity": 11, "Luck": 10}
            self.setStats(10, **stats)
            self.moveProfile = moveProfile or "Defensive"
            self.attackProfile = attackProfile or "Random"
            self.equipment = equipment("Daggers", "Knife", 500, 0, 0, 8, 0, 0)
            self.shortName = "Clown"
        elif name == "Giant Bat":
            self.level = 5
            stats = {
                    "Voice": 11, "Stamina": 7, "Speed": 7, "Strength": 9,
                    "Dexterity": 6}
            self.setStats(7, **stats)
            self.attackProfile = attackProfile or "Singer"
            self.moveProfile = moveProfile or "Aggressive-Singer"
            self.powers.append("Flying Movement")
            self.powers.append("Sonorous Voice")
            self.powers.append("Vocal Attack: Increased Resonance I")
            self.powers.append("Vocal Attack: Ignore Movement")
            self.shortName = "Bat"
        elif name == "Goblin":
            self.level = 1
            stats = {"Dexterity": 6, "Stamina": 5, "Speed": 5}
            self.setStats(5, **stats)
            self.moveProfile = moveProfile or "Aggressive"
            self.attackProfile = attackProfile or "Random"
            self.equipment = equipment(
                    "Swords", "Goblin Sword", 50, 0, 0, 3, 0, 0)
        elif name == "Mannequin":
            self.level = 6
            stats = {"Strength": 14, "Stamina": 8, "Speed": 5}
            self.setStats(7, **stats)
            self.moveProfile = moveProfile or "SlowAdvance"
            self.attackProfile = attackProfile or "Random"
            self.powers.append("Poisonous Attack")
            self.powers.append("Unarmed Attack: Increased Damage I")
            self.powers.append("Unarmed Attack: Increased Damage II")
        elif name == "Marionette":
            self.level = 10
            self.boss = True
            stats = {
                    "Stamina": 17, "Intelligence": 25, "Strength": 13,
                    "Dexterity": 13, "Speed": 6}
            self.setStats(12, **stats)
            self.moveProfile = moveProfile or "Defensive"
            self.attackProfile = attackProfile or "Spellcaster"
            self.powers.append("Freeze III")
            self.powers.append("Magic: Cost Reduction I")
            self.shortName = "Marion"
        elif name == "Skeleton Warrior":
            self.level = 9
            stats = {"Strength": 16, "Stamina": 10, "Speed": 7}
            self.setStats(9, **stats)
            self.shortName = "Skull W."
            self.moveProfile = moveProfile or "Defensive"
            self.attackProfile = attackProfile or "ChallengeAccepting"
            self.equipment = equipment(
                    "Swords", "Middle Sword", 250, 0, 0, 5, 0, 0)
            self.powers.append("Command: Luck: Counterattack")
            self.powers.append("Defense: Fire Vulnerability")
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
            self.powers.append("Mounted Movement")
            self.shortName = "Knight"
        elif name == "Zombie":
            self.level = 5
            stats = {
                    "Strength": 13, "Dexterity": 7, "Speed": 5, "Stamina": 10,
                    "Luck": 12}
            self.setStats(6, **stats)
            self.moveProfile = moveProfile or "SlowAdvance"
            self.attackProfile = attackProfile or "Random"
            self.powers.append("Unarmed Attack: Increased Damage I")
            self.powers.append("Poisonous Attack")
            self.powers.append("Luck: Counterattack")
            self.powers.append("Defense: Fire Vulnerability")
        else:
            print(
                    "Battle Setup Error! Attempted to create monster not in "
                    "list!")

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
        self.initiativePoints = 0
        self.actedThisRound = False
        self.hasEquipped = False
        self.status = []
        self.trophies = []
        if playerClass:
            if playerClass == "Assassin":
                self.growth = self.initializeRandomStats(
                        "Strength", "Dexterity")
            elif playerClass == "Archer":
                self.growth = self.initializeRandomStats(
                        "Dexterity", "Speed", "Strength")
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
            elif playerClass == "Hero":
                self.growth = self.initializeRandomStats(
                        "Strength", "Intelligence")
            elif playerClass == "Knight":
                self.growth = self.initializeRandomStats("Strength", "Speed")
            elif playerClass == "Monk":
                self.growth = self.initializeRandomStats("Faith", "Strength")
            elif playerClass == "Priest":
                self.growth = self.initializeRandomStats("Faith", "Charisma")
            elif playerClass == "Samurai":
                self.growth = self.initializeRandomStats("Stamina", "Faith")
            elif playerClass == "Sky Battler":
                self.growth = self.initializeRandomStats("Speed", "Dexterity")
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
            elif playerClass == "Ninja":
                self.growth = self.initializeRandomStats(
                        "Dexterity", "Intelligence")
            elif playerClass == "Survivor":
                self.growth = self.initializeRandomStats("Voice", "Stamina")
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
        if chatter:
            print(f"{self.name} the {self.race} {self.title} created.")
        self.assignPower(chatter)
        self.career = f"    Career Path: {self.title}"
        if chatter:
            for statName, statValue in self.stats.items():
                print("    {} of {}".format(statName, statValue))
            print("")

    def assignPower(self, chatter=False):
        if "Mounted" in self.title and "Mounted Movement" not in self.powers:
            self.powers.append("Mounted Movement")
            return
        elif "Sky" in self.title and "Flying Movement" not in self.powers:
            self.powers.append("Flying Movement")
            return
        else:
            listOfPowers = []
            if "Alchemist" in self.title:
                listOfPowers = [
                        "Random Additional Spell I", "Convert Faith and Magic",
                        "Heal I", "Defense: Being Routed Deals Damage",
                        "Attack: Chance of Confusion",
                        "Defense: Being Routed Adds Silence",
                        "Random Additional Spell II", "Conduit I"]
            elif "Archer" in self.title:
                listOfPowers = [
                        "Equip: Arrows", "Quick Shot", "Aimed Shot",
                        "Arrows: Increased Damage I",
                        "Increased Terrain Advantage I",
                        "Arrows: Add Effect: Poison",
                        "Luck: Enable Triple Attack",
                        "Arrows: Range + 1"]
            elif "Assassin" in self.title:
                listOfPowers = [
                        "Stealthy Movement", "Paralyze I",
                        "Attack: Bonus Move", "Death I", "Shield I",
                        "Death II", "Equip: Sacred Swords",
                        "Luck: Critical Hit Adds Silence"]
            elif "Bard" in self.title:
                listOfPowers = [
                        "Equip: Daggers", "Heal I", "Equip: Arrows",
                        "Luck: Counterattack",
                        "Luck: Increased Dodge Chance I",
                        "Command: Health Regeneration I",
                        "Cast Spell: Add Resonance",
                        "Command: Increased Luck I"]
            elif "Baron" in self.title:
                listOfPowers = [
                        "Equip: Swords", "Command: Luck: Counterattack",
                        "Luck: Reverse Death",
                        "Command: Allies Increase Defense",
                        "Luck: Critical Drain I",
                        "Swords: Increased Damage I",
                        "Death II", "Luck: Critical Drain II"]
            elif "Berserker" in self.title:
                listOfPowers = [
                        "Unarmed Attack: Increased Damage I",
                        "Unhindered Movement",
                        "Unarmed Attack: Rout Deals Damage", "Equip: Axes",
                        "Axes: Lost Health Adds Damage I",
                        "Axes: Bonus Unarmed Attack",
                        "Axes: Increased Critical Chance I",
                        "Axes: Increased Critical Chance II"]
            elif "Blood Mage" in self.title:
                listOfPowers = [
                        "Drain I", "Poison I", "Drain II", "Equip: Daggers",
                        "Muddle I", "Death I",
                        "Daggers: Cast Spell Adds Bonus Attack", "Poison II"]
            elif "Bolt Mage" in self.title:
                listOfPowers = [
                        "Bolt I", "Blaze I", "Freeze I",
                        "Teleport I", "Bolt II", "Bolt III",
                        "Death I", "Bolt IV"]
            elif "Brass Gunner" in self.title:
                listOfPowers = [
                        "Equip: Brass Guns", "Unhindered Movement",
                        "Brass Guns: Critical Damage I",
                        "Defense: Physical I",
                        "Mounted Movement",
                        "Brass Guns: Critical Damage II",
                        "Defense: Physical II",
                        "Brass Guns: Minumum Range - 1"]
            elif "Cantor" in self.title:
                listOfPowers = [
                        "Mounted Movement", "Luck: Increased Rout I",
                        "Vocal Attack: Remove Enemy Resonance",
                        "Vocal Attack: Increased Damage I",
                        "Luck: Increased Rout II",
                        "Defense: Dark Magic I",
                        "Vocal Attack: Increased Damage II"
                        "Rout: Add Effect: Paralyze"]
            elif "Chorister" in self.title:
                listOfPowers = [
                        "Vocal Attack: Sustain Effect", "Heal I",
                        "Blast I", "Command: Vocal Attack: Increased Damage I",
                        "Blast II",
                        "Command: Vocal Attack: Increased Damage II",
                        "Vocal Attack: Increased Damage III", "Blast III"]
            elif "Dark Mage" in self.title:
                listOfPowers = [
                        "Blaze I", "Freeze I", "Defense: Magic", "Blaze II",
                        "Death I", "Freeze II", "Death II", "Bolt I"]
            elif "Druid" in self.title:
                listOfPowers = [
                        "Stealthy Movement", "Defense: Increased Resistance I",
                        "Detox I", "Blast I", "Conduit I", "Blast II",
                        "Defense: Increased Resistance II", "Blast III"]
            elif "Duelist" in self.title:
                listOfPowers = [
                        "Equip: Swords", "Luck: Counterattack",
                        "Defense: Swords I", "Swords: Increased Luck I",
                        "Swords: Increased Luck II",
                        "Luck: Dodge Grants Counterattack",
                        "Swords: Increased Luck III",
                        "Luck: Counterattack First"]
            elif "Fire Mage" in self.title:
                listOfPowers = [
                        "Blaze I", "Magic: Cost Reduction I", "Paralyze I",
                        "Blaze II", "Defense: Counterspell I", "Blaze III",
                        "Magic: Increased Damage I", "Blaze IV"]
            elif "Frost Mage" in self.title:
                listOfPowers = [
                        "Freeze I", "Blaze I", "Freeze II", "Blaze II",
                        "Freeze III", "Bolt I", "Freeze IV", "Bolt II"]
            elif "Gambler" in self.title:
                listOfPowers = [
                        "Equip: Axes", "Luck: Dodge Chance Increased I",
                        "Increased Luck When Outnumbered I",
                        "Luck: Dodge Grants Counterattack",
                        "Luck: Reverse Death", "Axes: Range + 1",
                        "Increased Luck When Outnumbered II",
                        "Luck: Dodge Chance Increased II"]
            elif "Harbinger" in self.title:
                listOfPowers = [
                        "Unarmed Attack: Damage I",
                        "Vocal Attack: Increased Luck I",
                        "Teleport I", "Luck: Reverse Death",
                        "Defense: Fire I", "Unarmed Attack: Gain Wind Element",
                        "Defense: Fire II", "Vocal Attack: Increased Luck II"
                        ]
            elif "Hero" in self.title:
                listOfPowers = [
                        "Egress I", "Swords: Increased Luck I",
                        "Equip: Sacred Swords", "Luck: Counterattack",
                        "Bolt I", "Magic: Cost Reduction I", "Bolt II",
                        "Swords: Increased Luck II"]
            elif ("Knight" in self.title and "Mage Knight" not in
                    self.title and "Steam Knight" not in self.title):
                listOfPowers = [
                        "Mounted Movement", "Equip: Polearms",
                        "Lances: Movement Increases Strength Damage I",
                        "Spears: Increased Damage I", "Defense: Lance I",
                        "Defense: Arrow I",
                        "Faith: Add Damage on Unholy Ground",
                        "Defense: Dark Magic I"]
            elif "Mage Knight" in self.title:
                listOfPowers = [
                        "Equip: Polearms", "Mounted Movement", "Blaze I",
                        "Defense: Dark Magic I", "Freeze I", "Bolt I",
                        "Faith: Add Damage on Unholy Ground",
                        "Defense: Dark Magic II"]
            elif "Monk" in self.title:
                listOfPowers = [
                        "Heal I", "Unarmed Attack: Increased Damage I",
                        "Heal II", "Heal III",
                        "Faith: Add Damage on Holy Ground", "Heal IV",
                        "Silence I", "Aura I"]
            elif "Ninja" in self.title:
                listOfPowers = [
                        "Equip: Daggers", "Luck: Counterattack", "Luck: Steal",
                        "Daggers: Range +1", "Stealthy Movement",
                        "Ninja Fire I", "Ninja Bolt I", "Ninja Fire II"]
            elif "Orator" in self.title:
                listOfPowers = [
                        "Aura I", "Vocal Attack: Increased Resonance I",
                        "Shield I", "Aura II", "Aura III",
                        "Vocal Attack: Increased Resonance II", "Aura IV",
                        "Vocal Attack: Sustain Effect"]
            elif "Priest" in self.title:
                listOfPowers = [
                        "Heal I", "Detox I", "Heal II",
                        "Healing Magic: Increased Range I", "Heal III",
                        "Healing Magic: Reduced Cost I", "Heal IV",
                        "Healing Magic: Additional Effect: Bonus Turn"]
            elif "Prophet" in self.title:
                listOfPowers = [
                        "Heal I", "Heal II", "Slow I", "Heal III", "Aura I",
                        "Healing Magic: Additional Effect: Cleanse", "Heal IV",
                        "Aura II"]
            elif "Samurai" in self.title:
                listOfPowers = [
                        "Equip: Swords", "Increased Damage I",
                        "Swords: Fire Element", "Defense: Melee I",
                        "Swords: Increased Damage II", "Equip: Katanas"
                        "Swords: Increased Damage III",
                        "Swords: Increased Damage IV"]
            elif "Scholar" in self.title:
                listOfPowers = [
                        "Paralyze I", "Magic: Cost Reduction I", "Muddle I",
                        "Silence I", "Magic: All Spells +1 Rank",
                        "Magic: Cost Reduction II",
                        "Magic: Effects Always Hit"]
            elif "Sky Battler" in self.title:
                listOfPowers = [
                        "Flying Movement", "Equip: Swords",
                        "Luck: Counterattack", "Luck: Increased Dodge I",
                        "Swords: Increased Luck II",
                        "Luck: Increased Dodge II", "Movement: Ignore Enemies",
                        "Swords: Increased Luck III"]
            elif "Sky Lord" in self.title:
                listOfPowers = [
                        "Flying Movement", "Equip: Lances",
                        "Lances: Movement Increases Strength Damage I",
                        "Lances: Increased Damage I",
                        "Luck: Increased Dodge I", "Lances: Increased Luck I"
                        "Luck: Increased Dodge II",
                        "Dodge: Add Movement I"]
            elif "Soldier" in self.title:
                listOfPowers = [
                        "Unarmed Attack: Increased Damage I",
                        "Equip: Brass Guns",
                        "Unarmed Attack: Increased Damage II",
                        "Defense: Physical I", "Whirlwind Attack",
                        "Attack: Lightning Element", "Luck: Counterattack",
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
                        "Lances: Increased Critical Chance I",
                        "Unhindered Movement",
                        "Lances: Increased Critical Chance II",
                        "Defense: Weapons II"]
            elif "Student" in self.title:
                listOfPowers = ["Blaze I"]
            elif "Survivor" in self.title:
                listOfPowers = [
                        "Defense: Magic I",
                        "Unarmed Attack: Increased Damage I",
                        "Luck: Increased Dodge I", "Flying Movement",
                        "Defense: Magic II", "Unarmed Attack: Fire Element",
                        "Defense: Weapons I",
                        "Critical Attack: Bolt III"]  # ??? Really?
            elif "Titan" in self.title:
                listOfPowers = [
                        "Defense: Weapons I", "Defense: Fire I",
                        "Unarmed Attack: Increased Damage I",
                        "Defense: Reduced Critical Damage I",
                        "Unarmed Attack: Increased Damage II",
                        "Attack: Remove Target From Initiative",
                        "Defense: Fire II", "Critical: Added Effect: Muddle"]
            elif "Trickster" in self.title:
                listOfPowers = [
                        "Teleport I", "Ninja Fire I", "Teleport II",
                        "Ninja Bolt I", "Initiative: First Move",
                        "Portal I", "Teleport III", "Teleport: Add Turn"]
            elif "Troubadour" in self.title:
                listOfPowers = [
                        "Equip: Arrows", "Vocal Attack: Increased Damage I",
                        "Vocal Attack: Ignore Movement", "Sonorous Voice",
                        "Luck: Counterattack",
                        "Vocal Attack: Increased Damage II",
                        "Arrows: Support Counterattack",
                        "Arrows: Add Effect: Muddle"]
            elif "Valkyrie" in self.title:
                listOfPowers = [
                        "Equip: Lances", "Defense: Melee Attacks I",
                        "Vocal Attack: Lost Health Adds Damage II",
                        "Luck: Increased Rout I",
                        "Defense: Melee Attacks II", "Vocal Attack: Heal Self",
                        "Vocal Attack: Lost Health Adds Damage II",
                        "Flying Movement"]
            elif "Warrior" in self.title:
                listOfPowers = [
                        "Equip: Axes", "Defense: Melee Attacks I",
                        "Axes: Increased Damage I",
                        "Swords: Increased Luck I", "Whirlwind Attack",
                        "Defense: Melee Attacks II", "Rout: Follow-up Attack",
                        "Axes: Increased Damage I"]
            elif "Werewolf" in self.title:
                listOfPowers = [
                        "Unarmed Attack: Increased Damage I",
                        "Unarmed Attack: Increased Damage II",
                        "Rout: Follow-up Attack",
                        "Unarmed Attack: Increased Damage III",
                        "Unarmed Attack: Ice Element",
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
                        self.powers.extend(["Equip: Lances"])
                        self.powers.extend(["Equip: Spears"])
                    if 'Captain' in self.title and not any([
                            knownPower for knownPower in self.powers
                            if 'Command:' in knownPower]):
                        if 'Command:' not in nameOfPower:
                            nameOfPower = 'Command: ' + nameOfPower
                    self.powers.append(nameOfPower)
                    if chatter:
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
                self.powers.append("Equip: Arrows")
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
                self.title = "Bard"
            elif secondStat == "Faith":
                self.title = "Prophet"
            elif secondStat == "Fame":
                self.title = "Baron"
            elif secondStat == "Intelligence":
                self.title = "Dark Mage"
            elif secondStat == "Luck":
                self.title = "Gambler"
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
                self.title = "Ninja"
            elif secondStat == "Faith":
                self.title = "Druid"
            elif secondStat == "Fame":
                if self.stats["Luck"] < (5 + self.level / 4):
                    self.title = "Werewolf"
                else:
                    self.title = "Archer"
            elif secondStat == "Intelligence":
                self.title = "Ninja"
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
                self.title = "Alchemist"
            elif secondStat == "Speed":
                self.title = "Cantor"
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
            if secondStat == "Charisma":
                self.title = "Gambler"
            elif secondStat == "Dexterity":
                self.title = "Bard"
            elif secondStat == "Faith":
                self.title = "Alchemist"
            elif secondStat == "Fame":
                self.title = "Gambler"
            elif secondStat == "Intelligence":
                self.title = "Alchemist"
            elif secondStat == "Speed":
                self.title = "Gambler"
            elif secondStat == "Soldier":
                self.title = "Soldier"
            elif secondStat == "Strength":
                self.title = "Soldier"
            elif secondStat == "Voice":
                self.title = "Cantor"
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
                self.title = "Baron"
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
                self.title = "Troubadour"
            elif secondStat == "Speed":
                self.title = "Cantor"
            elif secondStat == "Stamina":
                self.title = "Valkyrie"
            elif secondStat == "Strength":
                self.title = "Baron"
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

    def levelUp(self, chatter=True):
        if chatter:
            print('{} hit level {}!'.format(self.name, self.level + 1))
        preLevelStatIncreaseCount = self.statIncreaseCount
        self.level += 1
        if self.statIncreaseCount != 0:
            bonus = self.level * 4 / self.statIncreaseCount
        else:
            bonus = 1
        if bonus <= 0.5:
            bonus = 0.55
        elif bonus > 2:
            bonus = 2
        beforeDict = {}
        afterDict = {}
        for statName, statValue in self.growth.items():
            beforeDict[statName] = self.stats[statName]
            roll = random.randint(1, 10)
            result = math.floor(bonus * roll)
            if result >= statValue:
                statIncrease = math.ceil(result / 10)
                self.stats[statName] += statIncrease
                self.statIncreaseCount += statIncrease
        while preLevelStatIncreaseCount == self.statIncreaseCount:
            for statName, statValue in self.growth.items():
                result = math.floor(bonus * random.randint(1, 10))
                if result >= statValue:
                    statIncrease = math.ceil(result / 10)
                    self.stats[statName] += statIncrease
                    self.statIncreaseCount += statIncrease
                    break
        if chatter:
            happy = self.statIncreaseCount >= (self.level * 4 - 1)
            breakthrough = (
                    self.statIncreaseCount - preLevelStatIncreaseCount > 5)
            for statName, statValue in self.growth.items():
                afterDict[statName] = self.stats[statName]
            fulfilled = 0
            # Stamina
            stamString = f"{'Stamina':<12} {beforeDict['Stamina']}"
            stamString = f"{stamString:<16}"
            if afterDict['Stamina'] > beforeDict['Stamina']:
                if self.growth["Stamina"] == 5:
                    fulfilled += 1
                stamString += f" --> {afterDict['Stamina']}"
            stamString = f"{stamString:<25}"
            # Speed
            spdString = f"{'Speed':<12} {beforeDict['Speed']}"
            spdString = f"{spdString:<16}"
            if afterDict['Speed'] > beforeDict['Speed']:
                if self.growth["Speed"] == 5:
                    fulfilled += 1
                spdString += f" --> {afterDict['Speed']}"
            spdString = f"{spdString:<25}"
            # Strength
            strString = f"{'Strength':<12} {beforeDict['Strength']}"
            strString = f"{strString:<16}"
            if afterDict['Strength'] > beforeDict['Strength']:
                if self.growth["Strength"] == 5:
                    fulfilled += 1
                strString += f" --> {afterDict['Strength']}"
            strString = f"{strString:<25}"
            # Intelligence
            intString = f"{'Intelligence':<12} {beforeDict['Intelligence']}"
            intString = f"{intString:<16}"
            if afterDict['Intelligence'] > beforeDict['Intelligence']:
                if self.growth["Intelligence"] == 5:
                    fulfilled += 1
                intString += f" --> {afterDict['Intelligence']}"
            intString = f"{intString:<25}"
            # Dexterity
            dexString = f"{'Dexterity':<12} {beforeDict['Dexterity']}"
            dexString = f"{dexString:<16}"
            if afterDict['Dexterity'] > beforeDict['Dexterity']:
                if self.growth["Dexterity"] == 5:
                    fulfilled += 1
                dexString += f" --> {afterDict['Dexterity']}"
            dexString = f"{dexString:<25}"
            # Faith
            faithString = f"{'Faith':<12} {beforeDict['Faith']}"
            faithString = f"{faithString:<16}"
            if afterDict['Faith'] > beforeDict['Faith']:
                if self.growth["Faith"] == 5:
                    fulfilled += 1
                faithString += f" --> {afterDict['Faith']}"
            faithString = f"{faithString:<25}"
            # Charisma
            chaString = f"{'Charisma':<12} {beforeDict['Charisma']}"
            chaString = f"{chaString:<16}"
            if afterDict['Charisma'] > beforeDict['Charisma']:
                if self.growth["Charisma"] == 5:
                    fulfilled += 1
                chaString += f" --> {afterDict['Charisma']}"
            chaString = f"{chaString:<25}"
            # Voice
            voiceString = f"{'Voice':<12} {beforeDict['Voice']}"
            voiceString = f"{voiceString:<16}"
            if afterDict['Voice'] > beforeDict['Voice']:
                if self.growth["Voice"] == 5:
                    fulfilled += 1
                voiceString += f" --> {afterDict['Voice']}"
            voiceString = f"{voiceString:<25}"
            # Fame
            fameString = f"{'Fame':<12} {beforeDict['Fame']}"
            fameString = f"{fameString:<16}"
            if afterDict['Fame'] > beforeDict['Fame']:
                if self.growth["Fame"] == 5:
                    fulfilled += 1
                fameString += f" --> {afterDict['Fame']}"
            fameString = f"{fameString:<25}"
            # Luck
            luckString = f"{'Luck':<12} {beforeDict['Luck']}"
            luckString = f"{luckString:<16}"
            if afterDict['Luck'] > beforeDict['Luck']:
                if self.growth["Luck"] == 5:
                    fulfilled += 1
                luckString += f" --> {afterDict['Luck']}"
            luckString = f"{luckString:<25}"
            print(f"    {stamString}    {spdString}")
            print(f"    {strString}    {intString}")
            print(f"    {dexString}    {faithString}")
            print(f"    {chaString}    {voiceString}")
            print(f"    {fameString}    {luckString}")

        if self.level % 5 == 0:
            beforeTitle = self.title
            self.assignTitle(chatter)
            self.assignPower(chatter)
            self.updateGrowth()
            if chatter:
                print("")
                if self.title != beforeTitle:
                    print(
                            f"{self.name}: \"Today I will become a "
                            f"{self.title}!\"")
                else:
                    print(
                            f"{self.name}: \"Another step on my chosen path "
                            f"as a {self.title}!\"")
        else:
            if chatter:
                if fulfilled == 2:
                    if happy:
                        if breakthrough:
                            print(
                                    f"{self.name}: \"These are the moments "
                                    "that define the legends of the "
                                    f"{self.title}!\"")
                        else:
                            print(
                                    f"{self.name}: \"Yes! I am the epitome "
                                    f"of a {self.title}!\"")
                    else:
                        if breakthrough:
                            print(
                                    f"{self.name}: \"What is this? This "
                                    "power! It seems like so much more than a "
                                    f"mere {self.title}!\"")
                        else:
                            print(
                                    f"{self.name}: \"At least I know this is "
                                    f"the path a {self.title} should be "
                                    "taking.\"")
                elif fulfilled == 1:
                    if happy:
                        if breakthrough:
                            print(
                                    f"{self.name}: \"Wow! That really opened "
                                    "up some new perspectives!\"")
                        else:
                            print(
                                    f"{self.name}: \"This will make me a "
                                    f"stronger {self.title}!\"")
                    else:
                        if breakthrough:
                            print(
                                    f"{self.name}: \"Finally, something "
                                    f"about being a {self.title} is making "
                                    "sense.\"")
                        else:
                            print(
                                    f"{self.name}: \"Being a {self.title} is "
                                    "a lot harder than I expected.\"")
                else:
                    if happy:
                        if breakthrough:
                            print(
                                    f"{self.name}: \"I... I've had a vision. "
                                    "I've never seen myself in that light "
                                    "before...\"")
                        else:
                            print(
                                    f"{self.name}: \"Well, that is a "
                                    "disappointment, to say the least.\"")
                    else:
                        if breakthrough:
                            print(
                                f"{self.name}: \"Maybe I'll never be a great "
                                f"{self.title}, but perhaps there are other "
                                "options opening up!\"")
                        else:
                            print(
                                    f"{self.name}: \"Aww, maybe I'm not cut "
                                    f"out to be a {self.title}.\"")

    def maxFP(self):
        if self.equipment:
            return self.stats["Faith"] + self.equipment.fp
        else:
            return self.stats["Faith"]

    def maxHP(self):
        return ((self.stats["Stamina"] * 2) + self.level)

    def maxMP(self):
        if self.equipment:
            return self.stats["Intelligence"] + self.equipment.mp
        else:
            return self.stats["Intelligence"]

    def printCharacterSheet(self):
        print(f"{self.title:12} {self.name}")
        strength = self.stats["Strength"]
        dex = self.stats["Dexterity"]
        cha = self.stats["Charisma"]
        voi = self.stats["Voice"]
        fame = self.stats["Fame"]
        luck = self.stats["Luck"]
        speed = self.stats["Speed"]
        print(f"  Level:    {self.level:3}    Strength: {strength}")
        print(f"  HP:   {self.hp:3}/{self.maxHP():3}    Dexterity: {dex}")
        print(f"  FP:   {self.fp:3}/{self.maxFP():3}    Charisma: {cha}")
        print(f"  MP:   {self.mp:3}/{self.maxMP():3}    Voice: {voi}")
        print(f"  Moves: {self.movementPoints:2}/{speed:3}    Luck: {luck:3}")
        print(
                f"  Exp:  {self.xp:3}/100    Fame:    {fame:3}"
                f"")
        sortedPowers = sorted(self.powers)
        print("Powers:")
        print("  " + " - ".join(sortedPowers))
        if self.equipment:
            print(f"Equipped: {self.equipment.name}")
        print(f"Trophies: {len(self.trophies):3}")

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
stop = input("Type debug to enter debug mode.")
if stop == "debug":
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
        recruit = playerCharacter("Slade", "Wererat", "Ninja", chatter)
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
