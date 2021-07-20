from characters import equipment
import math
import random


class shop(object):
    def __init__(self, game, listOfGoods, listOfDealGoods, skillLevel=None):
        self.goods = []
        if skillLevel:
            game.setMinSkill(skillLevel)
        for goodName in listOfGoods:
            self.goods.append(self.createGood(goodName))
        self.deal = self.createGood(random.choice(listOfDealGoods))
        if self.deal.name in [good.name for good in self.goods]:
            self.deal.price = math.ceil(self.deal.price / 2)
        self.goods.insert(0, self.deal)

    def buyGood(self, game, itemToBuy):
        item = self.goods[itemToBuy]
        if game.money < item.price:
            print("\"Sorry, kid, but you ain't got the bills for that one.\"")
        else:
            game.money -= item.price
            equip = equipment(
                item.type,
                item.name,
                item.price,
                item.skill,
                item.minRange,
                item.maxRange,
                item.damage,
                item.fp,
                item.fp,
                item.powers,
            )
            game.inventory.append(equip)
            print("\"Thanks for the scrolls, kid!\"")
            print("Would you like to equip it right away?")
            game.equipItem(equip)
            if item == self.deal:
                self.goods.remove(item)

    def createGood(self, name):
        # Arrows
        if name == "Elven Arrow":
            return potentialItem("Arrows", name, 2300, 18, 1, 2, 12, 0, 0)
        elif name == "Faerie Arrow":
            return potentialItem(
                "Arrows", name, 9000, 24, 1, 2, 20, 1, 2, ["Quick Shot"]
            )
        elif name == "Hyperial Arrow":
            return potentialItem("Arrows", name, 17000, 40, 1, 3, 27, 0, 0)
        elif name == "Robin's Arrow":
            return potentialItem("Arrows", name, 1480, 14, 1, 1, 11, 0, 0)
        elif name == "Steel Arrow":
            return potentialItem("Arrows", name, 1200, 12, 1, 1, 9, 0, 0)
        elif name == "Wooden Arrow":
            return potentialItem("Arrows", name, 150, 1, 1, 1, 5, 0, 0)

        # Axes
        elif name == "Atlas Axe":
            return potentialItem("Axes", name, 11000, 40, 0, 0, 22, 0, 28, ["Atlas I"])
        elif name == "Battle Axe":
            return potentialItem("Axes", name, 2600, 24, 0, 0, 11, 0, 0)
        elif name == "Great Axe":
            return potentialItem("Axes", name, 10000, 36, 0, 0, 18, 0, 0)
        elif name == "Hand Axe":
            return potentialItem("Axes", name, 200, 5, 0, 0, 4, 0, 0)
        elif name == "Heat Axe":
            return potentialItem(
                "Axes",
                name,
                4400,
                25,
                0,
                0,
                15,
                0,
                10,
                ["Axes: Added Effect: Fire", "Blaze II"],
            )
        elif name == "Middle Axe":
            return potentialItem("Axes", name, 300, 12, 0, 0, 7, 0, 0)
        elif name == "Power Axe":
            return potentialItem("Axes", name, 1100, 18, 0, 0, 11, 0, 0)
        elif name == "Short Axe":
            return potentialItem("Axes", name, 120, 1, 0, 0, 3, 0, 0)

        # Brass Guns
        elif name == "Ancient Cannon":
            return potentialItem("Brass Guns", name, 6000, 28, 1, 1, 22, 0, 0)
        elif name == "Assault Shell":
            return potentialItem("Brass Guns", name, 4500, 36, 1, 2, 18, 0, 0)
        elif name == "Buster Shot":
            return potentialItem("Brass Guns", name, 12400, 40, 1, 2, 23, 0, 0)
        elif name == "Grand Cannon":
            return potentialItem(
                "Brass Guns", name, 18500, 44, 1, 2, 29, 0, 18, ["Muddle I"]
            )
        elif name == "Iron Shot":
            return potentialItem("Brass Guns", name, 800, 1, 1, 1, 7, 0, 0)

        # Daggers
        elif name == "Bloody Knife":
            return potentialItem(
                "Daggers", name, 4500, 19, 0, 0, 14, 0, 0, ["Luck: Critical Drain I"]
            )
        elif name == "Dagger":
            return potentialItem("Daggers", name, 320, 4, 0, 0, 5, 0, 0)
        elif name == "Knife":
            return potentialItem("Daggers", name, 500, 6, 0, 0, 8, 0, 0)
        elif name == "Ritual Dagger":
            return potentialItem(
                "Daggers",
                name,
                9500,
                29,
                0,
                0,
                17,
                8,
                0,
                ["Daggers: Added Effect: Poison"],
            )
        elif name == "Short Knife":
            return potentialItem("Daggers", name, 70, 1, 0, 0, 3, 0, 0)
        elif name == "Thief's Dagger":
            return potentialItem(
                "Daggers", name, 1000, 11, 0, 0, 12, 0, 0, ["Daggers: Increased Luck"]
            )

        # Lances
        elif name == "Bronze Lance":
            return potentialItem("Lances", name, 300, 8, 0, 0, 6, 0, 0)
        elif name == "Chrome Lance":
            return potentialItem("Lances", name, 4500, 24, 0, 0, 15, 0, 0)
        elif name == "Devil Lance":
            return potentialItem(
                "Lances", name, 7000, 34, 0, 0, 23, 0, 0, ["Cursed Weapon"]
            )
        elif name == "Halberd":
            return potentialItem("Lances", name, 5000, 30, 0, 0, 17, 0, 16, ["Bolt I"])
        elif name == "Steel Lance":
            return potentialItem("Lances", name, 3000, 16, 0, 0, 12, 0, 0)

        # Spears
        elif name == "Balista Bolt":
            return potentialItem("Spears", name, 14000, 42, 0, 1, 23, 0, 0)
        elif name == "Power Spear":
            return potentialItem("Spears", name, 900, 12, 0, 1, 10, 0, 0)
        elif name == "Spear":
            return potentialItem("Spears", name, 150, 5, 0, 1, 5, 0, 0)
        elif name == "Wooden Spear":
            return potentialItem("Spears", name, 100, 1, 0, 1, 3, 0, 0)

        # Staffs
        elif name == "Demon Rod":
            return potentialItem(
                "Staffs", name, 5000, 38, 0, 0, 23, -6, -6, ["Conduit I"]
            )
        elif name == "Guardian Staff":
            return potentialItem("Staffs", name, 3200, 28, 0, 0, 12, 12, 12)
        elif name == "Holy Staff":
            return potentialItem(
                "Staffs", name, 8000, 36, 0, 0, 17, 24, 24, ["Blast II"]
            )
        elif name == "Power Staff":
            return potentialItem("Staffs", name, 500, 8, 0, 0, 4, 6, 6)
        elif name == "Wooden Staff":
            return potentialItem("Staffs", name, 80, 1, 0, 0, 1, 3, 3)

        # Swords
        elif name == "Broadsword":
            return potentialItem("Swords", name, 4800, 36, 0, 0, 14, 0, 0)
        elif name == "Doom Blade":
            return potentialItem("Katanas", name, 5000, 40, 0, 0, 17, 0, 0)
        elif name == "Katana":
            return potentialItem("Katanas", name, 6000, 44, 0, 0, 20, 0, 0)
        elif name == "Long Sword":
            return potentialItem("Swords", name, 750, 18, 0, 0, 8, 0, 0)
        elif name == "Middle Sword":
            return potentialItem("Swords", name, 250, 8, 0, 0, 5, 0, 0)
        elif name == "Short Sword":
            return potentialItem("Swords", name, 100, 1, 0, 0, 3, 0, 0)
        elif name == "Steel Sword":
            return potentialItem("Swords", name, 2500, 24, 0, 0, 12, 0, 0)
        elif name == "Sword of Darkness":
            return potentialItem(
                "Sacred Swords",
                name,
                8000,
                27,
                0,
                0,
                27,
                0,
                12,
                ["Death I", "Cursed Weapon"],
            )
        elif name == "Sword of Light":
            return potentialItem(
                "Sacred Swords", name, 7200, 24, 0, 0, 24, 0, 30, ["Bolt II"]
            )
        elif name == "Sword of Order":
            return potentialItem(
                "Sacred Swords", name, 7200, 27, 0, 27, 0, 20, ["Freeze III"]
            )
        else:
            print(f"warning. No shop item called {name} exists.")

    def goShopping(self, game):
        print("You enter a shop.")
        print("The shopkeeper looks up. \"You here to buy, or just look?\"")
        if self.deal in self.goods:
            if self.deal and (self.deal.name in [good.name for good in self.goods]):
                print(
                    "Today as special, I've got a one-time discount on a "
                    f"{self.deal.name}!"
                )
            else:
                print(
                    f"Feast yer eyes on this {self.deal.name} -- She's "
                    "the only one of 'er kind in town!"
                )
        command = None
        while command not in ("L", "l"):
            allowedCommands = ["B", "b", "E", "e", "L", "l"]
            print("(B) Buy weapons.")
            print("(E) Equip your troops.")
            if any([weapon for weapon in game.inventory if not weapon.equippedBy]):
                print("Type (S) to sell weapons you are not using.")
                allowedCommands.append("S")
                allowedCommands.append("s")
            print("(L) Leave the shop.")
            print()
            while command not in allowedCommands:
                command = input("Type a letter to make your choice: ")
            if command in ("B", "b"):
                command = None
                itemToBuy = None
                while itemToBuy not in [
                    self.goods.index(item) for item in self.goods
                ] or (itemToBuy != len(self.goods)):
                    self.printShopItems(game)
                    print(f"({len(self.goods)}) Don't buy anything.")
                    print(f"You have {game.money} Scroulings.")
                    print()
                    try:
                        itemToBuy = int(input("Type a number to buy a weapon: "))
                    except ValueError:
                        itemToBuy = None
                    if itemToBuy == len(self.goods):
                        break
                    if itemToBuy is not None:
                        if itemToBuy in [self.goods.index(item) for item in self.goods]:
                            self.buyGood(game, itemToBuy)
                            itemToBuy = None
                            print()
                        else:
                            itemToBuy = None
            elif command in ("E", "e"):
                command = None
                itemToEquip = None
                while itemToEquip not in [
                    game.inventory.index(item) for item in game.inventory
                ] or (itemToEquip != len(game.inventory)):
                    for item in game.inventory:
                        itemString = f"({game.inventory.index(item)}) {item.name} "
                        if item.equippedBy:
                            itemString += f"E: {item.equippedBy.name}"
                        print(itemString)
                    print(f"({len(game.inventory)}) Done equipping my troops.")
                    try:
                        itemToEquip = int(input("Type a number to equip: "))
                    except ValueError:
                        itemToEquip = None
                    if itemToEquip == len(game.inventory):
                        break
                    if itemToEquip is not None:
                        game.equipItem(game.inventory[itemToEquip])
                        itemToEquip = None
                        print()
            elif command in ("S", "s"):
                command = None
                allowedItems = [item for item in game.inventory if not item.equippedBy]
                whatToSell = None
                while whatToSell not in allowedItems or (
                    whatToSell != len(allowedItems)
                ):
                    for item in allowedItems:
                        price = game.getSellPrice(item)[0]
                        sellString = (
                            f"({allowedItems.index(item)}) {item.name} - "
                            f"{price} Scroulings"
                        )
                        print(sellString)
                    print(f"({len(allowedItems)}) I'm done selling.")
                    try:
                        whatToSell = int(input("Type a number to sell a weapon: "))
                    except ValueError:
                        whatToSell = None
                    if whatToSell == len(allowedItems):
                        break
                    if whatToSell is not None:
                        self.sellItem(game, allowedItems[whatToSell])
                        whatToSell = None
                        print()
                        allowedItems = [
                            item for item in game.inventory if not item.equippedBy
                        ]
                        if not any(allowedItems):
                            break
        print("\"Thanks for coming in, kid.\"")

    def printShopItems(self, game):
        for item in self.goods:
            shopString = (
                f"({self.goods.index(item)}) {item.name} - {item.price} Scroulings"
            )
            damageUp = False
            faithUp = False
            mpUp = False
            for pc in game.playerCharacters:
                if item.canEquip(pc):
                    if pc.equipment:
                        if item.damage > pc.equipment.damage:
                            damageUp = True
                        if item.fp > pc.equipment.fp:
                            faithUp = True
                        if item.mp > pc.equipment.mp:
                            mpUp = True
                    else:
                        if item.damage > 0:
                            damageUp = True
                        if item.fp > 0:
                            faithUp = True
                        if item.mp > 0:
                            mpUp = True
            if damageUp:
                shopString += " Damage Upgrade!"
            if faithUp:
                shopString += " Faith Upgrade!"
            if mpUp:
                shopString += " Magic Upgrade!"
            print(shopString)

    def sellItem(self, game, item):
        price, blame = game.getSellPrice(item)
        game.money += price
        game.inventory.remove(item)
        if blame:
            print(
                f"I've always wanted to own a {item.name} that {blame} used in battle!"
            )
        else:
            print(
                "\"Ahh, this will fetch a good price... if we make it "
                "through the war.\""
            )


class potentialItem(object):
    def __init__(
        self,
        equipType,
        name,
        price,
        skill=0,
        minRange=0,
        maxRange=0,
        damage=3,
        fp=0,
        mp=0,
        powers=[],
    ):
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
        self.skill = skill

    def canEquip(self, unit):
        return unit.skills[self.type] >= self.skill
