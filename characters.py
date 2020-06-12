import math
from operator import itemgetter
import random


class playerCharacter(object):
    """docstring for PlayerCharacter"""

    def __init__(self, name=None, playerClass=None, chatter=False):
        self.powers = []
        if playerClass:
            if playerClass == "Archer":
                self.growth = self.initializeRandomStats(
                        "Dexterity", "Stamina")
            elif playerClass == "Fire Mage":
                self.growth = self.initializeRandomStats(
                        "Intelligence", "Charisma")
            elif playerClass == "Frost Mage":
                self.growth = self.initializeRandomStats(
                        "Intelligence", "Stamina")
            elif playerClass == "Knight":
                self.growth = self.initializeRandomStats("Strength", "Speed")
            elif playerClass == "Monk":
                self.growth = self.initializeRandomStats("Faith", "Strength")
            elif playerClass == "Priest":
                self.growth = self.initializeRandomStats("Faith", "Charisma")
            elif playerClass == "Swordsman":
                self.growth = self.initializeRandomStats(
                        "Strength", "Intelligence")
            elif playerClass == "Warrior":
                self.growth = self.initializeRandomStats("Strength", "Stamina")
            else:
                self.growth = self.initializeRandomStats()
        else:
            self.growth = self.initializeRandomStats()
        self.stats = {}
        for statName, statValue in self.growth.items():
            self.stats[statName] = 20 - statValue
        self.level = 0
        self.statIncreaseCount = 0
        if name:
            self.name = name
        else:
            self.name = 'Test Subject {}'.format(random.randint(1, 9999))
        print('{} created.'.format(self.name))
        self.title = "newbie"
        self.career = ""
        self.assignTitle(chatter)
        self.assignPower()
        self.career = f"    Career Path: {self.title}"
        if chatter:
            for statName, statValue in self.stats.items():
                print("    {} of {}".format(statName, statValue))
            print("")

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
            if secondStat == "Intelligence":
                self.title = "Dark Mage"
            elif secondStat == "Strength":
                self.title = "Knight"
            elif secondStat == "Faith":
                self.title = "Prophet"
            else:
                self.title = "Orator"
        elif primeStat == "Dexterity":
            if secondStat == "Luck":
                self.title = "Bard"
            elif secondStat in ("Charisma", "Intelligence"):
                self.title = "Thief"
            else:
                self.title = "Archer"
        elif primeStat == "Faith":
            if secondStat == "Voice":
                self.title = "Chorister"
            elif secondStat in ("Charisma", "Intelligence", "Luck"):
                self.title = "Priest"
            elif secondStat in ("Strength", "Dexterity", "Stamina"):
                self.title = "Monk"
            else:
                self.title = "Scholar"
        elif primeStat == "Intelligence":
            if secondStat == "Luck":
                self.title = "Bolt Mage"
            elif secondStat == "Charisma":
                self.title = "Fire Mage"
            elif secondStat == "Stamina":
                self.title = "Frost Mage"
            elif secondStat == "Strength":
                self.title = "Swordsman"
            else:
                self.title = "Scholar"
        elif primeStat == "Luck":
            if secondStat in ("Dexterity", "Charisma"):
                self.title = "Bard"
            else:
                self.title = "Gambler"
        elif primeStat == "Stamina":
            if secondStat == "Strength":
                if self.stats["Luck"] < (11 + self.level / 4):
                    self.title = "Berserker"
                self.title = "Warrior"
            elif secondStat == "Intelligence":
                self.title = "Blood Mage"
            else:
                self.title = "Duelist"
        elif primeStat == "Strength":
            if secondStat in ("Charisma", "Speed"):
                if self.stats["Intelligence"] > max(
                        self.stats["Faith"], self.stats["Dexterity"]) \
                        and self.level > 4:
                    self.title = "Mage Knight"
                else:
                    self.title = "Knight"
            elif secondStat == "Faith":
                self.title = "Monk"
            elif secondStat == "Intelligence":
                listOfStatValues = [
                        statValue for statName, statValue
                        in self.stats.items()]
                if self.stats["Fame"] < max(list(set(listOfStatValues))[:3]) \
                        and self.level > 9:
                    self.title = "Steam Knight"
                else:
                    self.title = "Swordsman"
            elif secondStat == "Stamina":
                if self.stats["Luck"] < (11 + self.level / 4):
                    self.title = "Berserker"
                self.title = "Warrior"
            else:
                self.title = "Duelist"
        elif primeStat == "Voice":
            self.title = "Chorister"
        if self.title == "newbie":
            if self.stats["Intelligence"] < self.stats["Strength"]:
                self.title = "Squire"
            else:
                self.title = "Student"
        if self.stats["Fame"] >= 25 and "Captain" not in self.title:
            self.title = self.title + " Captain"
        if self.stats["Speed"] > 25 <= 40 and (
                "Mounted" not in self.title and "Knight" not in self.title):
            self.title = "Mounted " + self.title
        elif self.stats["Speed"] > 40 and "Sky " not in self.title:
            self.title = "Sky " + self.title
        if self.title != oldTitle:
            if chatter:
                print(f"{self.name} became a {self.title}!")
            self.career += f" --> {self.title} ({self.level})"

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
                        "Equip: Bows", "Quick Shot", "Aimed Shot",
                        "Ranged Attack: Range +1", "Poison Arrow",
                        "Luck: Enable Triple Attack", "Holy Arrow",
                        "Point-Blank Shot"]
            elif "Bard" in self.title:
                listOfPowers = [
                        "Equip: Dagger", "Heal I", "Equip: Bows",
                        "Counterattack", "Luck: Enable Triple Attack",
                        "Luck: Enable Double Dodge",
                        "Symphony: Increased Effect I",
                        "Command: Added Effect: Random"]
            elif "Berserker" in self.title:
                listOfPowers = [
                        "Equip: Axes", "Unarmed Attack: Increased Damage I",
                        "Unhindered Movement", "Axes: Armor Penetration I",
                        "Unarmed Attack: Add Effect: Slow",
                        "Low Health: Damage Increase I",
                        "Unarmed Attack: Increased Damage II",
                        "Unarmed Attack: Throw Enemy"]
            elif "Blood Mage" in self.title:
                listOfPowers = [
                        "Drain I", "Poison I", "Drain II", "Equip: Daggers",
                        "Muddle I", "Death I",
                        "Magic: Critical Damage Increased I", "Poison II"]
            elif "Bolt Mage" in self.title:
                listOfPowers = [
                        "Bolt I", "Blaze I", "Freeze I",
                        "Magic: Increased Area I", "Bolt II", "Bolt III",
                        "Death I", "Bolt IV"]
            elif "Chorister" in self.title:
                listOfPowers = [
                        "Symphony: Increased Effect I", "Heal I", "Blast I",
                        "Symphony: Increased Effect II", "Blast II", "Heal II",
                        "Symphony: Increased Effect III", "Blast III"]
            elif "Dark Mage" in self.title:
                listOfPowers = [
                        "Blaze I", "Defense: Magic", "Freeze I", "Blaze II",
                        "Death I", "Freeze II", "Death II", "Bolt I"]
            elif "Duelist" in self.title:
                listOfPowers = [
                        "Equip: Long Swords", "Counterattack",
                        "Defense: Swords I", "Swords: Increased Luck I",
                        "Swords: Increased Luck II", "Luck: Parry",
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
                        "Dodge: Added Effect - Counterattack",
                        "Luck: Reverse Death", "Axes: Ranged + 1",
                        "Luck: Dodge Chance Increased II",
                        "Dodge: Added Effect - Stealth"]
            elif ("Knight" in self.title and "Mage Knight" not in
                    self.title and "Sky Knight" not in
                    self.title and "Steam Knight" not in self.title):
                listOfPowers = [
                        "Mounted Movement", "Equip: Polearms", "Charge",
                        "Spears: Armor Penetration I", "Defense: Lance I",
                        "Defense: Arrow I", "Equip: Holy Polearms",
                        "Defense: Dark Magic I"]
            elif "Mage Knight" in self.title:
                listOfPowers = [
                        "Mounted Movement", "Equip: Polearms",
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
                        "Aura I", "Symphony: Increased Effect I", "Shield I",
                        "Aura II", "Aura III", "Symphony: Increased Effect II",
                        "Aura IV", "Symphony: Increased Range I"]
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
            elif "Scholar" in self.title:
                listOfPowers = [
                        "Sleep I", "Magic: Cost Reduction I", "Muddle I",
                        "Seal I", "Magic: All Spells +1 Rank",
                        "Magic: Cost Reduction II",
                        "Magic: Effects Always Hit"]
            elif "Steam Knight" in self.title:
                listOfPowers = [
                        "Equip: Lances",
                        "Defense: Added Effect: Reduce armor penetration",
                        "Defense: Weapons I",
                        "Defense: Fire Adds Haste",
                        "Lances: Armor Penetration I", "Unhindered Movement",
                        "Lances: Armor Penetration II", "Defense: Weapons II"]
            elif "Swordsman" in self.title:
                listOfPowers = [
                        "Egress I", "Equip: Long Swords",
                        "Equip: Sacred Swords", "Counterattack",
                        "Swords: Increased Luck I", "Bolt I", "Bolt II",
                        "Swords: Increased Luck II"]
            elif "Thief" in self.title:
                listOfPowers = [
                        "Equip: Daggers", "Counterattack", "Luck: Steal",
                        "Daggers: Range +1", "Stealthy Movement",
                        "Ninja Fire I", "Ninja Bolt I", "Ninja Fire II"]
            elif "Warrior" in self.title:
                listOfPowers = [
                        "Equip: Axes", "Defense: Melee Attacks I",
                        "Axes: Increased Damage I",
                        "Swords: Armor Penetration I", "Whirlwind Attack",
                        "Defense: Melee Attacks II", "Leap",
                        "Axes: Increased Damage I"]
            for power in listOfPowers:
                if not any([
                        knownPower for knownPower in self.powers
                        if power in knownPower]):
                    nameOfPower = power
                    if 'Captain' in self.title and not any([
                            knownPower for knownPower in self.powers
                            if 'Command:' in knownPower]):
                        nameOfPower = 'Command: ' + nameOfPower
                    self.powers.append(nameOfPower)
                    print(f"{self.name} learned {nameOfPower}!")
                    return

    def initializeRandomStats(self, bestStat=None, secondBestStat=None):
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
                print("")

    def updateGrowth(self):
        sortedGrowth = sorted(self.growth.items(), key=itemgetter(1))
        growthLevel = 5
        advance = True
        for statGrowthKey, statGrowthValue in sortedGrowth:
            self.growth[statGrowthKey] = growthLevel
            advance = not advance
            if advance:
                growthLevel += 1


