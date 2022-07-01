import pandas as pd
import random


class Story:
    def __init__(self, city, verb, action):
        self.city = city
        self.verb = verb
        self.action = action
    def city_choice(self):
        df = pd.read_excel('game_data.xlsx')
        t = df.columns.ravel()
        Names = df[t[2]].tolist()
        Names = Names[0:100]
        selected = random.randint(1,100)
        city = Names[selected]
        return city
    def verb_choice(self):
        df = pd.read_excel('game_data.xlsx')
        t = df.columns.ravel()
        Names = df[t[3]].tolist()
        Names = Names[0:100]
        selected = random.randint(1,100)
        verb = Names[selected]
        return verb
    def action_choice(self):
        df = pd.read_excel('game_data.xlsx')
        t = df.columns.ravel()
        Names = df[t[2]].tolist()
        Names = Names[0:100]
        selected = random.randint(1,100)
        action = Names[selected]
        return action

    def __repr__(self):
        return f'went to city of the {self.city_choice()} to {self.verb_choice()} beer in Tavern where unfortunately a {self.action_choice()} was waiting ready to fight!\n'