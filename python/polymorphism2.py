#______________LEVEL-2 Q1)______________#

class Developer:
    def kaam_karo(self):
        print("Code Likh raha hai!")
class Designer:
    def kaam_karo(self):
        print("Design bana raha hai")
class Manager:
    def kaam_karo(self):
        print("Meeting lee raha hai!")

working=[Developer(), Designer(), Manager()]
for work in working:
    work.kaam_karo()


#______________LEVEL-3 Q1)______________#


class warrior:
    def attack(self):
        print("Attack by sword!")
    def defend(self):
        print("Shield de defence kar raha hai!")

class Archer:
    def attack(self):
        print("Teer se attack kar rahi hai")
    def defend(self):
        print("Shield se protect hai!")

class wizarrd:
    def attack(self):
        print("Attack throug fire ball")
    def defend(self):
        print("Defend through Invesible shield")

class Healer:
    def attack(self):
        print("Healing other Team member")
    def defend(self):
        print("special power defend kar rahi hai")

clash=[warrior(), Archer(), wizarrd(), Healer()]
for clans in clash:
    clans.attack()
    clans.defend()