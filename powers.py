import random


class powerBook(object):
    """The dictionary containing all of the powers in the given game"""

    def __init__(self, game):
        self.book = {}
        # Tier one powers
        self.book["Alchemist Bolt Rank"] = self.power(
            game,
            "Bolt",
            "Alchemist Bolt Rank",
            "Alchemist",
            ["Faith", "Luck"],
            9,
            spellRank=True,
        )
        self.book["Archmage Tier 1 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Tier 1 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            spellRank=True,
        )
        self.book["Archmage Teleport"] = self.power(
            game,
            "Teleport",
            "Archmage Teleport",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            spellRank=True,
        )
        self.book["Archmage Root 1 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Root 1 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            spellRank=True,
        )
        self.book["Arrows: Add Effect: Poison"] = self.power(
            game,
            "Poisoned Tips",
            "Arrows: Add Effect: Poison",
            "Archer",
            ["Focus", "Dexterity"],
            9,
        )
        self.book["Begin Battle with Two Ranks of Focus"] = self.power(
            game,
            "Preparation",
            ["Begin Battle with Two Ranks of Focus"],
            "Archer",
            ["Focus", "Dexterity"],
            9,
        )
        self.book["Gain Extra Gold On Kills"] = self.power(
            game,
            "Lucre",
            "Gain Extra Gold On Kills",
            "Alchemist",
            ["Faith", "Luck"],
            9,
        )
        self.book["Increased Terrain Advantage I"] = self.power(
            game,
            "Higher Ground",
            "Increased Terrain Advantage I",
            "Archer",
            ["Focus", "Dexterity"],
            9,
        )
        self.book["Random Additional Spell I"] = self.power(
            game,
            "Mercurial Knowledge I",
            "Random Additional Spell I",
            "Alchemist",
            ["Faith", "Luck"],
            9,
        )

        # Tier two powers
        self.book["Archmage Tier 2 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Tier 2 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            8,
            [self.book["Archmage Tier 1 Bolt"]],
            spellRank=True,
        )
        self.book["Arrows: Increased Damage I"] = self.power(
            game,
            "Composite Grip",
            "Arrows: Increased Damage I",
            "Archer",
            ["Focus", "Dexterity"],
            8,
            [self.book["Arrows: Add Effect: Poison"]],
        )
        self.book["Convert Faith and Magic"] = self.power(
            game,
            "Mercurial Exchange",
            "Convert Faith and Magic",
            "Alchemist",
            ["Faith", "Luck"],
            8,
            [self.book["Random Additional Spell I"]],
        )
        self.book["Lightning Damage Breaks Focus"] = self.power(
            game,
            "Sudden Shock",
            "Lightning Damage Breaks Focus",
            "Archmage",
            ["Intelligence", "Luck"],
            8,
            [self.book["Archmage Tier 1 Bolt"]],
        )
        self.book["Random Additional Spell II"] = self.power(
            game,
            "Mercurial Knowledge II",
            "Random Additional Spell II",
            "Alchemist",
            ["Faith", "Luck"],
            8,
            [self.book["Random Additional Spell I"]],
        )
        self.book["Ranged Attacks Don't Miss"] = self.power(
            game,
            "Aimed Shot",
            "Ranged Attacks Don't Miss",
            "Archer",
            ["Focus", "Dexterity"],
            8,
            [self.book["Arrows: Add Effect: Poison"]],
        )

        # Tier three powers
        self.book["Archmage Tier 3 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Tier 2 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            7,
            [self.book["Archmage Tier 2 Bolt"]],
            [self.book["Lightning Damage Breaks Focus"]],
            spellRank=True,
        )
        self.book["Command Your Random Spells"] = self.power(
            game,
            "Mercurial Education",
            "Command Your Random Spells",
            "Alchemist",
            ["Faith", "Luck"],
            7,
            self.book["Convert Faith and Magic"],
            self.book["Random Additional Spell II"],
        )
        self.book["Arrows: Increased Range"] = self.power(
            game,
            "Far Shot",
            "Arrows: Increased Range",
            "Archer",
            ["Focus", "Dexterity"],
            7,
            [self.book["Arrows: Increased Damage I"]],
            [self.book["Ranged Attacks Don't Miss"]],
        )


class power(object):
    def __init__(
        self,
        game,
        name,
        description,
        unitClass,
        stats,
        multiplier,
        requirement1=[],
        requirement2=[],
        antiStat=[],
        bannedClass=[],
        spellRank=False,
    ):
        self.name = name
