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
        self.book["Assassin Tier 1 Death"] = self.power(
            game,
            "Death",
            "Assassin Tier 1 Death",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            bannedClasses=["Knight"],
            spellRank=True,
        )
        self.book["Assassin Tier 1 Sleep"] = self.power(
            game,
            "Sleep",
            "Assassin Tier 1 Sleep",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            bannedClasses=["Knight"],
            spellRank=True,
        )
        self.book["Attacking Does Not Interupt Your Singing"] = self.power(
            game,
            "Battle Song",
            "Attacking Does Not Interupt Your Singing",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
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
        self.book["Increased Fame Effect On Allies"] = self.power(
            game,
            "Charismatic Leadership",
            "Increased Fame Effect On Allies",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
        )
        self.book["Increased Terrain Advantage I"] = self.power(
            game,
            "Higher Ground",
            "Increased Terrain Advantage I",
            "Archer",
            ["Focus", "Dexterity"],
            9,
        )
        self.book["Move After Attacking"] = self.power(
            game,
            "Maneuverability",
            "Move After Attacking",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            bannedClasses=["Knight"],
        )
        self.book["Random Additional Spell I"] = self.power(
            game,
            "Mercurial Knowledge I",
            "Random Additional Spell I",
            "Alchemist",
            ["Faith", "Luck"],
            9,
        )
        self.book["Tile Resonance Increases Charisma Effects"] = self.power(
            game,
            "Bragging Verse",
            "Tile Resonance Increases Charisma Effects",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
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
        self.book["Assassin Tier 2 Death"] = self.power(
            game,
            "Death",
            "Assassin Tier 2 Death",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            5,
            [self.book["Move After Attacking"]],
            bannedClasses=["Knight"],
            spellRank=True,
        )
        self.book["Banshee Tier 2 Axe Damage"] = self.power(
            game,
            "Axe Damage",
            "Banshee Tier 2 Axe Damage",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            4,
            [self.book["Tile Resonance Increases Charisma Effects"]],
        )
        self.book["Charm Targets Instead of Routing Them"] = self.power(
            game,
            "Siren Song",
            "Charm Targets Instead of Routing Them",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            4,
            [self.book["Tile Resonance Increases Charisma Effects"]],
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
        self.book["Prevent Enemy Counterattacks"] = self.power(
            game,
            "Smoke Bomb",
            "Prevent Enemy Counterattacks",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            5,
            [self.book["Move After Attacking"]],
            bannedClasses=["Knight"],
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
        self.book["Critical Hits Inflict Silence"] = self.power(
            game,
            "Hush Hit",
            "Critical Hits Inflict Silence",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            4,
            [self.book["Assassin Tier 2 Death"]],
            [self.book["Prevent Enemy Counterattacks"]],
            bannedClasses=["Knight"],
        )
        self.book["When Focused, All Attacks Charm"] = self.power(
            game,
            "Irresistable Voice",
            "When Focused, All Attacks Charm",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            3,
            [self.book["Banshee Tier 2 Axe Damage"]],
            [self.book["Charm Targets Instead of Routing Them"]],
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
        bannedClasses=[],
        spellRank=False,
    ):
        self.name = name
