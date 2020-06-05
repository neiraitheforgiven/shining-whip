import math
from operator import itemgetter
import random


class playerCharacter(object):
    """docstring for PlayerCharacter"""

    def __init__(self):
        self.growth = self.initializeRandomStats()
        self.stats = {}
        for statName, statValue in self.growth.items():
            self.stats[statName] = 20 - statValue
        self.level = 0
        self.statIncreaseCount = 0
        self.name = 'Test Subject {}'.format(random.randint(1, 9999))
        print('{} created.'.format(self.name))
        self.title = "newbie"
        self.assignTitle()
        for statName, statValue in self.stats.items():
            print("    {} of {}".format(statName, statValue))
        print("")

    def assignTitle(self):
        oldTitle = self.title
        primeStat = max(self.stats.items(), key=itemgetter(1))[0]
        listOfStats = {}
        for stat in self.stats:
            if stat != primeStat:
                listOfStats[stat] = self.stats[stat]
        secondStat = max(listOfStats.items(), key=itemgetter(1))[0]
        if primeStat == "Voice":
            self.title = "Chorister"
        elif primeStat == "Strength":
            if secondStat == "Stamina":
                self.title = "Warrior"
        elif primeStat == "Faith":
            if secondStat == "Charisma":
                self.title = "Prophet"
            if secondStat == "Voice":
                self.title = "Chorister"
        elif self.stats["Intelligence"] < self.stats["Strength"]:
            self.title = "Squire"
        else:
            self.title = "Student"
        if self.stats["Fame"] >= 25:
            self.title = "Pop-" + self.title
        if self.title != oldTitle:
            print(f"{self.name} became a {self.title}!")

    def initializeRandomStats(self):
        statsToAssign = [
                "Strength", "Dexterity", "Intelligence", "Faith", "Charisma",
                "Luck", "Speed", "Stamina", "Voice", "Fame"]
        statsCount = len(statsToAssign)
        growth = {}
        growthLevel = 5
        advance = True
        for i in range(statsCount):
            stat = random.choice(statsToAssign)
            growth[stat] = growthLevel
            statsToAssign.remove(stat)
            advance = not advance
            if advance:
                growthLevel += 1
        return growth

    def levelUp(self, num=1):
        print('{} hit level {}!'.format(self.name, self.level + 1))
        preLevelStatIncreaseCount = self.statIncreaseCount
        for i in range(num):
            if self.statIncreaseCount != 0:
                bonus = self.level * 4 / self.statIncreaseCount
            else:
                bonus = 1
            if bonus <= 0.5:
                bonus = 0.55

            for statName, statValue in self.growth.items():
                roll = random.randint(1, 10)
                result = math.floor(bonus * roll)

                if result >= statValue:

                    statIncrease = math.ceil(result / 10)
                    self.stats[statName] += statIncrease
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
                    print("    {} became {}{}".format(
                            statName, self.stats[statName],
                            '!' * statIncrease))
                    self.statIncreaseCount += statIncrease
                    break
        self.level += 1
        print("")
        if self.level % 5 == 0:
            print(f"It's time for {self.name}'s class review.")
            for statName, statValue in self.stats.items():
                print("    {} of {}".format(statName, statValue))
            print("")


party = []
partySize = int(input("How many characters should I create? "))
for i in range(partySize):
    recruit = playerCharacter()
    party.append(recruit)
levelUpNum = int(input("How many levels should they get? "))
for i in range(levelUpNum):
    for pc in party:
        pc.levelUp()
