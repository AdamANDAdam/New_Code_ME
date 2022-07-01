import pandas
import random
import sys

choice = ['Ancestral Crushers Device', 'Bar of Spirit Sphere','Brew of Strength Conjuration','Buckler of Wind Nets',
'Dancers Shield','Elves Belt','Endless Banded Mail of Flame Spans','Envenomed Buckler','Fine Icy Shield','Glammered Banded Mail'
,'Hatchet of Negate Sound','Lordly Hauberk','Mace of Earth Hail','Perfect White Cudgel of the Endless Insect','Ring Mail of the Chant of Infertility Absorbtion',
'Royal Sycthe','Sacred Harpoon','Saintly Crossbow','Villainous Gray Drum of the Speakers','Abjuration of Dust','Worldly Sharp Cone']
backpack = []
energy = ['10%','10%','10%','10%','10%','10%','10%','10%','10%', '10%']
def randomiser():
    for i in range(1,5):
        back_pack_list = random.choice(choice)
        backpack.append(back_pack_list)
    return backpack
class Warrior:
    def __init__(self, backpack = [], energy = []):
        self.backpack = backpack
        self.energy = energy

    def show_backpack(self):
        return f'Your backpack contains:\n {self.backpack}\n and your energy level is:\n {self.energy}.'
    def energy_loss(self):
        if len(self.energy) >= 1:
            self.energy.pop()
        else:
            print('Your warrior is dead')
            sys.exit()
        return self.energy

    def item_loss(self):
        if len(self.backpack) >= 1:
            self.backpack.pop()
        else:
            print('Your warrior lost all items and got killed')
            sys.exit()
        return self.energy
    def current_warrior(warrior):
        return warrior.show_backpack()

    def __repr__(self):
        return f'Your backpack contains:\n {self.backpack}\n and your energy level is:\n {self.energy}.'

# def main():
#     warrior = Warrior([randomiser()], energy)
#
#
# if __name__ == '__main__':
#     main()