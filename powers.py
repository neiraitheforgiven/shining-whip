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
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Archmage Teleport"] = self.power(
            game,
            "Teleport",
            "Archmage Teleport",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Archmage Root 1 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Root 1 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Archmage Tier 1 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Tier 1 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Arrows: Add Effect: Poison"] = self.power(
            game,
            "Poisoned Tips",
            "Arrows: Add Effect: Poison",
            "Archer",
            ["Focus", "Dexterity"],
            9,
            "Arrows Skill",
        )
        self.book["Assassin Tier 1 Death"] = self.power(
            game,
            "Death",
            "Assassin Tier 1 Death",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            "Status Effectiveness",
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
            "Status Effectiveness",
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
            "Vocal Strength",
        )
        self.book["Attacks Change Type To Match Vulnerabilities"] = self.power(
            game,
            "Suffering",
            "Attacks Change Type To Match Vulnerabilities",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            7,
            "Damage vs Vulnerability",
        )
        self.book["Axes: Extra Unarmed Attack"] = self.power(
            game,
            "Axe Punch",
            ["Axes: Extra Unarmed Attack"],
            "Berserker",
            ["Stamina", "Strength"],
            10,
            "Axe Skill",
            antiStat=["Luck"],
        )
        self.book["Baron Root 1 Drain On Crit"] = self.power(
            game,
            "Essence Sap",
            ["Baron Root 1 Drain On Crit"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            "Drained Health",
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
            "Drained Health",
            antiStat=["Intelligence"],
            spellRank=True,
        )
        self.book["Begin Battle with Two Ranks of Focus"] = self.power(
            game,
            "Preparation",
            ["Begin Battle with Two Ranks of Focus"],
            "Archer",
            "Focus Intensity",
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
            "Heavy Damage Chance",
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
            "Heavy Damage Chance",
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
            "Healing Amount",
            spellRank=True,
        )
        self.book["Bishop Tier 1 Aura"] = self.power(
            game,
            "Aura",
            ["Bishop Tier 1 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            10,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Blood Mage Tier 1 Drain"] = self.power(
            game,
            "Drain",
            ["Blood Mage Tier 1 Drain"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            "Drained Health",
            spellRank=True,
        )  # Note to self: Drain should leave targets bleeding
        self.book["Blood Mage Tier 1 Muddle"] = self.power(
            game,
            "Muddle",
            ["Blood Mage Tier 1 Muddle"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Catechumen Tier 1 Vocal Cascade"] = self.power(
            game,
            "Cascade",
            "Catechumen Tier 1 Vocal Cascade",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            "Vocal Strength",
            spellRank=True,
        )
        self.book["Chance to Return from the Dead Each Turn"] = self.power(
            game,
            "Overcome the Grave",
            ["Chance to Return from the Dead Each Turn"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            "Luckiness",
            antiStat=["Intelligence"],
        )
        self.book["Channeller Root 1 Surge"] = self.power(
            game,
            "Surge",
            "Channeller Root 1 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            "Water Damage",
            spellRank=True,
        )
        self.book["Channeller Root 2 Surge"] = self.power(
            game,
            "Surge",
            "Channeller Root 2 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            "Water Damage",
            spellRank=True,
        )
        self.book["Channeller Tier 1 Surge"] = self.power(
            game,
            "Surge",
            "Channeller Tier 1 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            "Water Damage",
            spellRank=True,
        )
        self.book["Command: Fill Focus If An Ally Dies On Your Tile"] = self.power(
            game,
            "Solemn Vow",
            ["Command: Fill Focus If An Ally Dies On Your Tile"],
            "Bishop",
            ["Faith", "Focus"],
            10,
            "Focus Intensity",
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
            "Focus Intensity",
        )
        self.book["Command: MP Regeneration"] = self.power(
            game,
            "Bardic Command",
            ["Command: MP Regeneration"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
            "MP Amount",
        )
        self.book["Daggers Give Extra MP"] = self.power(
            game,
            "Ritual Blades",
            ["Daggers Give Extra MP"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            "MP Amount",
        )
        self.book["Daggers Range + 1"] = self.power(
            game,
            "Ninja Fire",
            "Daggers Range + 1",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            8,
            "Daggers Skill",
        )
        self.book["Dark Mage Tier 1 Blaze"] = self.power(
            game,
            "Blaze",
            "Dark Mage Tier 1 Blaze",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            "Fire Damage",
            spellRank=True,
        )
        self.book["Dark Mage Tier 1 Freeze"] = self.power(
            game,
            "Freeze",
            "Dark Mage Tier 1 Freeze",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            "Ice Damage",
            spellRank=True,
        )
        self.book["Defense Against Magic Damage"] = self.power(
            game,
            "Magical Defense",
            "Defense Against Magic Damage",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            "HP Amount",
        )
        self.book["Defense Against Ranged Physical Damage"] = self.power(
            game,
            "Projectile Defense",
            "Defense Against Ranged Physical Damage",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            7,
            "HP Amount",
        )
        self.book["Defense Against Sword Damage"] = self.power(
            game,
            "Sword Defense",
            "Defense Against Sword Damage",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            "HP Amount",
            antiStat=["Faith"],
        )
        self.book["Dodging Grants and Spends One Charge Of Focus"] = self.power(
            game,
            "Flash Step",
            ["Dodging Grants and Spends One Charge Of Focus"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            "Focus Intensity",
            7,
        )
        self.book["Double Chances For Multiple Attacks"] = self.power(
            game,
            "Sleight Of Hand",
            "Double Chances For Multiple Attacks",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            "Luckiness",
            7,
        )
        self.book["Druid Tier 1 Blast"] = self.power(
            game,
            "Natural Resistance",
            "Druid Tier 1 Blast",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            "Wind Damage",
            spellRank=True,
        )
        self.book["Druid Tier 1 Natural Resistance"] = self.power(
            game,
            "Natural Resistance",
            "Druid Tier 1 Natural Resistance",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            "HP Amount",
            spellRank=True,
        )
        self.book["Duelist Counterattack"] = self.power(
            game,
            "Counterattack",
            "Duelist Counterattack",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            "Swords Skill",
            antiStat=["Faith"],
        )
        self.book["Fame Reduces Enemy Stats"] = self.power(
            game,
            "Intimidation",
            "Fame Reduces Enemy Stats",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            7,
            "Fame",
        )
        self.book["Flamecaster Root 1 Blaze"] = self.power(
            game,
            "Blaze",
            "Flamecaster Root 1 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            "Fire Damage",
            spellRank=True,
        )
        self.book["Flamecaster Tier 1 Blaze"] = self.power(
            game,
            "Blaze",
            "Flamecaster Tier 1 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            "Fire Damage",
            spellRank=True,
        )
        self.book["Gain Extra Gold On Kills"] = self.power(
            game,
            "Lucre",
            "Gain Extra Gold On Kills",
            "Alchemist",
            ["Faith", "Luck"],
            9,
            "Luckiness",
        )
        self.book["Hero Counterattack"] = self.power(
            game,
            "Counterattack",
            "Hero Counterattack",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            7,
            "Swords Skill",
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
            "MP Amount",
            spellRank=True,
        )
        self.book["Hero Tier 1 Bolt"] = self.power(
            game,
            "Bolt",
            "Hero Tier 1 Bolt",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            7,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Ignore Opponents on First Two Tiles of Movement"] = self.power(
            game,
            "Stealthy Movement",
            "Ignore Opponents on First Two Tiles of Movement",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            "Movement Speed",
        )
        self.book["Increases Critical Chance"] = self.power(
            game,
            "Bardic Luck",
            ["Increases Critical Chance"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
            "Luckiness",
        )
        self.book["Increases Critical Hit Damage"] = self.power(
            game,
            "Explosives",
            "Increases Critical Hit Damage",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            7,
            "Critical Hit Damage",
        )
        self.book["Increases Damage Dealt On Unholy Ground"] = self.power(
            game,
            "Avenging Wrath",
            "Increases Damage Dealt On Unholy Ground",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            7,
            "Damage On Unholy Ground",
        )
        self.book["Increases Dodge Chance"] = self.power(
            game,
            "Dodge Roll",
            ["Increases Dodge Chance"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            7,
            "Luckiness",
        )
        self.book["Increases Fame Effect On Allies"] = self.power(
            game,
            "Charismatic Leadership",
            "Increases Fame Effect On Allies",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
            "Fame",
        )
        self.book["Increases Lance Damage For Each Tile Moved This Turn"] = self.power(
            game,
            "Charge",
            "Increases Lance Damage For Each Tile Moved This Turn",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            7,
            "Lance Skill",
            antiStat=["Intelligence"],
        )
        self.book["Increases Luck When Outnumbered"] = self.power(
            game,
            "Never Tell Me The Odds",
            ["Increases Luck When Outnumbered"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            7,
            "Luckiness",
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
            "Swords Skill",
            antiStat=["Faith"],
        )
        self.book["Increases Terrain Advantage I"] = self.power(
            game,
            "Higher Ground",
            "Increases Terrain Advantage I",
            "Archer",
            ["Focus", "Dexterity"],
            9,
            "Terrain Advantage",
        )
        self.book["Increases Your Area Of Holy Resonance To Five Tiles"] = self.power(
            game,
            "Booming Voice",
            "Increases Your Area Of Holy Resonance To Five Tiles",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Mage Knight Root 1 Blaze"] = self.power(
            game,
            "Blaze",
            "Mage Knight Root 1 Blaze",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            5,
            "Fire Damage",
            spellRank=True,
        )
        self.book["Mage Knight Root 2 Bolt"] = self.power(
            game,
            "Bolt",
            "Mage Knight Root 2 Bolt",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            5,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Mage Knight Tier 1 Freeze"] = self.power(
            game,
            "Freeze",
            "Mage Knight Tier 1 Freeze",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            5,
            "Ice Damage",
            spellRank=True,
        )
        self.book["Magic Cost Reduction"] = self.power(
            game,
            "Arcane Efficiency",
            "Magic Cost Reduction",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            "MP Amount",
        )
        self.book["Monk Root 1 Silence"] = self.power(
            game,
            "Silence",
            "Monk Root 1 Silence",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            7,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Monk Tier 1 Heal"] = self.power(
            game,
            "Heal",
            "Monk Tier 1 Heal",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Move After Attacking"] = self.power(
            game,
            "Maneuverability",
            "Move After Attacking",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            "Movement Speed",
            bannedClasses=["Knight"],
        )
        self.book[
            "Move an Additional Tile As Long As You Don't Move On Unstable Ground"
        ] = self.power(
            game,
            "Mounted Movement",
            "Move an Additional Tile As Long As You Don't Move On Unstable Ground",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            7,
            "Movement Speed",
            antiStat=["Intelligence"],
        )
        self.book["Move Faster On Holy Ground"] = self.power(
            game,
            "Beautiful Strides",
            "Move Faster On Holy Ground",
            "Catachumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            "Movement Speed",
        )
        self.book["Movement Does Not Interupt Your Singing"] = self.power(
            game,
            "Rhythmic Chanting",
            "Movement Does Not Interupt Your Singing",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Ninja Tier 1 Ninja Fire"] = self.power(
            game,
            "Ninja Fire",
            "Ninja Tier 1 Ninja Fire",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            8,
            "Fire Damage",
            spellRank=True,
        )
        self.book["One Negative Status Cleanses Itself Each Turn"] = self.power(
            game,
            "Pure of Heart",
            "One Negative Status Cleanses Itself Each Turn",
            "Peregrine",
            ["Faith", "Speed"],
            9,
            "FP Amount",
        )
        self.book["Orator Tier 1 Shield"] = self.power(
            game,
            "Shield",
            "Orator Tier 1 Shield",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            7,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Peregrine Root 1 Dispel"] = self.power(
            game,
            "Dispel",
            "Peregrine Root 1 Dispel",
            "Peregrine",
            ["Faith", "Speed"],
            9,
            "FP Amount",
            spellRank=True,
        )
        self.book["Peregrine Tier 1 Blast"] = self.power(
            game,
            "Blast",
            "Peregrine Tier 1 Blast",
            "Peregrine",
            ["Faith", "Speed"],
            9,
            "Wind Damage",
            spellRank=True,
        )
        self.book["Priest Root 1 Detox"] = self.power(
            game,
            "Detox",
            "Priest Root 1 Detox",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            7,
            "FP Amount",
            spellRank=True,
        )
        self.book["Priest Root 1 Heal"] = self.power(
            game,
            "Heal",
            "Priest Root 1 Heal",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Priest Tier 1 Heal"] = self.power(
            game,
            "Heal",
            "Priest Tier 1 Heal",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Prophet Root 1 Aura"] = self.power(
            game,
            "Aura",
            "Prophet Root 1 Aura",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Prophet Root 1 Heal"] = self.power(
            game,
            "Heal",
            "Prophet Root 1 Heal",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Prophet Tier 1 Slow"] = self.power(
            game,
            "Slow",
            "Prophet Tier 1 Slow",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            7,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Random Additional Spell I"] = self.power(
            game,
            "Mercurial Knowledge I",
            "Random Additional Spell I",
            "Alchemist",
            ["Faith", "Luck"],
            9,
            "Luckiness",
        )
        self.book["Ranged Attacks Add Resonance to Target's Tile"] = self.power(
            game,
            "Whistling Shots",
            ["Ranged Attacks Add Resonance to Target's Tile"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
            "Vocal Strength",
        )
        self.book["Reduces the Effect of Unholy Ground By One Rank"] = self.power(
            game,
            "Blessed Shield",
            "Reduces the Effect of Unholy Ground By One Rank",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            7,
            "Damage On Unholy Ground",
            antiStat=["Intelligence"],
        )
        self.book["Regenerate Health On Holy Ground"] = self.power(
            game,
            "Sustenance",
            "Regenerate Health On Holy Ground",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            "Damage On Unholy Ground",
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
            "Movement Speed",
        )
        self.book["Tile Resonance Increases Charisma Effects"] = self.power(
            game,
            "Bragging Verse",
            "Tile Resonance Increases Charisma Effects",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
            "Vocal Strength",
        )
        self.book["Vocal Attacks Have A Chance To Add Bleed"] = self.power(
            game,
            "Piercing Screams",
            "Vocal Attacks Have A Chance To Add Bleed",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Vocal Attacks Have A Change To Double Attack"] = self.power(
            game,
            "Vocal Agility",
            "Vocal Attacks Have A Change To Double Attack",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            6,
            "Vocal Strength",
        )
        self.book["When Focused, Double Your Luck"] = self.power(
            game,
            "Make Your Own Luck",
            "When Focused, Double Your Luck",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            6,
            "Vocal Strength",
        )
        self.book["When Focused, Spell Are Free"] = self.power(
            game,
            "Transcendant Ninjitsu",
            "When Focused, Spell Are Free",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            8,
            "MP Amount",
        )
        self.book["Your Vocal Attacks Ignore Penalty From Evil Resonance"] = self.power(
            game,
            "Overcome the Darkness",
            "Your Vocal Attacks Ignore Penalty From Evil Resonance",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            6,
            "Vocal Strength",
        )
        self.book["Your Resonating Tiles Stay Resonating Longer"] = self.power(
            game,
            "Sustaining Notes",
            "Your Resonating Tiles Stay Resonating Longer",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            7,
            "Vocal Strength",
        )

        # Tier two powers
        self.book["Archmage Tier 2 Bolt"] = self.power(
            game,
            "Bolt",
            "Archmage Tier 2 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            8,
            "Lightning Damage",
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
            "Arrows Skill",
            [self.book["Arrows: Add Effect: Poison"]],
        )
        self.book["Assassin Tier 2 Death"] = self.power(
            game,
            "Death",
            "Assassin Tier 2 Death",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            5,
            "Status Effectiveness",
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
            "Axe Skill",
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
            "Heavy Damage Chance"[
                self.book["Slower Movement That Ignores Terrain Cost And Blockers"]
            ],
        )
        self.book["Banshee Tier 2 Axe Damage"] = self.power(
            game,
            "Axe Damage",
            "Banshee Tier 2 Axe Damage",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            4,
            "Axe Skill",
            [self.book["Tile Resonance Increases Charisma Effects"]],
        )
        self.book["Bishop Tier 2 Aura"] = self.power(
            game,
            "Aura",
            ["Bishop Tier 2 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            9,
            "Healing Amount",
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
            "Drained Health",
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
            "MP Amount",
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
            "MP Amount",
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
            "Status Effectiveness",
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
            "Water Damage",
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
            "Status Effectiveness",
            [self.book["Tile Resonance Increases Charisma Effects"]],
        )
        self.book["Convert Faith and Magic"] = self.power(
            game,
            "Mercurial Exchange",
            "Convert Faith and Magic",
            "Alchemist",
            ["Faith", "Luck"],
            8,
            "MP Amount",
            [self.book["Random Additional Spell I"]],
        )
        self.book["Command: Casting Does Not Interupt Your Singing"] = self.power(
            game,
            "Melodious Spellweaving",
            ["Command: Casting Does Not Interupt Your Singing"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            6,
            "Vocal Strength",
            [self.book["Command: MP Regeneration"]],
        )
        self.book["Command: Increases Defense On Resonant Tiles"] = self.power(
            game,
            "Radiant Shield",
            "Command: Increases Defense On Resonant Tiles",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            6,
            "Vocal Strength",
            [self.book["Increases Your Area Of Holy Resonance To Five Tiles"]],
        )
        self.book["Counter Enemy Attacks By Inflicting Bleed"] = self.power(
            game,
            "Sharpness",
            "Counter Enemy Attacks By Inflicting Bleed",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            6,
            "Daggers Skill",
            [self.book["Double Chances For Multiple Attacks"]],
        )
        self.book["Counter Enemy Vocal Attacks With Bleed"] = self.power(
            game,
            "Lacerating Response",
            "Counter Enemy Vocal Attacks With Bleed",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            6,
            "Daggers Skill",
            [self.book["Vocal Attacks Have A Chance To Add Bleed"]],
        )
        self.book["Critical Hits Reduce Next Spell Cost to 0"] = self.power(
            game,
            "Stroke of Luck",
            ["Critical Hits Reduce Next Spell Cost to 0"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            6,
            "Luckiness",
            [self.book["Command: MP Regeneration"]],
        )
        self.book["Dark Mage Tier 2 Death"] = self.power(
            game,
            "Death",
            "Dark Mage Tier 2 Death",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            8,
            "Status Effectiveness",
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
            "Status Effectiveness",
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
            "Swords Skill",
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
            "Focus Amount",
            [self.book["Increases Luck When Outnumbered"]],
        )
        self.book["Double Rout Chance Against Bleeding Targets"] = self.power(
            game,
            "Blood Cries Out",
            "Double Rout Chance Against Bleeding Targets",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            6,
            "Fame",
            [self.book["Vocal Attacks Have A Chance To Add Bleed"]],
        )
        self.book["Druid Tier 2 Conduit"] = self.power(
            game,
            "Conduit",
            "Druid Tier 2 Conduit",
            "Druid",
            ["Dexterity", "Faith"],
            8,
            "FP Amount",
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
            "FP Amount",
            [self.book["Druid Tier 1 Natural Resistance"]],
            spellRank=True,
        )
        self.book[
            "Enemy Lance and Spear Users Must Attack You If Possible"
        ] = self.power(
            game,
            "Knight's Challenge",
            "Enemy Lance and Spear Users Must Attack You If Possible",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            6,
            "HP Amount",
            [self.book["Reduces the Effect of Unholy Ground By One Rank"]],
            antiStat=["Intelligence"],
        )
        self.book["Fire Damage Consumes Bleed To Deal Double Damage"] = self.power(
            game,
            "Cauterize",
            "Fire Damage Consumes Bleed To Deal Double Damage",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            8,
            "Fire Damage",
            [self.book["Flamecaster Tier 1 Blaze"]],
        )
        self.book["Flamecaster Tier 2 Blaze"] = self.power(
            game,
            "Blaze",
            "Flamecaster Tier 2 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            8,
            "Fire Damage",
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
            "Lightning Damage",
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
            "MP Amount",
            [self.book["Hero Tier 1 Bolt"]],
        )
        self.book["Increases Damage Dealt On Unholy Ground"] = self.power(
            game,
            "Paladin",
            "Increases Damage Dealt On Unholy Ground",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            6,
            "Damage On Unholy Ground",
            [self.book["Reduces the Effect of Unholy Ground By One Rank"]],
            antiStat=["Intelligence"],
        )
        self.book["Increases Focus When Outnumbered"] = self.power(
            game,
            "Against All Odds",
            ["Increases Focus When Outnumbered"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            6,
            "Focus Intensity",
            [self.book["Increases Luck When Outnumbered"]],
        )
        self.book["Increases Focus When Stationary"] = self.power(
            game,
            "Unhindered Movement",
            "Increases Focus When Stationary",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            6,
            "Focus Intensity",
            [self.book["Slower Movement That Ignores Terrain Cost And Blockers"]],
        )
        self.book["Increases Healing Magic Range By 1"] = self.power(
            game,
            "Heal",
            "Increases Healing Magic Range By 1",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            6,
            "Healing Amount",
            [self.book["Priest Tier 1 Heal"]],
        )
        self.book["Increases Healing To Allies On Unholy Ground"] = self.power(
            game,
            "Heal",
            "Increases Healing To Allies On Unholy Ground",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            6,
            "Healing Amount",
            [self.book["Monk Tier 1 Heal"]],
        )
        self.book[
            "Lance Attacks Grant Vulnerability Against Known Spell Schools"
        ] = self.power(
            game,
            "Conductive Lance",
            "Lance Attacks Grant Vulnerability Against Known Spell Schools",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            4,
            "Lances Skill",
            [self.book["Mage Knight Root 1 Blaze"]],
        )
        self.book["Lightning Damage Breaks Focus"] = self.power(
            game,
            "Sudden Shock",
            "Lightning Damage Breaks Focus",
            "Archmage",
            ["Intelligence", "Luck"],
            8,
            "Lightning Damage",
            [self.book["Archmage Tier 1 Bolt"]],
        )
        self.book["Lost Health Increases Turn Speed"] = self.power(
            game,
            "Tunnel Vision",
            ["Lost Health Increases Turn Speed"],
            "Berserker",
            ["Stamina", "Strength"],
            9,
            "Axes Skill",
            [self.book["Berserker Tier 1 Berserking"]],
            antiStat=["Luck"],
        )
        self.book["Monk Tier 2 Heal"] = self.power(
            game,
            "Heal",
            "Monk Tier 2 Heal",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            6,
            "Healing Amount",
            [self.book["Monk Tier 1 Heal"]],
            spellRank=True,
        )
        self.book["Move To Follow Routed Enemies And Attack Again"] = self.power(
            game,
            "Follow-on Attack",
            "Move To Follow Routed Enemies And Attack Again",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            6,
            "Fame",
            [self.book["Double Chances For Multiple Attacks"]],
        )
        self.book["Ninja Tier 2 Ninja Bolt"] = self.power(
            game,
            "Ninja Bolt",
            "Ninja Tier 2 Ninja Bolt",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            7,
            "Lightning Damage",
            [self.book["Ninja Tier 1 Ninja Fire"]],
            spellRank=True,
        )
        self.book["Ninja Tier 2 Ninja Fire"] = self.power(
            game,
            "Ninja Fire",
            "Ninja Tier 2 Ninja Fire",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            7,
            "Fire Damage",
            [self.book["Ninja Tier 1 Ninja Fire"]],
            spellRank=True,
        )
        self.book["Peregrine Tier 2 Blast"] = self.power(
            game,
            "Blast",
            "Peregrine Tier 2 Blast",
            "Peregrine",
            ["Faith", "Speed"],
            8,
            "Wind Damage",
            [self.book["Peregrine Tier 1 Blast"]],
            spellRank=True,
        )
        self.book["Prevent Enemy Counterattacks"] = self.power(
            game,
            "Smoke Bomb",
            "Prevent Enemy Counterattacks",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            5,
            "Swords Skill",
            [self.book["Move After Attacking"]],
            bannedClasses=["Knight"],
        )
        self.book["Priest Tier 2 Heal"] = self.power(
            game,
            "Heal",
            "Priest Tier 2 Heal",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            6,
            "Healing Amount",
            [self.book["Priest Tier 1 Heal"]],
            spellRank=True,
        )
        self.book["Prophet Tier 2 Aura"] = self.power(
            game,
            "Aura",
            "Prophet Tier 2 Aura",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            6,
            "Healing Amount",
            [self.book["Prophet Tier 1 Slow"]],
            spellRank=True,
        )
        self.book["Prophet Tier 2 Quick"] = self.power(
            game,
            "Quick",
            "Prophet Tier 2 Quick",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            6,
            "FP Amount",
            [self.book["Prophet Tier 1 Slow"]],
            spellRank=True,
        )
        self.book["Random Additional Spell II"] = self.power(
            game,
            "Mercurial Knowledge II",
            "Random Additional Spell II",
            "Alchemist",
            ["Faith", "Luck"],
            8,
            "Luckiness",
            [self.book["Random Additional Spell I"]],
        )
        self.book["Ranged Attacks Don't Miss"] = self.power(
            game,
            "Aimed Shot",
            "Ranged Attacks Don't Miss",
            "Archer",
            ["Focus", "Dexterity"],
            8,
            "Arrows Skill",
            [self.book["Arrows: Add Effect: Poison"]],
        )
        self.book["Reduces Chance To Be Inflicted By Status Spells"] = self.power(
            game,
            "Defense Against The Dark Arts",
            "Reduces Chance To Be Inflicted By Status Spells",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            4,
            "Swords Skill",
            [self.book["Mage Knight Root 1 Blaze"]],
        )
        self.book["Staff Skills Increase the Damage of Vocal Attacks"] = self.power(
            game,
            "Singing Rod",
            "Staff Skills Increase the Damage of Vocal Attacks",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Vocal Attacks Have A Change To Double Attack"]],
        )
        self.book[
            "Spells You Target On One Of Your Resonating Tiles Target All Your Resonating Tiles"
        ] = self.power(
            game,
            "Brilliant Radiance",
            "Spells You Target On One Of Your Resonating Tiles Target All Your Resonating Tiles",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            6,
            "Vocal Strength",
            [self.book["Increases Your Area Of Holy Resonance To Five Tiles"]],
        )
        self.book["Unarmed Range + 1 and deals wind damage"] = self.power(
            game,
            "Throw the Wind",
            "Unarmed Range + 1 and deals wind damage",
            "Peregrine",
            ["Faith", "Speed"],
            8,
            "Unarmed Skill",
            [self.book["Peregrine Tier 1 Blast"]],
        )
        self.book["When Focused, All Area Spells Have Double Power"] = self.power(
            game,
            "Fervent Prayer",
            ["When Focused, All Area Spells Have Double Power"],
            "Bishop",
            ["Faith", "Focus"],
            9,
            "Focus Intensity",
            [self.book["Bishop Tier 1 Aura"]],
        )
        self.book[
            "Vocal Attack Targets Skip Their Next Attempt To Resist Status Effects"
        ] = self.power(
            game,
            "Jarring Shout",
            "Vocal Attack Targets Skip Their Next Attempt To Resist Status Effects",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Vocal Attacks Have A Change To Double Attack"]],
        )
        self.book["Vocal Cascade With Weapons"] = self.power(
            game,
            "Santified Movements",
            "Vocal Cascade With Weapons",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Catechumen Tier 1 Vocal Cascade"]],
        )
        self.book["Vocal Cascade Without Full Holy Resonance"] = self.power(
            game,
            "Indwelling Echoes",
            "Vocal Cascade Without Full Holy Resonance",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Catechumen Tier 1 Vocal Cascade"]],
        )
        self.book["Your Bleeding Heals Allies On Your Tile"] = self.power(
            game,
            "Sanguine Bond",
            ["Your Bleeding Heals Allies On Your Tile"],
            "Baron",
            ["Charisma", "Strength"],
            9,
            "Drained Health",
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
            "Swords Skill",
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
            "Lightning Damage",
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
            "Luckiness",
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
            "Arrows Skill",
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
            "Axes Skill",
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
            "Healing Amount",
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
            "Drained Health",
            [self.book["Bleeding Enemies Give MP"]],
            [self.book["Blood Mage Tier 2 Essence"]],
            spellRank=True,
        )
        self.book["Can Make Triple Attacks"] = self.power(
            game,
            "Triple Attack",
            "Can Make Triple Attacks",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            5,
            "Daggers Skill",
            [self.book["Move To Follow Routed Enemies And Attack Again"]],
            [self.book["Move To Follow Routed Enemies And Attack Again"]],
        )
        self.book["Catechumen Tier 3 Vocal Cascade"] = self.power(
            game,
            "Cascade",
            "Catechumen Tier 3 Vocal Cascade",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            "Vocal Strength",
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
            "Fame",
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
            "Fame",
            [self.book["Convert Faith and Magic"]],
            [self.book["Random Additional Spell II"]],
        )
        self.book["Critical Hits Inflict Silence"] = self.power(
            game,
            "Hush Up",
            "Critical Hits Inflict Silence",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            4,
            "Status Effectiveness",
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
            "Status Effectiveness",
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
            "HP Amount",
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
            "Swords Skill",
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
            "Fire Damage",
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
            "Lightning Damage",
            [self.book["Hero Tier 2 Bolt"]],
            [self.book["Killing Enemies Gives MP"]],
            spellRank=True,
        )
        self.book["Increases Chance To Rout On Unholy Ground"] = self.power(
            game,
            "Paladin",
            "Increases Chance To Rout On Unholy Ground",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            5,
            "Damage On Unholy Ground",
            [self.book["Enemy Lance and Spear Users Must Attack You If Possible"]],
            [self.book["Increases Damage Dealt On Unholy Ground"]],
            antiStat=["Intelligence"],
        )
        self.book["Increases Your Area Of Holy Resonance To Seven Tiles"] = self.power(
            game,
            "Brilliant Radiance",
            "Increases Your Area Of Holy Resonance To Seven Tiles",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Command: Increases Defense On Resonant Tiles"]],
            [
                self.book[
                    "Spells You Target On One Of Your Resonating Tiles Target All Your Resonating Tiles"
                ]
            ],
        )
        self.book["Monk Tier 3 Aura"] = self.power(
            game,
            "Aura",
            "Monk Tier 3 Aura",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            5,
            "Healing Amount",
            [self.book["Monk Tier 2 Heal"]],
            [self.book["Increases Healing To Allies On Unholy Ground"]],
            spellRank=True,
        )
        self.book["Ninja Tier 3 Ninja Bolt"] = self.power(
            game,
            "Ninja Bolt",
            "Ninja Tier 3 Ninja Bolt",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            6,
            "Lightning Damage",
            [self.book["Ninja Tier 2 Ninja Bolt"]],
            [self.book["Ninja Tier 2 Ninja Fire"]],
            spellRank=True,
        )
        self.book["Peregrine Tier 3 Blast"] = self.power(
            game,
            "Blast",
            "Peregrine Tier 3 Blast",
            "Peregrine",
            ["Faith", "Speed"],
            7,
            "Wind Damage",
            [self.book["Peregrine Tier 2 Blast"]],
            [self.book["Unarmed Range + 1 and deals wind damage"]],
            spellRank=True,
        )
        self.book["Priest Tier 3 Heal"] = self.power(
            game,
            "Heal",
            "Priest Tier 3 Heal",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            5,
            "Healing Amount",
            [self.book["Increases Healing Magic Range By 1"]],
            [self.book["Priest Tier 2 Heal"]],
            spellRank=True,
        )
        self.book["Prophet Tier 3 Slow"] = self.power(
            game,
            "Slow",
            "Prophet Tier 3 Slow",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            5,
            "Status Effectiveness",
            [self.book["Prophet Tier 2 Aura"]],
            [self.book["Prophet Tier 2 Quick"]],
            spellRank=True,
        )
        self.book["Reduces Minimum Attack Range By 1"] = self.power(
            game,
            "Unhindered Movement",
            "Reduces Minimum Attack Range By 1",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            5,
            "Brass Guns Skill",
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
            "Status Effectiveness",
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
            "Status Effectiveness",
            [self.book["Channeller Tier 2 Surge"]],
            [self.book["Channeller Tier 2 Silence"]],
        )
        self.book[
            "When Attacking A Target That Is Vulnerable To A Spell School You Know, Cast a Rank I Version Of The Spell At Them"
        ] = self.power(
            game,
            "Elemental Judgement",
            "When Attacking A Target That Is Vulnerable To A Spell School You Know, Cast a Rank I Version Of The Spell At Them",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            3,
            "MP Amount",
            [
                self.book[
                    "Lance Attacks Grant Vulnerability Against Known Spell Schools"
                ]
            ],
            [self.book["Reduces Chance To Be Inflicted By Status Spells"]],
        )
        self.book["When Focused, All Attacks Charm"] = self.power(
            game,
            "Irresistable Voice",
            "When Focused, All Attacks Charm",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            3,
            "Focus Intensity",
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
            "Focus Intensity",
            [self.book["Dodging Grants Focus Charge"]],
            [self.book["Increases Focus When Outnumbered"]],
        )
        self.book[
            "Vocal Attacks Isolate Targets From Their Allies' Effects"
        ] = self.power(
            game,
            "Deafening Voice",
            "Vocal Attacks Isolate Targets From Their Allies' Effects",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            4,
            "Vocal Strength",
            [self.book["Staff Skills Increase the Damage of Vocal Attacks"]],
            [
                self.book[
                    "Vocal Attack Targets Skip Their Next Attempt To Resist Status Effects"
                ]
            ],
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
        unlockCategory,
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
