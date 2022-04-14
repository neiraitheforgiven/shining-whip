from battleMap import battle
from characters import equipment
from characters import playerCharacter
from shopping import shop
import math
import os
import powers
import shelve
import time


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
                self.shelf = shelve.open(f"TSOTHASOTF-{self.saveName.lower()}")
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
                self.powerBook = powers.powerBook()
                self.shelf["book"] = self.powerBook
                self.battleStarted = 0
                self.shelf["battleStarted"] = self.battleStarted
                tutorial = input(
                    'Do you want to learn how to play? If so, type "Teach Me" now: '
                )
                if tutorial.strip().lower() == "teach me":
                    self.tutorial = self.initTutorial()
                else:
                    self.tutorial = {}
                    print()
                    time.sleep(1.2)
                self.shelf.close()
            else:
                self.shelf = shelve.open(f"TSOTHASOTF-{self.saveName.lower()}")
                if "Initialized" not in self.shelf:
                    print("A save file with that name was not found. Try again.")
                    self.shelf.close()
                    #  on windows, shelve.open will create the files.
                    # if the files exist, delete them
                    try:
                        os.remove(f"TSOTHASOTF-{self.saveName.lower()}.dat")
                    except FileNotFoundError:
                        pass
                    try:
                        os.remove(f"TSOTHASOTF-{self.saveName.lower()}.bak")
                    except FileNotFoundError:
                        pass
                    try:
                        os.remove(f"TSOTHASOTF-{self.saveName.lower()}.dir")
                    except FileNotFoundError:
                        pass
                    self.saveName = None
                    continue
                self.playerCharacters = self.shelf["playerCharacters"]
                self.inventory = self.shelf["inventory"]
                self.money = self.shelf["money"]
                self.maxPartySize = self.shelf["maxPartySize"]
                self.battleNum = self.shelf["battleNum"]
                self.shop = self.shelf["shop"]
                self.powerBook = self.shelf["book"]
                self.battleStarted = self.shelf["battleStarted"]
                if "tutorial" in self.shelf:
                    self.tutorial = self.shelf["tutorial"]
                else:
                    self.tutorial = {}
                self.shelf.close()
        self.battleStatus = None
        while self.battleNum < 33:
            self.doBattle(self.battleNum)

    def assignPower(self, character, powerName, chatter=False):
        if self.powerBook.book[powerName].not_yet_implemented:
            print()
            print(
                f"Warning: the power {powerName} has not been implemented"
                " yet. Let Neirai the Forgiven know to add it to the list of things to do!"
            )
            print()
        character.powers.append(powerName)
        if chatter:
            print(f"{self.name} learned {powerName}!")

    def doBattle(self, battleNum):
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
            self.teach("Hero")
            if self.battleStarted < 1:
                recruit = playerCharacter("Max", "Human", "Hero", False, 0)
                self.assignPower(recruit, "Hero Root 1 Egress")
                self.equipOnCharacter(
                    equipment("Swords", "Middle Sword", 250, 1, 0, 0, 5, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Lowe", "Hobbit", "Priest", False, 0)
                self.assignPower(recruit, "Priest Tier 1 Heal")
                self.equipOnCharacter(
                    equipment("Staffs", "Wooden Staff", 80, 1, 0, 0, 1, 3, 3),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Tao", "Elf", "Flamecaster", False, 0)
                self.assignPower(recruit, "Flamecaster Tier 1 Blaze")
                self.equipOnCharacter(
                    equipment("Staffs", "Wooden Staff", 80, 1, 0, 0, 1, 3, 3),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Luke", "Dwarf", "Warrior", False, 0)
                self.assignPower(recruit, "Move Right One More Tile If Ally Present")
                self.equipOnCharacter(
                    equipment("Axes", "Short Axe", 120, 1, 0, 0, 3, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Ken", "Centaur", "Knight", False, 0)
                self.assignPower(
                        recruit, "Move an Additional Tile As Long As You Don't Move On Unstable Ground")
                self.equipOnCharacter(
                    equipment("Spears", "Wooden Spear", 100, 1, 0, 1, 3, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                recruit = playerCharacter("Hans", "Elf", "Archer", False, 0)
                self.assignPower(
                        recruit, "Begin Battle with Two Ranks of Focus")
                self.equipOnCharacter(
                    equipment("Arrows", "Wooden Arrow", 150, 1, 1, 1, 3, 0, 0),
                    recruit,
                    False,
                )
                self.playerCharacters.append(recruit)
                self.battleStarted = 1
                self.save()
            self.party = self.playerCharacters
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(8, "king")
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "king")
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
                self.reckoning(25, "lonely priest")
                self.battleStarted = 2
                self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(8, "lonely priest")
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "lonely priest")
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
                self.reckoning(25, "widow of your mentor")
                self.battleStarted = 3
                self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(8, "widow of your mentor")
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "widow of your mentor")
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif battleNum == 4:
            print("")
            print("You arrive in Ulmara, a small merchant city bordering Yatahal.")
            print("The King of Ulmara greets you warmly, bestowing lavish gifts.")
            if self.battleStarted < 4:
                self.reckoning(40, "King of Ulmara")
            print('The King gestures to the shopping district: "Go visit a smith!"')
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
            print('"Don\'t trust the king!", she hisses, then spirits away.')
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
            print('"My people built this palace and the prison." She smirks.')
            print('"Come with me -- we\'ll have to fight our way out of town."')
            print('"We have to go north to inform Her Majesty of her father\'s death."')
            print('"I\'m Khris. The priesthood is still loyal to Yatahal."')
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
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(15, "priests")
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "priests")
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
                self.reckoning(30, "the courtiers")
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
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(15, "the courtiers")
                    self.shop.goShopping(self)
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "the courtiers")
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
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(15, "the royal coffers")
                    self.shop.goShopping(self)
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "the royal coffers")
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
                "\"It's sacred because it give the wielder the power to "
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
                "illusion! This must be Darksol's handiwork -- and here "
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
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(15, "the royal coffers")
                    self.shop.goShopping(self)
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "the royal coffers")
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
                "room, that can only be opened by the Keepers, Angelic "
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
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(15, "Anri")
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "Anri")
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
                self.reckoning(40, "the Keepers")
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
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(15, "the townsfolk")
                    self.shop.goShopping(self)
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "the townsfolk")
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
                self.reckoning(40, "the grateful townsfolk")
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
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(15, "the townsfolk")
                    self.shop.goShopping(self)
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "the townsfolk")
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
                self.reckoning(55, "a plot device")
            self.battleStarted = 11
            self.save()
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(25, "the townsfolk")
                    self.shop.goShopping(self)
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "the townsfolk")
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        elif self.battleNum == 12:
            if self.battleStarted < 12:
                print("")
                print(
                    "After defeating the evil Beast, the mercenary who fell off of the"
                    " cliffside climbs back up."
                )
                print("He pledges his allegience to your cause.")
                print("Pelle the Knight joins the Force!")
                pelle = playerCharacter("Pelle", "Centaur", "Knight", False, 9)
                self.equipOnCharacter(
                    equipment("Spears", "Power Spear", 900, 12, 0, 1, 10, 0, 0),
                    pelle,
                    False,
                )
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                pelle.levelUp(False)
                self.playerCharacters.append(pelle)
                print("")
                print(
                    "After crossing the mountains, you travel east until you come to"
                    " the great plains of Sikahl."
                )
                print(
                    "Here, flatlands spread in all directions, punctuated by wells like"
                    " oases in a desert."
                )
                print(
                    "Merchant caravans traverse the plains, for company as much as for"
                    " defense."
                )
                input("<Press enter to continue>")
                print()
                print(
                    "One night, as you sit amongst a caravan resting at a well, a man"
                    " dressed in dark armor approaches."
                )
                print('"I am Edrik Sohorn, General of Yaranguld." he says.')
                print(
                    '"Yaranguld has always been the ally of Yatahal." he continues. "In'
                    " fact, Yaranguld's old kings founded Yatahal and set it aside as"
                    ' a holy city-state."'
                )
                print('"This would make us allies."')
                print("Sohorn sighs.")
                print(
                    '"Alas, this is not to be. Darksol has corrupted the mind of King'
                    " Raman of Yaranguld so that he is blinded with hatred for all that"
                    ' is holy."'
                )
                print(
                    '"Years ago, the royal historians of Yaranguld unearthed the body'
                    ' of a great dragon. A great, vile, evil corpse."'
                )
                print(
                    '"They plan to revive it, using dark magic and--" he pauses,'
                    " removing his helmet."
                )
                input("<Press enter to continue>")
                print()
                print("Beneath the helmet, his face is that of a dragon.")
                print(
                    'He continues, his face contorting. "Dark magic and the blood of'
                    ' the dragonkin, my people."'
                )
                print(
                    '"I have no choice but to fight. Darksol treats me as his puppet.'
                    " If I stay my hand, Darksol will slaughter those who are left of"
                    ' our people."'
                )
                print(
                    '"Raman once gave us protection, but no longer. My orders are to'
                    ' burn and destroy every free town from here to Yatahal."'
                )
                print(
                    "Perhaps it is luck or fate that you stand between me and my"
                    " orders."
                )
                print(
                    '"Tomorrow, I shall assault you on the open plains. If you defeat'
                    " me, hurry to confront Raman in Yaranguld, and save my people from"
                    ' Darksol."'
                )
                input("<Press enter to continue>")
                print()
                print("With that, General Sohorn bids you prepare and makes his leave.")
                print(
                    "Two other travellers, who overheard the exchange, come forward and"
                    " offer their help in the coming battle."
                )
                print("Kokichi the Sky Lord joins your force!")
                kokichi = playerCharacter("Kokichi", "Human", "Sky Lord", False, 9)
                self.equipOnCharacter(
                    equipment("Lances", "Steel Lance", 3000, 16, 0, 0, 12, 0, 0),
                    kokichi,
                    False,
                )
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                kokichi.levelUp(False)
                self.playerCharacters.append(kokichi)
                print()
                print("Vankar the Knight joins your force!")
                vankar = playerCharacter("Vankar", "Centaur", "Knight", False, 9)
                self.equipOnCharacter(
                    equipment("Spears", "Power Spear", 900, 12, 0, 1, 10, 0, 0),
                    vankar,
                    False,
                )
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                vankar.levelUp(False)
                self.playerCharacters.append(vankar)
                print()
            print()
            print("The next day, some merchants approach you.")
            print("They point to the approaching Yaranguld army on the horizon.")
            print('"Do something!" they yell. "That army intends to slaughter us!')
            print('"We will finance your army! Do whatever it taks to save us!"')
            if self.battleStarted < 12:
                self.reckoning(75, "the merchants")
            print("Of course, being merchants, they do make you pay for gear.")
            print("")
            if self.battleStarted < 12:
                self.shop = shop(
                    self,
                    [
                        "Long Sword",
                        "Bronze Lance",
                        "Power Spear",
                        "Middle Axe",
                        "Power Staff",
                        "Steel Arrow",
                        "Iron Shot",
                        "Thief's Dagger",
                    ],
                    [
                        "Power Axe",
                        "Heat Axe",
                        "Assault Shell",
                        "Bloody Knife",
                        "Steel Lance",
                    ],
                    18,
                )
            self.battleStarted = 12
            self.save()
            self.shop.goShopping(self)
            self.party = self.playerCharacters
            self.battleStatus = None
            while self.battleStatus != "victory":
                if self.battleStatus == "egress":
                    self.reckoning(35, "the merchants")
                    self.shop.goShopping(self)
                elif self.battleStatus == "defeat":
                    self.reckoning(0, "the merchants")
                    self.shop.goShopping(self)
                battle(self, self.party, self.battleNum)
            else:
                self.battleNum += 1
        else:
            self.printCredits()
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
                    currentDamage = math.ceil(unit.skills["Unarmed Attack"] / 2)
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
        if isinstance(character, str):
            pc = [player for player in self.party if player.name == character][0]
        elif isinstance(character, playerCharacter):
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

    def unitKnowsSpellRank(self, unit, spellName):
        rank = 0
        for power in unit.powers:
            entry = self.powerBook.book[power]
            if entry.spellRank:
                if entry.name == spellName:
                    rank += 1
        return rank

    def printCredits(self):
        print()
        print("Thank you for playing my game! It means a lot to me!")
        time.sleep(0.45)
        print("**CREDITS**")
        time.sleep(0.45)
        print("Code and game design by John 'Neirai the Forgiven' den Otter.")
        time.sleep(0.75)
        print(
            "Original Shining Force character, story, and encounter design by SEGA. "
            "Used without permission. Please don't sue."
        )
        time.sleep(0.75)
        print(
            "Character ability and Talent design by John 'Neirai the Forgiven' den"
            " Otter."
        )
        time.sleep(0.75)
        print("Story retelling by John 'Neirai the Forgiven' den Otter.")
        time.sleep(0.75)
        print("Art and music by")
        time.sleep(0.75)
        print()
        print()
        time.sleep(0.25)
        print(
            "Very special thanks to my testers. Without you this wouldn't have been so"
            " fun."
        )
        time.sleep(0.75)
        print(
            "Solver, for providing his insights and perspectives and demanding better"
            " QOL."
        )
        time.sleep(0.75)
        print("rockbandit")
        time.sleep(0.75)
        print()
        time.sleep(0.15)
        print(
            "Until next time, I hope you enjoyed your time in the game. The game is"
            " currently being updated, so try it again later!"
        )
        time.sleep(0.44)
        print("God bless. -- John")

    def reckoning(self, bounty, patron):
        clergyCost = sum(
            [unit.level * 10 for unit in self.playerCharacters if unit.hp <= 0]
        )
        if not any(
            unit
            for unit in self.playerCharacters
            if "Egress I" in unit.powers and unit.hp > 0
        ):
            clergyCost += math.floor(self.money / 2)
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
        self.shelf["tutorial"] = self.tutorial
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

    def initTutorial(self):
        print()
        time.sleep(0.4)
        print("Tutorial elements loaded.")
        print()
        time.sleep(1.2)
        tutorial = {}
        # heavy attacks
        # routing
        # class changes
        # death
        # fame
        tutorial["Flying Movement"] = [
            "Let me teach you about Flying Movement.",
            "",
            "Certain characters, such as birdmen like Amon and Balbaroy, are capable of"
            " flight.",
            "Flying units enjoy a different set of rules for movement and blocking than"
            " land units.",
            "Flying units ignore the movement costs associated with terrain and cannot"
            " be blocked by land units.",
            "Instead, flying units are only blocked by other flying units.",
            "It only takes one flying enemy to prevent a flying character from moving"
            " through a tile,",
            "and only two flying enemies are needed to prevent a flying character from"
            " leaving a tile at all.",
        ]
        tutorial["Focus"] = [
            "Let me teach you about Focus.",
            "",
            "Focus represents a character's ability to muster just a little bit more"
            " oomph for a short period of time.",
            "Each of your characters will gain a bit of focus as time passes on the"
            " battlefield.",
            "As your character gains focus, they will achieve ranks of focus, from 1"
            " to 4.",
            "Because Hans is an Archer, he starts each battle with focus rank 2 already"
            " achieved.",
            "When you choose to enter a focused state, the character will"
            " consume all of the available ranks of focus,",
            f"and their stats will each be increased by 25% for each rank of focus"
            f" consumed.",
            "This is an excellent window of opportunity to deal more damage to a"
            " heavily-armored character, like a Traitor Knight, or to resist incoming"
            " damage!",
            "",
            "If a character suffers a heavy or critical attack, or is routed or"
            " stunned, that character will lose some of their focus.",
            "Additionally, enemy characters can enter a focused state just like you"
            " can, so be careful of enemies that have been left alone for too long!",
        ]
        tutorial["Hero"] = [
            "Let me teach you about Max, your Hero.",
            "",
            "Max is a Hero.",
            "As a Hero, Max is capable of casting the spell Egress, which returns you"
            " to the last save point you passed.",
            "As a Hero, Max must survive each battle. If Max dies, you will lose the"
            " battle and have to attempt it again.",
            "",
            "Over the course of the game, you other characters may be able to learn to"
            " be Heroes.",
            "If this happens, then only one of your Heroes needs to survive each"
            " battle. If one dies, the others can continue to lead your Force.",
        ]
        tutorial["Mounted Movement"] = [
            "Let me teach you about mounted movement.",
            "",
            "Certain characters, such as centaurs like Ken, will have a special Mounted"
            " Movement type.",
            "Units with the Mounted Movement trait can move an extra tile every turn,"
            " except if they start on or move through unstable terrain.",
            "If a mounted unit starts on or moves through unstable terrain such as Sand"
            " or Loose Rocks,",
            "they will not only lose their bonus one-tile move distance, but also lose"
            " an additional tile of movement.",
            "For this reason, on some maps, Mounted units will be your fastest units,"
            " and on others, they will be hampered.",
        ]
        tutorial["Movement"] = [
            "Let me teach you about movement.",
            "",
            "Each character can move a number of tiles based on their Speed or Strength"
            " stats.",
            "Different tile types have different costs of movement. For example, Paths"
            " are very easy to move through, but Loose Rocks are hard.",
            "Up to four friendly characters and up to four enemy characters can occupy"
            " the same tile on the map.",
            "",
            "When a player's movement encounters enemies, they may become blocked.",
            "These are the rules for land movement when it comes to blocking:",
            "A character cannot move through the far side of any tile that contains two"
            " or more enemies.",
            "Likewise, a character cannot move out of a tile at all if it contains four"
            " enemies.",
            "",
            "Different characters may have different movement rules. I will teach you"
            " about them in time.",
        ]
        tutorial["Stealthy Movement"] = [
            "Let me teach you about stealthy movement.",
            "",
            "A character with the Stealthy Movement trait ignores any enemy blockers in"
            " the first two tiles that the character can move through.",
            "After the first two tiles, the character can be blocked as normal.",
        ]
        tutorial["Trophies"] = [
            "Let me teach you about Trophies.",
            "",
            "Whenever one of your characters kills an enemy unit type for the first"
            " time, they will get a trophy.",
            "The trophy is worth quite a bit of extra Experience, and is also worth"
            " Scroulings -- Yatahal's currency -- at the end of each battle.",
            "The more trophies you collect, by having each of your characters kill each"
            " enemy type, the more Scroulings you will receive.",
            "",
            "On each of your characters' turns, the enemies that belong to a type that"
            " the character has not killed yet are marked on the map with a star (*).",
        ]
        tutorial["VocalAttack"] = [
            "Let me teach you about Vocal Attacks.",
            "",
            "Your units can speak out phrases of the Songs of the Creator to repel evil"
            " beings.",
            "Conversely, the powers of evil can create unspeakable sounds that"
            " demoralize and even defeat your forces.",
            "Whenever a unit does not move or cast magic on their turn, they will chant"
            " phrases from the Holy Cantos,",
            "which will shift the alignment of their current tile, and nearby tiles,"
            " one rank towards Holy.",
            "Each rank of alignment on a given tile will boost friendly vocal attack"
            " damage by 25%,",
            "and reduce enemy vocal attack damage by 25%.",
            "At four ranks, friendly vocal attack damage is doubled, and enemy vocal"
            " attacks can't even be used!",
            "",
            "When using a vocal attack, a character deals damage to all enemies"
            " standing on the same tile.",
            "The vocal attack will do more damage when used by characters with a higher"
            " Voice stat.",
            "",
            "A unit that is routed, stunned, or killed will immediately stop chanting,"
            " and their contribution to any tiles' alignment rank immediately ends.",
        ]
        return tutorial

    def teach(self, entry):
        if not self.tutorial:
            return
        if entry in self.tutorial:
            print()
            print(f"Tutorial activated: {self.tutorial[entry][0]}")
            input("<Press enter to continue>")
            print("\n".join(self.tutorial[entry][1:]))
            print()
            input("<Press enter to continue>")
            print()
            del self.tutorial[entry]


