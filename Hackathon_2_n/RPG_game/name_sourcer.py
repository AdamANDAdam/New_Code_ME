import pandas as pd
import random

class person:

    def __init__(self, Name, selected, gender):
        self.Name = Name
        self.age = selected
        self.gender = gender
    def typed_warrior(self):
        return f'Warrior Name: {self.Name.title()} \nWarrior Age: {self.age} \nWarrior Gender: {self.gender}\n'
    def person_details(self):
        df = pd.read_excel('game_data.xlsx')
        t = df.columns.ravel()
        Names = df[t[0]].tolist()
        Names = Names[0:100]
        selected = random.randint(1,100)
        Name = Names[selected]
        if selected < 50:
            gender = 'Female'
        else:
            gender = 'Male'

        return (f'Warrior Name: {Name} \nWarrior Age: {selected} \nWarrior Gender: {gender}\n')
