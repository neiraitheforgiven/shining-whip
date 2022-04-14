import random


class powerBook(object):
    """The dictionary containing all of the powers in the given game"""

    def __init__(self):
        self.book = {}
        # Tier one powers
        self.book["Alchemist Bolt Rank"] = power(
            "Bolt",
            "Alchemist Bolt Rank",
            "Alchemist",
            ["Faith", "Luck"],
            9,
            "Lightning Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Archmage Teleport"] = power(
            "Teleport",
            "Archmage Teleport",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Archmage Root 1 Bolt"] = power(
            "Bolt",
            "Archmage Root 1 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            "Lightning Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Archmage Tier 1 Bolt"] = power(
            "Bolt",
            "Archmage Tier 1 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            9,
            "Lightning Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Arrows: Add Effect: Poison"] = power(
            "Poisoned Tips",
            "Arrows: Add Effect: Poison",
            "Archer",
            ["Focus", "Dexterity"],
            9,
            "Arrows Skill",
        )
        self.book["Assassin Tier 1 Death"] = power(
            "Death",
            "Assassin Tier 1 Death",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            "Status Effectiveness",
            bannedClasses=["Knight"],
            spellRank=True,
        )
        self.book["Assassin Tier 1 Sleep"] = power(
            "Sleep",
            "Assassin Tier 1 Sleep",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            "Status Effectiveness",
            bannedClasses=["Knight"],
            spellRank=True,
        )
        self.book["Attacking Does Not Interupt Your Singing"] = power(
            "Battle Song",
            "Attacking Does Not Interupt Your Singing",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
            "Vocal Strength",
        )
        self.book["Attacks Change Type To Match Vulnerabilities"] = power(
            "Suffering",
            "Attacks Change Type To Match Vulnerabilities",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            7,
            "Damage vs Vulnerability",
        )
        self.book["Axes: Extra Unarmed Attack"] = power(
            "Axe Punch",
            ["Axes: Extra Unarmed Attack"],
            "Berserker",
            ["Stamina", "Strength"],
            10,
            "Axe Skill",
            antiStat=["Luck"],
        )
        self.book["Baron Root 1 Drain On Crit"] = power(
            "Essence Sap",
            ["Baron Root 1 Drain On Crit"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            "Drained Health",
            antiStat=["Intelligence"],
            spellRank=True,
        )
        self.book["Baron Tier 1 Drain On Crit"] = power(
            "Essence Sap",
            ["Baron Tier 1 Drain On Crit"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            "Drained Health",
            antiStat=["Intelligence"],
            spellRank=True,
        )
        self.book["Begin Battle with Two Ranks of Focus"] = power(
            "Preparation",
            ["Begin Battle with Two Ranks of Focus"],
            "Archer",
            "Focus Intensity",
            ["Focus", "Dexterity"],
            9,
        )
        self.book["Berserker Tier 1 Heavy Damage"] = power(
            "Heavy Damage",
            ["Berserker Tier 1 Heavy Damage"],
            "Berserker",
            ["Stamina", "Strength"],
            10,
            "Heavy Attack Chance",
            antiStat=["Luck"],
            spellRank=True,
        )
        self.book[
            "Berserker Tier 1 Berserking"
        ] = power(  # Lost Health Adds Damage
            "Berserking",
            ["Berserker Tier 1 Berserking"],
            "Berserker",
            ["Stamina", "Strength"],
            10,
            "Heavy Attack Chance",
            antiStat=["Luck"],
            spellRank=True,
        )
        self.book["Bishop Root 1 Aura"] = power(
            "Aura",
            ["Bishop Root 1 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            10,
            "Healing Amount",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Bishop Tier 1 Aura"] = power(
            "Aura",
            ["Bishop Tier 1 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            10,
            "Healing Amount",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Blood Mage Tier 1 Drain"] = power(
            "Drain",
            ["Blood Mage Tier 1 Drain"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            "Drained Health",
            spellRank=True,
            not_yet_implemented=False
        )  # Note to self: Drain should leave targets bleeding
        self.book["Blood Mage Tier 1 Muddle"] = power(
            "Muddle",
            ["Blood Mage Tier 1 Muddle"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Catechumen Tier 1 Vocal Cascade"] = power(
            "Cascade",
            "Catechumen Tier 1 Vocal Cascade",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            "Vocal Strength",
            spellRank=True,
        )
        self.book["Chance to Return from the Dead Each Turn"] = power(
            "Overcome the Grave",
            ["Chance to Return from the Dead Each Turn"],
            "Baron",
            ["Charisma", "Strength"],
            10,
            "Luckiness",
            antiStat=["Intelligence"],
        )
        self.book["Channeller Root 1 Surge"] = power(
            "Surge",
            "Channeller Root 1 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            "Water Damage",
            spellRank=True,
        )
        self.book["Channeller Root 2 Surge"] = power(
            "Surge",
            "Channeller Root 2 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            "Water Damage",
            spellRank=True,
        )
        self.book["Channeller Tier 1 Surge"] = power(
            "Surge",
            "Channeller Tier 1 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            9,
            "Water Damage",
            spellRank=True,
        )
        self.book["Command: Fill Focus If An Ally Dies On Your Tile"] = power(
            "Solemn Vow",
            ["Command: Fill Focus If An Ally Dies On Your Tile"],
            "Bishop",
            ["Faith", "Focus"],
            10,
            "Focus Intensity",
        )
        self.book[
            "Command: Increase Focus Generation on Fully Holy Tiles"
        ] = power(
            "Sacred Dance",
            "Command: Increase Focus Generation on Fully Holy Tiles",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
            "Focus Intensity",
        )
        self.book["Command: MP Regeneration"] = power(
            "Bardic Command",
            ["Command: MP Regeneration"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
            "MP Amount",
        )
        self.book["Daggers Give Extra MP"] = power(
            "Ritual Blades",
            ["Daggers Give Extra MP"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            8,
            "MP Amount",
        )
        self.book["Daggers Range + 1"] = power(
            "Ninja Fire",
            "Daggers Range + 1",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            8,
            "Daggers Skill",
        )
        self.book["Dark Mage Tier 1 Blaze"] = power(
            "Blaze",
            "Dark Mage Tier 1 Blaze",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            "Fire Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Dark Mage Tier 1 Freeze"] = power(
            "Freeze",
            "Dark Mage Tier 1 Freeze",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            "Ice Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Defense Against Magic Damage"] = power(
            "Magical Defense",
            "Defense Against Magic Damage",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            9,
            "HP Amount",
        )
        self.book["Defense Against Melee Physical Damage"] = power(
            "Survival",
            "Defense Against Melee Physical Damage",
            "Survivor",
            ["Luck", "Speed", "Stamina", "Strength"],
            8,
            "HP Amount",
            requiresDragonOr25=True,
        )
        self.book["Defense Against Melee Damage"] = power(
            "Dwarven Armor",
            "Defense Against Melee Damage",
            "Warrior",
            ["Luck", "Stamina", "Strength"],
            6,
            "HP Amount",
        )
        self.book["Defense Against Ranged Physical Damage"] = power(
            "Projectile Defense",
            "Defense Against Ranged Physical Damage",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            7,
            "HP Amount",
        )
        self.book["Defense Against Sword Damage"] = power(
            "Sword Defense",
            "Defense Against Sword Damage",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            "HP Amount",
            antiStat=["Faith"],
        )
        self.book["Dodging Grants and Spends One Charge Of Focus"] = power(
            "Flash Step",
            ["Dodging Grants and Spends One Charge Of Focus"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            "Focus Intensity",
            7,
        )
        self.book["Dodging Grants Additional Movement Next Turn"] = power(
            "Aleron Roll",
            ["Dodging Grants Additional Movement Next Turn"],
            "Sky Lord",
            ["Focus", "Intelligence", "Speed"],
            "Movement Speed",
            7,
        )
        self.book["Double and Triple Attacks Can Be Heavy Attacks"] = power(
            "Heavy Handed",
            "Double and Triple Attacks Can Be Heavy Attacks",
            "Titan",
            ["Focus", "Strength"],
            "Heavy Attack Chance",
            11,
            antiStat=["Speed"],
        )
        self.book["Double Chances For Multiple Attacks"] = power(
            "Sleight Of Hand",
            "Double Chances For Multiple Attacks",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            "Luckiness",
            7,
        )
        self.book["Druid Tier 1 Blast"] = power(
            "Natural Resistance",
            "Druid Tier 1 Blast",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            "Wind Damage",
            spellRank=True,
        )
        self.book["Druid Tier 1 Natural Resistance"] = power(
            "Natural Resistance",
            "Druid Tier 1 Natural Resistance",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            "HP Amount",
            spellRank=True,
        )
        self.book["Duelist Counterattack"] = power(
            "Counterattack",
            "Duelist Counterattack",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            "Swords Skill",
            antiStat=["Faith"],
        )
        self.book["Elemental Spell Damage Gives Targets Vulnerability To Element"] = power(
            "Saturation",
            "Elemental Spell Damage Gives Targets Vulnerability To Element",
            "Trickster",
            ["Intelligence", "Speed"],
            8,
            "Status Effectiveness"
        )
        self.book["Fame Increases With Kills"] = power(
            "Bestial Reputation",
            "Fame Increases With Kills",
            "Werewolf",
            ["Dexterity", "Speed", "Stamina", "Strength"],
            8,
            "Fame",
            antiStat=["Luck"]
        )
        self.book["Fame Reduces Enemy Stats"] = power(
            "Intimidation",
            "Fame Reduces Enemy Stats",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            7,
            "Fame",
        )
        self.book["Flamecaster Root 1 Blaze"] = power(
            "Blaze",
            "Flamecaster Root 1 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            "Fire Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Flamecaster Tier 1 Blaze"] = power(
            "Blaze",
            "Flamecaster Tier 1 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            "Fire Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Flying Movement"] = power(
            "Flying Movement",
            "Flying Movement",
            "Sky Battler",
            ["Charisma", "Dexterity", "Luck", "Speed", "Stamina"],
            5,
            "Movement Speed",
        )
        self.book[
            "From Stationary, Move Forward One Square and Push Slowest Enemy"
        ] = power(
            "Bulldozer",
            "From Stationary, Move Forward One Square and Push Slowest Enemy",
            "Steam Knight",
            ["Focus", "Stamina"],
            8,
            "Fame",
        )
        self.book["Gain Extra Gold On Kills"] = power(
            "Lucre",
            "Gain Extra Gold On Kills",
            "Alchemist",
            ["Faith", "Luck"],
            9,
            "Luckiness",
        )
        self.book["Hero Counterattack"] = power(
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
        self.book["Hero Root 1 Egress"] = power(
            "Egress",
            "Hero Root 1 Egress",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            7,
            "MP Amount",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Hero Tier 1 Bolt"] = power(
            "Bolt",
            "Hero Tier 1 Bolt",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            7,
            "Lightning Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Killing Enemies Grants You HP"] = power(
            "Survival of the Fittest",
            "Killing Enemies Grants You HP",
            "Survivor",
            ["Luck", "Speed", "Stamina", "Strength"],
            8,
            "HP Amount",
            requiresDragonOr25=True,
        )
        self.book["Ignore Opponents on First Two Tiles of Movement"] = power(
            "Stealthy Movement",
            "Ignore Opponents on First Two Tiles of Movement",
            "Druid",
            ["Dexterity", "Faith"],
            9,
            "Movement Speed",
        )
        self.book["Ignore Opponents When Moving To Tiles With Damaged Enemies"] = power(
            "Scent of Blood",
            "Ignore Opponents When Moving To Tiles With Damaged Enemies",
            "Werewolf",
            ["Dexterity", "Speed", "Stamina", "Strength"],
            8,
            "Movement Speed",
            antiStat=["Luck"]
        )
        self.book["Increases Critical Chance"] = power(
            "Bardic Luck",
            ["Increases Critical Chance"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
            "Luckiness",
        )
        self.book["Increases Critical Chance For A Turn After Dodging"] = power(
            "On Their Six",
            ["Increases Critical Chance For A Turn After Dodging"],
            "Sky Lord",
            ["Focus", "Intelligence", "Speed"],
            "Movement Speed",
            7,
        )
        self.book["Increases Critical Hit Damage"] = power(
            "Explosives",
            "Increases Critical Hit Damage",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            7,
            "Critical Hit Damage",
        )
        self.book["Increases Damage Dealt On Unholy Ground"] = power(
            "Avenging Wrath",
            "Increases Damage Dealt On Unholy Ground",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            7,
            "Swords Skill",
        )
        self.book["Increases Damage Dealt To Flying Enemies"] = power(
            "Air Superiority",
            ["Increases Damage Dealt To Flying Enemies"],
            "Sky Lord",
            ["Focus", "Intelligence", "Speed"],
            "Movement Speed",
            7,
        )
        self.book["Increases Damage Dealt To Isolated Enemies"] = power(
            "Diving Strike",
            "Increases Damage Dealt To Isolated Enemies",
            "Sky Battler",
            ["Charisma", "Dexterity", "Luck", "Speed", "Stamina"],
            5,
            "Damage On Unholy Ground",
        )
        self.book["Increases Damage Dealt When Outnumbered"] = power(
            "Wicked Rage",
            "Increases Damage Dealt When Outnumbered",
            "Werewolf",
            ["Dexterity", "Speed", "Stamina", "Strength"],
            8,
            "Movement Speed",
            antiStat=["Luck"]
        )
        self.book["Increases Defense On Unholy Ground"] = power(
            "Psalmic Meditation",
            "Increases Defense On Unholy Ground",
            "Chorister",
            ["Dexterity", "Faith", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Increases Dodge Chance"] = power(
            "Dodge Roll",
            ["Increases Dodge Chance"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            7,
            "Luckiness",
        )
        self.book["Increases Dodge Chance vs Slower Attackers"] = power(
            "Maneuverability",
            "Increases Dodge Chance vs Slower Attackers",
            "Sky Battler",
            ["Charisma", "Dexterity", "Luck", "Speed", "Stamina"],
            5,
            "Movement Speed",
        )
        self.book["Increases Fame Effect On Allies"] = power(
            "Charismatic Leadership",
            "Increases Fame Effect On Allies",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
            "Fame",
        )
        self.book["Increases Focus When Stationary"] = power(
            "Rolling Boil",
            "Increases Focus When Stationary",
            "Steam Knight",
            ["Focus", "Stamina"],
            8,
            "Focus Intensity",
        )
        self.book["Increases Heavy Attack Chance"] = power(
            "Heavy Weapons",
            "Increases Heavy Attack Chance",
            "Titan",
            ["Focus", "Strength"],
            "Heavy Attack Chance",
            11,
            antiStat=["Speed"],
        )
        self.book["Increases Heavy Attack Damage"] = power(
            "Heavier Attacks",
            "Increases Heavy Attack Damage",
            "Titan",
            ["Focus", "Strength"],
            "Heavy Attack Chance",
            11,
            antiStat=["Speed"],
        )
        self.book["Increases Lance Damage For Each Tile Moved This Turn"] = power(
            "Charge",
            "Increases Lance Damage For Each Tile Moved This Turn",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            7,
            "Lance Skill",
            antiStat=["Intelligence"],
        )
        self.book["Increases Luck When Outnumbered"] = power(
            "Never Tell Me The Odds",
            ["Increases Luck When Outnumbered"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            7,
            "Luckiness",
        )
        self.book[
            "Increases Special Attack Chance When Sword Is Equipped"
        ] = power(
            "Fencing Skill",
            "Increases Special Attack Chance When Sword Is Equipped",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            7,
            "Swords Skill",
            antiStat=["Faith"],
        )
        self.book[
            "Increases Sword Damage If You Haven't Moved Since Last Attack"
        ] = power(
            "Ono-ha Itto-ryu",
            ["Increases Sword Damage If You Haven't Moved Since Last Attack"],
            "Samurai",
            ["Charisma", "Faith", "Stamina"],
            10,
            "Swords Skill",
        )
        self.book["Increases Terrain Advantage I"] = power(
            "Higher Ground",
            "Increases Terrain Advantage I",
            "Archer",
            ["Focus", "Dexterity"],
            9,
            "Terrain Advantage",
        )
        self.book["Increases Your Area Of Holy Resonance To Five Tiles"] = power(
            "Booming Voice",
            "Increases Your Area Of Holy Resonance To Five Tiles",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Mage Knight Root 1 Blaze"] = power(
            "Blaze",
            "Mage Knight Root 1 Blaze",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            5,
            "Fire Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Mage Knight Root 2 Bolt"] = power(
            "Bolt",
            "Mage Knight Root 2 Bolt",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            5,
            "Lightning Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Mage Knight Tier 1 Freeze"] = power(
            "Freeze",
            "Mage Knight Tier 1 Freeze",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            5,
            "Ice Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Magic Cost Reduction"] = power(
            "Arcane Efficiency",
            "Magic Cost Reduction",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            9,
            "MP Amount",
        )
        self.book["Monk Root 1 Silence"] = power(
            "Silence",
            "Monk Root 1 Silence",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            7,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Monk Tier 1 Heal"] = power(
            "Heal",
            "Monk Tier 1 Heal",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Move After Attacking"] = power(
            "Hit and Run",
            "Move After Attacking",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            6,
            "Movement Speed",
            bannedClasses=["Knight"],
        )
        self.book[
            "Move an Additional Tile As Long As You Don't Move On Unstable Ground"
        ] = power(
            "Mounted Movement",
            "Move an Additional Tile As Long As You Don't Move On Unstable Ground",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            7,
            "Movement Speed",
            antiStat=["Intelligence"],
        )
        self.book["Move Faster On Holy Ground"] = power(
            "Beautiful Strides",
            "Move Faster On Holy Ground",
            "Catachumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            "Movement Speed",
        )
        self.book["Move Right One More Tile If Ally Present"] = power(
            "To The Frontlines",
            "Move Right One More Tile If Ally Present",
            "Warrior",
            ["Luck", "Stamina", "Strength"],
            6,
            "Movement Speed",
        )
        self.book["Movement Does Not Interupt Your Singing"] = power(
            "Rhythmic Chanting",
            "Movement Does Not Interupt Your Singing",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Ninja Tier 1 Ninja Fire"] = power(
            "Ninja Fire",
            "Ninja Tier 1 Ninja Fire",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            8,
            "Fire Damage",
            spellRank=True,
        )
        self.book["One Negative Status Cleanses Itself Each Turn"] = power(
            "Pure of Heart",
            "One Negative Status Cleanses Itself Each Turn",
            "Peregrine",
            ["Faith", "Speed"],
            9,
            "FP Amount",
        )
        self.book["Orator Tier 1 Shield"] = power(
            "Shield",
            "Orator Tier 1 Shield",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            7,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Peregrine Root 1 Dispel"] = power(
            "Dispel",
            "Peregrine Root 1 Dispel",
            "Peregrine",
            ["Faith", "Speed"],
            9,
            "FP Amount",
            spellRank=True,
        )
        self.book["Peregrine Tier 1 Blast"] = power(
            "Blast",
            "Peregrine Tier 1 Blast",
            "Peregrine",
            ["Faith", "Speed"],
            9,
            "Wind Damage",
            spellRank=True,
        )
        self.book["Prevent Focus Lost From Enemy Attacks"] = power(
            "True Grit",
            "Prevent Focus Lost From Enemy Attacks",
            "Soldier",
            ["Dexterity", "Focus", "Strength"],
            7,
            "Focus Intensity",
        )
        self.book["Priest Root 1 Detox"] = power(
            "Detox",
            "Priest Root 1 Detox",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            7,
            "FP Amount",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Priest Root 1 Heal"] = power(
            "Heal",
            "Priest Root 1 Heal",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Priest Tier 1 Heal"] = power(
            "Heal",
            "Priest Tier 1 Heal",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Prophet Root 1 Aura"] = power(
            "Aura",
            "Prophet Root 1 Aura",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            7,
            "Healing Amount",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Prophet Root 1 Heal"] = power(
            "Heal",
            "Prophet Root 1 Heal",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            7,
            "Healing Amount",
            spellRank=True,
        )
        self.book["Prophet Tier 1 Slow"] = power(
            "Slow",
            "Prophet Tier 1 Slow",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            7,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Random Additional Spell I"] = power(
            "Mercurial Knowledge I",
            "Random Additional Spell I",
            "Alchemist",
            ["Faith", "Luck"],
            9,
            "Luckiness",
        )
        self.book["Ranged Attacks Add Resonance to Target's Tile"] = power(
            "Whistling Shots",
            ["Ranged Attacks Add Resonance to Target's Tile"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            7,
            "Vocal Strength",
        )
        self.book["Receive Commmands From Further Away"] = power(
            "Under Authority",
            "Receive Commmands From Further Away",
            "Soldier",
            ["Dexterity", "Focus", "Strength"],
            7,
            "Fame",
        )
        self.book["Reduces Critical Hit Damage Taken"] = power(
            "Heavy Plate",
            "Reduces Critical Hit Damage Taken",
            "Steam Knight",
            ["Focus", "Stamina"],
            8,
            "HP Amount",
        )
        self.book["Reduces Damage Taken From Vocal Attacks"] = power(
            "Studied Ignorance",
            "Reduces Damage Taken From Vocal Attacks",
            "Valkyrie",
            ["Stamina", "Voice"],
            9,
            "Vocal Strength",
        )
        self.book["Reduces the Effect of Unholy Ground By One Rank"] = power(
            "Blessed Shield",
            "Reduces the Effect of Unholy Ground By One Rank",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            7,
            "Damage On Unholy Ground",
            antiStat=["Intelligence"],
        )
        self.book["Regenerate Health On Holy Ground"] = power(
            "Sustenance",
            "Regenerate Health On Holy Ground",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            6,
            "Damage On Unholy Ground",
        )
        self.book["Resist Magic, But Gain Fire and Melee Physical Vulnerability"] = power(
            "Glass Cannon",
            "Resist Magic, But Gain Fire and Melee Physical Vulnerability",
            "Wizard",
            ["Intelligence", "Stamina"],
            9,
            "Ice Damage",
        )
        self.book["Samurai Root 1 Boost"] = power(
            "Boost",
            ["Samurai Root 1 Boost"],
            "Samurai",
            ["Charisma", "Faith", "Stamina"],
            10,
            "Faith Amount",
            spellRank=True,
        )
        self.book["Scholar Root 1 Muddle"] = power(
            "Muddle",
            ["Scholar Root 1 Muddle"],
            "Scholar",
            ["Intelligence", "Focus"],
            9,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Scholar Tier 1 Silence"] = power(
            "Silence",
            ["Scholar Tier 1 Silence"],
            "Scholar",
            ["Intelligence", "Focus"],
            9,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Scholar Root 1 Sleep"] = power(
            "Sleep",
            ["Scholar Root 1 Sleep"],
            "Scholar",
            ["Intelligence", "Focus"],
            9,
            "Status Effectiveness",
            spellRank=True,
        )
        self.book["Single Sword Attacks Grant Focus Charge"] = power(
            "Iaijutsu",
            ["Single Sword Attacks Grant Focus Charge"],
            "Samurai",
            ["Charisma", "Faith", "Stamina"],
            10,
            "Focus Amount",
        )
        self.book[
            "Slower Movement That Ignores Terrain Cost And Blockers"
        ] = power(
            "Unhindered Movement",
            "Slower Movement That Ignores Terrain Cost And Blockers",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            7,
            "Movement Speed",
        )
        self.book["Sorceror Root 1 Apollo"] = power(
            "Apollo",
            "Sorceror Root 1 Apollo",
            "Sorceror",
            ["Intelligence", "Voice"],
            9,
            "Fire Damage",
            spellRank=True,
        )
        self.book["Sorceror Root 1 Dao"] = power(
            "Dao",
            "Sorceror Root 1 Dao",
            "Sorceror",
            ["Intelligence", "Voice"],
            9,
            "Earth Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Sorceror Tier 1 Dao"] = power(
            "Dao",
            "Sorceror Tier 1 Dao",
            "Sorceror",
            ["Intelligence", "Voice"],
            9,
            "Earth Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Swap-move With Most Damaged Ally If No Space Available"] = power(
            "Castle Move",
            "Swap-move With Most Damaged Ally If No Space Available",
            "Warrior",
            ["Luck", "Stamina", "Strength"],
            6,
            "Movement Speed",
        )
        self.book["Tile Resonance Increases Charisma Effects"] = power(
            "Bragging Verse",
            "Tile Resonance Increases Charisma Effects",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            5,
            "Vocal Strength",
        )
        self.book["Trickster Root 1 Teleport"] = power(
            "Teleport",
            "Trickster Root 1 Teleport",
            "Trickster",
            ["Intelligence", "Speed"],
            8,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Trickster Tier 1 Teleport"] = power(
            "Teleport",
            "Trickster Tier 1 Teleport",
            "Trickster",
            ["Intelligence", "Speed"],
            8,
            "Lightning Damage",
            spellRank=True,
        )
        self.book["Unarmed Attacks Deal Fire Damage"] = power(
            "Burning Hands",
            "Unarmed Attacks Deal Fire Damage",
            "Survivor",
            ["Luck", "Speed", "Stamina", "Strength"],
            8,
            "Fire Damage",
            requiresDragonOr25=True,
        )
        self.book["Vocal Attacks Act As If Tiles Are One Rank More Holy"] = power(
            "Sacred Hymns",
            "Vocal Attacks Act As If Tiles Are One Rank More Holy",
            "Chorister",
            ["Dexterity", "Focus", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Vocal Attacks Do Not Interupt Singing"] = power(
            "Harmony",
            "Vocal Attacks Do Not Interupt Singing",
            "Chorister",
            ["Dexterity", "Focus", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Vocal Attacks Have A Chance To Add Bleed"] = power(
            "Piercing Screams",
            "Vocal Attacks Have A Chance To Add Bleed",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            7,
            "Vocal Strength",
        )
        self.book["Vocal Attacks Have A Change To Double Attack"] = power(
            "Vocal Agility",
            "Vocal Attacks Have A Change To Double Attack",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            6,
            "Vocal Strength",
        )
        self.book["When Focused, Double Your Luck"] = power(
            "Make Your Own Luck",
            "When Focused, Double Your Luck",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            6,
            "Vocal Strength",
        )
        self.book["When Focused, Spell Are Free"] = power(
            "Transcendant Ninjitsu",
            "When Focused, Spell Are Free",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            8,
            "MP Amount",
        )
        self.book["Wizard Root 1 Freeze"] = power(
            "Freeze",
            "Wizard Root 1 Freeze",
            "Wizard",
            ["Intelligence", "Stamina"],
            9,
            "Ice Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Wizard Tier 1 Freeze"] = power(
            "Freeze",
            "Wizard Tier 1 Freeze",
            "Wizard",
            ["Intelligence", "Stamina"],
            9,
            "Ice Damage",
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Your Vocal Attack Damage is Increased By Missing Health"] = power(
            "Higher Notes",
            "Your Vocal Attack Damage is Increased By Missing Health",
            "Valkyrie",
            ["Stamina", "Voice"],
            9,
            "Vocal Strength",
        )
        self.book["Your Vocal Attacks Ignore Penalty From Evil Resonance"] = power(
            "Overcome the Darkness",
            "Your Vocal Attacks Ignore Penalty From Evil Resonance",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            6,
            "Vocal Strength",
        )
        self.book["Your Voice Statistic Contributes to Defense"] = power(
            "Basso Voice",
            "Your Voice Statistic Contributes to Defense",
            "Valkyrie",
            ["Stamina", "Voice"],
            9,
            "Vocal Strength",
        )
        self.book["Your Resonating Tiles Stay Resonating Longer"] = power(
            "Sustaining Notes",
            "Your Resonating Tiles Stay Resonating Longer",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            7,
            "Vocal Strength",
        )

        # Tier two powers
        self.book["Archmage Tier 2 Bolt"] = power(
            "Bolt",
            "Archmage Tier 2 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            8,
            "Lightning Damage",
            [self.book["Archmage Tier 1 Bolt"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Arrows: Increases Damage I"] = power(
            "Composite Grip",
            "Arrows: Increases Damage I",
            "Archer",
            ["Focus", "Dexterity"],
            8,
            "Arrows Skill",
            [self.book["Arrows: Add Effect: Poison"]],
        )
        self.book["Assassin Tier 2 Death"] = power(
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
        self.book["Attack an Additional Enemy In Melee Range"] = power(
            "Cleaving Attacks",
            "Attack an Additional Enemy In Melee Range",
            "Warrior",
            ["Luck", "Stamina", "Strength"],
            5,
            "Heavy Attack Chance",
            [self.book["Defense Against Melee Damage"]],
        )
        self.book["Attack Each Enemy In Range On Death"] = power(
            "Final Stand",
            ["Attack Each Enemy In Range On Death"],
            "Berserker",
            ["Stamina", "Strength"],
            9,
            "Axe Skill",
            [self.book["Berserker Tier 1 Berserking"]],
            antiStat=["Luck"],
        )
        self.book["Attacks Are Always Heavy When Your Health Is Full"] = power(
            "Unhindered Movement",
            "Attacks Are Always Heavy When Your Health Is Full",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            6,
            "Heavy Attack Chance",
            [self.book["Slower Movement That Ignores Terrain Cost And Blockers"]],
        )
        self.book["Banshee Tier 2 Axe Damage"] = power(
            "Axe Damage",
            "Banshee Tier 2 Axe Damage",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            4,
            "Axe Skill",
            [self.book["Tile Resonance Increases Charisma Effects"]],
        )
        self.book["Bishop Tier 2 Aura"] = power(
            "Aura",
            ["Bishop Tier 2 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            9,
            "Healing Amount",
            [self.book["Bishop Tier 1 Aura"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Bleeding Enemies Heal You"] = power(
            "Vampiric Thirst",
            ["Bleeding Enemies Heal You"],
            "Baron",
            ["Charisma", "Strength"],
            9,
            "Drained Health",
            [self.book["Baron Tier 1 Drain On Crit"]],
            antiStat=["Intelligence"],
        )
        self.book["Bleeding Enemies Give MP"] = power(
            "Essence",
            ["Bleeding Enemies Give MP"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            7,
            "MP Amount",
            [self.book["Blood Mage Tier 1 Drain"]],
            spellRank=True,
        )
        self.book["Blood Mage Tier 2 Essence"] = power(
            "Essence",
            ["Blood Mage Tier 2 Essence"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            7,
            "MP Amount",
            [self.book["Blood Mage Tier 1 Drain"]],
            spellRank=True,
        )
        self.book["Channeller Tier 2 Silence"] = power(
            "Silence",
            "Channeller Tier 2 Silence",
            "Channeller",
            ["Dexterity", "Intelligence"],
            8,
            "Status Effectiveness",
            [self.book["Channeller Tier 1 Surge"]],
            spellRank=True,
        )
        self.book["Channeller Tier 2 Surge"] = power(
            "Surge",
            "Channeller Tier 2 Surge",
            "Channeller",
            ["Dexterity", "Intelligence"],
            8,
            "Water Damage",
            [self.book["Channeller Tier 1 Surge"]],
            spellRank=True,
        )
        self.book["Charm Targets Instead of Routing Them"] = power(
            "Siren Song",
            "Charm Targets Instead of Routing Them",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            4,
            "Status Effectiveness",
            [self.book["Tile Resonance Increases Charisma Effects"]],
        )
        self.book["Convert Faith and Magic"] = power(
            "Mercurial Exchange",
            "Convert Faith and Magic",
            "Alchemist",
            ["Faith", "Luck"],
            8,
            "MP Amount",
            [self.book["Random Additional Spell I"]],
        )
        self.book["Command: Casting Does Not Interupt Your Singing"] = power(
            "Melodious Spellweaving",
            ["Command: Casting Does Not Interupt Your Singing"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            6,
            "Vocal Strength",
            [self.book["Command: MP Regeneration"]],
        )
        self.book["Command: Increases Defense On Resonant Tiles"] = power(
            "Radiant Shield",
            "Command: Increases Defense On Resonant Tiles",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            6,
            "Vocal Strength",
            [self.book["Increases Your Area Of Holy Resonance To Five Tiles"]],
        )
        self.book["Command: Reduces Damage Taken From Vocal Attacks"] = power(
            "Outshout for the Audience",
            "Command: Reduces Damage Taken From Vocal Attacks",
            "Valkyrie",
            ["Stamina", "Voice"],
            8,
            "Vocal Strength",
            [self.book["Your Vocal Attack Damage is Increased By Missing Health"]]
        )
        self.book["Counter Enemy Attacks By Inflicting Bleed"] = power(
            "Sharpness",
            "Counter Enemy Attacks By Inflicting Bleed",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            6,
            "Daggers Skill",
            [self.book["Double Chances For Multiple Attacks"]],
        )
        self.book[
            "Counter Enemy Attacks By Adding A Rank Of Holy Resonance To The Source Tile"
        ] = power(
            "Counterpoint",
            "Counter Enemy Attacks By Adding A Rank Of Holy Resonance To The Source Tile",
            "Chorister",
            ["Dexterity", "Focus", "Voice"],
            6,
            "Vocal Strength",
            [self.book["Vocal Attacks Act As If Tiles Are One Rank More Holy"]],
        )
        self.book[
            "Counter Enemy Attacks By Casting A Random Spell You Know"
        ] = power(
            "Magical Riposte",
            ["Counter Enemy Attacks By Casting A Random Spell You Know"],
            "Scholar",
            ["Intelligence", "Focus"],
            8,
            "MP Amount",
            [self.book["Scholar Tier 1 Silence"]],
        )
        self.book["Counter Enemy Attacks That You Dodged"] = power(
            "Aerialist Counterattack",
            "Counter Enemy Attacks That You Dodged",
            "Sky Battler",
            ["Charisma", "Dexterity", "Luck", "Speed", "Stamina"],
            4,
            "Swords Skill",
            [self.book["Flying Movement"]],
        )
        self.book["Counter Enemy Vocal Attacks With Bleed"] = power(
            "Lacerating Response",
            "Counter Enemy Vocal Attacks With Bleed",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            6,
            "Daggers Skill",
            [self.book["Vocal Attacks Have A Chance To Add Bleed"]],
        )
        self.book["Critical Attacks Grant Temporary Damage Reduction"] = power(
            "Monster Armor",
            "Critical Attacks Grant Temporary Damage Reduction",
            "Survivor",
            ["Luck", "Speed", "Stamina", "Strength"],
            7,
            "HP Amount",
            [self.book["Unarmed Attacks Deal Fire Damage"]],
            requiresDragonOr25=True,
        )
        self.book["Critical Hits Reduce Next Spell Cost to 0"] = power(
            "Stroke of Luck",
            ["Critical Hits Reduce Next Spell Cost to 0"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            6,
            "Luckiness",
            [self.book["Command: MP Regeneration"]],
        )
        self.book["Critical Attacks Cast Muddle On Target"] = power(
            "Disorienting Criticals",
            "Critical Attacks Cast Muddle On Target",
            "Titan",
            ["Focus", "Strength"],
            "Heavy Attack Chance",
            10,
            [self.book["Increases Heavy Attack Chance"]],
            antiStat=["Speed"],
        )
        self.book["Dark Mage Tier 2 Death"] = power(
            "Death",
            "Dark Mage Tier 2 Death",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            8,
            "Status Effectiveness",
            [self.book["Defense Against Magic Damage"]],
            spellRank=True,
        )
        self.book["Dark Mage Tier 2 Silence"] = power(
            "Silence",
            "Dark Mage Tier 2 Silence",
            "Dark Mage",
            ["Charisma", "Intelligence"],
            8,
            "Status Effectiveness",
            [self.book["Defense Against Magic Damage"]],
            spellRank=True,
        )
        self.book["Dodge Attacks That You Counter"] = power(
            "Parry",
            "Dodge Attacks That You Counter",
            "Duelist",
            ["Charisma", "Luck", "Speed", "Stamina"],
            6,
            "Swords Skill",
            [self.book["Duelist Counterattack"]],
            antiStat=["Faith"],
        )
        self.book["Dodging Grants Focus Charge"] = power(
            "Adrenaline Rush",
            ["Dodging Grants Focus Charge"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            6,
            "Focus Amount",
            [self.book["Increases Luck When Outnumbered"]],
        )
        self.book["Double the Chance of Multiple Ranged Attacks"] = power(
            "True Grit",
            "Double the Chance of Multiple Ranged Attacks",
            "Soldier",
            ["Dexterity", "Focus", "Strength"],
            7,
            "Focus Intensity",
        )
        self.book["Double Rout Chance Against Bleeding Targets"] = power(
            "Blood Cries Out",
            "Double Rout Chance Against Bleeding Targets",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            6,
            "Fame",
            [self.book["Vocal Attacks Have A Chance To Add Bleed"]],
        )
        self.book["Druid Tier 2 Conduit"] = power(
            "Conduit",
            "Druid Tier 2 Conduit",
            "Druid",
            ["Dexterity", "Faith"],
            8,
            "FP Amount",
            [self.book["Druid Tier 1 Natural Resistance"]],
            spellRank=True,
        )
        self.book["Druid Tier 2 Detox"] = power(
            "Detox",
            "Druid Tier 2 Detox",
            "Druid",
            ["Dexterity", "Faith"],
            8,
            "FP Amount",
            [self.book["Druid Tier 1 Natural Resistance"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book[
            "Enemy Lance and Spear Users Must Attack You If Possible"
        ] = power(
            "Knight's Challenge",
            "Enemy Lance and Spear Users Must Attack You If Possible",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            6,
            "HP Amount",
            [self.book["Reduces the Effect of Unholy Ground By One Rank"]],
            antiStat=["Intelligence"],
        )
        self.book["Fire Damage Consumes Bleed To Deal Double Damage"] = power(
            "Cauterize",
            "Fire Damage Consumes Bleed To Deal Double Damage",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            8,
            "Fire Damage",
            [self.book["Flamecaster Tier 1 Blaze"]],
        )
        self.book["Flamecaster Tier 2 Blaze"] = power(
            "Blaze",
            "Flamecaster Tier 2 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            8,
            "Fire Damage",
            [self.book["Flamecaster Tier 1 Blaze"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Heavy and Critical Attacks Ground Flying Enemies"] = power(
            "Wing Clip",
            ["Heavy and Critical Attacks Ground Flying Enemies"],
            "Sky Lord",
            ["Focus", "Intelligence", "Speed"],
            "Status Effectiveness",
            6,
            [self.book["Increases Damage Dealt To Flying Enemies"]],
        )
        self.book["Heavy Attacks Inflict Bleed"] = power(
            "Bloodied Blades",
            "Heavy Attacks Inflict Bleed",
            "Warrior",
            ["Luck", "Stamina", "Strength"],
            5,
            "Heavy Attack Chance",
            [self.book["Defense Against Melee Damage"]],
        )
        self.book["Hero Tier 2 Bolt"] = power(
            "Bolt",
            "Hero Tier 2 Bolt",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            6,
            "Lightning Damage",
            [self.book["Hero Tier 1 Bolt"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Ice Damage Inflicts Bleed"] = power(
            "Sharpened Ice",
            "Ice Damage Inflicts Bleed",
            "Wizard",
            ["Intelligence", "Stamina"],
            8,
            "Ice Damage",
            [self.book["Wizard Tier 1 Freeze"]]
        )
        self.book["Increases Damage Dealt On Unholy Ground"] = power(
            "Paladin",
            "Increases Damage Dealt On Unholy Ground",
            "Knight",
            ["Charisma", "Speed", "Stamina", "Strength"],
            6,
            "Damage On Unholy Ground",
            [self.book["Reduces the Effect of Unholy Ground By One Rank"]],
            antiStat=["Intelligence"],
        )
        self.book["Increases Damage Dealt To Flying And Mounted Enemies"] = power(
            "Leap Attack",
            "Increases Damage Dealt To Flying And Mounted Enemies",
            "Werewolf",
            ["Dexterity", "Speed", "Stamina", "Strength"],
            7,
            "Movement Speed",
            self.book["Ignore Opponents When Moving To Tiles With Damaged Enemies"],
            antiStat=["Luck"]
        )
        self.book["Increases Dodge Chance Against Flying Enemies"] = power(
            "Dogfighting",
            ["Increases Dodge Chance Against Flying Enemies"],
            "Sky Lord",
            ["Focus", "Intelligence", "Speed"],
            "Dodge Chance",
            6,
            [self.book["Increases Damage Dealt To Flying Enemies"]],
        )
        self.book[
            "Increases Dodge Chance Against The First Enemy To Attack You Each Round"
        ] = power(
            "Aerial Agility",
            "Increases Dodge Chance Against The First Enemy To Attack You Each Round",
            "Sky Battler",
            ["Charisma", "Dexterity", "Luck", "Speed", "Stamina"],
            4,
            "Dodge Chance",
            [self.book["Flying Movement"]],
        )
        self.book["Increases Focus When Outnumbered"] = power(
            "Against All Odds",
            ["Increases Focus When Outnumbered"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            6,
            "Focus Intensity",
            [self.book["Increases Luck When Outnumbered"]],
        )
        self.book["Increases Focus When Stationary"] = power(
            "Unhindered Movement",
            "Increases Focus When Stationary",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            6,
            "Focus Intensity",
            [self.book["Slower Movement That Ignores Terrain Cost And Blockers"]],
        )
        self.book["Increases Healing Magic Range By 1"] = power(
            "Heal",
            "Increases Healing Magic Range By 1",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            6,
            "Healing Amount",
            [self.book["Priest Tier 1 Heal"]],
        )
        self.book["Increases Healing To Allies On Unholy Ground"] = power(
            "Heal",
            "Increases Healing To Allies On Unholy Ground",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            6,
            "Healing Amount",
            [self.book["Monk Tier 1 Heal"]],
        )
        self.book["Killing Enemies Gives MP"] = power(
            "Destiny Unveiled",
            "Killing Enemies Gives MP",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            6,
            "MP Amount",
            [self.book["Hero Tier 1 Bolt"]],
        )
        self.book["Killing Enemies Grants a Rank of Focus"] = power(
            "Professionalism",
            "Killing Enemies Grants a Rank of Focus",
            "Soldier",
            ["Dexterity", "Focus", "Strength"],
            6,
            "Focus Intensity",
            [self.book["Prevent Focus Lost From Enemy Attacks"]],
        )
        self.book[
            "Lance Attacks Grant Vulnerability Against Known Spell Schools"
        ] = power(
            "Conductive Lance",
            "Lance Attacks Grant Vulnerability Against Known Spell Schools",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            4,
            "Lances Skill",
            [self.book["Mage Knight Root 1 Blaze"]],
        )
        self.book["Lightning Damage Breaks Focus"] = power(
            "Sudden Shock",
            "Lightning Damage Breaks Focus",
            "Archmage",
            ["Intelligence", "Luck"],
            8,
            "Lightning Damage",
            [self.book["Archmage Tier 1 Bolt"]],
        )
        self.book["Lost Health Increases Turn Speed"] = power(
            "Tunnel Vision",
            ["Lost Health Increases Turn Speed"],
            "Berserker",
            ["Stamina", "Strength"],
            9,
            "Axes Skill",
            [self.book["Berserker Tier 1 Berserking"]],
            antiStat=["Luck"],
        )
        self.book["Monk Tier 2 Heal"] = power(
            "Heal",
            "Monk Tier 2 Heal",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            6,
            "Healing Amount",
            [self.book["Monk Tier 1 Heal"]],
            spellRank=True,
        )
        self.book["Move To Follow Routed Enemies And Attack Again"] = power(
            "Follow-on Attack",
            "Move To Follow Routed Enemies And Attack Again",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            6,
            "Fame",
            [self.book["Double Chances For Multiple Attacks"]],
        )
        self.book["Ninja Tier 2 Ninja Bolt"] = power(
            "Ninja Bolt",
            "Ninja Tier 2 Ninja Bolt",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            7,
            "Lightning Damage",
            [self.book["Ninja Tier 1 Ninja Fire"]],
            spellRank=True,
        )
        self.book["Ninja Tier 2 Ninja Fire"] = power(
            "Ninja Fire",
            "Ninja Tier 2 Ninja Fire",
            "Ninja",
            ["Dexterity", "Intelligence", "Speed"],
            7,
            "Fire Damage",
            [self.book["Ninja Tier 1 Ninja Fire"]],
            spellRank=True,
        )
        self.book["Peregrine Tier 2 Blast"] = power(
            "Blast",
            "Peregrine Tier 2 Blast",
            "Peregrine",
            ["Faith", "Speed"],
            8,
            "Wind Damage",
            [self.book["Peregrine Tier 1 Blast"]],
            spellRank=True,
        )
        self.book["Prevent Enemy Counterattacks"] = power(
            "Smoke Bomb",
            "Prevent Enemy Counterattacks",
            "Assassin",
            ["Dexterity", "Strength", "Luck"],
            5,
            "Swords Skill",
            [self.book["Move After Attacking"]],
            bannedClasses=["Knight"],
        )
        self.book["Priest Tier 2 Heal"] = power(
            "Heal",
            "Priest Tier 2 Heal",
            "Priest",
            ["Charisma", "Faith", "Intelligence"],
            6,
            "Healing Amount",
            [self.book["Priest Tier 1 Heal"]],
            spellRank=True,
        )
        self.book["Prophet Tier 2 Aura"] = power(
            "Aura",
            "Prophet Tier 2 Aura",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            6,
            "Healing Amount",
            [self.book["Prophet Tier 1 Slow"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Prophet Tier 2 Quick"] = power(
            "Quick",
            "Prophet Tier 2 Quick",
            "Prophet",
            ["Charisma", "Faith", "Voice"],
            6,
            "FP Amount",
            [self.book["Prophet Tier 1 Slow"]],
            spellRank=True,
        )
        self.book["Pursue Enemies You Rout And Attack Again"] = power(
            "Dogged Hunter",
            "Pursue Enemies You Rout And Attack Again",
            "Werewolf",
            ["Dexterity", "Speed", "Stamina", "Strength"],
            7,
            "Movement Speed",
            self.book["Ignore Opponents When Moving To Tiles With Damaged Enemies"],
            antiStat=["Luck"]
        )
        self.book["Random Additional Spell II"] = power(
            "Mercurial Knowledge II",
            "Random Additional Spell II",
            "Alchemist",
            ["Faith", "Luck"],
            8,
            "Luckiness",
            [self.book["Random Additional Spell I"]],
        )
        self.book["Ranged Attacks Don't Miss"] = power(
            "Aimed Shot",
            "Ranged Attacks Don't Miss",
            "Archer",
            ["Focus", "Dexterity"],
            8,
            "Arrows Skill",
            [self.book["Arrows: Add Effect: Poison"]],
        )
        self.book["Reduces Chance To Be Inflicted By Status Spells"] = power(
            "Defense Against The Dark Arts",
            "Reduces Chance To Be Inflicted By Status Spells",
            "Mage Knight",
            ["Charisma", "Intelligence", "Speed", "Strength"],
            4,
            "Swords Skill",
            [self.book["Mage Knight Root 1 Blaze"]],
        )
        self.book[
            "Reduces Damage For Each Status Effect You Are Suffering"
        ] = power(
            "Overcomer",
            "Reduces Damage For Each Status Effect You Are Suffering",
            "Survivor",
            ["Luck", "Speed", "Stamina", "Strength"],
            7,
            "HP Amount",
            [self.book["Unarmed Attacks Deal Fire Damage"]],
            requiresDragonOr25=True,
        )
        self.book["Reduces Damage From Enemy Area Attacks"] = power(
            "Get Down!",
            "Reduces Damage From Enemy Area Attacks",
            "Soldier",
            ["Dexterity", "Focus", "Strength"],
            6,
            "Focus Intensity",
            [self.book["Prevent Focus Lost From Enemy Attacks"]],
        )
        self.book["Samurai Tier 2 Boost"] = power(
            "Boost",
            ["Samurai Tier 2 Boost"],
            "Samurai",
            ["Charisma", "Faith", "Stamina"],
            9,
            "Faith Amount",
            [
                self.book[
                    "Increases Sword Damage If You Haven't Moved Since Last Attack"
                ]
            ],
            spellRank=True,
        )
        self.book["Sorceror Tier 2 Atlas"] = power(
            "Atlas",
            "Sorceror Tier 2 Atlas",
            "Sorceror",
            ["Intelligence", "Voice"],
            8,
            "Lightning Damage",
            [self.book["Sorceror Tier 1 Dao"]],
            spellRank=True,
        )
        self.book["Sorceror Tier 2 Poseidon"] = power(
            "Poseidon",
            "Sorceror Tier 2 Poseidon",
            "Sorceror",
            ["Intelligence", "Voice"],
            8,
            "Water Damage",
            [self.book["Sorceror Tier 1 Dao"]],
            spellRank=True,
        )
        self.book["Staff Skills Increase the Damage of Vocal Attacks"] = power(
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
        ] = power(
            "Brilliant Radiance",
            "Spells You Target On One Of Your Resonating Tiles Target All Your Resonating Tiles",
            "Orator",
            ["Charisma", "Intelligence", "Voice"],
            6,
            "Vocal Strength",
            [self.book["Increases Your Area Of Holy Resonance To Five Tiles"]],
        )
        self.book["Taking Magic Damage Adds A Focus Rank"] = power(
            "Boiling Point",
            "Taking Magic Damage Adds A Focus Rank",
            "Steam Knight",
            ["Focus", "Stamina"],
            7,
            "Focus Intensity",
            [self.book["Increases Focus When Stationary"]],
        )
        self.book["Teleporting Does Not End Turns"] = power(
            "Flash Steps",
            "Teleporting Does Not End Turns",
            "Trickster",
            ["Intelligence", "Speed"],
            7,
            "Lightning Damage",
            [self.book["Trickster Tier 1 Teleport"]],
            spellRank=True,
        )
        self.book["Trickster Tier 2 Portal"] = power(
            "Portal",
            "Trickster Tier 2 Portal",
            "Trickster",
            ["Intelligence", "Speed"],
            7,
            "Lightning Damage",
            [self.book["Trickster Tier 1 Teleport"]],
            spellRank=True,
        )
        self.book["Unarmed Range + 1 and deals wind damage"] = power(
            "Throw the Wind",
            "Unarmed Range + 1 and deals wind damage",
            "Peregrine",
            ["Faith", "Speed"],
            8,
            "Unarmed Skill",
            [self.book["Peregrine Tier 1 Blast"]],
        )
        self.book[
            "Use Greatest of Charisma, Faith, or Strength to deal Fire Damage When Attacking"
        ] = power(
            "Boost",
            "Use Greatest of Charisma, Faith, or Strength to deal Fire Damage When Attacking",
            "Samurai",
            ["Charisma", "Faith", "Stamina"],
            9,
            "Faith Amount",
            [
                self.book[
                    "Increases Sword Damage If You Haven't Moved Since Last Attack"
                ]
            ],
        )
        self.book["When Focused, All Area Spells Have Double Power"] = power(
            "Fervent Prayer",
            "When Focused, All Area Spells Have Double Power",
            "Bishop",
            ["Faith", "Focus"],
            9,
            "Focus Intensity",
            [self.book["Bishop Tier 1 Aura"]],
        )
        self.book["When Focused, All Attacks Stun"] = power(
            "Titanic Smash",
            "When Focused, All Attacks Stun",
            "Titan",
            ["Focus", "Strength"],
            "Heavy Attack Chance",
            10,
            [self.book["Increases Heavy Attack Chance"]],
            antiStat=["Speed"],
        )
        self.book["When Focused, All Status Spells Always Succeed"] = power(
            "Complete Knowledge",
            ["When Focused, All Status Spells Always Succeed"],
            "Scholar",
            ["Intelligence", "Focus"],
            8,
            "Focus Amount",
            [self.book["Scholar Tier 1 Silence"]],
        )
        self.book["When Focused, Strength is Doubled"] = power(
            "Pneumatic Musculature",
            "When Focused, Strength is Doubled",
            "Steam Knight",
            ["Focus", "Stamina"],
            7,
            "Focus Intensity",
            [self.book["Increases Focus When Stationary"]],
        )
        self.book["Wizard Tier 2 Freeze"] = power(
            "Freeze",
            "Wizard Tier 2 Freeze",
            "Wizard",
            ["Intelligence", "Stamina"],
            8,
            "Ice Damage",
            [self.book["Wizard Tier 1 Freeze"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book[
            "Vocal Attack Targets Skip Their Next Attempt To Resist Status Effects"
        ] = power(
            "Jarring Shout",
            "Vocal Attack Targets Skip Their Next Attempt To Resist Status Effects",
            "Oracle",
            ["Charisma", "Focus", "Luck", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Vocal Attacks Have A Change To Double Attack"]],
        )
        self.book["Vocal Attacks Can Target Any Tile You Are Resonating"] = power(
            "Voice From The Clouds",
            "Vocal Attacks Can Target Any Tile You Are Resonating",
            "Chorister",
            ["Dexterity", "Focus", "Voice"],
            6,
            "Vocal Strength",
            [self.book["Vocal Attacks Act As If Tiles Are One Rank More Holy"]],
        )
        self.book["Vocal Attacks Have a Chance to Deafen Targets"] = power(
            "Earsplitting Notes",
            "Vocal Attacks Have a Chance to Deafen Targets",
            "Valkyrie",
            ["Stamina", "Voice"],
            8,
            "Vocal Strength",
            [self.book["Your Vocal Attack Damage is Increased By Missing Health"]]
        )

        self.book["Vocal Cascade With Weapons"] = power(
            "Santified Movements",
            "Vocal Cascade With Weapons",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Catechumen Tier 1 Vocal Cascade"]],
        )
        self.book["Vocal Cascade Without Full Holy Resonance"] = power(
            "Indwelling Echoes",
            "Vocal Cascade Without Full Holy Resonance",
            "Catechumen",
            ["Charisma", "Dexterity", "Strength", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Catechumen Tier 1 Vocal Cascade"]],
        )
        self.book["Your Bleeding Heals Allies On Your Tile"] = power(
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
        ] = power(
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
        self.book["Archmage Tier 3 Bolt"] = power(
            "Bolt",
            "Archmage Tier 2 Bolt",
            "Archmage",
            ["Intelligence", "Luck"],
            7,
            "Lightning Damage",
            [self.book["Archmage Tier 2 Bolt"]],
            [self.book["Lightning Damage Breaks Focus"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Add the Command Keyword to All Your Powers"] = power(
            "Bardic Leadership",
            ["Add the Command Keyword to All Your Powers"],
            "Bard",
            ["Charisma", "Dexterity", "Luck"],
            5,
            "Luckiness",
            [self.book["Command: Casting Does Not Interupt Your Singing"]],
            [self.book["Critical Hits Reduce Next Spell Cost to 0"]],
        )
        self.book["Arrows: Increases Range"] = power(
            "Far Shot",
            "Arrows: Increases Range",
            "Archer",
            ["Focus", "Dexterity"],
            7,
            "Arrows Skill",
            [self.book["Arrows: Increases Damage I"]],
            [self.book["Ranged Attacks Don't Miss"]],
        )
        self.book["Attacks Deal Wind Damage, Hit an Additional Melee Target, Cause Bleed"] = power(
            "Whirlwind Attacks",
            "Attacks Deal Wind Damage, Hit an Additional Melee Target, Cause Bleed",
            "Warrior",
            ["Luck", "Stamina", "Strength"],
            4,
            "Heavy Attack Chance",
            [self.book["Attack an Additional Enemy In Melee Range"]],
            [self.book["Heavy Attacks Inflict Bleed"]],
        )
        self.book["Berserker Tier 3 Berserking"] = power(
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
        self.book["Bishop Tier 3 Aura"] = power(
            "Aura",
            ["Bishop Tier 3 Aura"],
            "Bishop",
            ["Faith", "Focus"],
            8,
            "Healing Amount",
            [self.book["Bishop Tier 2 Aura"]],
            [self.book["When Focused, All Area Spells Have Double Power"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Blood Mage Tier 3 Drain"] = power(
            "Drain",
            ["Blood Mage Tier 3 Drain"],
            "Blood Mage",
            ["Intelligence", "Stamina"],
            6,
            "Drained Health",
            [self.book["Bleeding Enemies Give MP"]],
            [self.book["Blood Mage Tier 2 Essence"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Can Make Triple Attacks"] = power(
            "Triple Attack",
            "Can Make Triple Attacks",
            "Jongleur",
            ["Charisma", "Dexterity", "Focus"],
            5,
            "Daggers Skill",
            [self.book["Counter Enemy Attacks By Inflicting Bleed"]],
            [self.book["Move To Follow Routed Enemies And Attack Again"]],
        )
        self.book["Catechumen Tier 3 Vocal Cascade"] = power(
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
        self.book["Command: Counterattacks"] = power(
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
        self.book["Command Your Random Spells"] = power(
            "Mercurial Education",
            "Command Your Random Spells",
            "Alchemist",
            ["Faith", "Luck"],
            7,
            "Fame",
            [self.book["Convert Faith and Magic"]],
            [self.book["Random Additional Spell II"]],
        )
        self.book["Critical Attacks Cast Bolt III"] = power(
            "Dragon Breath",
            "Critical Attacks Cast Bolt III",
            "Survivor",
            ["Luck", "Speed", "Stamina", "Strength"],
            6,
            "Lightning Damage",
            [self.book["Reduces Damage For Each Status Effect You Are Suffering"]],
            [self.book["Critical Attacks Grant Temporary Damage Reduction"]],
            requiresDragonOr25=True,
        )
        self.book["Critical Hits Inflict Silence"] = power(
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
        self.book["Dark Mage Tier 3 Death"] = power(
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
        self.book["Druid Tier 3 Natural Resistance"] = power(
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
        self.book["Enemy Sword Users Must Attack You If Possible"] = power(
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
        self.book["Flamecaster Tier 3 Blaze"] = power(
            "Blaze",
            "Flamecaster Tier 3 Blaze",
            "Flamecaster",
            ["Charisma", "Intelligence"],
            7,
            "Fire Damage",
            [self.book["Flamecaster Tier 2 Blaze"]],
            [self.book["Fire Damage Consumes Bleed To Deal Double Damage"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Heavy and Critical Attacks Destroy Focus"] = power(
            "Shock Tactics",
            ["Heavy and Critical Attacks Destroy Focus"],
            "Sky Lord",
            ["Focus", "Intelligence", "Speed"],
            "Heavy Attack Chance",
            5,
            [self.book["Increases Dodge Chance Against Flying Enemies"]],
            [self.book["Heavy and Critical Attacks Ground Flying Enemies"]],
        )
        self.book[
            "Heavy Attacks Deal Extra Damage For Each Status Effect On The Target"
        ] = power(
            "Trauma Hammer",
            "Heavy Attacks Deal Extra Damage For Each Status Effect On The Target",
            "Titan",
            ["Focus", "Strength"],
            "Heavy Attack Chance",
            9,
            [self.book["Critical Attacks Cast Muddle On Target"]],
            [self.book["When Focused, All Attacks Stun"]],
            antiStat=["Speed"],
        )
        self.book["Hero Tier 3 Bolt"] = power(
            "Bolt",
            "Hero Tier 3 Bolt",
            "Hero",
            ["Intelligence", "Luck", "Strength"],
            5,
            "Lightning Damage",
            [self.book["Hero Tier 2 Bolt"]],
            [self.book["Killing Enemies Gives MP"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book[
            "When You Have Four Ranks Of Focus, Your Stats Are Increased"
        ] = power(
            "Boiling Point",
            "When You Have Four Ranks Of Focus, Your Stats Are Increased",
            "Steam Knight",
            ["Focus", "Stamina"],
            6,
            "Focus Intensity",
            [self.book["Taking Magic Damage Adds A Focus Rank"]],
            [self.book["When Focused, Strength is Doubled"]],
        )
        self.book["Increases Chance To Rout On Unholy Ground"] = power(
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
        self.book["Increases Your Area Of Holy Resonance To Seven Tiles"] = power(
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
        self.book["Ignore Enemies When You Move"] = power(
            "Trails In The Sky",
            "Ignore Enemies When You Move",
            "Sky Battler",
            ["Charisma", "Dexterity", "Luck", "Speed", "Stamina"],
            3,
            "Movement Speed",
            [self.book["Counter Enemy Attacks That You Dodged"]],
            [
                self.book[
                    "Increases Dodge Chance Against The First Enemy To Attack You Each Round"
                ]
            ],
        )
        self.book["Monk Tier 3 Aura"] = power(
            "Aura",
            "Monk Tier 3 Aura",
            "Monk",
            ["Faith", "Stamina", "Strength"],
            5,
            "Healing Amount",
            [self.book["Monk Tier 2 Heal"]],
            [self.book["Increases Healing To Allies On Unholy Ground"]],
            spellRank=True,
            not_yet_implemented=False
        )
        self.book["Ninja Tier 3 Ninja Bolt"] = power(
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
        self.book["Peregrine Tier 3 Blast"] = power(
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
        self.book["Priest Tier 3 Heal"] = power(
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
        self.book["Prophet Tier 3 Slow"] = power(
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
        self.book["Reduces Minimum Attack Range By 1"] = power(
            "Unhindered Movement",
            "Reduces Minimum Attack Range By 1",
            "Heavy Shot",
            ["Dexterity", "Speed", "Stamina"],
            5,
            "Brass Guns Skill",
            [self.book["Attacks Are Always Heavy When Your Health Is Full"]],
            [self.book["Increases Focus When Stationary"]],
        )
        self.book["Routing Adds Silence"] = power(
            "Deafening Fear",
            "Routing Adds Silence",
            "Cantor",
            ["Luck", "Speed", "Voice"],
            5,
            "Status Effectiveness",
            [self.book["Double Rout Chance Against Bleeding Targets"]],
            [self.book["Counter Enemy Vocal Attacks With Bleed"]],
        )
        self.book["Scholar Tier 3 Petrify"] = power(
            "Pertify",
            ["Scholar Tier 3 Petrify"],
            "Scholar",
            ["Intelligence", "Focus"],
            7,
            "Status Effectiveness",
            [self.book["Counter Enemy Attacks By Casting A Random Spell You Know"]],
            [self.book["When Focused, All Status Spells Always Succeed"]],
        )
        self.book["Silence Enemies Who Cast A Spell That You Know On You"] = power(
            "Counterspell",
            "Silence Enemies Who Cast A Spell That You Know On You",
            "Channeller",
            ["Dexterity", "Intelligence"],
            7,
            "Status Effectiveness",
            [self.book["Channeller Tier 2 Surge"]],
            [self.book["Channeller Tier 2 Silence"]],
        )
        self.book["Sorceror Tier 3 Atlas"] = power(
            "Poseidon",
            "Sorceror Tier 3 Atlas",
            "Sorceror",
            ["Intelligence", "Voice"],
            7,
            "Lightning Damage",
            [self.book["Sorceror Tier 2 Atlas"]],
            [self.book["Sorceror Tier 2 Poseidon"]],
            spellRank=True,
        )
        self.book["Trickster Tier 3 Teleport"] = power(
            "Teleport",
            "Trickster Tier 3 Teleport",
            "Trickster",
            ["Intelligence", "Speed"],
            6,
            "Lightning Damage",
            [self.book["Teleporting Does Not End Turns"]],
            [self.book["Trickster Tier 2 Portal"]],
            spellRank=True,
        )
        self.book["Unarmed Attacks Have +1 Range, Deal Ice Damage, And Cause Curses"] = power(
            "Dark Ice Claws",
            "Unarmed Attacks Have +1 Range, Deal Ice Damage, And Cause Curses",
            "Werewolf",
            ["Dexterity", "Speed", "Stamina", "Strength"],
            6,
            "Ice Damage",
            self.book["Pursue Enemies You Rout And Attack Again"],
            self.book["Increases Damage Dealt To Flying And Mounted Enemies"],
            antiStat=["Luck"]
        )
        self.book[
            "Use Greatest of Charisma, Faith, Or Strength when Dodging and Defending"
        ] = power(
            "Hyoho Niten Ichi-ryu",
            "Use Greatest of Charisma, Faith, Or Strength when Dodging and Defending",
            "Samurai",
            ["Charisma", "Faith", "Stamina"],
            8,
            "Sword Skills",
            [self.book["Samurai Tier 2 Boost"]],
            [
                self.book[
                    "Use Greatest of Charisma, Faith, or Strength to deal Fire Damage When Attacking"
                ]
            ],
        )
        self.book["Vocal Attacks Act As If Tiles Are Two Ranks More Holy"] = power(
            "Beatified Songs",
            "Vocal Attacks Act As If Tiles Are Two Ranks More Holy",
            "Chorister",
            ["Dexterity", "Focus", "Voice"],
            5,
            "Vocal Strength",
            [self.book["Vocal Attacks Can Target Any Tile You Are Resonating"]],
            [
                self.book[
                    "Counter Enemy Attacks By Adding A Rank Of Holy Resonance To The Source Tile"
                ]
            ],
        )
        self.book["Vocal Attacks Grant You Flying On Your Next Turn"] = power(
            "Ride of the Valkyries",
            "Vocal Attacks Grant You Flying On Your Next Turn",
            "Valkyrie",
            ["Stamina", "Voice"],
            7,
            "Vocal Strength",
            [self.book["Command: Reduces Damage Taken From Vocal Attacks"]],
            [self.book["Vocal Attacks Have a Chance to Deafen Targets"]],
        )
        self.book[
            "Vocal Attacks Isolate Targets From Their Allies' Effects"
        ] = power(
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
        self.book[
            "When Attacking A Target That Is Vulnerable To A Spell School You Know, Cast a Rank I Version Of The Spell At Them"
        ] = power(
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
        self.book["When Focused, All Attacks Charm"] = power(
            "Irresistable Voice",
            "When Focused, All Attacks Charm",
            "Banshee",
            ["Charisma", "Focus", "Strength", "Voice"],
            3,
            "Focus Intensity",
            [self.book["Banshee Tier 2 Axe Damage"]],
            [self.book["Charm Targets Instead of Routing Them"]],
        )
        self.book["When Focused, Attacks Gain +1 Range"] = power(
            "Sniper's Focus",
            "When Focused, Attacks Gain +1 Range",
            "Soldier",
            ["Dexterity", "Focus", "Strength"],
            5,
            "Focus Intensity",
            [self.book["Killing Enemies Grants a Rank of Focus"]],
            [self.book["Reduces Damage From Enemy Area Attacks"]],
        )
        self.book["When Focused, You Cannot Be Reduced Below 1 HP"] = power(
            "Die Hard",
            ["When Focused, You Cannot Be Reduced Below 1 HP"],
            "Gambler",
            ["Focus", "Luck", "Speed"],
            5,
            "Focus Intensity",
            [self.book["Dodging Grants Focus Charge"]],
            [self.book["Increases Focus When Outnumbered"]],
        )
        self.book["Wizard Tier 3 Freeze"] = power(
            "Freeze",
            "Wizard Tier 3 Freeze",
            "Wizard",
            ["Intelligence", "Stamina"],
            8,
            "Ice Damage",
            [self.book["Ice Damage Inflicts Bleed"]],
            [self.book["Wizard Tier 2 Freeze"]],
            spellRank=True,
            not_yet_implemented=False
        )

        # Cross-over powers

    def choose_power_or_spillover(
            self, character, current_options, weighted_array, picked_powers):
        if any(current_options):
            picked_power = random.choice(current_options)
            picked_powers.append(picked_power)
        else:
            weighted_array_options = [
                    option for option in weighted_array
                    if power not in character.powers
                    and power.requirements_unlocked(character)
                    and power not in picked_powers]
            if any(weighted_array_options):
                picked_power = random.choice(weighted_array_options)
                picked_powers.append(picked_power)
        return picked_powers

    def get_power_options(self, character, chatter=True):
        power_options = []

        # if a character lacks a specific choice from the other choice categories,
        # they will be presented with a randomized power from the weighted array instead.
        weighted_array = []
        for power in self.book:
            weighting = 0
            for stat in power.stats:
                weighting += character.stats[stat]
            for stat in power.antiStat:
                weighting -= character.stats[stat]
            weighting = max(0, weighting) * power.multiplier
            weighted_array.extend([power] * weighting)

        # current class power
        # assemble the options
        current_class_options = [
                power for power in self.book
                if power not in character.powers
                and power.unitClass in character.title
                and power.requirements_unlocked(character)]

        power_options = self.choose_power_or_spillover(
                character, current_class_options, weighted_array, power_options)

        # a power from all of the classes that the character has ever picked a power from
        known_class_options = [
                power for power in self.book
                if power not in character.powers
                and power.unitClass in character.knownClasses
                and power.requirements_unlocked(character)
                and power not in power_options]

        power_options = self.choose_power_or_spillover(
                character, known_class_options, weighted_array, power_options)

        # a power of tier 2 or 3 that the character has unlocked the requirements for
        power_with_unlocked_requirements_options = [
                power for power in self.book
                if power not in character.powers
                and power.requirement1
                and power.requirements_unlocked(character)
                and power not in power_options]

        power_options = self.choose_power_or_spillover(
                character, power_with_unlocked_requirements_options, weighted_array,
                power_options)

        # a power derived from the character's highest stat(s)
        highest_character_stats = [
                stat for stat in character.stats
                if character.stats[stat] == max([
                        character.stats[stat] for stat in character.stats])]

        highest_stats_options = []
        for stat in highest_character_stats:
            stat_powers = [
                    power for power in weighted_array
                    if power not in character.powers
                    and stat in power.stats
                    and power.requirements_unlocked(character)
                    and power not in power_options]
            for sp in stat_powers:
                highest_stats_options.append(sp)

        power_options = self.choose_power_or_spillover(
                character, highest_stats_options, weighted_array, power_options)

        weighted_random_options = [
                power for power in weighted_array
                if power not in character.powers
                and power.requirements_unlocked(character)
                and power not in power_options]

        power_options = self.choose_power_or_spillover(
                character, weighted_random_options, weighted_array, power_options)

        return power_options


class power(object):
    def __init__(
        self,
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
        requiresDragonOr25=False,
        not_yet_implemented=True
    ):
        self.name = name
        self.description = description
        self.unitClass = unitClass
        self.stats = stats
        self.multiplier = multiplier
        self.unlockCategory = unlockCategory
        self.requirement1 = requirement1
        self.requirement2 = requirement2
        self.antiPower = antiPower
        self.antiStat = antiStat
        self.bannedClasses = bannedClasses
        self.not_yet_implemented = not_yet_implemented
        if not descriptionOverride:
            self.descriptionOverride = description
        else:
            self.descriptionOverride = descriptionOverride
        self.requiresDragonOr25 = requiresDragonOr25
        if requiresDragonOr25:
            self.minimumLevel = 25
        else:
            self.minimumLevel = minimumLevel
        self.spellRank = spellRank

    def requirements_unlocked(self, character):
        if self.requirement1:
            if self.requirement1 not in character.powers:
                return False
        if self.requirement2:
            if self.requirement2 not in character.powers:
                return False
        return True
