
class shop(object):

    def __init__(self, listOfGoods):
        self.goods = []
        for goodName in listOfGoods:
            self.goods. append(self.addGoodToShop(name))

    def addGoodToShop(self, name):
        if name == "Ancient Cannon":
            return potentialItem("Brass Guns", name, 6000, 1, 1, 22, 0, 0)
        elif name == "Assault Shell":
            return potentialItem("Brass Guns", name, 4500, 1, 2, 18, 0, 0)
        elif name == "Atlas Axe":
            return potentialItem(
                    "Axes", name, 11000, 0, 0, 22, 0, 28, ["Atlas I"])
        elif name == "Balista Bolt":
            return potentialItem("Spears", name, 14000, 0, 1, 23, 0, 0)
        elif name == "Battle Axe":
            return potentialItem("Axes", name, 2600, 0, 0, 11, 0, 0)
        elif name == "Broadsword":
            return potentialItem("Long Swords", name, 4800, 0, 0, 14, 0, 0)
        elif name == "Bronze Lance":
            return potentialItem("Lances", name, 300, 0, 0, 6, 0, 0)
        elif name == "Buster Shot":
            return potentialItem("Brass Guns", name, 12400, 1, 2, 23, 0, 0)
        elif name == "Chrome Lance":
            return potentialItem("Lances", name, 4500, 0, 0, 15, 0, 0)
        elif name == "Demon Rod":
            return potentialItem(
                    "Staffs", name, 5000, 0, 0, 23, -6, -6, ["Conduit I"])
        elif name == "Devil Lance":
            return potentialItem(
                    "Lances", name, 7000, 0, 0, 23, 0, 0, ["Cursed Weapon"])
        elif name == "Doom Blade":
            return potentialItem("Katanas", name, 5000, 0, 0, 17, 0, 0)
        elif name == "Elven Arrow":
            return potentialItem("Arrows", name, 2300, 1, 2, 12, 0, 0)
        elif name == "Faerie Arrow":
            return potentialItem(
                    "Arrows", name, 9000, 1, 2, 20, 0, 0, ["Quick Shot"])
        elif name == "Grand Cannon":
            return potentialItem(
                    "Brass Guns", name, 18500, 1, 2, 29, 0, 18, ["Muddle I"])
        elif name == "Great Axe":
            return potentialItem("Axes", name, 10000, 0, 0, 18, 0, 0)
        elif name == "Guardian Staff":
            return potentialItem("Staffs", name, 3200, 0, 0, 12, 12, 12)
        elif name == "Halberd":
            return potentialItem(
                    "Lances", name, 5000, 0, 0, 17, 0, 16, ["Bolt I"])
        elif name == "Hand Axe":
            return potentialItem("Axes", name, 200, 0, 0, 4, 0, 0)
        elif name == "Heat Axe":
            return potentialItem(
                    "Axes", name, 4400, 0, 0, 15, 0, 10,
                    ["Axes: Added Effect: Fire", "Blaze II"])
        elif name == "Holy Staff":
            return potentialItem(
                    "Staffs", name, 8000, 0, 0, 17, 24, 24, ["Blast II"])
        elif name == "Hyperial Arrow":
            return potentialItem("Arrows", name, 17000, 1, 3, 27, 0, 0)
        elif name == "Iron Shot":
            return potentialItem("Brass Guns", name, 800, 1, 1, 7, 0, 0)
        elif name == "Katana":
            return potentialItem("Katanas", name, 6000, 0, 0, 20, 0, 0)
        elif name == "Long Sword":
            return potentialItem("Long Swords", name, 750, 0, 0, 8, 0, 0)
        elif name == "Middle Axe":
            return potentialItem("Axes", name, 200, 0, 0, 7, 0, 0)
        elif name == "Middle Sword":
            return potentialItem("Swords", name, 250, 0, 0, 5, 0, 0)
        elif name == "Power Spear":
            return potentialItem("Spears", name, 900, 0, 1, 10, 0, 0)
        elif name == "Power Staff":
            return potentialItem("Staffs", name, 500, 0, 0, 8, 6, 6)
        elif name == "Robin's Arrow":
            return potentialItem("Arrows", name, 1480, 1, 1, 11, 0, 0)
        elif name == "Short Sword":
            return potentialItem("Swords", name, 100, 0, 0, 3, 0, 0)
        elif name == "Spear":
            return potentialItem("Spears", name, 150, 0, 1, 5, 0, 0)
        elif name == "Steel Arrow":
            return potentialItem("Arrows", name, 1200, 0, 0, 9, 0, 0)
        elif name == "Steel Lance":
            return potentialItem("Lances", name, 3000, 0, 0, 12, 0, 0)
        elif name == "Steel Sword":
            return potentialItem("Swords", name, 2500, 0, 0, 12, 0, 0)
        elif name == "Sword of Darkness":
            return potentialItem(
                    "Sacred Swords", name, 8000, 0, 0, 27, 0, 12,
                    ["Death I", "Cursed Weapon"])
        elif name == "Sword of Light":
            return potentialItem(
                    "Sacred Swords", name, 7200, 0, 0, 24, 0, 30, ["Bolt II"])
        elif name == "Sword of Order":
            return potentialItem(
                    "Sacred Swords", name, 7200, 0, 0, 27, 0, 20,
                    ["Freeze III"])
        elif name == "Wooden Arrow":
            return potentialItem("Arrows", name, 150, 1, 1, 5, 0, 0)
        elif name == "Wooden Staff":
            return potentialItem("Staffs", name, 80, 0, 0, 1, 3, 3)


class potentialItem(object):

    def __init__(
            self, equipType, name, price, minRange=0, maxRange=0, damage=3,
            fp=0, mp=0, powers=[]):
        self.type = equipType
        self.name = name
        self.minRange = minRange
        self.maxRange = maxRange
        self.damage = damage
        self.equippedBy = None
        self.fp = fp
        self.mp = mp
        self.price = price
        self.powers = powers


def createPotentialItemModule(game, moduleNum):

