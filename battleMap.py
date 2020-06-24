

class battleTile(object):
    """docstring for BattleTile"""

    def __init__(self, terrain):
        self.name = terrain
        self.cost = 5
        # Assign cost
        if self.name == "Tiled Floor":
            self.cost = 5
        elif self.name == "Grass":
            self.cost = 6
        elif self.name in ("Sand", "Overgrowth"):
            self.cost = 7
        elif self.name in (
                "Ascending Stairway", "Descending Stairway", "Loose Rocks"):
            self.cost = 8
        elif self.name == "Forest":
            self.cost = 10

        # is it unstable?
        if self.name in ("Sand", "Loose Rocks"):
            self.unstable = True
        else:
            self.unstable = False
        self.units = []

class battleField(object):

    def __init__(self, listOfTiles, listOfUnits):
        self.terrainArray = []
        for tile in listOfTiles:
            self.terrainArray.append(battleTile(tile))
        for unit, position in listOfUnits:
            tile = self.terrainArray[position]
            tileUnits = tile.units
            tileUnits.append(unit)
        print([
                f"{tile.units} on {tile.name}: {tile.cost}"
                for tile in self.terrainArray])


print("Let's do a test!")
battleField([
        "Grass", "Grass", "Grass", "Ascending Stairway", "Rubble",
        "Tiled Floor", "Tiled Floor", "Tiled Floor", "Rubble", "Rubble"],
        [("Goblin", 5), ("Goblin", 8), ("Dark Dwarf", 8)])
