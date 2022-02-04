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
        self.book["Axes: Extra Unarmed Attack"] = self.power(
            game,
            "Axe Punch",
            ["Axes: Extra Unarmed Attack"],
            "Berserker",
            ["Stamina", "Strength"],
            10,
            antiStat=["Luck"],
        )
        self.book["Baron Root 1 Drain On Crit"] = self.power(
            game,
            "Essence Sap",
            ["Baron Root 1 Drain On Crit"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            antiStat=["Intelligence"],
            spellRank=True,
        )
        self.book["Baron Tier 1 Drain On Crit"] = self.power(
            game,
            "Essence Sap",
            ["Baron Tier 1 Drain On Crit"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            antiStat=["Intelligence"],
            spellRank=True,
        )
        self.book["Begin Battle with Two Ranks of Focus"] = self.power(
            game,
            "Preparation",
            ["Begin Battle with Two Ranks of Focus"],
            "Archer",
            ["Focus", "Dexterity"],
            9,
        )
        self.book["Berserker Tier 1 Heavy Damage"] = self.power(
            game,
            "Heavy Damage",
            ["Berserker Tier 1 Heavy Damage"],
            "Berserker",
            ["Stamina", "Strength"],
            10,
            antiStat=["Luck"],
            spellRank=True,
        )
        self.book[
            "Berserker Tier 1 Berserking"
        ] = self.power(  # Lost Health Adds Damage
            game,
            "Berserking",
            ["Berserker Tier 1 Berserking"],
            "Berserker",
            ["Stamina", "Strength"],
            10,
            antiStat=["Luck"],
            spellRank=True,
        )
        self.book["Bishop Root 1 Aura"] = self.power(
            game,
            "Aura",
            ["Bishop Root 1 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            10,
            spellRank=True,
        )
        self.book["Bishop Tier 1 Aura"] = self.power(
            game,
            "Aura",
            ["Bishop Tier 1 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            10,
            spellRank=True,
        )
        self.book["Blood Mage Tier 1 Drain"] = self.power(
            game,
            "Drain",
            ["Blood Mage Tier 1 Drain"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            spellRank=True,
        )  # Note to self: Drain should leave targets bleeding
        self.book["Blood Mage Tier 1 Muddle"] = self.power(
            game,
            "Muddle",
            ["Blood Mage Tier 1 Muddle"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            spellRank=True,
        )
        self.book["Chance to Return from the Dead Each Turn"] = self.power(
            game,
            "Overcome the Grave",
            ["Chance to Return from the Dead Each Turn"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            antiStat=["Intelligence"],
        )
        self.book["Command: Fill Focus If An Ally Dies On Your Tile"] = self.power(
            game,
            "Aura",
            ["Command: Fill Focus If An Ally Dies On Your Tile"],
            "Bishop",
            ["Faith", "Focus"],
            10,
        )
        self.book["Command: MP Regeneration"] = self.power(
            game,
            "Bardic Command",
            ["Command: MP Regeneration"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
        )
        self.book["Daggers Give Extra MP"] = self.power(
            game,
            "Ritual Blades",
            ["Daggers Give Extra MP"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
        )
        self.book["Gain Extra Gold On Kills"] = self.power(
            game,
            "Lucre",
            "Gain Extra Gold On Kills",
            "Alchemist",
            ["Faith", "Luck"],
            9,
        )
        self.book["Increases Fame Effect On Allies"] = self.power(
            game,
            "Charismatic Leadership",
            "Increases Fame Effect On Allies",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
        )
        self.book["Increases Critical Chance"] = self.power(
            game,
            "Bardic Luck",
            ["Increases Critical Chance"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
        )
        self.book["Increases Terrain Advantage I"] = self.power(
            game,
            "Higher Ground",
            "Increases Terrain Advantage I",
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
        self.book["Ranged Attacks Add Resonance to Target's Tile"] = self.power(
            game,
            "Whistling Shots",
            ["Ranged Attacks Add Resonance to Target's Tile"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
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
        self.book["Arrows: Increases Damage I"] = self.power(
            game,
            "Composite Grip",
            "Arrows: Increases Damage I",
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
        self.book["Attack Each Enemy In Range On Death"] = self.power(
            game,
            "Final Stand",
            ["Attack Each Enemy In Range On Death"],
            "Berserker",
            ["Stamina", "Strength"],
            9,
            [self.book["Berserker Tier 1 Berserking"]],
            antiStat=["Luck"],
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
        self.book["Bishop Tier 2 Aura"] = self.power(
            game,
            "Aura",
            ["Bishop Tier 2 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            9,
            [self.book["Bishop Root 1 Aura"]],
            spellRank=True,
        )
        self.book["Bleeding Enemies Heal You"] = self.power(
            game,
            "Vampiric Thirst",
            ["Bleeding Enemies Heal You"],
            "Baron",
            ["Charisma", "Strength"],
            9,
            [self.book["Baron Root 1 Drain On Crit"]],
            antiStat=["Intelligence"],
        )
        self.book["Bleeding Enemies Give MP"] = self.power(
            game,
            "Essence",
            ["Bleeding Enemies Give MP"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            7,
            [self.book["Blood Mage Tier 1 Drain"]],
            spellRank=True,
        )
        self.book["Blood Mage Tier 2 Essence"] = self.power(
            game,
            "Essence",
            ["Blood Mage Tier 2 Essence"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            7,
            [self.book["Blood Mage Tier 1 Drain"]],
            spellRank=True,
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
        self.book["Command: Casting Does Not Interupt Your Singing"] = self.power(
            game,
            "Melodious Spellweaving",
            ["Command: Casting Does Not Interupt Your Singing"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            6,
            [self.book["Command: MP Regeneration"]],
        )
        self.book["Critical Hits Reduce Next Spell Cost to 0"] = self.power(
            game,
            "Stroke of Luck",
            ["Critical Hits Reduce Next Spell Cost to 0"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            6,
            [self.book["Command: MP Regeneration"]],
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
        self.book["Lost Health Increases Turn Speed"] = self.power(
            game,
            "Tunnel Vision",
            ["Lost Health Increases Turn Speed"],
            "Berserker",
            ["Stamina", "Strength"],
            9,
            [self.book["Berserker Tier 1 Berserking"]],
            antiStat=["Luck"],
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
        self.book["When Focused, All Area Spells Have Double Power"] = self.power(
            game,
            "Fervent Prayer",
            ["When Focused, All Area Spells Have Double Power"],
            "Bishop",
            ["Faith", "Focus"],
            9,
            [self.book["Bishop Root 1 Aura"]],
        )
        self.book["Your Bleeding Heals Allies On Your Tile"] = self.power(
            game,
            "Sanguine Bond",
            ["Your Bleeding Heals Allies On Your Tile"],
            "Baron",
            ["Charisma", "Strength"],
            9,
            [self.book["Baron Root 1 Drain On Crit"]],
            antiStat=["Intelligence"],
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
        self.book["Add the Command Keyword to All Your Powers"] = self.power(
            game,
            "Bardic Leadership",
            ["Add the Command Keyword to All Your Powers"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            5,
            [self.book["Command: Casting Does Not Interupt Your Singing"]],
            [self.book["Critical Hits Reduce Next Spell Cost to 0"]],
        )
        self.book["Arrows: Increases Range"] = self.power(
            game,
            "Far Shot",
            "Arrows: Increases Range",
            "Archer",
            ["Focus", "Dexterity"],
            7,
            [self.book["Arrows: Increases Damage I"]],
            [self.book["Ranged Attacks Don't Miss"]],
        )
        self.book["Berserker Tier 3 Berserking"] = self.power(
            game,
            "Berserking",
            ["Berserker Tier 3 Berserking"],
            "Berserker",
            ["Stamina", "Strength"],
            8,
            [self.book["Attack Each Enemy In Range On Death"]],
            [self.book["Lost Health Increases Turn Speed"]],
            antiStat=["Luck"],
            spellRank=True,
        )
        self.book["Bishop Tier 3 Aura"] = self.power(
            game,
            "Aura",
            ["Bishop Tier 3 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            8,
            [self.book["Bishop Tier 2 Aura"]],
            [self.book["When Focused, All Area Spells Have Double Power"]],
            spellRank=True,
        )
        self.book["Blood Mage Tier 3 Drain"] = self.power(
            game,
            "Drain",
            ["Blood Mage Tier 3 Drain"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            6,
            [self.book["Bleeding Enemies Give MP"]],
            [self.book["Blood Mage Tier 2 Essence"]],
            spellRank=True,
        )
        self.book["Command: Counterattacks"] = self.power(
            game,
            "Vampiric Command",
            ["Command: Counterattacks"],
            "Baron",
            ["Charisma", "Strength"],
            8,
            [self.book["Bleeding Enemies Heal You"]],
            [self.book["Your Bleeding Heals Allies On Your Tile"]],
            antiStat=["Intelligence"],
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

        # Cross-over powers


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
