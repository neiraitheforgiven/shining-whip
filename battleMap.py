from characters import equipment
from characters import playerCharacter
from characters import monster
from operator import itemgetter
from shopping import shop
import math
import os
import random
import shelve
import time

#  import traceback


class battle(object):
    def __init__(self, game, party, num=None):
        self.totalTimePassed = 0
        self.roundCount = 0
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
                self.battleField = battleField(
                    [
                        "Forest",
                        "Grass",
                        "Grass",
                        "Upward Stair",
                        "Rubble",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Rubble",
                        "Rubble",
                        "Tiled Floor",
                    ],
                    [
                        (monster("Goblin"), 7),
                        (monster("Traitor Knight"), 7),
                        (monster("Goblin"), 8),
                        (monster("Crazed Dwarf"), 9),
                        (monster("Crazed Dwarf"), 9),
                        (monster("Goblin"), 10),
                        (monster("Goblin"), 10),
                    ],
                    self.party,
                    game,
                )
            elif num == 2:
                self.battleField = battleField(
                    [
                        "Loose Rocks",
                        "Loose Rocks",
                        "Loose Rocks",
                        "Loose Rocks",
                        "Loose Rocks",
                        "Grass",
                        "Forest",
                        "Grass",
                        "Loose Rocks",
                        "Grass",
                        "Grass",
                        "Path",
                        "Bridge",
                        "Path",
                        "Path",
                        "Path",
                        "Grass",
                        "Grass",
                    ],
                    [
                        (monster("Goblin", "Retreat-Defensive", "Weakest"), 3),
                        (monster("Goblin", "Retreat-Defensive", "Weakest"), 3),
                        (monster("Goblin", "Retreat-Defensive", "Weakest"), 3),
                        (monster("Goblin", "Advance-Defensive", "Weakest"), 9),
                        (monster("Goblin", "Advance-Defensive", "Weakest"), 9),
                        (monster("Goblin", "Advance-Defensive", "Weakest"), 9),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Retreat-Defensive",
                                "ChallengeAccepting",
                            ),
                            9,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Retreat-Defensive",
                                "ChallengeAccepting",
                            ),
                            10,
                        ),
                        (monster("Crazed Dwarf", None, "ChallengeAccepting"), 10),
                        (monster("Traitor Knight", "Advance-Defensive"), 17),
                        (monster("Traitor Knight", "Advance-Defensive"), 17),
                    ],
                    self.party,
                    game,
                )
            elif num == 3:
                self.battleField = battleField(
                    [
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                    ],
                    [
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            5,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            5,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            5,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            7,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            7,
                        ),
                        (monster("Giant Bat"), 8),
                        (monster("Giant Bat"), 9),
                        (monster("Giant Bat"), 9),
                        (monster("Giant Bat"), 9),
                        (monster("Giant Bat"), 10),
                        (monster("Traitor Knight"), 11),
                        (monster("Traitor Knight"), 11),
                        (monster("Traitor Knight"), 11),
                        (monster("Traitor Knight"), 11),
                        (monster("Traitor Knight"), 12),
                    ],
                    self.party,
                    game,
                )
            elif num == 4:
                self.battleField = battleField(
                    [
                        "Path",
                        "Path",
                        "Path",
                        "Bridge",
                        "Bridge",
                        "Path",
                        "Path",
                        "Bridge",
                        "Path",
                        "Path",
                        "Path",
                        "Bridge",
                        "Bridge",
                        "Path",
                        "Path",
                        "Path",
                        "Path",
                        "Bridge",
                        "Bridge",
                        "Path",
                    ],
                    [
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            11,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            11,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            11,
                        ),
                        (
                            monster(
                                "Crazed Dwarf",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            11,
                        ),
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
                        (monster("Dark Apprentice"), 19),
                    ],
                    self.party,
                    game,
                )
            elif num == 5:
                self.battleField = battleField(
                    [
                        "Grass",
                        "Grass",
                        "Grass",
                        "Grass",
                        "Grass",
                        "Bridge",
                        "Grass",
                        "Grass",
                        "Sand",
                        "Sand",
                        "Sand",
                        "Sand",
                        "Sand",
                        "Sand",
                        "Sand",
                        "Sand",
                        "Sand",
                    ],
                    [
                        (monster("Crazed Dwarf", "Defensive", "ChallengeAccepting"), 6),
                        (monster("Crazed Dwarf", "Defensive", "ChallengeAccepting"), 6),
                        (monster("Crazed Dwarf", "Defensive", "ChallengeAccepting"), 6),
                        (monster("Giant Bat"), 10),
                        (monster("Sniper"), 11),
                        (monster("Sniper"), 11),
                        (monster("Dark Apprentice", "SlowAdvance"), 12),
                        (monster("Giant Bat"), 14),
                        (monster("Giant Bat"), 15),
                        (monster("Zombie"), 14),
                        (monster("Zombie"), 14),
                        (monster("Zombie"), 16),
                        (monster("Zombie"), 16),
                        (monster("Dark Apprentice"), 16),
                        (monster("Dark Apprentice"), 16),
                    ],
                    self.party,
                    game,
                )
            elif num == 6:
                self.battleField = battleField(
                    [
                        "Cavern",
                        "Cavern",
                        "Cavern",
                        "Cavern",
                        "Cavern",
                        "Bridge",
                        "Cavern",
                        "Cavern",
                        "Cavern",
                        "Loose Rocks",
                        "Cavern",
                        "Loose Rocks",
                        "Cavern",
                    ],
                    [
                        (monster("Zombie"), 3),
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
                        (monster("Skeleton Warrior"), 12),
                    ],
                    self.party,
                    game,
                )
            elif num == 7:
                self.battleField = battleField(
                    [
                        "Sand",
                        "Sand",
                        "Sand",
                        "Upward Stair",
                        "Upward Stair",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                    ],
                    [
                        (monster("Body Puppet"), 3),
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
                        (monster("Marionette"), 10),
                    ],
                    self.party,
                    game,
                    -2,
                )
            elif num == 8:
                self.battleField = battleField(
                    [
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Downward Stair",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                        "Tiled Floor",
                    ],
                    [
                        (
                            monster(
                                "Skeleton Warrior",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            3,
                        ),
                        (monster("Zombie"), 4),
                        (monster("Zombie"), 4),
                        (
                            monster(
                                "Skeleton Warrior",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            4,
                        ),
                        (monster("Zombie"), 5),
                        (monster("Zombie"), 5),
                        (
                            monster(
                                "Skeleton Warrior",
                                "Advance-Defensive",
                                "ChallengeAccepting",
                            ),
                            5,
                        ),
                        (monster("Ghoul"), 5),
                        (monster("Zombie"), 7),
                        (monster("Zombie"), 7),
                    ],
                    self.party,
                    game,
                    2,
                )
            elif num == 9:
                self.battleField = battleField(
                    [
                        "Grass",
                        "Grass",
                        "Downward Stair",
                        "Downward Stair",
                        "Grass",
                        "Grass",
                        "Loose Rock",
                        "Cavern",
                        "Cavern",
                        "Cavern",
                        "Loose Rock",
                        "Loose Rock",
                        "Cavern",
                        "Downward Stair",
                        "Downward Stair",
                        "Cavern",
                        "Cavern",
                        "Cavern",
                        "Downward Stair",
                        "Downward Stair",
                        "Loose Rock",
                        "Loose Rock",
                        "Loose Rock",
                        "Upward Stair",
                        "Upward Stair",
                        "Upward Stair",
                        "Cavern",
                        "Cavern",
                    ],
                    [
                        (monster("Skeleton Warrior"), 5),
                        (monster("Skeleton Warrior"), 7),
                        (monster("Dark Magi"), 12),
                        (monster("Vile Chanter"), 13),
                        (monster("Skeleton Warrior"), 15),
                        (monster("Vile Chanter"), 16),
                        (monster("Vile Chanter"), 16),
                        (monster("Skeleton Warrior"), 17),
                        (monster("Skeleton Warrior"), 17),
                        (monster("Dark Elf Sniper"), 17),
                        (monster("Dark Elf Sniper"), 18),
                        (monster("Dark Magi"), 18),
                        (monster("Skeleton Warrior"), 22),
                        (monster("Lizardman"), 22),
                        (monster("Vile Chanter"), 27),
                        (monster("Master Mage"), 27),
                    ],
                    self.party,
                    game,
                )
            elif num == 10:
                self.battleField = battleField(
                    [
                        "Loose Rock",  # 0
                        "Grass",
                        "Grass",
                        "Grass",
                        "Grass",  # 4
                        "Forest",
                        "Forest",
                        "Forest",
                        "Forest",  # 8
                        "Forest",
                        "Forest",
                        "Forest",
                        "Forest",  # 12
                        "Forest",
                        "Loose Rock",
                        "Loose Rock",  # 15
                    ],
                    [
                        (monster("Skeleton Warrior"), 4),
                        (monster("Skeleton Warrior"), 4),
                        (monster("Skeleton Warrior"), 4),
                        (monster("Dark Elf Sniper"), 6),
                        (monster("Dark Elf Sniper"), 6),
                        (monster("Lizardman"), 7),
                        (monster("Skeleton Warrior"), 7),
                        (monster("Vile Chanter"), 7),
                        (monster("Skeleton Warrior"), 7),
                        (monster("Pteropus Knight"), 12),
                        (monster("Pteropus Knight"), 12),
                        (monster("Pteropus Knight"), 15),
                        (monster("Pteropus Knight"), 15),
                        (monster("Lizardman"), 15),
                        (monster("Vile Chanter"), 15),
                    ],
                    self.party,
                    game,
                )
            elif num == 11:
                self.battleField = battleField(
                    [
                        "Grass",  # 0
                        "Grass",
                        "Path",
                        "Path",
                        "Path",  # 4
                        "Path",
                        "Path",
                        "Path",
                        "Path",  # 8
                        "Path",
                        "Path",
                        "Path",
                        "Path",  # 12
                        "Path",
                        "Path",
                        "Path",
                        "Path",  # 16
                        "Path",
                        "Path",
                        "Path",
                        "Downward Stair",  # 20
                        "Downward Stair",
                        "Downward Stair",
                        "Grass",
                    ],
                    [
                        (monster("Lizardman"), 8),
                        (monster("Vile Chanter"), 11),
                        (monster("Pteropus Knight"), 12),
                        (monster("Pteropus Knight"), 13),
                        (monster("Lizardman"), 13),
                        (monster("Pteropus Knight"), 14),
                        (monster("Lizardman"), 14),
                        (monster("Lizardman"), 14),
                        (monster("The Screaming Beast"), 19),
                        (monster("Mercenary Knight"), 19),
                        (monster("Vile Chanter"), 20),
                        (monster("Lizardman"), 21),
                        (monster("Dark Elf Sniper"), 21),
                        (monster("Mercenary Knight"), 22),
                        (monster("Dark Elf Sniper"), 22),
                        (monster("Dark Elf Sniper"), 22),
                    ],
                    self.party,
                    game,
                )
            for unit in self.battleField.units:
                unit.focusTime = 0
                unit.hp = unit.maxHP()
                if self.getPower(unit, "Convert Faith and Magic"):
                    combined = unit.stats["Faith"] + unit.stats["Intelligence"]
                    unit.fp = combined
                    unit.mp = combined
                else:
                    unit.fp = unit.stats["Faith"]
                    unit.mp = unit.stats["Intelligence"]
                if self.getPower(unit, "Begin Battle With Rank II Focus"):
                    unit.focus = 1500
                else:
                    unit.focus = 0
                unit.bleedTime = 0
                unit.lastTurnFocusRank = 0
                unit.actedThisRound = False
                unit.status = []
                if unit.equipment:
                    unit.fp += unit.equipment.fp
                    unit.mp += unit.equipment.mp
                if self.getPower(unit, "Egress I") and unit.mp < self.mpCost(unit, 8):
                    print(f"warning: {unit.name} has too few mp to Egress")
                unit.resonating = []
                unit.extraPowerSlot = None
                unit.extraPowerSlot2 = None
            self.determineStartingInitiative()
            self.game.battleStatus = 'ongoing'
            while self.battleOn():
                self.roundCount += 1
                self.doRound()

    def addResonance(self, unit, tile, area=1):
        tileIndex = self.battleField.terrainArray.index(tile)
        if area == 0:
            unit.resonating.append(tile)
            unit.resonating.append(tile)
            return
        for tileId in range(tileIndex - area, tileIndex + area + 1):
            if tileId >= len(self.battleField.terrainArray) or tileId < 0:
                continue
            tile2 = self.battleField.terrainArray[tileId]
            unit.resonating.append(tile2)
            unit.resonating.append(tile2)

    def assembleParty(self, party, maxPartySize):
        if len(party) <= maxPartySize:
            return party
        else:
            print("It's time to assemble your party!")
            currentParty = []
            leaders = [unit for unit in party if "Egress I" in unit.powers]
            if len(leaders) == 1:
                currentParty.append(leaders[0])
                print(f"{leaders[0].name} leads the Force into battle!")
            else:
                print("Who will lead the Force?")
                leaderChoice = None
                while leaderChoice not in [
                    leaders.index(leader) for leader in leaders
                ] or (leaderChoice not in ('L', 'l')):
                    leaderString = ''
                    leaderStringAdds = []
                    count = 0
                    for leader in leaders:
                        leaderStringAdds.append(f"({count}) {leader.name}")
                        count += 1
                    leaderString += ", ".join(leaderStringAdds)
                    print(leaderString)
                    leaderChoice = input(
                        "Type a number to choose a leader for the party. "
                        "Press (L) to look more closely at a leader. "
                    )
                    if leaderChoice in ('L', 'l'):
                        leaderChoice = None
                        while leaderChoice not in (
                            [leaders.index(leader) for leader in leaders]
                        ):
                            try:
                                leaderChoice = int(
                                    input(
                                        "Type a number to choose which leader to "
                                        f"look at or press {count} to go "
                                        "back: "
                                    )
                                )
                                leaders[leaderChoice].printCharacterSheet()
                            except ValueError:
                                leaderChoice = None
                            except IndexError:
                                if leaderChoice == count:
                                    break
                                leaderChoice = None
                            leaderChoice = None
                    else:
                        try:
                            leaderChoice = int(leaderChoice)
                            currentParty.append(leaders[leaderChoice])
                            print(
                                f"{leaders[leaderChoice].name} leads the "
                                "Force into battle!"
                            )
                            break
                        except ValueError:
                            leaderChoice = None
                        except IndexError:
                            leaderChoice = None
            while len(currentParty) < maxPartySize:
                unitChoice = None
                partyOptions = [unit for unit in party if unit not in currentParty]
                while unitChoice not in (
                    [partyOptions.index(option) for option in partyOptions],
                    'L',
                    'l',
                ):

                    optionString = ''
                    optionStringAdds = []
                    count = 0
                    for unit in partyOptions:
                        optionStringAdds.append(f"({count}) {unit.name}")
                        count += 1
                    optionString += ", ".join(optionStringAdds)
                    print(optionString)
                    unitChoice = input(
                        "Type a number to choose a character to join "
                        "the party. Press (L) to look more closely at a "
                        "character. Press (S) to start the battle without "
                        "adding any new characters. "
                    )
                    if unitChoice in ('L', 'l'):
                        unitChoice = None
                        while unitChoice not in (
                            [partyOptions.index(option) for option in partyOptions]
                        ):
                            try:
                                unitChoice = int(
                                    input(
                                        "Type a number to choose a character to "
                                        "look at: "
                                    )
                                )
                            except ValueError:
                                unitChoice = None
                            if unitChoice and (
                                unitChoice
                                not in (
                                    [
                                        partyOptions.index(option)
                                        for option in partyOptions
                                    ]
                                )
                            ):
                                unitChoice = None
                            partyOptions[unitChoice].printCharacterSheet()
                    elif unitChoice in ('S', 's'):
                        return currentParty
                    else:
                        try:
                            unitChoice = int(unitChoice)
                        except ValueError:
                            unitChoice = None
                        if (
                            unitChoice
                            and (unitChoice <= len(partyOptions) - 1)
                            or unitChoice == 0
                        ):
                            currentParty.append(partyOptions[unitChoice])
                            print(f"{partyOptions[unitChoice].name} joins the party!")
                            partyOptions = [
                                unit for unit in party if unit not in currentParty
                            ]
                            break
            return currentParty

    def attack(self, unit, target, pursuitAttack=False):
        bf = self.battleField
        counterattack = False
        poisonEnemy = False
        routEnemy = False
        targetStunned = False
        doubleChanceArray = []
        dex = self.getStat(unit, "Dexterity")
        luck = self.getStat(unit, "Luck")
        stamina = self.getStat(unit, "Stamina")
        if self.getPower(unit, "Swords: Increased Luck I"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck II"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if self.getPower(unit, "Swords: Increased Luck III"):
            if unit.equipment and unit.equipment.type == "Swords":
                luck = math.ceil(luck * 1.3)
        if pursuitAttack:
            attackCount = 1
        else:
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
                time.sleep(4.0 / 10)
            elif i > 0:
                print(f"{unit.name} attacks again!")
                time.sleep(4.0 / 10)
            attackTypeArray = []
            targetLuck = self.getStat(target, "Luck")
            attackTypeArray.extend(["normal"] * (100 - (luck - targetLuck)))
            strength = self.getStat(unit, "Strength")
            criticalChance = math.floor(strength + (strength * (luck / 10)))
            attackTypeArray.extend(["critical"] * criticalChance)
            routSkill = max(self.getStat(unit, "Charisma"), self.getStat(unit, "Voice"))
            routChance = math.floor(routSkill + (routSkill * (luck / 10)))
            if self.getPower(unit, "Luck: Increased Rout I"):
                routChance = math.ceil(routChance * 1.3)
            if self.getPower(unit, "Luck: Increased Rout II"):
                routChance = math.ceil(routChance * 1.3)
            attackTypeArray.extend(["routing"] * routChance)
            if i + 1 == attackCount:
                heavyChance = math.floor(stamina + (stamina * (luck / 10)))
                attackTypeArray.extend(["heavy"] * heavyChance)
            if not self.getPower(unit, "Aimed Shot"):
                if self.battleField.canMove(target):
                    dodgeSkill = math.floor(
                        max(
                            self.getStat(target, "Intelligence"),
                            targetLuck,
                            self.getStat(target, "Speed"),
                        )
                        * (1 + ((targetLuck / 10)))
                    )
                    if self.getPower(target, "Luck: Dodge Chance  Up I"):
                        dodgeSkill = math.ceil(dodgeSkill * 1.3)
                    if self.getPower(target, "Luck: Dodge Chance  Up II"):
                        dodgeSkill = math.ceil(dodgeSkill * 1.3)
                    attackTypeArray.extend(["dodge"] * dodgeSkill)
            if self.getPower(target, "Luck: Counterattack"):
                counterSkill = math.floor(
                    self.getStat(target, "Dexterity") * (1 + targetLuck / 10)
                )
                attackTypeArray.extend(["counter"] * counterSkill)
            attackType = random.choice(attackTypeArray)
            if self.getPower(unit, "Poisonous Attack"):
                stamina = self.getStat(unit, "Stamina")
                vsStamina = self.getStat(target, "Stamina")
                poisonChance = luck + stamina - vsStamina
                if poisonChance > 0:
                    attackTypeArray.extend(["poison"] * poisonChance)
            if attackType == 'dodge':
                time.sleep(1.0 / 10)
                print(f"{target.name} dodges the attack!")
                self.giveExperience(unit, target, 1)
            else:
                if attackType == 'critical':
                    time.sleep(2.0 / 10)
                    print("")
                    print("A Critical Attack!")
                    print("")
                    time.sleep(4.0 / 10)
                elif attackType == 'normal':
                    if self.getPower(
                        unit, "Heavy Attack Instead of Normal For Ranged Tile"
                    ):
                        unitPos = self.battleField.getUnitPos(unit)
                        targetPos = self.battleField.getUnitPos(target)
                        if unitPos != targetPos:
                            attackType = 'heavy'
                damage = max(strength, dex)
                if attackType == 'heavy':
                    time.sleep(2.0 / 10)
                    print("")
                    print("A heavy attack!")
                    print("")
                    damage *= 1.15
                    if self.getPower(unit, "Increased Heavy Damage I"):
                        damage *= 1.3
                    if self.getPower(unit, "Increased Heavy Damage II"):
                        damage *= 1.3
                    if self.getPower(unit, "Increased Heavy Damage III"):
                        damage *= 1.3
                    if self.getPower(unit, "Increased Heavy Damage IV"):
                        damage *= 1.3
                    self.rattle(unit, target, damage * 30)
                    if self.getPower(unit, "Heavy Attacks Inflict Bleed"):
                        self.bleedStart(target)
                    time.sleep(1.0 / 10)
                if unit.equipment:
                    damageString = f"{unit.equipment.type}: Increased Damage "
                else:
                    damageString = "Unarmed Attack: Increased Damage "
                    damage += math.ceil(unit.skills["Unarmed Attack"] / 2)
                if self.getPower(unit, damageString + "I"):
                    damage *= 1.3
                if self.getPower(unit, damageString + "II"):
                    damage *= 1.3
                if self.getPower(unit, damageString + "III"):
                    damage *= 1.3
                if self.getPower(unit, damageString + "IV"):
                    damage *= 1.3
                if self.getPower(unit, "Extra Damage to Single Target"):
                    if (
                        len(
                            [
                                tileUnit
                                for tileUnit in bf.unitsAtPosition(bf.getUnitPos(unit))
                                if type(tileUnit) == type(target)
                            ]
                        )
                        == 1
                    ):
                        damage *= 1.3
                strengthForDamage = strength
                if self.getPower(unit, "Lances: Movement Increases Strength Damage I"):
                    if unit.equipment and unit.equipment.type == "Lances":
                        strengthForDamage += math.ceil(
                            (self.getStat(unit, "Speed") - unit.movementPoints) / 5
                        )
                damage = max(strengthForDamage, damage)
                if i == 0:
                    if self.getPower(unit, "Jump Attack"):
                        if self.getPower(target, "Mounted Movement") or self.getPower(
                            target, "Flying Movement"
                        ):
                            print(f"{unit.name} leaps onto {target.name}!")
                            damage *= 1.3
                if self.getPower(target, "Defense: Melee Attacks I") and (
                    bf.getUnitPos(unit) == bf.getUnitPos(target)
                ):
                    damage *= 0.7
                    damage = math.floor(damage)
                element = None
                if unit.equipment:
                    damage += unit.equipment.damage
                else:
                    if self.getPower(unit, "Wind Fists: Unarmed Range and Wind"):
                        element = "Wind"
                if element:
                    if self.getPower(target, f"Defense: {element} Resistance"):
                        damage = math.floor(damage / 1.3)
                    if self.getPower(target, f"Defense: {element} Vulnerability"):
                        damage = math.ceil(damage * 1.3)
                # Terrain bonuses section -- consider breaking out
                # elevation damage
                unitTile = bf.terrainArray[bf.getUnitPos(unit)]
                targetTile = bf.terrainArray[bf.getUnitPos(target)]
                unitHeight = unitTile.elevation
                targetHeight = targetTile.elevation
                heightBonus = 1 + ((unitHeight - targetHeight) / 20)
                damage = math.ceil(damage * heightBonus)
                if heightBonus > 1:
                    if self.getPower(unit, "Increased Terrain Advantage I"):
                        damage = math.ceil(damage * heightBonus)
                if self.getResonance(unitTile) > 0:
                    if self.getPower(unit, "Faith: Add Damage on Holy Ground I"):
                        damage = math.ceil(damage + (self.getStat(unit, "Faith") / 3))
                    if self.getPower(unit, "Faith: Add Damage on Holy Ground II"):
                        damage = math.ceil(damage + (self.getStat(unit, "Faith") / 3))
                if attackType != 'critical':
                    if self.getPower(target, "Use Voice For Defense"):
                        damage -= max(
                            self.getStat(target, "Strength"),
                            self.getStat(target, "Dexterity"),
                            self.getStat(target, "Faith"),
                            self.getStat(target, "Voice"),
                        )
                    else:
                        damage -= max(
                            self.getStat(target, "Strength"),
                            self.getStat(target, "Dexterity"),
                            self.getStat(target, "Faith"),
                        )
                damage = max(damage, 1)
                damage = min(damage, target.hp)
                print(f"{unit.name} deals {damage} damage to {target.name}!")
                if attackType == 'critical':
                    self.rattle(unit, target, damage * 30)
                    if self.getPower(unit, "Luck: Critical Drain I") or (
                        self.getPower(unit, "Luck: Critical Drain II")
                    ):
                        if self.getPower(unit, "Luck: Critical Drain II"):
                            heal = min(math.ceil(damage * 0.6), unit.maxHP())
                        else:
                            heal = min(math.ceil(damage * 0.3), unit.maxHP())
                        print(f"{unit.name} drained {heal} health during the attack!")
                        unit.hp += heal
                target.hp -= damage
                if attackType == 'heavy':
                    if self.getPower(unit, "Heavy Attacks Inflict Bleed"):
                        self.bleedStart(target)
                if self.getPower(unit, "Attacking Adds Resonance"):
                    darkTile = self.getResonance(unitTile) <= -1
                    if darkTile:
                        print(
                            f'{unit.name} shouts a few lines from the '
                            'holy song, hoping to be heard over the '
                            'unholy din.'
                        )
                    elif self.getResonance(unitTile) >= 1:
                        print(
                            f'{unit.name} sings along with the holy song of the Force.'
                        )
                    else:
                        print(f'{unit.name} sings out a stanza from the holy song.')
                    self.addResonance(unit, unitTile, 0)
                    if darkTile and self.getResonance(unitTile) > -1:
                        print(f"{unit.name}'s voice overcame the darkness!")
                if self.getPower(unit, "Daggers: Add Effect: Bleed"):
                    if unit.equipment and unit.equipment.type == "Daggers":
                        self.bleedStart(target)
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
                    self.rattle(unit, target, math.ceil(target.focus * 0.75))
                    if type(target) == playerCharacter:
                        moveTo = self.battleField.getUnitPos(target) - 1
                    elif type(target) == monster:
                        moveTo = self.battleField.getUnitPos(target) + 1
                    if 0 <= moveTo <= len(self.battleField.terrainArray) - 1:
                        if (
                            len(
                                [
                                    tileUnit
                                    for tileUnit in bf.terrainArray[moveTo].units
                                    if type(tileUnit) == type(target)
                                ]
                            )
                            < 4
                        ):
                            print(f"{target.name} was routed!")
                            moveFrom = self.battleField.getUnitPos(target)
                            self.battleField.move(target, moveTo)
                            self.cleanupResonance(target)
                            self.cleanupResonance(target)
                            if not pursuitAttack:
                                if self.getPower(unit, "Rout: Pursuit Attack"):
                                    adjust = moveTo - moveFrom
                                    if (
                                        len(
                                            [
                                                tileUnit
                                                for tileUnit in bf.terrainArray[
                                                    moveTo
                                                ].units
                                                if type(tileUnit) == type(unit)
                                            ]
                                        )
                                        < 4
                                    ):
                                        self.battleField.move(
                                            unit,
                                            self.battleField.getUnitPos(unit) + adjust,
                                        )
                                        print(f"{unit.name} pursued {target.name}!")
                                        self.attack(unit, target, True)
                        else:
                            print(f"{target.name} was stunned!")
                            targetStunned = True
                            time.sleep(4.0 / 10)
                            setback = min(
                                15, math.ceil(225 / self.determineInitiative(target))
                            )
                            if target.initiativePoints < (
                                self.currentInitiative - setback
                            ):
                                setback = math.ceil(setback / 2)
                            if target.initiativePoints < (
                                self.currentInitiative - 3 * setback
                            ):
                                setback = math.floor(setback / 2)
                            target.initiativePoints -= setback
                            if target in self.turnOrder:
                                self.turnOrder.remove(target)
                            self.cleanupResonance(target)
                            self.cleanupResonance(target)
                    else:
                        print(f"{target.name} was stunned!")
                        targetStunned = True
                        time.sleep(4.0 / 10)
                        setback = min(
                            15, math.ceil(225 / self.determineInitiative(target))
                        )
                        target.initiativePoints -= setback
                        if target in self.turnOrder:
                            self.turnOrder.remove(target)
                        self.cleanupResonance(target)
                        self.cleanupResonance(target)
                if attackType == 'heavy':
                    setback = math.ceil(stamina / 2)
                    if target.initiativePoints < (self.currentInitiative - setback):
                        setback = math.ceil(setback / 2)
                    if target.initiativePoints < (self.currentInitiative - 3 * setback):
                        setback = math.floor(setback / 2)
                    target.initiativePoints -= setback
                    if target in self.turnOrder:
                        self.turnOrder.remove(target)
                if counterattack and ((i + 1) == attackCount):
                    if bf.canAttack(target) and not targetStunned:
                        bf.checkAttack(target, bf.getUnitPos(target))
                        if unit in target.allowedAttacks:
                            self.attack(target, unit)

    def battleOn(self):
        if self.game.battleStatus == 'victory':
            return False
        if self.egressing:
            self.game.battleStatus = 'egress'
            return False
        if any(
            [
                unit
                for unit in self.battleField.units
                if type(unit) == playerCharacter
                and self.getPower(unit, "Egress I")
                and unit.hp > 0
                and not (unit.status and "Petrified" in unit.status)
            ]
        ):
            if any(
                [
                    unit
                    for unit in self.battleField.units
                    if type(unit) == monster
                    and unit.hp > 0
                    and not (unit.status and "Petrified" in unit.status)
                ]
            ):
                return True
            else:
                self.game.battleStatus = 'victory'
                return False
        else:
            print("D E F E A T E D")
            print("")
            self.game.battleStatus = 'defeat'
            print("A priest managed to recall your soul from the grave.")
            print("")
            return False

    def bleed(self, unit):
        coef = round(unit.hp / unit.maxHP(), 2)
        damage = math.ceil(unit.hp * coef)
        print(f"{unit.name} bled for {min(damage, unit.hp)} damage.")
        unit.hp -= damage
        if unit.hp <= 0:
            self.kill(unit)

    def bleedStart(self, target):
        shoutOut = False
        if target.bleedTime == 0:
            shoutOut = True
        target.bleedTime = min(45, target.bleedTime + 15)
        if shoutOut:
            print("The wound begins to bleed.")

    def castAreaSpell(
        self,
        unit,
        targetId,
        spellName,
        cost,
        damage,
        area=0,
        element=None,
        spread=False,
        faith=False,
        speedUp=False,
    ):
        bf = self.battleField
        if element:
            elementWithSpace = element + " "
        else:
            elementWithSpace = None
        if self.getPower(unit, "Convert Faith and Magic"):
            unit.fp -= self.mpCost(unit, cost)
            unit.mp -= self.mpCost(unit, cost)
        else:
            if faith:
                unit.fp -= self.mpCost(unit, cost)
            else:
                unit.mp -= self.mpCost(unit, cost)
        spellTarget = unit.allowedSpells[spellName][targetId]
        if type(spellTarget) == int:
            position = spellTarget
        else:
            position = bf.terrainArray.index(spellTarget)
        print(f"{unit.name} casts {spellName}!")
        minRange = max(0, position - area)
        maxRange = min(position + area, len(bf.terrainArray) - 1)
        if spread and damage > 0:
            count = len(
                [
                    target
                    for target in [
                        tile for tile in bf.terrainArray[minRange : maxRange + 1]
                    ]
                    if type(target) != type(unit)
                ]
            )
        for i in range(minRange, maxRange + 1):
            tile = bf.terrainArray[i]
            for target in list(tile.units):
                if not self.battleField.canBeTarget(unit):
                    continue
                if damage < 0:
                    # spell is a healing spell
                    if type(target) == type(unit):
                        healing = min(abs(damage), (target.maxHP() - target.hp))
                        print(
                            f"{unit.name} restores {healing} health to {target.name}!"
                        )
                        target.hp += healing
                        if target.hp == target.maxHP():
                            if target.bleedTime > 0:
                                target.bleedTime = 0
                                print(
                                    f"{unit.name}'s magic stopped "
                                    f"{target.name}'s bleeding!"
                                )
                        self.giveExperience(unit, target, healing)
                elif damage > 0:
                    # spell is a damage spell
                    if "shielded" in target.status:
                        print(f"{target.name} was shielded from damage!")
                        target.status.remove("shielded")
                        if "shielded" not in target.status:
                            print(f"{target.name} is no longer shielded.")
                        self.giveExperience(unit, target, 1)
                    else:
                        targetDamage = damage
                        if type(target) != type(unit):
                            if spread:
                                targetDamage = math.ceil(targetDamage / count)
                            if self.getPower(target, "Defense: Magic"):
                                targetDamage = math.floor(targetDamage / 1.3)
                            if self.getPower(target, f"Defense: {element} Resistance"):
                                targetDamage = math.floor(targetDamage / 1.3)
                            if self.getPower(
                                target, f"Defense: {element} Vulnerability"
                            ):
                                targetDamage = math.ceil(targetDamage * 1.3)
                            targetDamage = min(targetDamage, target.hp)
                            print(
                                f"{unit.name} deals {targetDamage} "
                                f"{elementWithSpace}damage to "
                                f"{target.name}!"
                            )
                            target.hp -= targetDamage
                            self.giveExperience(unit, target, targetDamage)
                            if target.hp <= 0:
                                self.kill(target)
        if speedUp:
            intel = self.getStat(unit, "Intelligence")
            unit.initiativePoints += intel

    def castSingleSpell(
        self,
        unit,
        targetId,
        spellName,
        cost,
        damage,
        element=None,
        faith=False,
        speedUp=False,
    ):
        if self.getPower(unit, "Convert Faith and Magic"):
            unit.fp -= self.mpCost(unit, cost)
            unit.mp -= self.mpCost(unit, cost)
        else:
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
            if "shielded" in target.status:
                print(f"{target.name} was shielded from damage!")
                target.status.remove("shielded")
                if "shielded" not in target.status:
                    print(f"{target.name} is no longer shielded.")
                self.giveExperience(unit, target, 1)
            else:
                if self.getPower(target, "Defense: Magic"):
                    damage = math.floor(damage / 1.3)
                if self.getPower(target, f"Defense: {element} Resistance"):
                    damage = math.floor(damage / 1.3)
                if self.getPower(target, f"Defense: {element} Vulnerability"):
                    damage = math.ceil(damage * 1.3)
                damage = min(damage, target.hp)
                if element:
                    element += " "
                print(f"{unit.name} deals {damage} {element}damage to {target.name}!")
                target.hp -= damage
                self.giveExperience(unit, target, damage)
                if target.hp <= 0:
                    self.kill(target)
        if self.getPower(unit, "Sonorous Spells"):
            attackTypeArray = []
            luck = self.getStat(unit, "Luck")
            attackTypeArray.extend(["normal"] * (100 - (luck)))
            sleepChance = luck
            attackTypeArray.extend(["sleep"] * sleepChance)
            result = random.choice(attackTypeArray)
            if result == "sleep":
                target.status.append("Lulled to Sleep")
                print(f"{target.name} fell asleep!")
                # calling it twice will wipe all resonance unless the target has sustain
                self.cleanupResonance(target)
                self.cleanupResonance(target)
        if speedUp:
            intel = self.getStat(unit, "Intelligence")
            unit.initiativePoints += intel

    def castStatusSpell(
        self,
        unit,
        targetId,
        spellName,
        cost,
        statusName,
        faith=False,
        gold=False,
        stats=[],
        counterStats=["Stamina", "Faith"],
        friendly=False,
    ):
        if self.getPower(unit, "Convert Faith and Magic"):
            unit.fp -= self.mpCost(unit, cost)
            unit.mp -= self.mpCost(unit, cost)
        else:
            if faith:
                unit.fp -= self.mpCost(unit, cost)
            else:
                unit.mp -= self.mpCost(unit, cost)
        target = unit.allowedSpells[spellName][targetId]
        print(f"{unit.name} casts {spellName} on {target.name}!")
        if friendly:
            print(f"{target.name} is {statusName}!")
            target.status.append(statusName)
            target.status.append(statusName)
        else:
            # assemble chance array
            chanceArray = []
            successChance = sum(self.getStat(unit, stat) for stat in stats)
            chanceArray.extend(['success'] * successChance)
            resistChance = 0
            if "Life" in counterStats:
                resistChance += target.hp
                counterStats.remove("Life")
            resistChance += math.floor(
                sum(
                    (self.getStat(target, stat) * (self.getStat(target, "Luck") * 0.1))
                    for stat in counterStats
                )
            )
            chanceArray.extend(['fail'] * resistChance)
            result = random.choice(chanceArray)
            if result == "success":
                print(f"{target.name} is {statusName}!")
                target.status.append(statusName)
                if gold and type(unit) == playerCharacter:
                    print(
                        f"{unit.name} discovered a statue worth {target.hp} scroulings!"
                    )
                    self.game.money += target.hp
                self.giveExperience(unit, target, math.ceil(target.hp / 3))
            else:
                print(f"By sheer will, {target.name} was not {statusName}!")
                self.giveExperience(unit, target, math.ceil(target.hp / 10))

    def castSpell(self, unit, spellName, targetId):
        if spellName == "Afflict I":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 13)
                unit.mp -= self.mpCost(unit, 13)
            else:
                unit.mp -= self.mpCost(unit, 13)
            print(f"{unit.name} casts Afflict I!")
            self.castStatusSpell(
                unit,
                targetId,
                "Sleep",
                0,
                "Lulled to Sleep",
                stats=["Luck", "Intelligence"],
                counterStats=["Stamina", "Faith"],
            )
            self.castStatusSpell(
                unit,
                targetId,
                "Poison",
                0,
                "Poisoned",
                stats=["Luck", "Intelligence"],
                counterStats=["Stamina", "Faith"],
            )
            self.castStatusSpell(
                unit,
                targetId,
                "Petrify",
                0,
                "Petrified",
                stats=["Luck", "Intelligence"],
                counterStats=["Stamina", "Faith"],
            )
        elif spellName == "Aura I":
            self.castAreaSpell(unit, targetId, "Aura I", 7, -15, faith=True)
        elif spellName == "Aura II":
            self.castAreaSpell(unit, targetId, "Aura II", 11, -15, faith=True)
        elif spellName == "Aura III":
            self.castAreaSpell(unit, targetId, "Aura III", 15, -30, 1, faith=True)
        elif spellName == "Aura IV":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 20)
                unit.mp -= self.mpCost(unit, 20)
            else:
                unit.fp -= self.mpCost(unit, 20)
            print(f"{unit.name} casts {spellName}!")
            for target in self.party:
                healing = min(25, (target.maxHP() - target.hp))
                print(f"{unit.name} restores {healing} health to {target.name}!")
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
            self.castAreaSpell(unit, targetId, "Bolt II", 15, 16, 1, "Lightning")
        elif spellName == "Bolt III":
            self.castAreaSpell(unit, targetId, "Bolt III", 20, 25, 1, "Lightning")
        elif spellName == "Bolt IV":
            self.castSingleSpell(unit, targetId, "Bolt IV", 20, 72, "Lightning")
        elif spellName == "Dao I":
            self.castAreaSpell(unit, targetId, "Dao I", 8, 18, 0, "Earth", spread=True)
        elif spellName == "Dao II":
            self.castAreaSpell(
                unit, targetId, "Dao II", 15, 40, 0, "Earth", spread=True
            )
        elif spellName == "Detox I":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 3)
                unit.mp -= self.mpCost(unit, 3)
            else:
                unit.fp -= self.mpCost(unit, 3)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            if "Petrified" in target.status:
                target.initiativePoints = unit.initiativePoints - 15
            target.status = []
            print(f"{target.name} recovers!")
            self.giveExperience(unit, target, 10)
        elif spellName == "Drain I":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 5)
                unit.mp -= self.mpCost(unit, 5)
            else:
                unit.mp -= self.mpCost(unit, 5)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(10, target.hp)
            print(f"{unit.name} drains {damage} health from {target.name}!")
            if self.getPower(target, "Defense: Magic"):
                damage = math.floor(damage / 1.3)
            if self.getPower(target, "Defense: Death Resistance"):
                damage = math.floor(damage / 1.3)
            if self.getPower(target, "Defense: Death Vulnerability"):
                damage = math.ceil(damage * 1.3)
            target.hp -= damage
            unit.hp = min(unit.hp + damage, unit.maxHP())
            self.giveExperience(unit, target, damage)
            if target.hp <= 0:
                self.kill(target, unit)
        elif spellName == "Drain II":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 12)
                unit.mp -= self.mpCost(unit, 12)
            else:
                unit.mp -= self.mpCost(unit, 12)
            target = unit.allowedSpells[spellName][targetId]
            print(f"{unit.name} casts {spellName} on {target.name}!")
            damage = min(18, target.hp)
            print(f"{unit.name} drains {damage} health from {target.name}!")
            if self.getPower(target, "Defense: Magic"):
                damage = math.floor(damage / 1.3)
            if self.getPower(target, "Defense: Death Resistance"):
                damage = math.floor(damage / 1.3)
            if self.getPower(target, "Defense: Death Vulnerability"):
                damage = math.ceil(damage * 1.3)
            mdamage = min(6, target.mp)
            if self.getPower(target, "Defense: Magic"):
                mdamage = math.floor(mdamage / 1.3)
            if self.getPower(target, "Defense: Death Resistance"):
                mdamage = math.floor(mdamage / 1.3)
            if self.getPower(target, "Defense: Death Vulnerability"):
                mdamage = math.ceil(mdamage * 1.3)
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
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 8)
                unit.mp -= self.mpCost(unit, 8)
            else:
                unit.mp -= self.mpCost(unit, 8)
            print(f"{unit.name} casts {spellName}!")
            self.egressing = True
            print(
                "A whistling fills your ears as the battlefield melts "
                "into a bright light."
            )
            print(
                "The light becomes too bright to bear, and you blink to block it out."
            )
            print(
                "When you open your eyes, you are somewhere else, with a priest, safe."
            )
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
                unit,
                targetId,
                "Midas I",
                8,
                "Petrified",
                gold=True,
                stats=["Intelligence", "Dexterity", "Luck"],
                counterStats=["Stamina", "Dexterity"],
            )
        elif spellName == "Portal I":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 21)
                unit.mp -= self.mpCost(unit, 21)
            else:
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
        elif spellName == "Ninja Fire I":
            self.castAreaSpell(
                unit, targetId, "Ninja Fire I", 6, 6, 0, "Fire", speedUp=True
            )
        elif spellName == "Ninja Fire II":
            self.castAreaSpell(
                unit, targetId, "Ninja Fire II", 10, 9, 0, "Fire", speedUp=True
            )
        elif spellName == "Ninja Fire III":
            self.castSingleSpell(
                unit, targetId, "Ninja Fire III", 12, 32, "Fire", speedUp=True
            )
        elif spellName == "Shield I":
            self.castStatusSpell(
                unit, targetId, "Shield I", 12, "shielded", faith=True, friendly=True
            )
        elif spellName == "Shield II":
            self.castStatusSpell(
                unit, targetId, "Shield II", 7, "shielded", faith=True, friendly=True
            )
        elif spellName == "Sleep I":
            self.castStatusSpell(
                unit,
                targetId,
                "Sleep I",
                6,
                "Lulled to Sleep",
                stats=["Intelligence", "Charisma", "Luck"],
            )
        elif spellName == "Sleep I":
            self.castStatusSpell(
                unit,
                targetId,
                "Sleep II",
                10,
                "Lulled to Sleep",
                stats=["Intelligence", "Charisma", "Luck"],
            )
        elif spellName == "Teleport I":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 5)
                unit.mp -= self.mpCost(unit, 5)
            else:
                unit.mp -= self.mpCost(unit, 5)
            field = self.battleField
            moveFromTile = field.terrainArray[field.getUnitPos(unit)]
            moveToTile = unit.allowedSpells[spellName][targetId]
            moveFromTile.units.remove(unit)
            moveToTile.units.append(unit)
            self.giveExperience(unit, unit, 5)
        elif spellName == "Teleport II":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 10)
                unit.mp -= self.mpCost(unit, 10)
            else:
                unit.mp -= self.mpCost(unit, 10)
            field = self.battleField
            moveFromTile = field.terrainArray[field.getUnitPos(unit)]
            moveToTile = unit.allowedSpells[spellName][targetId]
            moveFromTile.units.remove(unit)
            moveToTile.units.append(unit)
            self.giveExperience(unit, unit, 10)
        elif spellName == "Teleport III":
            if self.getPower(unit, "Convert Faith and Magic"):
                unit.fp -= self.mpCost(unit, 6)
                unit.mp -= self.mpCost(unit, 6)
            else:
                unit.mp -= self.mpCost(unit, 6)
            field = self.battleField
            moveFromTile = field.terrainArray[field.getUnitPos(unit)]
            moveToTile = unit.allowedSpells[spellName][targetId]
            moveFromTile.units.remove(unit)
            moveToTile.units.append(unit)
            self.giveExperience(unit, unit, 10)

    def checkMonsterFocus(self, monster):
        if monster.focusTime > 0:
            return
        if monster.focusProfile == "Patient" and monster.focus < 3000:
            return
        if monster.focus > 750:
            if monster.focusProfile == "Aggressive":
                self.enterFocus(monster)
            elif monster.focusProfile == "Murderous":
                if any(
                    target
                    for target in monster.allowedAttacks
                    if target.hp < math.ceil(target.maxHP() / 2)
                ):
                    self.enterFocus(monster)
            elif monster.focusProfile == "Patient":
                # focus will be 3000
                self.enterFocus(monster)
            elif monster.focusProfile == "Vengeful":
                if monster.hp < monster.maxHP():
                    self.enterFocus(monster)
            else:
                print(
                    f"Error: {monster.name} called with invalid "
                    f"focusProfile: {monster.focusProfile}"
                )

    def cleanupResonance(self, unit):
        if not unit.resonating:
            return
        if not self.getPower(unit, "Vocal Attack: Sustain Effect"):
            setRes = set(unit.resonating)
            for res in setRes:
                unit.resonating.remove(res)
        unit.resonating = list(set(unit.resonating))

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
            self.getStat(unit, "Dexterity"),
        )
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
        self.checkMonsterFocus(monster)
        field = self.battleField
        if monster.attackProfile == "ChallengeAccepting":
            # will attack the highest level, charisma, strength
            candidates = [
                target
                for target in monster.allowedAttacks
                if target.level == max(unit.level for unit in monster.allowedAttacks)
            ]
            candidates = [
                target
                for target in candidates
                if self.getStat(target, "Charisma")
                == max(self.getStat(unit, "Charisma") for unit in candidates)
            ]
            candidates = [
                target
                for target in candidates
                if self.getStat(target, "Strength")
                == max(self.getStat(unit, "Strength") for unit in candidates)
            ]
            target = random.choice(candidates)
            self.attack(monster, target)
        elif monster.attackProfile == "Healer-Singer":
            # if there are targets that can be healed, heal the most damaged on
            mostDamaged = []
            mostDamage = 0
            position = field.getUnitPos(monster)
            for friend in field.unitsAtPosition(position):
                if type(friend) == type(monster):
                    friendDamage = friend.maxHP() - friend.hp
                    if friendDamage > 0:
                        if friendDamage > mostDamage:
                            mostDamaged = [friend]
                            mostDamage = friendDamage
                        elif friendDamage == mostDamage:
                            mostDamaged.append(friend)
            if mostDamaged:
                healTarget = random.choice(mostDamaged)
                monster.allowedSpells["Heal I"] = [healTarget]
                self.castSpell(monster, "Heal I", 0)
            else:
                if monster.allowedAttacks:
                    if field.checkVocal(monster):
                        self.doVocalAttack(monster)
                    else:
                        target = random.choice(monster.allowedAttacks)
                        self.attack(monster, target)
        elif monster.attackProfile == "Random":
            target = random.choice(monster.allowedAttacks)
            self.attack(monster, target)
        elif monster.attackProfile == "ScreamingBeast":
            print(f"debug: {monster.name} has {monster.focus} focus")
            if monster.focusTime == 0:
                print(f" {monster.name} sucks in a tremendous breath!")
                if monster.focus > 2525:
                    print(f" {monster.name}'s body is FULLY INFLATED!!")
                elif monster.focus > 2100:
                    print(f" Sections of {monster.name}'s body are inflating.")
                elif monster.focus > 1500:
                    print(f" Pouches on {monster.name}'s neck are inflating.")
            else:
                self.doVocalScreamAttack(monster, 0)
                monster.focusTime = 0
                monster.focus = 1500
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
                    for tile in field.terrainArray[minRange : (maxRange + 1)]:
                        targets = [
                            unit for unit in tile.units if type(unit) != type(monster)
                        ]
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
                    if any(
                        [unit for unit in tile.units if type(unit) != type(monster)]
                    ):
                        monster.allowedSpells["Freeze II"] = [position]
                        self.castSpell(monster, "Freeze II", 0)
            elif self.getPower(monster, "Freeze I"):
                if monster.mp >= self.mpCost(monster, 3):
                    canCast = True
                    position = field.getUnitPos(monster)
                    tile = field.terrainArray[position]
                    targets = [
                        target for target in tile.units if type(target) != type(monster)
                    ]
                    candidates = [
                        target
                        for target in targets
                        if target.hp == min(unit.hp for unit in targets)
                    ]
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
                    for tile in field.terrainArray[minRange : (maxRange + 1)]:
                        targets = [
                            unit for unit in tile.units if type(unit) != type(monster)
                        ]
                        if len(targets) > numTargets:
                            targetTile = tile
                            numTargets = len(targets)
                    if targetTile:
                        targetPosition = field.terrainArray.index(targetTile)
                        monster.allowedSpells["Blaze II"] = [targetPosition]
                        self.castSpell(monster, "Blaze II", 0)
            if not canCast:
                monster.attackProfile = "Random"
                self.doMonsterAttack(monster)
        elif monster.attackProfile == "Weakest":
            candidates = [
                target
                for target in monster.allowedAttacks
                if target.hp == min(unit.hp for unit in monster.allowedAttacks)
            ]
            target = random.choice(candidates)
            self.attack(monster, target)

    def doRound(self):
        idleUnits = [
            unit
            for unit in self.battleField.units
            if unit.hp > 0 and not unit.actedThisRound
        ]
        while idleUnits:
            self.turnOrder = []
            nextInitiative = max(
                [
                    unit.initiativePoints
                    for unit in self.battleField.units
                    if (
                        unit.hp > 0 and not (unit.status and "Petrified" in unit.status)
                    )
                ]
            )
            nextUnits = [
                unit
                for unit in self.battleField.units
                if unit.initiativePoints == nextInitiative and unit.hp > 0
            ]
            for unit in nextUnits:
                self.turnOrder.append(
                    (unit, unit.initiativePoints, self.getStat(unit, "Luck"))
                )
            self.turnOrder = sorted(self.turnOrder, key=itemgetter(1, 2), reverse=True)
            for entry in self.turnOrder:
                unit = entry[0]
                # unit may have died since this loop started.
                if unit.hp <= 0:
                    continue
                if not unit.actedThisRound:
                    if type(unit) == playerCharacter:
                        unit.hasEquipped = False
                    unit.movementPoints = 3 + math.ceil(self.getStat(unit, "Speed") / 2)
                else:
                    if unit.movementPoints <= 0:
                        unit.actedThisRound = True
                        # push back the unit's initiative
                        setback = min(
                            15, math.ceil(225 / self.determineInitiative(unit))
                        )
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
                    fame = round((self.getFameBonus(pc) - 1) * 100)
                    mvType = ""
                    if self.getPower(pc, "Mounted Movement"):
                        mvType = "M"
                    if pc.equipment:
                        maxFP += pc.equipment.fp
                        maxMP += pc.equipment.mp
                    print(f"It's {pc.name}'s turn! (Level {pc.level} {pc.title})")
                    currentFocusRank = self.getFocusRank(unit)
                    if currentFocusRank > unit.lastTurnFocusRank:
                        print(f"{pc.name} gained a rank of focus!")
                    unit.lastTurnFocusRank = currentFocusRank
                    print(
                        f"  (HP: {pc.hp}/{maxHP} FP: {pc.fp}/{maxFP} "
                        f"MP: {pc.mp}/{maxMP} "
                        f"Move: {pc.movementPoints}{mvType} "
                        f"Focus: {currentFocusRank} "
                        f"Fame Bonus: {fame}%)"
                    )
                    time.sleep(2.0 / 10)
                    position = self.battleField.getUnitPos(pc)
                    tile = self.battleField.terrainArray[position]
                    print(
                        f"{pc.name} is standing on ("
                        f"{self.battleField.terrainArray.index(tile)}) "
                        f"{tile.name}."
                    )
                unit.actedThisRound = True
                # push back the unit's initiative
                setback = min(15, math.ceil(225 / self.determineInitiative(unit)))
                unit.initiativePoints -= setback
                endBattle = self.doTurn(unit)
                if endBattle:
                    return
            idleUnits = [
                unit
                for unit in self.battleField.units
                if unit.hp > 0 and not unit.actedThisRound
            ]
            #  degrade the tiles now
            self.elapseTime(self.currentInitiative, nextInitiative)
            self.currentInitiative = nextInitiative
        for unit in self.battleField.units:
            unit.actedThisRound = False

    def doTurn(self, unit, moved=False, statusChecked=False, attacked=False):
        if unit.status and "Petrified" in unit.status:
            return
        position = self.battleField.getUnitPos(unit)
        tile = self.battleField.terrainArray[position]
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
            resistSkill = sum(
                [
                    self.getStat(unit, "Faith"),
                    self.getStat(unit, "Intelligence"),
                    self.getStat(unit, "Stamina"),
                ]
            )
            resistChance = math.floor(resistSkill + (resistSkill * (luck / 10)))
            if self.getPower(unit, "Defense: Increased Resistance I"):
                resistChance = math.ceil(resistChance * 1.3)
            if self.getPower(unit, "Defense: Increased Resistance II"):
                resistChance = math.ceil(resistChance * 1.3)
            if self.getPower(unit, "Unholy: Increased Resistance I"):
                if self.getResonance(tile) < 0:
                    resistChance = math.ceil(resistChance * 1.66)
            resistArray = []
            resistArray.extend(['resist'] * resistChance)
            resistArray.extend(['fail'] * (50 - (luck)))
            result = random.choice(resistArray)
            if state != "shielded":
                if result == 'resist':
                    if state == "Lulled to Sleep":
                        print(f"{unit.name} woke up!")
                    else:
                        print(f"{unit.name} recovered from being {state}!")
                    unit.status.remove(state)
                else:
                    if state == 'Poisoned':
                        print(f"{unit.name} is Poisoned!")
                        damage = math.floor(self.getStat(unit, "Stamina") * 1.5)
                        unit.hp -= damage
                        print(f"{unit.name} takes {damage} damage from the poison.")
                        if unit.hp <= 0:
                            self.kill(unit)
                    if state == 'Lulled to Sleep':
                        print(f"{unit.name} is asleep.")
                        return
            if "shielded" in state:
                state.remove("shielded")
                if "shielded" not in state:
                    print(f"{unit.name} is no longer shielded!")
            statusChecked = True
        otherUnits = ", ".join(
            [tileUnit.name for tileUnit in tile.units if tileUnit != unit]
        )
        if type(unit) == playerCharacter:
            if (
                self.getPower(unit, 'Random Additional Spell I')
                and not unit.extraPowerSlot
            ):
                unit.extraPowerSlot = self.getExtraSpell(unit, 1)
            if (
                self.getPower(unit, 'Random Additional Spell II')
                and not unit.extraPowerSlot2
            ):
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
            if attackEnabled and not attacked:
                self.battleField.printAttackString(unit)
                print("Type (A) to attack.")
                allowedCommands.append("A")
                allowedCommands.append("a")
            if not unit.hasEquipped and not moved:
                print("Type (E) to equip or unequip weapons.")
                allowedCommands.append("E")
                allowedCommands.append("e")
            if self.getFocusRank(unit) >= 1 and unit.focusTime == 0:
                print("Type (F) to enter a focused state!")
                allowedCommands.append("F")
                allowedCommands.append("f")
            spellEnabled = self.battleField.checkSpells(unit, position)
            if spellEnabled and not attacked:
                self.battleField.printSpellString(unit)
                print("Type (S) to cast a spell.")
                allowedCommands.append("S")
                allowedCommands.append("s")
            if (not moved and not attacked) or self.getPower(
                unit, "Vocal Attack: Ignore Movement"
            ):
                vocalEnabled = self.battleField.checkVocal(unit)
                if vocalEnabled:
                    print(f"Type (V) to make a vocal attack.")
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
                if unit.bleedTime > 0:
                    self.bleed(unit)
                self.doTurn(unit, True, statusChecked, attacked)
            elif command in ("A", "a"):
                attackTarget = None
                while attackTarget not in [
                    unit.allowedAttacks.index(target) for target in unit.allowedAttacks
                ]:
                    try:
                        attackTarget = int(input("Type a number to attack: "))
                    except ValueError:
                        attackTarget = None
                self.doAttack(unit, attackTarget)
                if not moved or self.getPower(unit, "Vocal Attack: Ignore Movement"):
                    darkTile = self.getResonance(tile) <= -1
                    if darkTile:
                        print(
                            f'{unit.name} shouts a few lines from the '
                            'holy song, hoping to be heard over the '
                            'unholy din.'
                        )
                    elif self.getResonance(tile) >= 1:
                        print(
                            f'{unit.name} sings along with the holy song of the Force.'
                        )
                    else:
                        print(f'{unit.name} sings out a stanza from the holy song.')
                    area = 1
                    if self.getPower(unit, "Vocal Attack: Increased Area I"):
                        area += 1
                    if self.getPower(unit, "Vocal Attack: Increased Area II"):
                        area += 1
                    self.addResonance(unit, tile, area)
                    if darkTile and self.getResonance(tile) > -1:
                        print(f"{unit.name}'s voice overcame the darkness!")
                if unit.bleedTime > 0:
                    self.bleed(unit)
                if self.getPower(unit, "Attack: Bonus Move"):
                    self.doTurn(unit, moved, statusChecked, True)
            elif command in ("C", "c"):
                print()
                unit.printCharacterSheet()
                print(f"Scroulings: {self.game.money}")
                print()
                self.doTurn(unit, moved, statusChecked)
            elif command in ("E", "e"):
                allowedEquipment = [
                    item
                    for item in self.game.inventory
                    if unit.canEquip(item) and not item.equippedBy
                ]
                itemToEquip = None
                while itemToEquip not in [
                    allowedEquipment.index(item) for item in allowedEquipment
                ] and (
                    itemToEquip
                    not in (len(allowedEquipment), len(allowedEquipment) + 1)
                ):
                    for item in allowedEquipment:
                        print(f"({allowedEquipment.index(item)}) {item.name}")
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
                    self.game.equipOnCharacter(allowedEquipment[itemToEquip], unit)
                    itemToEquip = None
                    unit.hasEquipped = True
                    if unit.fp > self.getStat(unit, "Faith") + unit.equipment.fp:
                        unit.fp = self.getStat(unit, "Faith") + unit.equipment.fp
                    if unit.mp > (
                        self.getStat(unit, "Intelligence") + unit.equipment.mp
                    ):
                        unit.mp = self.getStat(unit, "Intelligence") + unit.equipment.mp
                    print()
                self.doTurn(unit, True, statusChecked)
            elif command in ("F", "f"):
                self.enterFocus(unit)
                self.doTurn(unit, moved, statusChecked)
            elif command in ("L", "l"):
                tileChoice = None
                while tileChoice not in (
                    [
                        self.battleField.terrainArray.index(lookTile)
                        for lookTile in self.battleField.terrainArray
                    ]
                ):
                    try:
                        tileChoice = int(
                            input("Type the number of a tile to look from: ")
                        )
                    except ValueError:
                        tileChoice = None
                self.battleField.viewMap(tileChoice)
                self.doTurn(unit, moved, statusChecked)
            elif command in ("S", "s"):
                spellChoice = None
                spellTarget = None
                spellKeys = list(unit.allowedSpells.keys())
                while spellChoice not in [
                    spellKeys.index(spell) for spell in spellKeys
                ]:
                    try:
                        spellChoice = int(
                            input("Type the number of the spell to cast: ")
                        )
                    except ValueError:
                        spellChoice = None
                spellToCast = spellKeys[spellChoice]
                self.battleField.printSpellTargetString(unit, spellToCast)
                targetList = unit.allowedSpells[spellToCast]
                while targetList != 'Self' and spellTarget not in (
                    targetList.index(target) for target in targetList
                ):
                    try:
                        spellTarget = int(input("Type a number to target: "))
                    except ValueError:
                        spellTarget = None
                self.castSpell(unit, spellToCast, spellTarget)
                if unit.bleedTime > 0:
                    self.bleed(unit)
            elif command in ("V", "v"):
                self.doVocalAttack(unit)
                if unit.bleedTime > 0:
                    self.bleed(unit)
            elif command in ("W", "w"):
                if not moved or self.getPower(unit, "Vocal Attack: Ignore Movement"):
                    darkTile = self.getResonance(tile) <= -1
                    if darkTile:
                        print(
                            f'{unit.name} shouts a few lines from the '
                            'holy song, hoping to be heard over the '
                            'unholy din.'
                        )
                    elif self.getResonance(tile) >= 1:
                        print(
                            f'{unit.name} sings along with the holy song of the Force.'
                        )
                    else:
                        print(f'{unit.name} sings out a stanza from the holy song.')
                    area = 1
                    if self.getPower(unit, "Vocal Attack: Increased Area I"):
                        area += 1
                    if self.getPower(unit, "Vocal Attack: Increased Area II"):
                        area += 1
                    self.addResonance(unit, tile, area)
                    if darkTile and self.getResonance(tile) > -1:
                        print(f"{unit.name}'s voice overcame the darkness!")
                else:
                    print(f'{unit.name} waited.')
                time.sleep(6.0 / 10)
                endBattle = not self.battleOn()
                return endBattle
        elif type(unit) == monster:
            print("")
            print(f"It's {unit.name}'s turn!")
            if otherUnits:
                print(
                    f"{unit.name} is standing on ("
                    f"{self.battleField.terrainArray.index(tile)}) "
                    f"{tile.name} with {otherUnits}."
                )
            else:
                print(
                    f"{unit.name} is standing on ("
                    f"{self.battleField.terrainArray.index(tile)}) "
                    f"{tile.name}."
                )
            moveEnabled = self.battleField.checkMove(unit, position)
            if moveEnabled:
                moved = self.battleField.doMonsterMove(unit, position)
                if moved and unit.bleedTime > 0:
                    self.bleed(unit)
            position = self.battleField.getUnitPos(unit)
            attackEnabled = self.battleField.checkAttack(unit, position)
            if attackEnabled:
                self.doMonsterAttack(unit)
                if unit.bleedTime > 0:
                    self.bleed(unit)
            else:
                print(f"{unit.name} waited.")
            if self.getPower(unit, "Attack: Bonus Move"):
                moveEnabled = self.battleField.checkMove(unit, position)
                if moveEnabled:
                    moved = self.battleField.doMonsterMove(unit, position)
                    if moved and unit.bleedTime > 0:
                        self.bleed(unit)
            if not moved or self.getPower(unit, "Vocal Attack: Ignore Movement"):
                area = 1
                if self.getPower(unit, "Vocal Attack: Increased Area I"):
                    area += 1
                if self.getPower(unit, "Vocal Attack: Increased Area II"):
                    area += 1
                self.addResonance(unit, tile, area)
        self.cleanupResonance(unit)
        time.sleep(6.0 / 10)
        endBattle = not self.battleOn()
        return endBattle

    def doVocalAttack(self, unit):
        bf = self.battleField
        position = bf.getUnitPos(unit)
        tile = bf.terrainArray[position]
        print(f"{unit.name} sings out a note of power!")
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
        resonance = self.getResonance(tile)
        if type(unit) == playerCharacter:
            resonanceMult = 0.25 * (resonance + 4)
        else:
            resonanceMult = 0.25 * ((-1 * resonance) + 4)
        force = (
            max(self.getStat(unit, "Faith"), self.getStat(unit, "Voice"))
            * resonanceMult
        )
        attackType = random.choice(attackTypeArray)
        if attackType == "critical":
            print("")
            time.sleep(4.0 / 10)
            print("A Thunderous Attack!")
            print("")
            force *= 2
        self.doVocalDamage(bf, unit, tile, force)

    def doVocalScreamAttack(self, unit, penalty=0, position=None, cap=None):
        bf = self.battleField
        if position is None:
            position = bf.getUnitPos(unit)
            print(f"{unit.name} screams out an earshattering note!")
        tile = bf.terrainArray[position]
        resonance = self.getResonance(tile)
        if type(unit) == playerCharacter:
            if not cap:
                cap = resonance
            resonanceMult = min(cap, resonance) - penalty
            if resonanceMult < -3:
                print(f"{unit.name}'s scream can't be heard over the clamour!")
                return
            if resonance < 0 and resonance < cap:
                print(f"{unit.name}'s scream fades into the unholy din!")
                cap = resonance
        else:
            resonance *= -1
            if not cap:
                cap = resonance
            resonanceMult = min(cap, resonance) - penalty
            if resonanceMult < -3:
                print(f"{unit.name}'s scream is drowned out by the Holy Song!")
                return
            if resonance < 0 and resonance < cap:
                print(f"{unit.name}'s scream is weakened by the Holy Song!")
                cap = resonance
        force = math.ceil(
            max(self.getStat(unit, "Faith"), self.getStat(unit, "Voice"))
            * (resonanceMult + 4)
        )
        if force == 0:
            return
        if any(target for target in list(tile.units) if type(target) != type(unit)):
            self.doVocalDamage(bf, unit, tile, force)
            print("")
        if type(unit) == playerCharacter:
            position += 1
        else:
            position -= 1
        if 0 <= position <= len(self.battleField.terrainArray) - 1:
            self.doVocalScreamAttack(unit, penalty, position, cap)
        else:
            return

    def doVocalDamage(self, bf, unit, tile, force):
        if force < 0:
            force *= -1
        cha = self.getStat(unit, "Charisma")
        luck = self.getStat(unit, "Luck")
        voice = self.getStat(unit, "Voice")
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
                if self.getPower(unit, "Luck: Increased Rout I"):
                    routChance = math.ceil(routChance * 1.3)
                if self.getPower(unit, "Luck: Increased Rout II"):
                    routChance = math.ceil(routChance * 1.3)
                if self.getPower(unit, "Luck: Increased Rout III"):
                    routChance = math.ceil(routChance * 1.3)
                attackTypeArray.extend(["routing"] * routChance)
                attackType = random.choice(attackTypeArray)
                defense = max(
                    self.getStat(target, "Faith"), self.getStat(target, "Voice")
                )
                amount = max(1, force - defense) + math.ceil(
                    unit.skills["Holy Songs"] / 2
                )
                damage = math.ceil(amount / 4)
                damage = max(damage, 1)
                targetDamage = damage
                targetDamage = min(targetDamage, target.hp)
                print(f"The note deals {targetDamage} damage to {target.name}!")
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
                        if (
                            len(
                                [
                                    tileUnit
                                    for tileUnit in bf.terrainArray[moveTo].units
                                    if type(tileUnit) == type(target)
                                ]
                            )
                            < 4
                        ):
                            print(f"{target.name} was routed!")
                            self.battleField.move(target, moveTo)
                            self.cleanupResonance(target)
                            self.cleanupResonance(target)
                        else:
                            print(f"{target.name} was stunned!")
                            setback = min(
                                15, math.ceil(225 / self.determineInitiative(target))
                            )
                            if target.initiativePoints < (
                                self.currentInitiative - setback
                            ):
                                setback = math.ceil(setback / 2)
                            if target.initiativePoints < (
                                self.currentInitiative - 3 * setback
                            ):
                                setback = math.floor(setback / 2)
                            target.initiativePoints -= setback
                            self.cleanupResonance(target)
                            self.cleanupResonance(target)
                    else:
                        print(f"{target.name} was stunned!")
                        setback = min(
                            15, math.ceil(225 / self.determineInitiative(target))
                        )
                        if target.initiativePoints < (self.currentInitiative - setback):
                            setback = math.ceil(setback / 2)
                        if target.initiativePoints < (
                            self.currentInitiative - 3 * setback
                        ):
                            setback = math.floor(setback / 2)
                        target.initiativePoints -= setback
                        self.cleanupResonance(target)
                        self.cleanupResonance(target)
                elif attackType == "sleep":
                    target.status.append("Lulled to Sleep")
                    print(f"{target.name} fell asleep!")
                    # calling it twice will wipe all resonance unless the target has sustain
                    self.cleanupResonance(target)
                    self.cleanupResonance(target)

    def elapseTime(self, startInitiative, nextInitiative):
        timePassed = abs(nextInitiative - startInitiative)
        self.totalTimePassed += timePassed
        if timePassed <= 0:
            return
        # Do Focus changes
        for unit in self.battleField.units:
            if unit.focusTime > 0:
                unit.focusTime = max(0, unit.focusTime - (timePassed))
                if unit.focusTime == 0:
                    unit.focus = 0
                    print(f"{unit.name} is no longer focused.")
            else:
                unit.focus = min(
                    3000, unit.focus + (timePassed * self.getStat(unit, "Focus"))
                )
            if unit.bleedTime > 0:
                unit.bleedTime = max(0, unit.bleedTime - timePassed)
                if unit.bleedTime == 0:
                    print(f"{unit.name} stopped the bleeding!")

    def enterFocus(self, unit):
        oldMovementPoints = unit.movementPoints
        oldMoveSkill = 3 + math.ceil(self.getStat(unit, "Speed") / 2)
        unit.focusTime = self.getStat(unit, "Focus")
        newMoveSkill = 3 + math.ceil(self.getStat(unit, "Speed") / 2)
        unit.movementPoints = math.ceil(
            oldMovementPoints * (newMoveSkill / oldMoveSkill)
        )
        print(f"{unit.name} enters a focused state!")

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

        possibleSpells = [spell for spell in possibleSpells if spell not in unit.powers]
        if slot == 1:
            possibleSpells = [
                spell for spell in possibleSpells if spell not in unit.extraPowerSlot2
            ]
        elif slot == 2:
            possibleSpells = [
                spell for spell in possibleSpells if spell not in unit.extraPowerSlot
            ]
        spellChoice = random.choice(possibleSpells)
        if slot == 1:
            unit.extraPowerSlot = spellChoice
        if slot == 2:
            unit.extraPowerSlot2 = spellChoice
        print(f"{unit.name} learned {spellChoice}!")
        return spellChoice

    def getFameBonus(self, unit):
        return self.battleField.getFameBonus(unit)

    def getFocusRank(self, unit):
        return self.battleField.getFocusRank(unit)

    def getPower(self, unit, name):
        return self.battleField.getPower(unit, name)

    def getResonance(self, tile):
        return self.battleField.getResonance(tile)

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
                killer.fame += 1
                print(
                    f"The wicked {target.name} finally falls, slain "
                    f"by {killer.name}. {killer.name}'s name quickly "
                    "becomes a favorite tale of skalds and minstrels. "
                )
                print("You are victorious!")
                self.battleStatus = 'victory'
            else:
                self.party[0].fame += 1
                print(f"The monstrous {target.name} finally falls. You are victorious!")
                self.battleStatus = 'victory'
        del target
        time.sleep(7.0 / 10)
        return

    def mpCost(self, unit, amount):
        cost = amount
        if self.getPower(unit, "Magic: Cost Reduction I"):
            cost = math.ceil(cost * 0.75)
        return cost

    def printEstimatedValue(self, unit, equipment=None):
        bf = self.battleField
        bf.printEstimatedValue(unit, equipment)

    def rattle(self, unit, target, amount):
        currentFocusRank = self.getFocusRank(target)
        # I'm passing unit so that later I can check for powers on rattling
        focusResist = 30 * max(
            #  self.getStat(target, "Focus"),
            self.getStat(target, "Stamina"),
            self.getStat(target, "Intelligence"),
        )
        target.focus = min(target.focus, ((target.focus - amount) + focusResist))
        newFocusRank = self.getFocusRank(target)
        if newFocusRank < currentFocusRank:
            delimiter = currentFocusRank - newFocusRank
            if delimiter == 1:
                delimiter = 'a'
                rankword = 'rank'
            else:
                rankword = 'ranks'
            print(f"{unit.name} broke {delimiter} {rankword} of {target.name}'s focus!")


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
        elif self.name in ("Upward Stair", "Downward Stair", "Loose Rocks"):
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
        self.party = party
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
            # bug exists where unit may have focusTime from last battle
            pc.focusTime = 0
            luck = self.getStat(pc, "Luck")
            initiative = max(
                self.getStat(pc, "Charisma"),
                self.getStat(pc, "Speed"),
                self.getStat(pc, "Dexterity"),
            )
            initiativeOrder.append((pc, initiative, luck))
            initiativeOrder = sorted(initiativeOrder, key=itemgetter(1, 2))
            self.units.append(pc)

        characterBuffer = len(initiativeOrder)
        if characterBuffer < 5:
            for pc, _, _ in initiativeOrder:
                self.terrainArray[1].units.append(pc)
        elif characterBuffer < 9:
            for pc, _, _ in initiativeOrder[: characterBuffer - 4]:
                self.terrainArray[0].units.append(pc)
            for pc, _, _ in initiativeOrder[characterBuffer - 4 :]:
                self.terrainArray[1].units.append(pc)
        else:
            for pc, _, _ in initiativeOrder[: characterBuffer - 8]:
                self.terrainArray[0].units.append(pc)
            for pc, _, _ in initiativeOrder[characterBuffer - 8 : characterBuffer - 4]:
                self.terrainArray[1].units.append(pc)
            for pc, _, _ in initiativeOrder[characterBuffer - 4 :]:
                self.terrainArray[2].units.append(pc)

    def alliesAtPosition(self, me, position):
        return [
            unit
            for unit in self.terrainArray[position].units
            if type(unit) != type(me) and self.canBeTarget(unit) and (unit != me)
        ]

    def calculatePossibleMovement(
        self,
        unit,
        movementPoints,
        position,
        directionIsHigher,
        unstable,
        bonusSpent=False,
    ):
        tile = self.terrainArray[position]
        blocked = False
        # calculate if there is space
        if not unstable:
            unstable = tile.unstable
        if movementPoints <= 0 or (
            self.getPower(unit, "Unhindered Movement") and (movementPoints < 5)
        ):
            # mounted units may have bonus movement if they move on solids
            if (
                self.getPower(unit, "Mounted Movement")
                and not (bonusSpent)
                and not unstable
            ):
                bonusSpent = True
            else:
                return
        candidate = False
        if len(self.friendsAtPosition(unit, position, False)) < 4:
            candidate = True
        # remove movementPoints
        if self.getPower(unit, "Flying Movement") or (
            self.getPower(unit, "Unhindered Movement")
        ):
            movementPoints = movementPoints - 5
        else:
            movementPoints = movementPoints - tile.cost
        if movementPoints <= 0 or (
            self.getPower(unit, "Unhindered Movement") and (movementPoints < 5)
        ):
            # mounted units may have bonus movement if they move on solids
            if self.getPower(unit, "Mounted Movement") and not (
                self.getPower(unit, "Flying Movement")
            ):
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
                self.getPower(unit, "Unhindered Movement") and (movementPoints < 5)
            ):
                return
        else:
            if candidate:
                unit.allowedMovement.append(position)
        if not self.getPower(unit, "Movement: Ignore Enemies"):
            # calculate if we are blocked
            # flying units are easier to block but blocked by flying units only
            if self.getPower(unit, "Flying Movement"):
                if (
                    len(
                        [
                            tileUnit
                            for tileUnit in tile.units
                            if type(tileUnit) != type(unit)
                            and (
                                self.getPower(tileUnit, "Flying Movement")
                                or self.getPower(tileUnit, "Jump Attack")
                            )
                            and (self.canBlock(tileUnit))
                        ]
                    )
                    >= 1
                ):
                    blocked = True
            elif (
                len(
                    [
                        tileUnit
                        for tileUnit in tile.units
                        if type(tileUnit) != type(unit) and (self.canBlock(tileUnit))
                    ]
                )
                >= 2
            ):
                # Stealthy Movement prevents blocking for 2 tiles
                if self.getPower(unit, "Stealthy Movement") and (
                    abs(position - self.getUnitPos(unit)) <= 2
                ):
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
                        unit,
                        movementPoints,
                        position,
                        directionIsHigher,
                        unstable,
                        bonusSpent,
                    )
            else:
                position -= 1
                if position >= 0:
                    self.calculatePossibleMovement(
                        unit,
                        movementPoints,
                        position,
                        directionIsHigher,
                        unstable,
                        bonusSpent,
                    )

    def canAttack(self, unit):
        if unit.status:
            if "Petrified" in unit.status:
                return False
            if "Lulled to Sleep" in unit.status:
                return False
        return True

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
        if type(unit) == monster and unit.attackProfile == "ScreamingBeast":
            return True
        unit.allowedAttacks = []
        minRange, maxRange = self.checkRange(unit)
        if minRange == 0 and maxRange == 0:
            unit.allowedAttacks = self.enemiesAtPosition(unit, position)
            return bool(unit.allowedAttacks)
        else:
            lowRangeBottom = position - maxRange
            lowRangeTop = position - minRange
            highRangeBottom = position + minRange
            highRangeTop = position + maxRange
            tilesInRange = []
            for tile in self.terrainArray[lowRangeBottom : (lowRangeTop + 1)]:
                tilesInRange.append(tile) if tile not in tilesInRange else tilesInRange
            for tile in self.terrainArray[highRangeBottom : (highRangeTop + 1)]:
                tilesInRange.append(tile) if tile not in tilesInRange else tilesInRange
            for tile in tilesInRange:
                tilePos = self.terrainArray.index(tile)
                for tileUnit in self.enemiesAtPosition(unit, tilePos):
                    unit.allowedAttacks.append(tileUnit)
            return bool(unit.allowedAttacks)

    def checkMove(self, unit, position):
        unit.allowedMovement = []
        currentTile = self.terrainArray[position]
        unstable = currentTile.unstable
        if self.getPower(unit, "Movement: Ignore Enemies") or self.getPower(
            unit, "Stealthy Movement"
        ):
            retreatBlocked = False
            advancingBlocked = False
        else:
            # flyers are only blocked by other fliers but easier to block
            if self.getPower(unit, "Flying Movement"):
                retreatBlocked = (
                    len(
                        [
                            tileUnit
                            for tileUnit in currentTile.units
                            if type(tileUnit) != type(unit)
                            and self.getPower(tileUnit, "Flying Movement")
                            and (self.canBlock(tileUnit))
                        ]
                    )
                    >= 2
                )
                advancingBlocked = (
                    len(
                        [
                            tileUnit
                            for tileUnit in currentTile.units
                            if type(tileUnit) != type(unit)
                            and self.getPower(tileUnit, "Flying Movement")
                            and (self.canBlock(tileUnit))
                        ]
                    )
                    >= 1
                )
            else:
                retreatBlocked = (
                    len(
                        [
                            tileUnit
                            for tileUnit in currentTile.units
                            if type(tileUnit) != type(unit)
                            and (self.canBlock(tileUnit))
                        ]
                    )
                    >= 3
                )
                advancingBlocked = (
                    len(
                        [
                            tileUnit
                            for tileUnit in currentTile.units
                            if type(tileUnit) != type(unit)
                            and (self.canBlock(tileUnit))
                        ]
                    )
                    >= 2
                )
        if retreatBlocked and advancingBlocked:
            return False
        if (type(unit) == playerCharacter and not advancingBlocked) or (
            type(unit) == monster and not retreatBlocked
        ):
            calcPosition = position + 1
            if calcPosition <= len(self.terrainArray) - 1:
                self.calculatePossibleMovement(
                    unit, unit.movementPoints, calcPosition, True, unstable
                )
        if (type(unit) == playerCharacter and not retreatBlocked) or (
            type(unit) == monster and not advancingBlocked
        ):
            calcPosition = position - 1
            if calcPosition >= 0:
                self.calculatePossibleMovement(
                    unit, unit.movementPoints, calcPosition, False, unstable
                )
        if any(unit.allowedMovement):
            return True
        else:
            return False

    def checkRange(self, unit):
        if unit.equipment:
            minRange = unit.equipment.minRange
            maxRange = unit.equipment.maxRange
            if unit.equipment.type == 'Daggers':
                if self.getPower(unit, 'Daggers: Range +1'):
                    maxRange += 1
        else:
            minRange = 0
            maxRange = 0
            if self.getPower(unit, "Wind Fists: Unarmed Range and Wind"):
                maxRange += 1
        if type(unit) == monster:
            if self.getPower(unit, "Blaze II") or (self.getPower(unit, "Freeze III")):
                minRange = max(0, minRange)
                maxRange = max(1, minRange)
        return minRange, maxRange

    def checkSpell(
        self, unit, position, name, healing=False, range=0, area=0, blockingStatus=None
    ):
        if self.getPower(unit, "Healing Magic: Increased Range I"):
            if healing:
                range += 1
        minRange = max(0, (position - range))
        maxRange = min((position + range), len(self.terrainArray) - 1)
        if area == 0:
            targets = []
            for tile in self.terrainArray[minRange : (maxRange + 1)]:
                tileTargets = self.checkSpellTargets(
                    unit, tile, healing, blockingStatus
                )
                if any(tileTargets):
                    targets.extend(target for target in tileTargets)
            if any(targets):
                unit.allowedSpells[name] = targets
        elif area == 1:
            # area spells target tiles -- should they?
            targetTiles = []
            for tile in self.terrainArray[minRange : (maxRange + 1)]:
                tileTargets = self.checkSpellTargets(
                    unit, tile, healing, blockingStatus
                )
                if any(tileTargets):
                    targetTiles.append(tile)
            if any(targetTiles):
                unit.allowedSpells[name] = targetTiles
        elif area > 1:
            targets = []
            for i in range(minRange, (maxRange + 1)):
                minFocusedRange = max(0, i - (area - 1))
                maxFocusedRange = min(i + (area - 1), len(self.terrainArray - 1))
                tileTargets = []
                for tile in [
                    self.terrainArray[minFocusedRange : (maxFocusedRange + 1)]
                ]:
                    tileTargets = self.checkSpellTargets(
                        unit, tile, healing, blockingStatus
                    )
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

    def checkSpellTargets(self, unit, tile, healing, blockingStatus=None):
        position = self.terrainArray.index(tile)
        if healing:
            friends = self.friendsAtPosition(unit, position)
            return [
                friend
                for friend in friends
                if friend.hp < friend.maxHP() and (blockingStatus not in friend.status)
            ]
        else:
            return [
                enemy
                for enemy in self.enemiesAtPosition(unit, position)
                if blockingStatus not in enemy.status
            ]

    def checkSpells(self, unit, position):
        unit.allowedSpells = {}
        currentTile = self.terrainArray[position]
        if self.getPower(unit, "Afflict I") and (unit.mp >= self.mpCost(unit, 13)):
            self.checkSpell(unit, position, "Afflict I", False, 0, 0)
        if self.getPower(unit, "Aura I") and unit.fp >= self.mpCost(unit, 7):
            self.checkSpell(unit, position, "Aura I", True, 1, 1)
        if self.getPower(unit, "Aura II") and unit.fp >= self.mpCost(unit, 11):
            self.checkSpell(unit, position, "Aura II", True, 2, 2)
        if self.getPower(unit, "Aura III") and (unit.mp >= self.fpCost(unit, 15)):
            self.checkSpell(unit, position, "Aura III", True, 2, 2)
        if self.getPower(unit, "Aura IV") and unit.fp >= self.mpCost(unit, 20):
            targets = [
                target
                for target in self.party
                if target.hp > 0
                and target.hp < target.maxHP()
                and (self.canBeTarget(target))
            ]
            if any(targets):
                unit.allowedSpells["Aura IV"] = "Self"
        if self.getPower(unit, "Blaze I") and unit.mp >= self.mpCost(unit, 2):
            self.checkSpell(unit, position, "Blaze I", False, 0, 0)
        if self.getPower(unit, "Blaze II") and unit.mp >= self.mpCost(unit, 6):
            self.checkSpell(unit, position, "Blaze II", False, 1, 1)
        if self.getPower(unit, "Blaze III") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Blaze III", False, 1, 1)
        if self.getPower(unit, "Blaze IV") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Blaze IV", False, 1, 0)
        if self.getPower(unit, "Bolt I") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Bolt I", False, 0, 1)
        if self.getPower(unit, "Bolt II") and unit.mp >= self.mpCost(unit, 15):
            self.checkSpell(unit, position, "Bolt II", False, 2, 2)
        if self.getPower(unit, "Bolt III") and unit.mp >= self.mpCost(unit, 20):
            self.checkSpell(unit, position, "Bolt III", False, 2, 2)
        if self.getPower(unit, "Bolt IV") and unit.mp >= self.mpCost(unit, 20):
            self.checkSpell(unit, position, "Bolt IV", False, 2, 0)
        if self.getPower(unit, "Dao I") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Dao I", False, 1, 1)
        if self.getPower(unit, "Dao II") and unit.mp >= self.mpCost(unit, 15):
            self.checkSpell(unit, position, "Dao II", False, 1, 1)
        if self.getPower(unit, "Detox I") and unit.fp >= self.mpCost(unit, 3):
            targets = [
                target
                for target in currentTile.units
                if type(target) == type(unit) and target.status
            ]
            if any(targets):
                unit.allowedSpells["Detox I"] = targets
        if self.getPower(unit, "Drain I") and unit.mp >= self.mpCost(unit, 5):
            self.checkSpell(unit, position, "Drain I", False, 0, 0)
        if self.getPower(unit, "Drain II") and unit.mp >= self.mpCost(unit, 12):
            self.checkSpell(unit, position, "Drain II", False, 0, 0)
        if self.getPower(unit, "Egress I") and unit.mp >= self.mpCost(unit, 8):
            unit.allowedSpells["Egress I"] = 'Self'
        if self.getPower(unit, "Freeze I") and unit.mp >= self.mpCost(unit, 3):
            self.checkSpell(unit, position, "Freeze I", False, 0, 0)
        if self.getPower(unit, "Freeze II") and (unit.mp >= self.mpCost(unit, 7)):
            self.checkSpell(unit, position, "Freeze II", False, 0, 0)
        if self.getPower(unit, "Freeze III") and (unit.mp >= self.mpCost(unit, 10)):
            self.checkSpell(unit, position, "Freeze III", False, 1, 1)
        if self.getPower(unit, "Freeze IV") and (unit.mp >= self.mpCost(unit, 12)):
            self.checkSpell(unit, position, "Freeze IV", False, 2, 1)
        if self.getPower(unit, "Heal I") and unit.fp >= self.mpCost(unit, 3):
            self.checkSpell(unit, position, "Heal I", True, 0, 0)
        if self.getPower(unit, "Heal II") and unit.fp >= self.mpCost(unit, 6):
            self.checkSpell(unit, position, "Heal II", True, 1, 0)
        if self.getPower(unit, "Heal III") and (unit.fp >= self.mpCost(unit, 10)):
            self.checkSpell(unit, position, "Heal III", True, 2, 1)
        if self.getPower(unit, "Heal IV") and unit.fp >= self.mpCost(unit, 20):
            self.checkSpell(unit, position, "Heal IV", True, 0, 0)
        if self.getPower(unit, "Midas I") and unit.mp >= self.mpCost(unit, 8):
            self.checkSpell(unit, position, "Midas I", False, 0, 0)
        if self.getPower(unit, "Portal I") and (unit.mp >= self.mpCost(unit, 21)):
            targets = []
            minRange = max(0, (position - 2))
            maxRange = min((position + 2), len(self.terrainArray) - 1)
            currentTile = self.terrainArray[self.getUnitPos(unit)]
            passengers = self.friendsAtPosition(position)
            for tilePos in range(minRange, (maxRange + 1)):
                if tilePos != position:
                    if len(self.friendsAtPosition(tilePos, False)) <= (
                        4 - len(passengers)
                    ):
                        targets.extend(self.terrainArray[tilePos])
            if any(targets):
                unit.allowedSpells["Portal I"] = targets
        if self.getPower(unit, "Shield I") and (unit.fp >= self.mpCost(unit, 12)):
            self.checkSpell(unit, position, "Heal I", True, 1, 0)
        if self.getPower(unit, "Shield II") and (unit.fp >= self.mpCost(unit, 7)):
            self.checkSpell(unit, position, "Heal I", True, 1, 0)
        if self.getPower(unit, "Sleep I") and (unit.mp >= self.mpCost(unit, 6)):
            self.checkSpell(unit, position, "Sleep I", False, 1, 0, "Lulled to Sleep")
        if self.getPower(unit, "Sleep II") and (unit.mp >= self.mpCost(unit, 10)):
            self.checkSpell(unit, position, "Sleep II", False, 1, 1, "Lulled to Sleep")
        if self.getPower(unit, "Teleport I") and (unit.mp >= self.mpCost(unit, 5)):
            targets = []
            minRange = max(0, (position - 1))
            maxRange = min((position + 1), len(self.terrainArray) - 1)
            for tilePos in range(minRange, (maxRange + 1)):
                if tilePos != position:
                    if len(self.friendsAtPosition(tilePos, False)) < 4:
                        targets.append(self.terrainArray[tilePos])
            if any(targets):
                unit.allowedSpells["Teleport I"] = targets
        if self.getPower(unit, "Teleport II") and (unit.mp >= self.mpCost(unit, 10)):
            targets = []
            minRange = max(0, (position - 2))
            maxRange = min((position + 2), len(self.terrainArray) - 1)
            for tilePos in range(minRange, (maxRange + 1)):
                if tilePos != position:
                    if len(self.friendsAtPosition(position, False)) < 4:
                        targets.append(self.terrainArray[tilePos])
            if any(targets):
                unit.allowedSpells["Teleport II"] = targets
        if self.getPower(unit, "Teleport III") and (unit.mp >= self.mpCost(unit, 6)):
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
        vp = self.getResonance(currentTile)
        if (type(unit) == playerCharacter and (vp > -4)) or (
            type(unit) == monster and (vp < 4)
        ):
            return any(self.enemiesAtPosition(unit, position))

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
            maxPCs = max(
                [
                    len(self.playersAtPosition(position))
                    for position in monster.allowedMovement
                ]
            )
            if maxPCs > 0:
                for position in monster.allowedMovement:
                    if len(self.playersAtPosition(position)) == maxPCs:
                        candidates.append(position)
                if any(candidates):
                    candidates2 = []
                    maxMonsters = max(
                        [
                            len(self.monstersAtPosition(position))
                            for position in candidates
                        ]
                    )
                    for position in candidates:
                        if len(self.monstersAtPosition(position)) == (maxMonsters):
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
        elif monster.moveProfile == "Companion-Healer":
            # tends to be defensive but will move forward or back if there
            # are friendly units in those tiles
            moveTo = None
            if self.getPower(monster, "Heal I") and (
                monster.fp > self.mpCost(monster, 3)
            ):
                # set yourself up to heal, don't move if monsters hurt
                if any(
                    [
                        friend
                        for friend in self.unitsAtPosition(position)
                        if type(friend) == type(monster)
                        and (friend.hp < friend.maxHP())
                    ]
                ):
                    return False
                # otherwise look for friends nearby that are hurt
                candidates = []
                for tileIndex in monster.allowedMovement:
                    if any(
                        friend
                        for friend in self.unitsAtPosition(tileIndex)
                        if type(friend) == type(monster)
                        and (friend.hp < friend.maxHP())
                    ):
                        candidates.append(position)
                if any(candidates):
                    moveTo = random.choice(candidates)
                else:
                    for tileIndex in monster.allowedMovement:
                        if any(
                            friend
                            for friend in self.unitsAtPosition(tileIndex)
                            if type(friend) == type(monster)
                        ):
                            candidates.append(position)
                    if any(candidates):
                        moveTo = random.choice(candidates)
                if moveTo:
                    self.move(monster, moveTo)
                else:
                    return False
            else:
                monster.moveProfile = "Aggressive-Singer"
                moved = self.doMonsterMove(monster, position)
                return moved
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
                    candidate
                    for candidate in monster.allowedMovement
                    if candidate < position
                ]
                if candidates:
                    moveTo = max(candidates)
            if moveTo:
                self.move(monster, moveTo)
                return True
            else:
                return False
        elif monster.moveProfile == "Sniper":
            candidates = [
                target
                for target in self.party
                if target.hp > 0 and self.canBeTarget(target)
            ]
            candidates = [
                target
                for target in candidates
                if target.getFame() == max(unit.getFame() for unit in candidates)
            ]
            candidates = [
                target
                for target in candidates
                if target.hp == min(unit.hp for unit in candidates)
            ]
            try:
                if candidates:
                    targetPos = (
                        max([self.getUnitPos(target) for target in candidates]) + 1
                    )
                if candidates and (targetPos in monster.allowedMovement):
                    moveTo = targetPos
                else:
                    if targetPos < min(monster.allowedMovement):
                        moveTo = min(monster.allowedMovement)
                    elif targetPos > max(monster.allowedMovement):
                        moveTo = max(monster.allowedMovement)
                    else:
                        return False
            except TypeError:
                for cand in candidates:
                    print(f"debug: {cand.name}")
                print(
                    f"debug: Sniper candidate positions: "
                    + ", ".join([str(self.getUnitPos(target)) for target in candidates])
                )
            self.move(monster, moveTo)
            return True
        elif monster.moveProfile == "Stationary":
            return False

    def enemiesAtPosition(self, me, position):
        return [
            unit
            for unit in self.terrainArray[position].units
            if type(unit) != type(me) and self.canBeTarget(unit)
        ]

    def friendsAtPosition(self, me, position, filterTargets=True):
        if filterTargets:
            return [
                unit
                for unit in self.terrainArray[position].units
                if type(unit) == type(me) and self.canBeTarget(unit)
            ]
        else:
            return [
                unit
                for unit in self.terrainArray[position].units
                if type(unit) == type(me)
            ]

    def getFameBonus(self, unit):
        position = self.getUnitPos(unit)
        if not position:
            return 1
        allyFame = [ally.getFame() for ally in self.alliesAtPosition(unit, position)]
        if any(allyFame):
            return 1 + round((max(allyFame) / 100.0), 2)
        else:
            return 1

    def getFocusRank(self, unit):
        return math.floor(unit.focus / 750)

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
        if name not in ('Random Additional Spell I', 'Random Additional Spell II'):
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

    def getResonance(self, tile):
        heroes = [
            unit for unit in self.units if unit.hp > 0 and type(unit) == playerCharacter
        ]
        monsters = [
            unit for unit in self.units if unit.hp > 0 and type(unit) == monster
        ]
        heroCount = len([hero for hero in heroes if tile in hero.resonating])
        monsterCount = len(
            [monster for monster in monsters if tile in monster.resonating]
        )
        value = heroCount - monsterCount + tile.voicePower
        if value < -4:
            return -4
        else:
            return min(4, value)

    def getStat(self, unit, statName):
        #  is the unit focused?
        if unit.focusTime > 0:
            focusBonus = 1 + (self.getFocusRank(unit) * 0.25)
        else:
            focusBonus = 1
        stat = unit.stats[statName]
        stat = math.ceil(stat * self.getFameBonus(unit) * focusBonus)
        return stat

    def getUnitPos(self, unit):
        for tile in self.terrainArray:
            if unit in tile.units:
                return self.terrainArray.index(tile)

    def monstersAtPosition(self, position):
        return [
            unit
            for unit in self.terrainArray[position].units
            if type(unit) == monster and self.canBeTarget(unit)
        ]

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
            f"{self.terrainArray.index(moveToTile)}) {moveToTile.name}."
        )

    def mpCost(self, unit, amount):
        cost = amount
        if self.getPower(unit, "Magic: Cost Reduction I"):
            cost = math.ceil(cost * 0.75)
        return cost

    def playersAtPosition(self, position):
        return [
            unit
            for unit in self.terrainArray[position].units
            if type(unit) == playerCharacter and self.canBeTarget(unit)
        ]

    def printAttackString(self, unit):
        attackString = f"{unit.name} can attack "
        attackStringAdds = []
        for target in unit.allowedAttacks:
            targetHealth = target.maxHP()
            attackStringAdds.append(
                f"({unit.allowedAttacks.index(target)}) "
                f"{self.getName(unit, target)} "
                f"(HP: {target.hp}/{targetHealth})"
            )
        attackString += ", ".join(attackStringAdds)
        print(attackString + ".")

    def printEstimatedValue(self, unit, equipment=None):
        valueString = "  "
        incumbent = unit.equipment
        unitDamage = max(
            self.getStat(unit, "Strength"), self.getStat(unit, "Dexterity")
        )
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
            valueString += f"Damage: {round(fromDamage)}-->{round(toDamage)}  "
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
                    f"(HP: {target.hp}/{targetHealth})"
                )
                count += 1
            elif type(target) == battleTile:
                targetStringAdds.append(
                    f"({count}) {target.name} ({self.terrainArray.index(target)})"
                )
                count += 1
        targetString += ", ".join(targetStringAdds)
        print(targetString + ".")

    def printMoveString(self, unit):
        moveString = f"{unit.name} can move to "
        moveStringAdds = []
        unit.allowedMovement.sort()
        for position in unit.allowedMovement:
            moveStringAdds.append(f"({position}) {self.terrainArray[position].name}")
        moveString += ", ".join(moveStringAdds)
        print(moveString + ".")

    def unitsAtPosition(self, position):
        return [
            unit for unit in self.terrainArray[position].units if self.canBeTarget(unit)
        ]

    def viewMap(self, position):
        minRange = max(0, position - 3)
        maxRange = minRange + 7
        if maxRange > len(self.terrainArray) - 1:
            maxRange = len(self.terrainArray) - 1
            minRange = maxRange - 7
        tilesInRange = self.terrainArray[minRange : maxRange + 1]
        mapRow = ""
        for tile in tilesInRange:
            mapAdd = f"({self.terrainArray.index(tile)})"
            tileHeight = tile.elevation - 20
            if tileHeight > 0:
                mapAdd += f" +{tileHeight} "
            elif tileHeight < 0:
                mapAdd += f" {tileHeight} "
            resonance = self.getResonance(tile)
            if resonance > 0:
                mapAdd += f"(Holy {resonance})"
            elif resonance < 0:
                mapAdd += f"(Evil {resonance})"
            mapRow += f"{mapAdd:24}"
        print(mapRow)
        for i in range(11, -1, -1):
            mapRow = ""
            for tile in tilesInRange:
                try:
                    goodUnits = [
                        unit for unit in tile.units if type(unit) == playerCharacter
                    ]
                    goodUnits.sort(key=lambda x: x.shortName, reverse=True)
                    mapRow += f"{goodUnits[i].shortName:9}   "
                except IndexError:
                    mapRow += " " * 12
                try:
                    badUnits = [unit for unit in tile.units if type(unit) == monster]
                    badUnits.sort(key=lambda x: x.shortName, reverse=True)
                    mapRow += f"{badUnits[i].shortName:9}   "
                except IndexError:
                    mapRow += " " * 12
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
        print("Welcome to The Sword of Truth and the Holy Song of the Force!")
        self.saveName = None
        while self.saveName is None:
            self.saveName = input(
                "Enter a name for a save file or enter New for a new game: "
            )
            if self.saveName.lower() in ("n", "new"):
                self.saveName = input(
                    "Enter a name for your new save file. If a file with "
                    "that name already exists, you will overwrite it: "
                )
                self.shelf = shelve.open(f'TSOTHASOTF-{self.saveName.lower()}')
                self.playerCharacters = []
                self.shelf["playerCharacters"] = self.playerCharacters
                self.money = 0
                self.shelf["money"] = self.money
                self.inventory = []
                self.shelf["inventory"] = self.inventory
                self.maxPartySize = 12
                self.shelf["maxPartySize"] = self.maxPartySize
                self.battleNum = 1
                self.shelf["battleNum"] = self.battleNum
                self.shelf["Initialized"] = True
                self.shop = None
                self.shelf["shop"] = self.shop
                self.battleStarted = 0
                self.shelf["battleStarted"] = self.battleStarted
                self.shelf.close()
            else:
                self.shelf = shelve.open(f"TSOTHASOTF-{self.saveName.lower()}")
                if "Initialized" not in self.shelf:
                    print("A save file with that name was not found. Try again.")
                    self.shelf.close()
                    #  delete files
                    os.remove(f'TSOTHASOTF-{self.saveName.lower()}.dat')
                    os.remove(f'TSOTHASOTF-{self.saveName.lower()}.bak')
                    os.remove(f'TSOTHASOTF-{self.saveName.lower()}.dir')
                    self.saveName = None
                    continue
                self.playerCharacters = self.shelf["playerCharacters"]
                self.inventory = self.shelf["inventory"]
                self.money = self.shelf["money"]
                self.maxPartySize = self.shelf["maxPartySize"]
                self.battleNum = self.shelf["battleNum"]
                self.shop = self.shelf["shop"]
                self.battleStarted = self.shelf["battleStarted"]
                self.shelf.close()
        self.battleStatus = None
        while self.battleNum < 33:
            self.doBattle(self.battleNum)

    def doBattle(self, battleNum):
        chatter = True
        if battleNum == 1:
            print("You are the leader of a small part of misfits.")
            print("You are from Yatahal, the Holy City.")
            print(
                "Yatahal is a bastion of goodness, but the centaur Knights of Yatahal"
            )
            print("look down on all other people as unfit to participate in combat.")
            print(
                "Despite this, your mentor has assembled a small force of "
                "untrained fighters that he believes have potential."
            )
            print("Elves and Dwarves and the occaisional drummed-out Knight.")
            print(
                "You are the laughingstock of Yatahal's knights, but you "
                "believe that you are destined for greatness."
            )
            print("")
            print(
                "One day, you go out to bring supplies to the knight that "
                "guards the Ancient Sealed Door."
            )
            print(
                "When you arrive, you find that he is consorting with "
                "Goblins and plotting the downfall of Yatahal."
            )
            print("")
            print("Swallowing your fear, you draw arms and challenge them!")
            if self.battleStarted < 1:
                recruit = playerCharacter("Max", "Human", "Hero", False, 0)
                self.equipOnCharacter(
                    equipment("Swords", "Middle Sword", 250, 1, 0, 0, 5, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Lowe", "Hobbit", "Priest", False, 0)
                self.equipOnCharacter(
                    equipment("Staffs", "Wooden Staff", 80, 1, 0, 0, 1, 3, 3),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Tao", "Elf", "Flamecaster", False, 0)
                self.equipOnCharacter(
                    equipment("Staffs", "Wooden Staff", 80, 1, 0, 0, 1, 3, 3),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Luke", "Dwarf", "Warrior", False, 0)
                self.equipOnCharacter(
                    equipment("Axes", "Short Axe", 120, 1, 0, 0, 3, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Ken", "Centaur", "Knight", False, 0)
                self.equipOnCharacter(
                    equipment("Spears", "Wooden Spear", 100, 1, 0, 1, 3, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Hans", "Elf", "Archer", False, 0)
                self.equipOnCharacter(
                    equipment("Arrows", "Wooden Arrow", 150, 1, 1, 1, 3, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                self.battleStarted = 1
                self.save()
            self.party = self.playerCharacters
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(8, 'king')
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'king')
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 2:
            print("")
            print("The party arrives at a small hut overlooking the water.")
            print("There, a lonely priest lives in solitude, a penance.")
            print(
                "A Half-Giant, turned from his life of butchery to that of a holy monk,"
            )
            print("has come to bring him his supplies.")
            print("The monk, Gong, joins your cause!")
            print("")
            print("You spy a pillar of smoke rising from the direction of home.")
            print("That's not good....")
            print("")
            if self.battleStarted < 2:
                recruit = playerCharacter("Gong", "Half-Giant", "Monk", False, 1)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
                self.reckoning(25, 'lonely priest')
                self.battleStarted = 2
                self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(8, 'lonely priest')
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'lonely priest')
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 3:
            print("")
            print("The party arrives at the Holy City of Yatahal. It is burning.")
            print("Too late to intervene, you watch in horror as your mentor ")
            print("and your king are slain by a dark swordsman who looks ")
            print("exactly ;ike you. The swordsman disappears into a black void")
            print(
                "If you weren't in the room with them when this happened, you're sure "
            )
            print(
                "that the Knights of Yatahal would have posted a bounty on your head."
            )
            print("")
            print("In the aftermath of the assassination, your mentor's daughter, ")
            print("Mae, joins you! With her is a washed up former city guard, ")
            print("drunk on wine and thirsty for vengence, Gort!")
            print("")
            if self.battleStarted < 3:
                recruit = playerCharacter("Mae", "Centaur", "Knight", False, 2)
                self.playerCharacters.append(recruit)
                self.equipOnCharacter(
                    equipment("Lances", "Bronze Lance", 300, 4, 0, 0, 6, 0, 0),
                    recruit,
                    False,
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit = playerCharacter("Gort", "Dwarf", "Warrior", False, 2)
                self.playerCharacters.append(recruit)
                self.equipOnCharacter(
                    equipment("Axes", "Hand Axe", 200, 4, 0, 0, 4, 0, 0), recruit, False
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.reckoning(25, 'widow of your mentor')
                self.battleStarted = 3
                self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(8, 'widow of your mentor')
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'widow of your mentor')
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 4:
            print("")
            print("You arrive in Ulmara, a small merchant city bordering Yatahal.")
            print("The King of Ulmara greets you warmly, bestowing lavish gifts.")
            if self.battleStarted < 4:
                self.reckoning(40, "King of Ulmara")
            print("The King gestures to the shopping district: \"Go visit a smith!\"")
            print(
                "On your way to the shops, you notice a young Kyantol "
                "woman following you."
            )
            if self.battleStarted < 4:
                self.shop = shop(
                    self,
                    [
                        "Wooden Arrow",
                        "Hand Axe",
                        "Short Knife",
                        "Spear",
                        "Wooden Staff",
                        "Middle Sword",
                    ],
                    [
                        "Wooden Arrow",
                        "Hand Axe",
                        "Short Knife",
                        "Spear",
                        "Wooden Staff",
                        "Middle Sword",
                        "Middle Axe",
                        "Iron Shot",
                        "Bronze Lance",
                    ],
                    5,
                )
            self.shop.goShopping(self)
            print("")
            print(
                "As you leave the shop, the young Kyantol woman appears at your side."
            )
            print("\"Don't trust the king!\", she hisses, then spirits away.")
            print("She looked a bit wild, like a prophet.")
            print(
                "Before you can decide what to do, the king summons you to the castle."
            )
            print("There, the king reveals that he has made a deal with Darksol,")
            print("the dark wizard behind the army that destroyed Yatahal.")
            print("In exchange for keeping Ulmara safe, he is now supplying Darksol.")
            print("You are now to be sent to Darksol as more recruits.")
            print("")
            print("You refuse, so the king throws you into prison.")
            print("")
            print("")
            print("")
            print(
                "That night, a door opens in the wall of your cell and "
                "the Kyantol woman enters."
            )
            print("\"My people built this palace and the prison.\" She smirks.")
            print("\"Come with me -- we'll have to fight our way out of town.\"")
            print(
                "\"We have to go north to inform Her Majesty of her father's death.\""
            )
            print("\"I'm Khris. The priesthood is still loyal to Yatahal.\"")
            if self.battleStarted < 4:
                print("Khris joins your force!")
                recruit = playerCharacter("Khris", "Kyantol", "Priest", False, 4)
                self.equipOnCharacter(
                    equipment("Staffs", "Wooden Staff", 80, 1, 0, 0, 1, 3, 3),
                    recruit,
                    False,
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
                self.battleStarted = 4
                self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(15, 'priests')
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'priests')
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 5:
            print("")
            print("You arrive at Malanar, the Cathedral of magic.")
            print(
                "Malanar is the heart of magical and divine research and "
                "training in Yatahal, and "
            )
            print("still stands against the enemy forces.")
            print(
                "You ask to see Anri, the Princess and now the queen of "
                "Malanar and Yatahal."
            )
            print(
                "You are ushered into the court of the Ice Rose, "
                "retainers for the princess."
            )
            if self.battleStarted < 5:
                self.reckoning(30, 'the courtiers')
            print("A worried courtier directs you north, across the desert of Penance.")
            print(
                "She says that the princess is at the Chapel of Penance "
                "learning the secrets of the Songs of the Creator."
            )
            print(
                "Before you venture north, you establish a base of "
                "operations in Malanar and go shopping."
            )
            if self.battleStarted < 5:
                self.shop = shop(
                    self,
                    [
                        "Middle Sword",
                        "Spear",
                        "Bronze Lance",
                        "Wooden Staff",
                        "Power Staff",
                        "Iron Shot",
                    ],
                    [
                        "Steel Arrow",
                        "Middle Axe",
                        "Knife",
                        "Power Staff",
                        "Power Spear",
                    ],
                    8,
                )
                self.battleStarted = 5
                self.save()
            self.shop.goShopping(self)
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(15, 'the courtiers')
                    self.shop.goShopping(self)
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'the courtiers')
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 6:
            print("")
            print("You enter the chapel and immediately find the princess.")
            print(
                "You inform her that her father is dead and that she is now the Queen."
            )
            print("She turns white and orders you to take her back to Malanar at once.")
            print(
                "Once in Malanar, Anri mourns for half a day before "
                "gathering her resolve and summoning you."
            )
            if self.battleStarted < 6:
                self.reckoning(35, "new Queen")
            print(
                "Anri he informs you of her intent to join you "
                "and take the battle back to Darksol."
            )
            print("To do that, you will need to brave a dark cave under Malanar ")
            print("-- the very thing that Malanar was created to seal.")
            print("Within, she claims you will find a sacred sword.")
            if self.battleStarted < 6:
                print("Anri joins your force!")
                recruit = playerCharacter("Anri", "Human", "Wizard", False, 6)
                self.equipOnCharacter(
                    equipment("Staffs", "Power Staff", 500, 8, 0, 0, 4, 6, 6),
                    recruit,
                    False,
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
                self.battleStarted = 6
                self.save()
            print(
                "You head to the shopping district before descending into the cavern."
            )
            self.shop.goShopping(self)
            print("With that out of the way, you descend into the dark cavern.")
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(15, 'the royal coffers')
                    self.shop.goShopping(self)
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'the royal coffers')
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 7:
            print("")
            print(
                "After slaying the evil Skeleton, you find the sword "
                "buried in a sacred stone altar."
            )
            print('"It\'s the Sword of Truth." says Anri.')
            print(
                '"It\'s sacred because it give the wielder the power to '
                'see through falsehoods and illusions."'
            )
            print("You nod, gripping the Sword as you head up to the surface.")
            print("You'd better remember to equip the Sword for battle, if you can.")
            if self.battleStarted < 7:
                swordOfTruth = equipment(
                    "Sacred Swords",
                    "Sword of Truth",
                    7200,
                    1,
                    0,
                    0,
                    10,
                    0,
                    8,
                    ["Bolt I"],
                )
                self.inventory.append(swordOfTruth)
            print(
                "When you leave the cave, blinking in the sunlight over "
                "you notice a sinister sight on the outskirts of Malanar."
            )
            print(
                "Where once stood a pavilion for a traveling circus, "
                "instead stands a dark altar. Evil emanates from it, and "
                "lifeless bodies shuffle around it."
            )
            print(
                'Anri gasps. "The power of the Sword! It has dispelled an '
                'illusion! This must be Darksol\'s handiwork -- and here '
                'in the Holy City!"'
            )
            print("You steel yourself for a grueling battle. By going shopping.")
            if self.battleStarted < 7:
                self.reckoning(35, "Princess Anri")
            self.shop.goShopping(self)
            if self.battleStarted < 7:
                print("Near the altar, you meet a Knight named Arthur.")
                print(
                    "He suspects something of the illusion, and when the "
                    "power of the Sword dispels the illusion, he joins "
                    "you!"
                )
                recruit = playerCharacter("Arthur", "Centaur", "Knight", False, 4)
                self.equipOnCharacter(
                    equipment("Spears", "Spear", 150, 5, 0, 1, 5, 0, 0), recruit, False
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
                self.battleStarted = 7
                self.save()
            print(
                "Gritting your teeth, you rally the Force and head to the "
                "altar. What dark trials await?"
            )
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(15, 'the royal coffers')
                    self.shop.goShopping(self)
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'the royal coffers')
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 8:
            print("")
            print("Anri lets out a shuttering sigh, wiping the blood from her face.")
            print(
                "Once she catches her breath, she turns to you with a startling look."
            )
            print(
                '"That thing -- it was a dark creation." She says, "They '
                'should be held at bay by the words of the Holy Songs."'
            )
            print(
                '"But people have stopped singing the songs or teaching '
                'them to their children."'
            )
            print(
                '"The words of the Holy Songs are kept in a chapel to the '
                'North." She turns and points North.'
            )
            print(
                '"We need to retrieve them, now! If evil has come this '
                'close, the Holy Songs will be threatened!"'
            )
            print("With that, she gathers herself and heads North.")
            print("Unsure of what she is talking about, you follow.")
            print("")
            print(
                "When you arrive at the chapel, you are met by a group of "
                "priests, led by a tall Vicar."
            )
            if self.battleStarted < 8:
                self.reckoning(40, "the Vicar")
            print(
                'The vicar welcomes you, "The Words are kept in a warded '
                'room, that can only be opened by the Keepers, Angelic '
                'bird-men who are devoted to Heaven."'
            )
            print(
                "You watch as the Keepers remove the wards. But as soon "
                "as they do, the Vicar removes his hood and reveals "
                "himself to be Darksol!"
            )
            print(
                "He casts a dark spell, turning the Keepers to stone, "
                "then grabs the scrolls containing the words to the Songs "
                "of the Creator."
            )
            print(
                "They burst into dark blue flames as he laughs. As they "
                "burn, he disappears."
            )
            print(
                "What remains of his delegation lurches forward. The "
                "priests are dead, transformed to Zombies and Skeletons!"
            )
            if self.battleStarted < 8:
                self.battleStarted = 8
                self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(15, 'Anri')
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'Anri')
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 9:
            print("")
            print(
                "After the battle, Khris and Lowe pray for the Keepers, "
                "who are released from the stone."
            )
            print("Two of the Keepers, Amon and Balbaroy, approach you.")
            print(
                "With the scrolls containing the words to the Songs of "
                "the Creator destroyed, you need to find another source "
            )
            print("for the words.")
            print(
                "The Keepers tell you of a fortress, not build by mortal "
                "hands, which is etched with the words of the songs."
            )
            print(
                "The Fortess in indestructable, but it is also in "
                "Runefaust, far to the North, and under the sway of "
                "Darksol."
            )
            print(
                "The Keepers join you as guides and point you to the "
                "north, to the mountain land of Jaspet."
            )
            if self.battleStarted < 9:
                self.reckoning(40, 'the Keepers')
                print("Amon joins your force!")
                recruit = playerCharacter("Amon", "Birdman", "Sky Battler", False, 8)
                self.equipOnCharacter(
                    equipment("Swords", "Middle Sword", 250, 8, 0, 0, 5, 0, 0),
                    recruit,
                    False,
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
                print("Balbaroy joins your force!")
                recruit = playerCharacter(
                    "Balbaroy", "Birdman", "Sky Battler", False, 8
                )
                self.equipOnCharacter(
                    equipment("Swords", "Middle Sword", 250, 8, 0, 0, 5, 0, 0),
                    recruit,
                    False,
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
            print(
                "You head north to Jaspet, where you find that all of the "
                "men have been conscripted by Darksol!"
            )
            print(
                "An elf woman, Diane, asks you to go to the quarries "
                "the conscripts are being forced to work."
            )
            if self.battleStarted < 9:
                print("Diane joins your force!")
                recruit = playerCharacter("Diane", "Elf", "Archer", False, 8)
                self.equipOnCharacter(
                    equipment("Arrows", "Steel Arrow", 1200, 12, 1, 1, 9, 0, 0),
                    recruit,
                    False,
                )
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
                self.shop = shop(
                    self,
                    [
                        "Middle Sword",
                        "Power Spear",
                        "Bronze Lance",
                        "Middle Axe",
                        "Power Staff",
                        "Iron Shot",
                        "Steel Arrow",
                    ],
                    ["Thief's Dagger", "Power Axe", "Power Spear", "Middle Axe"],
                    12,
                )
                self.battleStarted = 9
                self.save()
            print("Before embarking on the rescue mission, you visit the local shop.")
            self.shop.goShopping(self)
            print(
                "Approaching the quarries, you hear the roar of voices "
                "chanting an evil incantation. What lies ahead?"
            )
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(15, 'the townsfolk')
                    self.shop.goShopping(self)
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'the townsfolk')
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif self.battleNum == 10:
            print("")
            print("You begin to set the men free. They tell you that they were forced ")
            print("to unearth an ancient monster, the Screaming Beast.")
            print(
                "The Screaming Beast has been brought to the North in order to unleash "
            )
            print(
                "its voice from a high point where it can destroy all of Yatahal and"
                " the "
            )
            print("surrounding lands.")
            print("")
            print(
                "Most of the workers are concerned about their lives and what will come"
                " of them."
            )
            print("One of the workers, a wolfman named Zylo, is more of man of action.")
            print(
                "He begs you to join him as he heads North to deal with the Screaming"
                " Beast."
            )
            print("")
            if self.battleStarted < 10:
                self.reckoning(40, 'the grateful townsfolk')
                print("Zylo joins your force!")
                recruit = playerCharacter("Zylo", "Wolfling", "Werewolf", False, 9)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                recruit.levelUp(False)
                self.playerCharacters.append(recruit)
            self.battleStarted = 10
            self.save()
            print("You stop back at the shop before heading off to the forest.")
            self.shop.goShopping(self)
            print(
                "You head into the forest, tracking North to find the Screaming Beast."
            )
            print(
                "Your enemies are lying in wait, seeking to prevent you from foiling"
                " their plans."
            )
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(15, 'the townsfolk')
                    self.shop.goShopping(self)
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'the townsfolk')
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif self.battleNum == 11:
            print("")
            print(
                "You come into a natural choke point: a path along the edge of the "
                "mountains."
            )
            print("Here, you find a group of mercenaries in the enemy employ.")
            print(
                "They are escorting a creature of nightmare, grey-skinned with a huge "
                "toothed smile and "
            )
            print("one red, unblinking eye, it is clearly a demon of sorts:")
            print("The Screaming Beast.")
            print("")
            print("As you approach, a shouting match breaks out in the enemy camp.")
            print("One of the mercenaries insists the the monster is an abomination.")
            print("He grabs his lance and charges towards the Beast.")
            print("The Beast opens its mouth and lets out an unholy shriek.")
            print(
                "The force of the wail is so great that the mercenary loses his feet "
                "and falls off the path, down the side of the mountain."
            )
            print("You take advantage of the chaos to enter the fight.")
            print("")
            if self.battleStarted < 11:
                self.reckoning(55, 'a plot device')
            self.battleStarted = 11
            self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != 'victory':
                if self.battleStatus == 'egress':
                    self.reckoning(25, 'the townsfolk')
                    self.shop.goShopping(self)
                elif self.battleStatus == 'defeat':
                    self.reckoning(0, 'the townsfolk')
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        else:
            print("You have won the game... for now.")
            self.battleNum = 40

    def equipItem(self, equipment):
        allowedUnits = [
            unit for unit in self.playerCharacters if unit.canEquip(equipment)
        ]
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
                    equipString += f"Damage: {currentDamage}-->{equipment.damage} "
                if equipment.fp != currentFaith:
                    equipString += f"Faith: {currentFaith}-->{equipment.fp} "
                if equipment.mp != currentMagic:
                    equipString += f"Magic: {currentMagic}-->{equipment.mp}"
                print(equipString)
            print(f"({len(allowedUnits)}) Just throw it in my bag.")
            command = None
            while command not in [allowedUnits.index(unit) for unit in allowedUnits]:
                try:
                    command = int(input("Type a number to equip the weapon: "))
                except ValueError:
                    command = None
                if command == len(allowedUnits):
                    break
            if command in [allowedUnits.index(unit) for unit in allowedUnits]:
                self.equipOnCharacter(equipment, allowedUnits[command])

    def equipOnCharacter(self, equipment, character, chatter=True):
        if type(character) == str:
            pc = [player for player in self.party if player.name == character][0]
        elif type(character) == playerCharacter:
            pc = character
        if pc:
            # does the pc already have equipment?
            if pc.equipment:
                # if so, unequip it
                incumbentEquipment = pc.equipment
                incumbentEquipment.equippedBy = None
                if incumbentEquipment not in self.inventory:
                    self.inventory.append(incumbentEquipment)
                pc.equipment = None
            # does the equipment have a current user?
            if equipment.equippedBy:
                incumbentUser = equipment.equippedBy
                incumbentUser.equipment = None
            equipment.equippedBy = pc
            pc.equipment = equipment
            if equipment not in self.inventory:
                self.inventory.append(equipment)
            if chatter:
                print(f"{pc.name} equipped the {equipment.name}.")

    def getSellPrice(self, item):
        equipString = f"Equip: {item.type}"
        blame = None
        equipable = [pc for pc in self.playerCharacters if equipString in pc.powers]
        if equipable:
            fame = max([pc.getFame() for pc in equipable])
            if fame > 15:
                blame = [
                    pc.name
                    for pc in self.playerCharacters
                    if equipString in pc.powers and pc.getFame() == fame
                ][0]
        else:
            fame = 0
        amount = math.floor(item.price * (0.1 + (fame / 100)))
        return amount, blame

    def reckoning(self, bounty, patron):
        clergyCost = sum(
            [unit.level * 10 for unit in self.playerCharacters if unit.hp <= 0]
        )
        trophies = sum([len(unit.trophies) for unit in self.playerCharacters])
        reward = trophies * bounty
        amount = reward - clergyCost
        if amount > 0:
            if clergyCost > 0:
                print(
                    f"The {patron} awards you with {amount} scroulings! "
                    "The priests recalled the souls of your party."
                )
            else:
                print(f"The {patron} awards you with {amount} scroulings!")
            self.money += amount
        elif amount < 0:
            if abs(amount) >= self.money:
                print(
                    f"The priests take all of your money to cover the "
                    f"cost of the prayers that saved you. Consider them "
                    f"generous."
                )
            else:
                print(
                    f"The priests request {-amount} scroulings for the "
                    "prayers that recalled the souls of your party."
                )
            self.money = max(0, self.money + amount)
        self.save()

    def save(self):
        self.shelf = shelve.open(f"TSOTHASOTF-{self.saveName.lower()}")
        self.shelf["playerCharacters"] = self.playerCharacters
        self.shelf["money"] = self.money
        self.shelf["inventory"] = self.inventory
        self.shelf["battleNum"] = self.battleNum
        self.shelf["shop"] = self.shop
        self.shelf["battleStarted"] = self.battleStarted
        self.shelf.close()

    def setMinSkill(self, level):
        for pc in self.playerCharacters:
            maxSkill = max(pc.skills[skill] for skill in pc.skills)
            if maxSkill < level:
                maxSkills = [
                    skill for skill in pc.skills if pc.skills[skill] == maxSkill
                ]
                if set(maxSkills) - set(["Unarmed Attack", "Holy Songs"]):
                    pc.upSkill()
                    self.setMinSkill(level)


game = game()
