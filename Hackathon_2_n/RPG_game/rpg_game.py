import sys
import warnings
import random
warnings.simplefilter(action='ignore', category=FutureWarning)
import warrior as wp
import story as st
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
        print(f'Your backpack contains:\n {self.backpack}\n and your energy level is:\n {self.energy}.')
    def energy_loss(self):
        if len(self.energy) >= 1:
            self.energy.pop()
        else:
            print('Your warrior is dead')
            sys.exit()
        return self.energy
    def current_warrior(warrior):
        return warrior.show_backpack()


def name_of_player():
    import name_sourcer as person1
    person1 = person1.person('Anna', 20, 'Female')
    return person1.person_details()

def reader():
    f = open("game_status.txt", "r")
    print(f.read())
def file_unsave():
    with open("game_status.txt") as file_in:
        lines = []
        energy = []
        story_name = []
        for line in file_in:
            lines.append(line)
        energy = lines[7]
        story_name = lines[0]
        # print(energy)
    print('Warrior selected:\n',lines[0].title(), lines[1].title(), lines[2].title(), 'Backpack content:\n', lines[5], 'Your energy level is:\n',lines[7])
    return energy
def st_name():
    with open("game_status.txt") as file_in:
        lines = []
        energy = []
        story_name = []
        for line in file_in:
            lines.append(line)
        story_name = str(lines[0])
        k = story_name.replace('Warrior Name:',' ')
        story_name = k
        # print(energy)
    return story_name

def st_contents():
    with open("game_status.txt") as file_in:
        lines = []
        contents = []
        for line in file_in:
            lines.append(line)
        contents = lines[5]
        # print(energy)
    return contents

def fight_outcome(fight,story_name):
    if fight == 1:
        print(f'The fight between{story_name}and an enemy broke out!You were hit badly!')
    else:
        print(f'{story_name}fled but was damaged and lost a lot of energy!')

def main():
    menu_tries = 1
    while menu_tries < 5:
        menu = input('New game Select 1\nContinue game Select 2\nExit now Select 3\n')
        if menu.isalpha() == True or 1 > int(menu) >= 4:
            print('Select a number only (HINT 1, 2 or 3 then hit enter\n')
            print(f'You have still {4-menu_tries} tries left.')
        elif int(menu) == 1:
            choice = int(input('Enter a name, gender and age of your warrior [Select 1]\n or select a random warrior [Select 2] '))
            if choice == 1:
                import name_sourcer as person1
                name = input('Enter name:')
                age = input(('Enter age:'))
                gender = input('Enter gender:')
                print('Let\'s begin:')
                #sys.stdout = open('game_status.txt', 'a')
                sys.stdout = open('game_status.txt', 'a')
                warrior = person1.person(name, age, gender)
                print(warrior.typed_warrior())

                War1 = Warrior([randomiser()], energy)
                bc_pack = War1.show_backpack()
                sys.stdout.close()
                sys.stdout = sys.__stdout__

                break
            elif choice == 2:
                sys.stdout = open('game_status.txt', 'a')
                k = name_of_player()
                print(k)
                War1 = Warrior([randomiser()], energy)
                bc_pack = War1.show_backpack()
                sys.stdout.close()
                sys.stdout = sys.__stdout__
                break
            else:
                print('You need to chose 1 or 2 and hit enter, try again')
                break

        elif int(menu) == 2:
            print('Resumed game:')
        elif int(menu) == 3:
            sys.exit()
        menu_tries += 1
    # reader()
    file_unsave()
    con = st_contents()
    chosen_warrior = wp.Warrior(con,energy)
    #chosen_warrior.energy_loss()
    # chosen_warrior.show_backpack()
    # chosen_warrior.energy_loss()
    # chosen_warrior.energy_loss()
    # print(chosen_warrior.energy_loss())
    # print(chosen_warrior.show_backpack())
    story = st.Story('New', 'New', 'New')
    city = story.city_choice()
    verb = story.verb_choice()
    action = story.action_choice()
    story_ctd = st.Story(city, verb, action)
    story_name = st_name()
    print(story_name)
    print(
      "| ^   ^ |\n"
     "@ (o) (o) @\n"
      "|   <   |\n"
      "|  ___  |\n"
       "\_____/\n"
     "____|  |____")
    print(story_ctd)

    # print(story_ctd)
    while True:
        print('You need to decide what you want to do:\n')
        fight = int(input('Stay to fight [Type 1]\nRun away [Type 2]'))
        if fight == 1:
            fight_outcome(fight, story_name)
            print('You were hit and lost 3 units of life!')
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            break
        elif fight == 2:
            fight_outcome(fight, story_name)
            print('You tried to run but you were hit and lost 6 units of life!')
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            break
        else:
            print('You need to choose to fight (Type 1) or run (Type 2)')
    print(chosen_warrior.show_backpack())
    while True:
        print('It is a time to take another decision!\n')
        fight = int(input('Go to another city [Type 1]\nReturn to the Tavern and fight [Type 2]'))
        if fight == 1:
            fight_outcome(fight, story_name)
            print('You were hit and lost 3 units of life!')
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            break
        elif fight == 2:
            fight_outcome(fight, story_name)
            print('You tried to run but you were hit and lost 6 units of life!')
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            chosen_warrior.energy_loss()
            break
        else:
            print('You need to choose to fight (Type 1) or run (Type 2)')

if __name__ == '__main__':
    main()