party = []
module = input("Type SF if you want me to run the SF module.")
chatty = input("Type chatty if you want to be barraged with leveling info.")
if chatty == 'chatty':
    chatter = True
    stopEveryLevel = input("Type slow if you want to stop for every level.")
else:
    chatter = False
    stopEveryLevel = "fast"
if module == 'SF':
    recruit = playerCharacter("Max", "Swordsman", chatter)
    party.append(recruit)
    recruit = playerCharacter("Lowe", "Priest", chatter)
    party.append(recruit)
    recruit = playerCharacter("Tao", "Fire Mage", chatter)
    party.append(recruit)
    recruit = playerCharacter("Luke", "Warrior", chatter)
    party.append(recruit)
    recruit = playerCharacter("Ken", "Knight", chatter)
    party.append(recruit)
    recruit = playerCharacter("Hans", "Archer", chatter)
    party.append(recruit)
    recruit = playerCharacter("Gong", "Monk", chatter)
    party.append(recruit)
    recruit = playerCharacter("Mae", "Knight", chatter)
    party.append(recruit)
    recruit = playerCharacter("Gort", "Warrior", chatter)
    party.append(recruit)
    recruit = playerCharacter("Khris", "Priest", chatter)
    party.append(recruit)
    recruit = playerCharacter("Anri", "Frost Mage", chatter)
    party.append(recruit)
    recruit = playerCharacter("Arthur", "Knight", chatter)
    party.append(recruit)
else:
    partySize = int(input("How many characters should I create? "))
    for i in range(partySize):
        recruit = playerCharacter(None, None, chatter)
        party.append(recruit)
levelUpNum = int(input("How many levels should they get? "))
for i in range(levelUpNum):
    for pc in party:
        pc.levelUp(chatter)
        if stopEveryLevel == "slow":
            stop = input()
for pc in party:
    print(f"{pc.name} is a level {pc.level} {pc.title}.")
    print(pc.career)
    if pc.powers:
        print("    Powers: " + " -> ".join(pc.powers))