spellCost = {}


spellCost["Afflict I"] = [13, "MP"]
spellCost["Aura I"] = [7, "FP"]
spellCost["Aura II"] = [11, "FP"]
spellCost["Aura III"] = [15, "FP"]
spellCost["Aura IV"] = [20, "FP"]
spellCost["Blaze I"] = [2, "MP"]
spellCost["Blaze II"] = [6, "MP"]
spellCost["Blaze III"] = [8, "MP"]
spellCost["Blaze IV"] = [8, "MP"]
spellCost["Bolt I"] = [8, "MP"]
spellCost["Bolt II"] = [15, "MP"]
spellCost["Bolt III"] = [20, "MP"]
spellCost["Bolt IV"] = [20, "MP"]
spellCost["Dao I"] = [8, "MP"]
spellCost["Dao II"] = [15, "MP"]
spellCost["Detox I"] = [3, "FP"]
spellCost["Drain I"] = [5, "MP"]
spellCost["Drain II"] = [12, "MP"]
spellCost["Egress I"] = [8, "MP"]
spellCost["Freeze I"] = [3, "MP"]
spellCost["Freeze II"] = [7, "MP"]
spellCost["Freeze III"] = [10, "MP"]
spellCost["Freeze IV"] = [12, "MP"]
spellCost["Heal I"] = [3, "FP"]
spellCost["Heal II"] = [6, "FP"]
spellCost["Heal III"] = [10, "FP"]
spellCost["Heal IV"] = [20, "FP"]
spellCost["Midas I"] = [8, "MP"]
spellCost["Portal I"] = [21, "MP"]
spellCost["Ninja Fire I"] = [6, "MP"]
spellCost["Ninja Fire II"] = [10, "MP"]
spellCost["Ninja Fire III"] = [12, "MP"]
spellCost["Shield I"] = [12, "FP"]
spellCost["Shield II"] = [12, "FP"]
spellCost["Sleep I"] = [6, "MP"]
spellCost["Sleep II"] = [6, "MP"]
spellCost["Slow I"] = [5, "MP"]
spellCost["Slow II"] = [20, "MP"]
spellCost["Teleport I"] = [5, "MP"]
spellCost["Teleport II"] = [10, "MP"]
spellCost["Teleport III"] = [6, "MP"]


game = game()
