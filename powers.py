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
        self.book["Archmage Tier 1 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Tier 1 Bolt",
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
        self.book["Catechumen Tier 1 Vocal Cascade"] = self.power(
            game,
            "Cascade",
            "Catechumen Tier 1 Vocal Cascade",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
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
        self.book["Channeller Root 1 Surge"] = self.power(
            game,
            "Surge",
            "Channeller Root 1 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            spellRank=True,
        )
        self.book["Channeller Root 2 Surge"] = self.power(
            game,
            "Surge",
            "Channeller Root 2 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            spellRank=True,
        )
        self.book["Channeller Tier 1 Surge"] = self.power(
            game,
            "Surge",
            "Channeller Tier 1 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            spellRank=True,
        )
        self.book["Command: Fill Focus If An Ally Dies On Your Tile"] = self.power(
            game,
            "Solemn Vow",
            ["Command: Fill Focus If An Ally Dies On Your Tile"],
            "Bishop",
            ["Faith", "Focus"],
            10,
        )
        self.book[
            "Command: Increase Focus Generation on Fully Holy Tiles"
        ] = self.power(
            game,
            "Sacred Dance",
            "Command: Increase Focus Generation on Fully Holy Tiles",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
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
        self.book["Dark Mage Tier 1 Blaze"] = self.power(
            game,
            "Blaze",
            "Dark Mage Tier 1 Blaze",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            spellRank=True,
        )
        self.book["Dark Mage Tier 1 Freeze"] = self.power(
            game,
            "Freeze",
            "Dark Mage Tier 1 Freeze",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            spellRank=True,
        )
        self.book["Defense Against Magic Damage"] = self.power(
            game,
            "Magical Defense",
            "Defense Against Magic Damage",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
        )
        self.book["Defense Against Ranged Physical Damage"] = self.power(
            game,
            "Projectile Defense",
            "Defense Against Ranged Physical Damage",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            7,
        )
        self.book["Defense Against Sword Damage"] = self.power(
            game,
            "Sword Defense",
            "Defense Against Sword Damage",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            antiStat=["Faith"],
        )
        self.book["Dodging Grants and Spends One Charge Of Focus"] = self.power(
            game,
            "Flash Step",
            ["Dodging Grants and Spends One Charge Of Focus"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            7,
        )
        self.book["Druid Tier 1 Blast"] = self.power(
            game,
            "Natural Resistance",
            "Druid Tier 1 Blast",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            spellRank=True,
        )
        self.book["Druid Tier 1 Natural Resistance"] = self.power(
            game,
            "Natural Resistance",
            "Druid Tier 1 Natural Resistance",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            spellRank=True,
        )
        self.book["Duelist Counterattack"] = self.power(
            game,
            "Counterattack",
            "Duelist Counterattack",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            antiStat=["Faith"],
        )
        self.book["Flamecaster Root 1 Blaze"] = self.power(
            game,
            "Blaze",
            "Flamecaster Root 1 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            spellRank=True,
        )
        self.book["Flamecaster Tier 1 Blaze"] = self.power(
            game,
            "Blaze",
            "Flamecaster Tier 1 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            spellRank=True,
        )
        self.book["Gain Extra Gold On Kills"] = self.power(
            game,
            "Lucre",
            "Gain Extra Gold On Kills",
            "Alchemist",
            ["Faith", "Luck"],
            9,
        )
        self.book["Hero Counterattack"] = self.power(
            game,
            "Counterattack",
            "Hero Counterattack",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            7,
            antiPower=[self.book["Duelist Counterattack"]],
            spellRank=True,
        )
        self.book["Duelist Counterattack"].antiPower = self.book["Hero Counterattack"]
        self.book["Hero Root 1 Egress"] = self.power(
            game,
            "Egress",
            "Hero Root 1 Egress",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            7,
            spellRank=True,
        )
        self.book["Hero Tier 1 Bolt"] = self.power(
            game,
            "Bolt",
            "Hero Tier 1 Bolt",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            7,
            spellRank=True,
        )
        self.book["Ignore Opponents on First Two Tiles of Movement"] = self.power(
            game,
            "Stealthy Movement",
            "Ignore Opponents on First Two Tiles of Movement",
            "Druid",
            ["Dexterity", "Faith"],
            9,
        )
        self.book["Increases Critical Chance"] = self.power(
            game,
            "Bardic Luck",
            ["Increases Critical Chance"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
        )
        self.book["Increases Critical Hit Damage"] = self.power(
            game,
            "Explosives",
            "Increases Critical Hit Damage",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            7,
        )
        self.book["Increases Dodge Chance"] = self.power(
            game,
            "Dodge Roll",
            ["Increases Dodge Chance"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            7,
        )
        self.book["Increases Fame Effect On Allies"] = self.power(
            game,
            "Charismatic Leadership",
            "Increases Fame Effect On Allies",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
        )
        self.book["Increases Luck When Outnumbered"] = self.power(
            game,
            "Never Tell Me The Odds",
            ["Increases Luck When Outnumbered"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            7,
        )
        self.book[
            "Increases Special Attack Chance When Sword Is Equipped"
        ] = self.power(
            game,
            "Fencing Skill",
            "Increases Special Attack Chance When Sword Is Equipped",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            antiStat=["Faith"],
        )
        self.book["Increases Terrain Advantage I"] = self.power(
            game,
            "Higher Ground",
            "Increases Terrain Advantage I",
            "Archer",
            ["Focus", "Dexterity"],
            9,
        )
        self.book["Magic Cost Reduction"] = self.power(
            game,
            "Arcane Efficiency",
            "Magic Cost Reduction",
            "Flamecaster",
            ["Charisma", "Intelligence"],
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
        self.book["Move Faster On Holy Ground"] = self.power(
            game,
            "Beautiful Strides",
            "Move Faster On Holy Ground",
            "Catachumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
        )
        self.book["Movement Does Not Interupt Your Singing"] = self.power(
            game,
            "Rhythmic Chanting",
            "Movement Does Not Interupt Your Singing",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
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
        self.book["Regenerate Health On Holy Ground"] = self.power(
            game,
            "Sustenance",
            "Regenerate Health On Holy Ground",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
        )
        self.book[
            "Slower Movement That Ignores Terrain Cost And Blockers"
        ] = self.power(
            game,
            "Unhindered Movement",
            "Slower Movement That Ignores Terrain Cost And Blockers",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
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
        self.book["Vocal Attacks Have A Chance To Add Bleed"] = self.power(
            game,
            "Piercing Screams",
            "Vocal Attacks Have A Chance To Add Bleed",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
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
        self.book["Attacks Are Always Heavy When Your Health Is Full"] = self.power(
            game,
            "Unhindered Movement",
            "Attacks Are Always Heavy When Your Health Is Full",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            6,
            [self.book["Slower Movement That Ignores Terrain Cost And Blockers"]],
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
            [self.book["Bishop Tier 1 Aura"]],
            spellRank=True,
        )
        self.book["Bleeding Enemies Heal You"] = self.power(
            game,
            "Vampiric Thirst",
            ["Bleeding Enemies Heal You"],
            "Baron",
            ["Charisma", "Strength"],
            9,
            [self.book["Baron Tier 1 Drain On Crit"]],
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
        self.book["Channeller Tier 2 Silence"] = self.power(
            game,
            "Silence",
            "Channeller Tier 2 Silence",
            "Channeller",
            ["Dexterity", "Intelligence"],
            8,
            [self.book["Channeller Tier 1 Surge"]],
            spellRank=True,
        )
        self.book["Channeller Tier 2 Surge"] = self.power(
            game,
            "Surge",
            "Channeller Tier 2 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            8,
            [self.book["Channeller Tier 1 Surge"]],
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
        self.book["Counter Enemy Vocal Attacks With Bleed"] = self.power(
            game,
            "Lacerating Response",
            "Counter Enemy Vocal Attacks With Bleed",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            6,
            [self.book["Vocal Attacks Have A Chance To Add Bleed"]],
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
        self.book["Dark Mage Tier 2 Death"] = self.power(
            game,
            "Death",
            "Dark Mage Tier 2 Death",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            8,
            [self.book["Defense Against Magic Damage"]],
            spellRank=True,
        )
        self.book["Dark Mage Tier 2 Silence"] = self.power(
            game,
            "Silence",
            "Dark Mage Tier 2 Silence",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            8,
            [self.book["Defense Against Magic Damage"]],
            spellRank=True,
        )
        self.book["Dodge Attacks That You Counter"] = self.power(
            game,
            "Parry",
            "Dodge Attacks That You Counter",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            6,
            [self.book["Duelist Counterattack"]],
            antiStat=["Faith"],
        )
        self.book["Dodging Grants Focus Charge"] = self.power(
            game,
            "Adrenaline Rush",
            ["Dodging Grants Focus Charge"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            6,
            [self.book["Increases Luck When Outnumbered"]],
        )
        self.book["Double Rout Chance Against Bleeding Targets"] = self.power(
            game,
            "Blood Cries Out",
            "Double Rout Chance Against Bleeding Targets",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            6,
            [self.book["Vocal Attacks Have A Chance To Add Bleed"]],
        )
        self.book["Druid Tier 2 Conduit"] = self.power(
            game,
            "Conduit",
            "Druid Tier 2 Conduit",
            "Druid",
            ["Dexterity", "Faith"],
            8,
            [self.book["Druid Tier 1 Natural Resistance"]],
            spellRank=True,
        )
        self.book["Druid Tier 2 Detox"] = self.power(
            game,
            "Detox",
            "Druid Tier 2 Detox",
            "Druid",
            ["Dexterity", "Faith"],
            8,
            [self.book["Druid Tier 1 Natural Resistance"]],
            spellRank=True,
        )
        self.book["Fire Damage Consumes Bleed To Deal Double Damage"] = self.power(
            game,
            "Cauterize",
            "Fire Damage Consumes Bleed To Deal Double Damage",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            8,
            [self.book["Flamecaster Tier 1 Blaze"]],
        )
        self.book["Flamecaster Tier 2 Blaze"] = self.power(
            game,
            "Blaze",
            "Flamecaster Tier 2 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            8,
            [self.book["Flamecaster Tier 1 Blaze"]],
            spellRank=True,
        )
        self.book["Hero Tier 2 Bolt"] = self.power(
            game,
            "Bolt",
            "Hero Tier 2 Bolt",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            6,
            [self.book["Hero Tier 1 Bolt"]],
            spellRank=True,
        )
        self.book["Killing Enemies Gives MP"] = self.power(
            game,
            "Destiny Unveiled",
            "Killing Enemies Gives MP",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            6,
            [self.book["Hero Tier 1 Bolt"]],
        )
        self.book["Increases Focus When Outnumbered"] = self.power(
            game,
            "Against All Odds",
            ["Increases Focus When Outnumbered"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            6,
            [self.book["Increases Luck When Outnumbered"]],
        )
        self.book["Increases Focus When Stationary"] = self.power(
            game,
            "Unhindered Movement",
            "Increases Focus When Stationary",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            6,
            [self.book["Slower Movement That Ignores Terrain Cost And Blockers"]],
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
            [self.book["Bishop Tier 1 Aura"]],
        )
        self.book["Vocal Cascade With Weapons"] = self.power(
            game,
            "Santified Movements",
            "Vocal Cascade With Weapons",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            5,
            [self.book["Catechumen Tier 1 Vocal Cascade"]],
        )
        self.book["Vocal Cascade Without Full Holy Resonance"] = self.power(
            game,
            "Indwelling Echoes",
            "Vocal Cascade Without Full Holy Resonance",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            5,
            [self.book["Catechumen Tier 1 Vocal Cascade"]],
        )
        self.book["Your Bleeding Heals Allies On Your Tile"] = self.power(
            game,
            "Sanguine Bond",
            ["Your Bleeding Heals Allies On Your Tile"],
            "Baron",
            ["Charisma", "Strength"],
            9,
            [self.book["Baron Tier 1 Drain On Crit"]],
            antiStat=["Intelligence"],
        )
        self.book[
            "Your Counterattacks Resolve Before The Attacks That Trigger Them"
        ] = self.power(
            game,
            "Flash Strike",
            "Your Counterattacks Resolve Before The Attacks That Trigger Them",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            6,
            [self.book["Duelist Counterattack"]],
            antiStat=["Faith"],
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
        self.book["Catechumen Tier 3 Vocal Cascade"] = self.power(
            game,
            "Cascade",
            "Catechumen Tier 3 Vocal Cascade",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            [self.book["Vocal Cascade With Weapons"]],
            [self.book["Vocal Cascade Without Full Holy Resonance"]],
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
            "Hush Up",
            "Critical Hits Inflict Silence",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            4,
            [self.book["Assassin Tier 2 Death"]],
            [self.book["Prevent Enemy Counterattacks"]],
            bannedClasses=["Knight"],
        )
        self.book["Dark Mage Tier 3 Death"] = self.power(
            game,
            "Death",
            "Dark Mage Tier 3 Death",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            7,
            [self.book["Dark Mage Tier 2 Death"]],
            [self.book["Dark Mage Tier 2 Silence"]],
            spellRank=True,
        )
        self.book["Druid Tier 3 Natural Resistance"] = self.power(
            game,
            "Natural Resistance",
            "Druid Tier 2 Natural Resistance",
            "Druid",
            ["Dexterity", "Faith"],
            7,
            [self.book["Druid Tier 2 Conduit"]],
            [self.book["Druid Tier 2 Detox"]],
            spellRank=True,
        )
        self.book["Enemy Sword Users Must Attack You If Possible"] = self.power(
            game,
            "Duelist's Challenge",
            "Enemy Sword Users Must Attack You If Possible",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            5,
            [self.book["Dodge Attacks That You Counter"]],
            [
                self.book[
                    "Your Counterattacks Resolve Before The Attacks That Trigger Them"
                ]
            ],
            antiStat=["Faith"],
        )
        self.book["Flamecaster Tier 3 Blaze"] = self.power(
            game,
            "Blaze",
            "Flamecaster Tier 3 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            7,
            [self.book["Flamecaster Tier 2 Blaze"]],
            [self.book["Fire Damage Consumes Bleed To Deal Double Damage"]],
            spellRank=True,
        )
        self.book["Hero Tier 3 Bolt"] = self.power(
            game,
            "Bolt",
            "Hero Tier 3 Bolt",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            5,
            [self.book["Hero Tier 2 Bolt"]],
            [self.book["Killing Enemies Gives MP"]],
            spellRank=True,
        )
        self.book["Reduces Minimum Attack Range By 1"] = self.power(
            game,
            "Unhindered Movement",
            "Reduces Minimum Attack Range By 1",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            5,
            [self.book["Attacks Are Always Heavy When Your Health Is Full"]],
            [self.book["Increases Focus When Stationary"]],
        )
        self.book["Routing Adds Silence"] = self.power(
            game,
            "Deafening Fear",
            "Routing Adds Silence",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            5,
            [self.book["Double Rout Chance Against Bleeding Targets"]],
            [self.book["Counter Enemy Vocal Attacks With Bleed"]],
        )
        self.book["Silence Enemies Who Cast A Spell That You Know On You"] = self.power(
            game,
            "Counterspell",
            "Silence Enemies Who Cast A Spell That You Know On You",
            "Channeller",
            ["Dexterity", "Intelligence"],
            7,
            [self.book["Channeller Tier 2 Surge"]],
            [self.book["Channeller Tier 2 Silence"]],
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
        self.book["When Focused, You Cannot Be Reduced Below 1 HP"] = self.power(
            game,
            "Die Hard",
            ["When Focused, You Cannot Be Reduced Below 1 HP"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            5,
            [self.book["Dodging Grants Focus Charge"]],
            [self.book["Increases Focus When Outnumbered"]],
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
        antiPower=[],
        antiStat=[],
        bannedClasses=[],
        descriptionOverride=None,
        minimumLevel=None,
        spellRank=False,
    ):
        self.name = name
        if not self.descriptionOverride:
            descriptionOverride = description
